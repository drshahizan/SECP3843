<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NUR IRDINA ALIAH BINTI ABDUL WAHAB
#### Matric No.: A20EC0115
#### Dataset: AIRBNB

## Question 3 (a)
On this project, the module for managing user registration and login will be placed in the 
mySQL database. This system is used by three types of people: customers, technical workers, 
and senior management. Describe in detail the creation of this module on the web server 
(Django) and the database (mySQL)

Define User Model 
```
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    cust = models.BooleanField(default=False)
    TechnicalWorker = models.BooleanField(default=False)
    SeniorManagement = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')


```

create views 
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
registration
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

separate dashboard
```
@login_required
def profile(request):
    user = request.user
    
    return render(request, 'profile.html', {'user': user})

@user_passes_test(Cust)
def customer_dashboard(request):
    
    return render(request, 'customer_dashboard.html')

@user_passes_test(TechnicalWorker)
def technical_worker_dashboard(request):
    
    return render(request, 'technical_worker_dashboard.html')

@user_passes_test(SeniorManagement)
def senior_management_dashboard(request):
    
    return render(request, 'senior_management_dashboard.html')
def redirect_dashboard(request):
    user = request.user
    if user.Cust:
        return redirect('customer_dashboard')
    elif user.TechnicalWorker:
        return redirect('technical_worker_dashboard')
    elif user.SeniorManagement:
        return redirect('senior_management_dashboard')
    else:
        
        return redirect('profile')

```

manage log out
```
def user_logout(request):
    logout(request)
    return redirect('login')
```
manage registration form
```
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Cust', 'Customer'),
        ('TechnicalWorker', 'Technical Worker'),
        ('SeniorManagement', 'Senior Management'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')

        if role == 'Customer':
            user.Cust = True
        elif role == 'TechnicalWorker':
            user.TechnicalWorker = True
        elif role == 'SeniorManagement':
            user.SeniorManagement = True

        if commit:
            user.save()
        return user
```
link to url
```
"""
URL configuration for AA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import register, user_login, redirect_dashboard, customer_dashboard, technical_worker_dashboard, senior_management_dashboard, user_logout

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

i use basic templates

login.html
```
{% extends 'Index.html' %} {% block content %}
<h3>LOGIN</h3>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```
Register.html
```
{% extends 'Index.html' %} {% block content %}
<h3>Register</h3>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">REGISTER</button>
</form>
<br />
<text>Have an account?</text><a href="{% url 'login' %}">Sign In</a>
{% endblock %}

```
migrate Data
use 
```
python manage.py makemigrations
python manage.py migrate
```
enter this in command prompt

## Question 3 (b)
When working with two different databases, the challenge of Data Replication and 
Synchronization arises between the MySQL and MongoDB databases. This challenge involves 
ensuring that any changes made in one database are accurately reflected in the other, thereby 
maintaining data consistency across both systems. To overcome this issue, it is recommended 
to explore database-specific replication techniques or leverage external tools that facilitate real-
time updates and seamless interaction between the databases. In your response, provide a 
detailed description of the steps involved in addressing this challenge. You may include 
relevant code snippets and screenshots that illustrate the solution implemented. 

To implement data replication and synchronization between MySQL and MongoDB databases in my Django Airbnb :

Step 1 :Install required packages

step 2 : databses connection
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dashboard',
        'USER': 'root',
        'HOST' : 'localhost',
        'PORT': '3306',
    },


'mongodb' : {
    'ENGINE': 'djongo',
    'NAME': 'Airbnb',
    'ENFORCE_SCHEMA': False,
    'CLIENT':{
     'host' : 'mongodb+srv://irdinaaliah2:Freekindome_00@cluster0.o4fadwf.mongodb.net/'
    }
}
}
```
create Django command
```
from django.core.management.base import BaseCommand
from mysql.connector import connect
from pymongo import MongoClient
from mysql_replication import BinLogStreamReader
from mysql_replication.row_event import WriteRowsEvent, UpdateRowsEvent, DeleteRowsEvent
from dashboard.models import AA


class Command(BaseCommand):
    help = 'Replicate and synchronize data between MySQL and MongoDB'

    def handle(self, *args, **options):
        # Connect to MySQL
        mysql_conn = connect(
            host='localhost',
            user='root',
            password='', 
            database='dashboard'
        )

        # Connect to MongoDB
        mongo_client = MongoClient('mongodb+srv://irdinaaliah2:Freekindome_00@cluster0.o4fadwf.mongodb.net/

        # Define a callback function to process MySQL events
        def process_event(event):
            if isinstance(event, WriteRowsEvent):
                for row in event.rows:
                    listing = dashboard(**row['values'])
                    listing.save(using='mongodb')
            elif isinstance(event, UpdateRowsEvent):
                for row in event.rows:
                    _id = row['after_values']['_id']
                    listing = dashboard.objects.using('mongodb').get(_id=_id)
                    for key, value in row['after_values'].items():
                        setattr(listing, key, value)
                    listing.save(using='mongodb')
            elif isinstance(event, DeleteRowsEvent):
                for row in event.rows:
                    _id = row['values']['_id']
                    dashboard.objects.using('mongodb').filter(_id=_id).delete()

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
        mongo_listings = mongodb.dashboard.find()
        for listing in mongo_listings:
            _id = listing['_id']
            try:
                mysql_listing = dashboard.objects.get(_id=_id)
                for key, value in listing.items():
                    setattr(mysql_listing, key, value)
                mysql_listing.save()
            except dashboard.DoesNotExist:
                new_listing = dashboard(**listing)
                new_listing.save()

        # Close MongoDB connection
        mongo_client.close()


```
add django extenstion
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    

    'django_extensions',
]
```

configure scheduled task
 

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


Schedule Data Replication
C:\Users\HP\AA\dashboard\Local\Programs\Python\Python311\python.exe C:\Users\HP\AA\dashboard\manage.py runjobs hourly

