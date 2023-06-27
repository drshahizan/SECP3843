<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Mikhel Adam Bin Muhammad Ezrin
#### Matric No.: A20EC0237
#### Dataset: [Tweets](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets)

## Question 3 (a)
As previously done, we'll need to create a Django project which follows these basic steps

 1. Install Django
 2. Create a new Django Project in a virtual environment 
 3. Start the app

The steps above can be seen in detail [here](https://github.com/drshahizan/SECP3843/blob/main/submission/HUNK12/question1/question1.md#question-1-a), Next, we'll see how to create a user management module which allows for user registration and login using the MySQL database.

#### Add url patterns
In `app/urls.py` file
```py
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login_view, name='login_view'),
   path('register', views.register, name='register'),

]
```
In `tweets/urls.py` file
```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
```

#### Create User Model
In `models.py` file
```py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField('Is Customer', default=False)
    is_technical_worker = models.BooleanField('Is Technical Worker', default=False)
    is_senior_management = models.BooleanField('Is Senior Management', default=False)
```
Then in the `settings.py` file add the line `AUTH_USER_MODEL  =  'app.User'`

#### Make migrations
Run the following commands to migrate the database to create the necessary tables
```
py manage.py makemigrations
py manage.py migrate
```

#### Create `forms.py` file in `app` folder
```py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_technical_worker', 'is_senior_management', 'is_customer')
```

#### Add views in `views.py` located in `app` folder
```py
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')
```
#### Add html files in `app/template` folder
In `index.html` file
```html
<!doctype html>
{% load static %}
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="{% static 'fonts/icomoon/style.css' %}">

    <link rel="stylesheet" href="{% static 'css/owl.carousel.min.css' %}">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">

    <!-- Style -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

    <title>Tweets Portal</title>
  </head>
  <body>
  <div class="content">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-6 contents">
          <div class="row justify-content-center">
            <div class="col-md-12">
              <div class="form-block">
                  <div class="mb-4">
                      <h1>Welcome!</h1>
                  </div>
                  <label>Log in if you already have registered!</label>
                  <div class="form-group last mb-4">
                      <div><button class="btn btn-pill text-white btn-block btn-primary"><a href="{% url 'login_view' %}">Login</a></button></div>
                  </div>
                  <label>If not register here!</label>
                  <div class="form-group last mb-4">
                      <div><button class="btn btn-pill text-white btn-block btn-primary"><a href="{% url 'register' %}">Register</a></button></div>
                  </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </div>
  </div>


    <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'js/popper.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>
  </body>
</html>
```

#### Runserver
Use the command below to test and check if the register and login functions work on the website
```
python manage.py runserver
```
Below this are screenshots showing the pages working as it should
![image](https://github.com/drshahizan/SECP3843/assets/3646429/9670cb98-69c0-45f7-8452-165a9c8d0f22)
![image](https://github.com/drshahizan/SECP3843/assets/3646429/a723bbca-6b03-41af-886a-c8b07f5a5b3b)
![image](https://github.com/drshahizan/SECP3843/assets/3646429/78bcb204-eeb3-470f-bf3d-0a008c486a09)




## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



