<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: FARAH IRDINA BINTI AHMAD BAHARUDIN
#### Matric No.: A20EC0035
#### Dataset: AIRBNB LISTINGS DATASET

## Question 3 (a)

### Steps to create this module on Django web server by using MySql database server

#### 1. Define the user models

By using the same file 'models.py', add a new class. This class is about the information of the users. Since this project requires three types of users which are customers, technical workers and senior management, thus creating a custom user model is essential. 

```
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
```

#### 2. Configure authentication backend

Since we will be using a custom user model, thus we need to update the AUTH_USER_MODEL inside settings.py.

```
AUTH_USER_MODEL = 'Listings.CustomUser'
```

#### 3. Create login and register views

When we runserver, views help us to open the page that we have set. Views also handle the form submission, validations and user authentication processes.

```
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Replace 'home' with the URL name for your home page
            return redirect('home')
    else:
        form = AuthenticationForm(request)

    return render(request, 'templates/Listings/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object
            login(request, user)  # Log in the user
            # Replace 'home' with the URL name for your home page
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'templates/Listings/register.html', {'form': form})

```

#### 4. Define url patterns

Open urls.py inside the project file, define both login and register views. 

```
from django.contrib import admin
from django.urls import path
from Listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    # Add more URL patterns as needed
]
```

#### 5. Create templates

Templates act as the interface that users will be accessing. Create forms inside both login.html and register.html files.

##### - login.html

```
{% extends 'base.html' %} {% block content %}
<h2>User Login</h2>
<form method="POST">
  {% csrf_token %} {{ login_form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```

##### - register.html

```
{% extends 'base.html' %} {% block content %}
<h2>User Registration</h2>
<form method="POST">
  {% csrf_token %} {{ registration_form.as_p }}
  <button type="submit">Register</button>
</form>
{% endblock %}
```

#### 6. Create forms.py file

Create a forms.py file in Django app and define the custom registration form based on our user model. We can use ModelForm to simplify the form creation process.

```
from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'user_type']
```

#### 7. Perform databsae migrations

Lastly, we need to perform a database migration to update the database schema.

```
python manage.py makemigrations Listings
python manage.py migrate
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/three.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/three2.png)

## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



