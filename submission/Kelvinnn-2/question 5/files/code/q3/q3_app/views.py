from .forms import UserRegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from pymongo  import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import pandas as pd
import io
import urllib
import base64
from django.http import HttpResponse
from django.template import loader
from django.core.cache import cache
from cachetools import cached, TTLCache

result_by_sector_cache = TTLCache(maxsize=1, ttl=3600)  # Cache for inspections_by_sector
inspections_by_month_cache = TTLCache(maxsize=1, ttl=3600)  # Cache for inspections_by_month


def inspections_by_sector(request):
     # Check if cached data is available
    cached_data = cache.get('inspections_by_sector')
    if cached_data:
        print("Using cached data")
        result_by_sector = cached_data
    else:
        print("Generating new data")
        # Create a MongoClient instance
        client = MongoClient('mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/')

        # Access the MongoDB database
        db = client['AA']

        # Access the collection named "city_inspectionsDataset"
        collection = db['city_inspectionsDataset']

        # Query the collection and retrieve the JSON data
        data = list(collection.find())

        # Create a DataFrame from the JSON data
        df = pd.DataFrame(data)

        # Calculate the result_by_sector DataFrame
        result_by_sector = df.groupby(['sector', 'result']).size().unstack().fillna(0)

        # Cache the result for future use
        cache.set('inspections_by_sector', result_by_sector)

    # Select top 5 results
    top_results = result_by_sector.sum().nlargest(5).index

    # Select top 5 sectors
    top_sectors = result_by_sector.sum(axis=1).nlargest(5).index

    # Filter the result_by_sector DataFrame based on the top results and sectors
    result_by_sector = result_by_sector.loc[top_sectors, top_results]

    # Increase the figure size and set a wider width
    plt.figure(figsize=(20, 10))

    # Plot the bar chart
    result_by_sector.plot(kind='bar', stacked=True, width=0.8)
    plt.xlabel('Sector')
    plt.ylabel('Number of Inspections')
    plt.title('Distribution of Top 5 Results by Top 5 Sectors')
    plt.xticks(rotation=30)
    plt.subplots_adjust(bottom=0.25)
    plt.subplots_adjust(bottom=0.25, left=0.1, right=0.9, top=0.9)  # Adjust the margins as needed

    # Save the chart to a file
    chart_path = 'q3_app/static/images/chart.png'
    plt.savefig(chart_path)

    # Pass the chart path to the template
    context = {'chart_path': chart_path}

    # Render the template with the data
    return render(request, 'registrations/management_dashboard.html', context)

@cached(inspections_by_month_cache)
def inspections_by_month(request):
    

    # Create a MongoClient instance
    client = MongoClient('mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "city_inspectionsDataset"
    collection = db['city_inspectionsDataset']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Extract the month from the 'date' column
    df['month'] = df['date'].dt.month

    # Calculate the number of inspections by month
    inspections_by_month = df.groupby('month').size()

    # Plot the line chart
    plt.plot(inspections_by_month.index, inspections_by_month.values, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Number of Inspections')
    plt.title('Trends in Inspections by Month')
    plt.xticks(range(1, 13))

    # Save the chart to a file
    chart_path = 'q3_app/static/images/inspections_by_month.png'
    plt.savefig(chart_path)

    # Pass the chart path to the template
    context = {'chart_path': chart_path}

    # Render the template with the data
    return render(request, 'registrations/management_dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f"Logged in as {username}")
            print(f"User type: {user.user_type}")
            
            if user.user_type == 'customer':
                print("Redirecting to customer dashboard")
                return redirect('customer_dashboard')
            elif user.user_type == 'technical_worker':
                print("Redirecting to technical worker dashboard")
                return redirect('technical_worker_dashboard')
            elif user.user_type == 'senior_management':
                print("Redirecting to management dashboard")
                return redirect('management_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def customer_dashboard(request):
    context = {}
    # Create a MongoClient instance
    client = MongoClient('mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "stories"
    collection = db['city_inspectionsDataset']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Extract the story descriptions
    business_names = []
    sector_names = []

    for shop in data:
        business_name = shop['business_name']
        sector_name = shop['sector']
        business_names.append(business_name)
        sector_names.append(sector_name)

    # Create an instance of CountVectorizer
    vectorizer = CountVectorizer()

    # Fit the vectorizer on the descriptions and transform them into a bag-of-words representation
    business_features = vectorizer.fit_transform(business_names)

    # Create an instance of the Decision Tree
    classifier = DecisionTreeClassifier()

    # Train the classifier on the features and encoded topic labels
    classifier.fit(business_features, sector_names)

    if request.method == 'POST':
        # Get the user input from the form
        new_data = [request.POST.get('business_name')]

        # Transform the user input using the vectorizer
        new_features = vectorizer.transform(new_data)

        # Use the trained classifier for prediction
        predicted_sector = classifier.predict(new_features)

        # Render the customer template with the prediction results
        return render(request, 'registrations/customer_dashboard.html', {'predicted_sector': predicted_sector})

    # Render the initial customer template
    return render(request, 'registrations/customer_dashboard.html', context)



def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def customer_dashboard_view(request):
    return render(request, 'customer_dashboard.html')

def technical_worker_dashboard_view(request):
    return render(request, 'technical_worker_dashboard.html')

def management_dashboard_view(request):
    return render(request, 'management_dashboard.html')