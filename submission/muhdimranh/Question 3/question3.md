<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: MUHAMMAD IMRAN HAKIMI BIN MOHD SHUKRI
#### Matric No.:A20EC0213
#### Dataset:AIRBNB

## Question 3 (a)

This module are divided into two parts which include Register and Login. In order to create this module on Django:

### Step 1: Database Configuration

To start developing the User module for the Airbnb Booking Portal, the first step is to configure the database settings. In this project, MySQL is used as the database engine. Below is the code that I have used to configure the database in `settings.py`:

```
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
		'NAME': 'airbnbportal',
		'USER': 'root',
		'HOST':'localhost',
		'PORT':'3306',     
        },

	'mongodb': {
		'ENGINE': 'djongo',
        'NAME': 'airbnbportal',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
        'host': 'mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/'
	}
}
}
```

### Step 2: Defining User Model

The next step is to define the User model for the Airbnb Booking Portal. The User model will extend Django's AbstractUser model and include additional fields to represent user roles. In `models.py`,

```
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technical_worker = models.BooleanField(default=False)
    is_senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')
```

### Step 3: Creating Views

After defining the User model, the next step is to create the views that handle user registration, login, profile, and role-based dashboards. In `views.py`,

> Importing necessary libraries

```
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import is_customer, is_technical_worker, is_senior_management
from django.contrib.auth.decorators import user_passes_test
```

> Implement the `user_login` view function to handle user login

```
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('User:', user) 
            if user is not None:
                login(request, user)
                print('User logged in successfully') 
                return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
```

> Implement the `register` view function to handle user registration

```
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
```

> Implement separate dashboard views for each user role (`customer_dashboard`, `technical_worker_dashboard`, `senior_management_dashboard`)

```
@login_required
def profile(request):
    user = request.user
    
    return render(request, 'profile.html', {'user': user})

@user_passes_test(is_customer)
def customer_dashboard(request):
    
    return render(request, 'customer_dashboard.html')

@user_passes_test(is_technical_worker)
def technical_worker_dashboard(request):
    
    return render(request, 'technical_worker_dashboard.html')

@user_passes_test(is_senior_management)
def senior_management_dashboard(request):
    
    return render(request, 'senior_management_dashboard.html')
```

> Implement the `redirect_dashboard` view function to redirect the user to their respective dashboard based on their role

```
def redirect_dashboard(request):
    user = request.user
    if user.is_customer:
        return redirect('customer_dashboard')
    elif user.is_technical_worker:
        return redirect('technical_worker_dashboard')
    elif user.is_senior_management:
        return redirect('senior_management_dashboard')
    else:
        
        return redirect('profile')
```

> Implement the `user_logout` view function to handle user logout

```
def user_logout(request):
    logout(request)
    return redirect('login')
```

### Step 4: Define Registration Form

In order to register users with their selected roles, a custom registration form needs to be created. In `forms.py`,

```
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')

        if role == 'customer':
            user.is_customer = True
        elif role == 'technical_worker':
            user.is_technical_worker = True
        elif role == 'senior_management':
            user.is_senior_management = True

        if commit:
            user.save()
        return user
```

### Step 5: Configure URLs

The next step is to configure the URL patterns for the User module in the `urls.py` file.

```
from django.contrib import admin
from django.urls import path
from AirbnbBookingPortal.views import register, user_login, redirect_dashboard, customer_dashboard, technical_worker_dashboard, senior_management_dashboard, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='register'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', redirect_dashboard, name='dashboard'),
    path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
    path('technical_worker_dashboard/', technical_worker_dashboard, name='technical_worker_dashboard'),
    path('senior_management_dashboard/', senior_management_dashboard, name='senior_management_dashboard'),
    path('logout/', user_logout, name='logout'),

]
```

### Step 6: Create Templates

Create the required HTML templates for user registration, login, profile, and role-based dashboards.

> `login.html`: Render the login form.

```
{% extends 'base.html' %} {% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```

> `register.html`: Render the registration form.

```
{% extends 'base.html' %} {% block content %}
<h2>Register</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Register</button>
</form>
<br />
<text>Already have an account?</text><a href="{% url 'login' %}">Sign In</a>
{% endblock %}

```

> `profile.html`: Display the user's profile information.
> `customer_dashboard.html`: Dashboard for customers.
> `technical_worker_dashboard.html`: Dashboard for technical workers.
> `senior_management_dashboard.html`: Dashboard for senior management.

### Step 7: Apply Migrations

To apply the changes made to the database models, run the following command in the terminal:

```
python manage.py makemigrations
python manage.py migrate
```

### Below shows the full implementation of user module.

> After defining User model, a custom User table will be created. In this case, there will be three tables created that follows django user authentication.

![Q3](files/images/q3.1.png)

> Run migration to apply changes to database.

![Q3](files/images/q3.2.png)

> In the register page, enter all required fields and click on Submit. This will proceed with registration and store information in database.

![Q3](files/images/q3.3.png)

![Q3](files/images/q3.8.png)

> In the login page, enter all required fields and click on Login. This will redirect users to different dashboards or pages depending on the role.

![Q3](files/images/q3.4.png)

![Q3](files/images/q3.5.png)

![Q3](files/images/q3.6.png)

![Q3](files/images/q3.7.png)

> Click on Logout to logout from session.



## Question 3 (b)

To implement data replication and synchronization between MySQL and MongoDB databases in my Django Airbnb Booking Portal:

