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