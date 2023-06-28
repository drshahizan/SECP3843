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


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )

    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
```

#### 2. Configure authentication backend

Since we will be using a custom user model, thus we need to update the AUTH_USER_MODEL inside settings.py.

```
AUTH_USER_MODEL = 'Listings.User'
```

#### 3. Create login and register views

When we runserver, views help us to open the page that we have set. Views also handle the form submission, validations and user authentication processes.

```
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request=request, template_name="Listings/login.html")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="Listings/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if user.type == 'customer':
                    return render(request=request, template_name="Listings/customer.html")
                elif user.type == 'technical_worker':
                    return render(request=request, template_name="Listings/worker.html")
                elif user.type == 'senior_management':
                    return render(request=request, template_name="Listings/senior.html")
                else:
                    return render(request=request, template_name="Listings/home.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Listings/login.html", context={"login_form": form})
```

#### 4. Define url patterns

Open urls.py inside the project file, define both login and register views. 

```
from django.contrib import admin
from django.urls import path
from Listings import views

app_name = "Listings"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login")
    # Add more URL patterns as needed
]
```

#### 5. Create templates

Templates act as the interface that users will be accessing. Create forms inside both login.html and register.html files.

##### - login.html

```
{% block content %} {% load crispy_forms_tags %}

<!--Login-->
<div class="container py-5">
  <h1>Login</h1>
  <form method="POST">
    {% csrf_token %} {{ login_form|crispy }}
    <button class="btn btn-primary" type="submit">Login</button>
  </form>
  <p class="text-center">
    Don't have an account? <a href="/register">Create an account</a>.
  </p>
</div>

{% endblock %}
```

##### - register.html

```
{% block content %} {% load crispy_forms_tags %}

<!--Register-->
<div class="container py-5">
  <h1>Register</h1>
  <form method="POST">
    {% csrf_token %} {{ register_form|crispy }}
    <button class="btn btn-primary" type="submit">Register</button>
  </form>
  <p class="text-center">
    If you already have an account, <a href="/login">login</a> instead.
  </p>
</div>

{% endblock %}
```

#### 6. Create forms.py file

Create a forms.py file in Django app and define the custom registration form based on our user model. We can use ModelForm to simplify the form creation process.

```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    ]

    type = forms.ChoiceField(choices=USER_TYPE_CHOICES,
                             widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "type")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
```

#### 7. Perform databsae migrations

Lastly, we need to perform a database migration to update the database schema.

```
python manage.py makemigrations Listings
python manage.py migrate
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/three.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/three2.png)

### Result

#### - Register page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/register.png)

#### - Login page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/login.png)

#### - Customer page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/customer.png)

#### - Technical worker page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/worker.png)

#### - Senior management page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/senior.png)

#### - MySQL Table User

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/mysql.png)


## Question 3 (b)

#### 1. 

a

```
DELIMITER $$

CREATE TRIGGER insert_trigger AFTER INSERT ON listings_user
FOR EACH ROW
BEGIN
    INSERT INTO listings_user_replicated (id, `password`, last_login, is_superuser, username, email, is_staff, is_active, date_joined, `type`) 
    VALUES (NEW.id, NEW.`password`, NEW.last_login, NEW.is_superuser, NEW.username, NEW.email, NEW.is_staff, NEW.is_active, NEW.date_joined, NEW.`type`);
END;$$

DELIMITER ;
```

#### 2. 

a

```
CREATE TABLE listings_user_replicated (
    id INT PRIMARY KEY,
    password VARCHAR(128),
    last_login DATETIME,
    is_superuser BOOLEAN,
    username VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN,
    is_active BOOLEAN,
    date_joined DATETIME,
    type VARCHAR(20)
);
```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