### Step 1: Install Required Packages

Install the following commands that will be required for this task :

```
pip install djongo
pip install mysqlclient
pip install mysql-replication
pip install django-extensions
```

### Step 2: Configure Django Settings

In my settings.py file, I have made changes to my database connection setup:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'airbnbportal',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'airbnbportal',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/'
        }
    }
}

```

### Step 3: Create a Django Management Command

Create a custom Django management command that handles data replication and synchronization. This command will implement two-way data synchronization between the two databases. This means capturing changes made in MongoDB and applying them to MySQL, as well as capturing changes made in MySQL and applying them to MongoDB. I create a new file named `replicate_data.py` in my Django project's directory and add the following code:

```
from django.core.management.base import BaseCommand
from mysql.connector import connect
from pymongo import MongoClient
from mysql_replication import BinLogStreamReader
from mysql_replication.row_event import WriteRowsEvent, UpdateRowsEvent, DeleteRowsEvent
from AirbnbBookingPortal.models import ListingAndReviews


class Command(BaseCommand):
    help = 'Replicate and synchronize data between MySQL and MongoDB'

    def handle(self, *args, **options):
        # Connect to MySQL
        mysql_conn = connect(
            host='localhost',
            user='root',
            password='', 
            database='airbnbportal'
        )

        # Connect to MongoDB
        mongo_client = MongoClient('mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/')
        mongodb = mongo_client.airbnbportal

        # Define a callback function to process MySQL events
        def process_event(event):
            if isinstance(event, WriteRowsEvent):
                for row in event.rows:
                    listing = ListingAndReviews(**row['values'])
                    listing.save(using='mongodb')
            elif isinstance(event, UpdateRowsEvent):
                for row in event.rows:
                    _id = row['after_values']['_id']
                    listing = ListingAndReviews.objects.using('mongodb').get(_id=_id)
                    for key, value in row['after_values'].items():
                        setattr(listing, key, value)
                    listing.save(using='mongodb')
            elif isinstance(event, DeleteRowsEvent):
                for row in event.rows:
                    _id = row['values']['_id']
                    ListingAndReviews.objects.using('mongodb').filter(_id=_id).delete()

        # Create a binlog stream reader for MySQL changes
        mysql_stream = BinLogStreamReader(
            connection_settings=mysql_conn,
            server_id=1,
            blocking=True,
            only_events=[WriteRowsEvent, UpdateRowsEvent, DeleteRowsEvent]
        )

        # Process MySQL events and apply changes to MongoDB
        for binlogevent in mysql_stream:
            process_event(binlogevent)

        # Close MySQL connection and stream reader
        mysql_stream.close()
        mysql_conn.close()

        # Retrieve MongoDB changes and apply them to MySQL
        mongo_listings = mongodb.listingandreviews.find()
        for listing in mongo_listings:
            _id = listing['_id']
            try:
                mysql_listing = ListingAndReviews.objects.get(_id=_id)
                for key, value in listing.items():
                    setattr(mysql_listing, key, value)
                mysql_listing.save()
            except ListingAndReviews.DoesNotExist:
                new_listing = ListingAndReviews(**listing)
                new_listing.save()

        # Close MongoDB connection
        mongo_client.close()

```

### Step 4: Schedule the Data Replication Task
To schedule the data replication task, I will use the django-extensions package, which provides a convenient way to run custom management commands on a schedule.

Install the django-extensions package by adding 'django_extensions' to the INSTALLED_APPS list in the `settings.py` file.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AirbnbBookingPortal',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_extensions',
]
```

In my `urls.py` file, I added the following code at the end:

```
from django_extensions.management.jobs import HourlyJob, DailyJob


from AirbnbBookingPortal.management.commands.replicate_data import Command as ReplicateDataCommand

# Define a job class for the data replication task
class DataReplicationJob(HourlyJob):  # Adjust the schedule as needed (e.g., HourlyJob, DailyJob)
    help = "Replicates data from MySQL to MongoDB"
    when = '*'

    def execute(self):
        ReplicateDataCommand().handle()

# Register the job
jobs = [
    DataReplicationJob,
]

```

### Step 5: Configure Scheduled Task

Here are the steps to set up a scheduled task using the Task Scheduler utility on Windows:

1. Open the Task Scheduler utility: Press the Windows key, type "Task Scheduler," and click on the "Task Scheduler" application that appears in the search results.

2. Create a new task: In the Task Scheduler window, click on "Create Basic Task" or "Create Task" in the Actions panel on the right. The exact wording may vary depending on your Windows version.

3. Provide a name and description: Enter a name and optional description for the task, such as "Airbnb Data Synchronization."

4. Set the trigger: Choose how often you want the task to run. In this case, I will select "Daily". Click "Next."

5. Set the action: Choose "Start a program" as the action and click "Next."

6. Specify the program and arguments:

- Program/script: Browse to locate the Python executable. Typically, it is located at C:\PythonXX\python.exe, where XX represents the Python version you have installed. In my case, it will be `Python311`.

- Add arguments: Enter the path to your Django project's manage.py file, followed by the command runjobs hourly. For example, this is mine:
```
C:\Users\imran\AppData\Local\Programs\Python\Python311\python.exe C:\Users\imran\Documents\AA Special Topic\AirbnbPortal\manage.py runjobs hourly
```

The Task Scheduler will now execute the scheduled task at the specified interval, running the Django management command runjobs daily to trigger the data synchronization process between MySQL and MongoDB.




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




