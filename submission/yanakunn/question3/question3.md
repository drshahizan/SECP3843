<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURARISSA DAYANA BINTI MOHD SUKRI
#### Matric No.: A20EC0120
#### Dataset: SALES

## Question 3 (a)
This project will incorporate a user registration and login module into the MySQL database. This module will serve three different types of users: customers, technical workers, and senior management. To build this module, we will use Django as the web server framework and MySQL as the database.

### Step 1: Set up the Django project and environment.
1. Create a new directory called project, and navigate into it.
  ``` ruby
  $ cd ~/desktop/
  $ mkdir project
  $ cd ~/desktop/project
  ```

2. Create and activate a new virtual environment called .venv in the directory.
  ``` ruby
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  ```
3. Install Django, create a new project called django_project, and start the local Django web server.
  ``` ruby
  (.venv) $ python3 -m pip install django
  (.venv) $ django-admin startproject django_project
  ```

### Step 2: Configure the MySQL database.
1. Install the MySQL client for Python
  ``` ruby
  pip3 install mysqlclient
  ```
2. In the project's core folder, go to settings.py file, update the `DATABASES` setting to use MySQL.
  ```ruby
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'NAME': 'your_database_name',
               'USER': 'your_username',
               'PASSWORD': 'your_password',
               'HOST': 'localhost',
               'PORT': '3306',
           }
       }
  ```

### Step 3: Create a custom User model.
1. In the app's models.py file, import the necessary modules and create a custom User model by extending Django's AbstractUser class.
  ```ruby
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  class CustomUser(AbstractUser):
     ROLE_CHOICES = (
         ('customer', 'Customer'),
         ('technical_worker', 'Technical Worker'),
         ('senior_management', 'Senior Management'),
     )
     
     role = models.CharField(max_length=20, choices=ROLE_CHOICES)
  ```

2. In the project's settings.py file, add the following setting to specify the custom user model:
  ```ruby
  AUTH_USER_MODEL = 'appname.CustomUser'
  ```

### Step 4: Generate database migrations

1. Run the following command to generate the initial migrations
  ```ruby
  python manage.py makemigrations
  ```
3. Apply the migrations to create the corresponding database tables
  ```ruby
  python manage.py migrate
  ```

### Step 5: Create user registration and login views with Django's built-in authentication views and forms.

1. Define the URL in your app's urls.py file:
  ```ruby
  from django.contrib.auth import views as auth_views
  
  urlpatterns = [
     # Login and logout views
     path('login/', auth_views.LoginView.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     # Registration view and URL
     path('register/', views.register, name='register'),
     # Other app URLs
     # ...
  ]
  ```
2. Create a register view in your app's views.py file to handle user registration.
  ```ruby
  from django.shortcuts import render, redirect
  from .forms import RegistrationForm
  
  def register(request):
     if request.method == 'POST':
         form = RegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('login')
     else:
         form = RegistrationForm()
     return render(request, 'registration/register.html', {'form': form})
  ```

3. Create a registration form in your app's forms.py file that inherits from Django's UserCreationForm and includes an additional field for the role.
  ```ruby
  from django import forms
  from .models import CustomUser
  from django.contrib.auth.forms import UserCreationForm
  
  class RegistrationForm(UserCreationForm):
     role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
     
     class Meta:
         model = CustomUser
         fields = ('username', 'password1', 'password2', 'role')
  ```


### Step 6: Start the Django development server
  ```ruby
  (.venv) $ python manage.py runserver
  ```

## Question 3 (b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



