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


@login_required(login_url="/login/")
def senior_management(request):
    template = "home/senior_management.html"
    context = {}

    return render(request, template, context)

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