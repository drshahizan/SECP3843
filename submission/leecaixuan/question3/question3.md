<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Cai Xuan
#### Matric No.: A20EC0062
#### Dataset: Analytics Dataset

## Question 3 (a)

<h4>Step 1 - Create and connect database</h4>

Create a database, 'aa_system' in MySQL database. In the aa_system VS code project file, connect to the database in the settings.py file.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa_system',
        'USER': 'root',
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}
```
<h4>Step 2 - Migrate into database</h4>

Create a new file named 'urls.py' to create the urls that direct users to different view page. 

```
from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name= 'index'),
      path('login/', views.login_view, name='login_view'),
      path('register/', views.register, name='register'),
      path('admin/', views.admin, name='admin'),
      path('customer/', views.customer, name='customer'),
      path('technical/', views.technical, name='technical'),
      path('senior/', views.senior, name='senior'),
]
```

After that, create models consist of users (Admin, Customer, Technical Workers, Senior Manager) in the models.py file.

```
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_technical = models.BooleanField('Is technical', default=False)
    is_senior = models.BooleanField('Is senior', default=False)
```

In the terminal, migrate using ```py manage.py makemigrations``` and ```py manage.py migrate```. The database will be update din the MySQL database.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/database.png" />
</p>

<h4>Step 3 - Create file for each view page</h4>

The image below shows the view file for each page.
<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/templates.png" />
</p>

- admin.py
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin page</title>
</head>
<body>
    <h1> hello {{ user.username }} Your user role is Admin</h1>
</body>
</html>
```

- base.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js" integrity="sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS" crossorigin="anonymous"></script>
    <!-- Add your additional CSS links or stylesheets here -->
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <!-- Add your additional JavaScript scripts or links here -->
</body>
</html>
```

- customer.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Customer page</title>
</head>
<body>
    <h1> hello {{ user.username }}  Your user role is Customer</h1>
</body>
</html>
```

- index.py

```
{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to your homepage!</h1>
    
{% endblock %}
```

- login.py

```
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

    <title>Multiple user login</title>
  </head>
  <body>
  <div class="content">
    <div class="container">
      <div class="row justify-content-center">
        <!-- <div class="col-md-6 order-md-2">
          <img src="images/undraw_file_sync_ot38.svg" alt="Image" class="img-fluid">
        </div> -->
        <div class="col-md-6 contents">
          <div class="row justify-content-center">
            <div class="col-md-12">
              <div class="form-block">
                  <div class="mb-4">
                </div>

              <span class="mb-0 text-muted">
                {% if msg %}
                    {{ msg | safe }}
                {% else %}
                    Login page
                {% endif %}
              </span>
                <form  method="post">
                    {% csrf_token %}
                  <div class="form-group first">
                    <label for="username">Username</label>
                      {{ form.username }}
                  </div>
                  <div class="form-group last mb-4">
                    <label for="username">Password</label>
                    {{ form.password }}
                  </div>

                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">Remember me</span>
                      <input type="checkbox" checked="checked"/>
                      <div class="control__indicator"></div>
                    </label>
                    <span class="ml-auto"><a href="#" class="forgot-pass">Forgot Password</a></span>
                  </div>

                  <input type="submit" value="Log In" class="btn btn-pill text-white btn-block btn-primary">
                </form>
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

- register.py

```
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

    <title>Multiple user login</title>
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
                      <h1>User Registration page</h1>
                </div>
                  <span class="mb-0 text-muted">
                {% if msg %}
                    {{ msg | safe }}
                {% else %}
                    Login page
                {% endif %}
              </span>
                <form  method="post">
                    {% csrf_token %}
                  <div class="form-group first">
                    <label for="username">Username</label>
                      {{ form.username }}
                  </div>
                  <div class="form-group first">
                    <label for="email">Email</label>
                      {{ form.email}}
                  </div>
                  <div class="form-group last mb-4">
                    <label for="password">Password</label>
                      {{ form.password1 }}
                  </div>
                  <div class="form-group last mb-4">
                    <label for="password">confirm Password</label>
                      {{ form.password2 }}
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">Admin</span>
                        {{ form.is_admin }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">customer</span>
                        {{ form.is_customer }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">technical worker</span>
                        {{ form.is_technical }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">Senior Management</span>
                        {{ form.is_senior }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                    <span class="text-error">{{ form.errors }}</span>
                  <input type="submit"  value="Register" class="btn btn-pill text-white btn-block btn-primary">
                </form>
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

- senior.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Senior Manager page</title>
</head>
<body>
    <h1> hello {{ user.username }}  Your user role is Senior Manager</h1>
</body>
</html>
```

- technical.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Technical Worker page</title>
</head>
<body>
    <h1> hello {{ user.username }}  Your user role is Technical Worker</h1>
</body>
</html>
```

<h4>Step 4 - Create registration form</h4>

```
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
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_customer', 'is_technical', 'is_senior')
```

<h4>Step 5 - Create superuser for testing system</h4>

Use this command line ```python manage.py createsuperuser``` to create a new superuser.

User Interfaces

- Registration Page
  
<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/register%20page.png" />
</p>

- Login Page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/Screenshot%202023-06-29%20015540.png" />
</p>

- Customer Page

<p align="center">
  <img height="100px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/customer.png" />
</p>

- Technical Workers Page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/technical.png" />
</p>

- Senior Manager Page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/senior%20manager.png" />
</p>

- Superuser view users page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/user%20view%20page.png" />
</p>

- Edit users page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/edit%20user.png" />
</p>




## Question 3 (b)





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


