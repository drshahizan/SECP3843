from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from user.forms import NewUserForm
from .forms import LoginForm
from django.contrib.auth import logout
from django.contrib import messages
from pymongo import MongoClient
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import numpy as np
from cachetools import cached, LRUCache
from django.core.cache import cache
import time  



def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/login/")
def customer(request):

    context = {}
    # Create a MongoClient instance
    client = MongoClient('mongodb://localhost:27017')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "stories"
    collection = db['stories']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Extract the story descriptions
    descriptions = []
    topic_names = []

    for story in data:
        description = story['description']
        topic_name = story['topic']['name']
        descriptions.append(description)
        topic_names.append(topic_name)

    # Create an instance of CountVectorizer
    vectorizer = CountVectorizer()

    # Fit the vectorizer on the descriptions and transform them into a bag-of-words representation
    features = vectorizer.fit_transform(descriptions)

    # Create an instance of the Naive Bayes classifier
    classifier = MultinomialNB()

    # Train the classifier on the features and encoded topic labels
    classifier.fit(features, topic_names)

    if request.method == 'POST':
        # Get the user input from the form
        new_data = [request.POST.get('instance')]

        # Transform the user input using the vectorizer
        new_features = vectorizer.transform(new_data)

        # Use the trained classifier for prediction
        predicted_topics = classifier.predict(new_features)

        # Render the customer template with the prediction results
        return render(request, 'home/customer.html', {'predicted_topics': predicted_topics})

    # Render the initial customer template
    return render(request, 'home/customer.html', context)

cache_key = 'my_data_cache_key'
cache_timeout = 60 


def get_data_from_cache_or_source():
    data = cache.get(cache_key)
    message = "Not cached"

    if data is not None:
        # Keeping track of total time taken
        timeTaken = time.time()
        time.sleep(1)  
        total_time_taken = time.time() - timeTaken
        message = f"I am executed with the function. Total time taken: {total_time_taken:.2f} seconds"
    
        return data, message

    # Data is not cached, compute or fetch it from the source
    # Create a MongoClient instance
    client = MongoClient('mongodb://localhost:27017')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "stories"
    collection = db['stories']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Store the data in the cache
    cache.set(cache_key, data, cache_timeout)

    # Set the message when data is not cached
    message = "Data is not cached"

    # Return the data and message
    return data, message




@login_required(login_url="/login/")
@cached(cache = LRUCache(maxsize=128))
def senior_management(request):
    context = {}
    data, message = get_data_from_cache_or_source()
    total_stories = len(data)  # Compute the total count of stories

    context['total_stories'] = total_stories  # Add the count to the context
    context['message'] = message

    return render(request, 'home/senior_management.html', context)

@login_required(login_url="/login/")
def technical_worker(request):
    template = "home/technical_worker.html"
    context = {}

    return render(request, template, context)

@login_required(login_url="/login/")
def index(request):
    template = "home/list.html"
    context = {}

    return render(request, template, context)




def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


def user_login(request):
    form = LoginForm()  # Instantiate the LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Pass the POST data to the form
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'customer':
                	return redirect('customer')
                elif user.user_type == 'technical_worker':
                	return redirect('technical_worker')
                elif user.user_type == 'senior_management':
                	return redirect('senior_management')
                else:
                      return redirect('index')
            else:
                messages.error(request, "Unsuccessful Login. Invalid information.")
                return render(request, 'registration/login.html', {'form': form})
        else:
            messages.error(request, "Form validation failed")
    return render(request, 'registration/login.html', {'form': form})



def top_5_topic(request):
    # Create a MongoClient instance
    client = MongoClient('mongodb://localhost:27017')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "stories"
    collection = db['stories']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Extract the topic names and their counts
    topic_counts = {}
    for story in data:
        topic_name = story['topic']['name']
        if topic_name in topic_counts:
            topic_counts[topic_name] += 1
        else:
            topic_counts[topic_name] = 1

    # Sort the topics by count in descending order
    sorted_topics = sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)

    # Take the top 5 topics and their counts
    top_topics = dict(sorted_topics[:5])
    topics = list(top_topics.keys())
    counts = list(top_topics.values())

    # Set the figure size
    plt.figure(figsize=(8, 6))

    # Set the bar width and padding
    bar_width = 0.5
    index = np.arange(len(topics))

    # Create the bar chart
    plt.bar(index, counts, width=bar_width, align='center')

    # Customize the x-axis labels and tick positions
    plt.xticks(index, topics)
    plt.xticks(rotation=45, ha='right')

    # Add padding between the bars
    plt.subplots_adjust(bottom=0.2)
    plt.margins(0.1)
    plt.autoscale(enable=True, axis='x', tight=True)

    # Add labels and title
    plt.xlabel('Topics')
    plt.ylabel('Count')
    plt.title('Top 5 Topics')

    # Save the chart to a file
    chart_path = 'user/static/images/chart.png' 
    plt.savefig(chart_path)


    chart_path = 'user/static/images/chart.png' 
    # Pass the chart path to the template
    context = {'chart_path': chart_path}

    # Render the template with the data
    return render(request, 'home/customer.html', context)

def top_5_by_comments(request):
    # Create a MongoClient instance
    client = MongoClient('mongodb://localhost:27017')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "stories"
    collection = db['stories']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Sort the stories by comment count in descending order and take the top 5
    top_stories = sorted(data, key=lambda x: x['comments'], reverse=True)[:5]

    # Calculate the total number of comments for all stories
    total_comments = sum(story['comments'] for story in data)

    # Calculate the percentage of comments for each story and create the labels and sizes lists
    labels = []
    sizes = []
    for story in top_stories:
        percentage = (story['comments'] / total_comments) * 100
        labels.append(story["title"])
        sizes.append(percentage)

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Top 5 Stories by Comment Percentage')

    # Save the chart to a file
    chart_path = 'user/static/images/pie_chart.png'
    plt.savefig(chart_path)

    # Pass the chart path to the template
    context = {'chart_path_pie': chart_path}

    # Render the template with the data
    return render(request, 'home/customer.html', context)
