<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Muhammad Naquib Bin Zakaria
#### Matric No.: A20BE0161
#### Dataset: 03 - Movie

## Question 3 (a)
<h4>Create module for managing user registration using and login using Django and MySQL</h4>

1. Initial setup
- <strong>Creating a Virtual Environment for Django Project</strong>
  - A virtual environment allows you to isolate your current project dependencies from the rest of packages installed globally on your system or in the other virtual environments. You can either use `virtualenv` which needs to be installed on your system or the `venv` module available as a module in recent versions of Python 3.
  - Type this in command prompt:
    ```
    $ python -m venv venv
    ```
    ![image](https://github.com/drshahizan/SECP3843/assets/92329710/d2c8c33b-2e87-424f-a1b6-3de07e508fd3)

  - Next, activate the virtual environment using:
    ```
    $ source env/Scripts/activate.bat
    ```
    ![image](https://github.com/drshahizan/SECP3843/assets/92329710/75762a4f-881e-4c54-b1e5-5b2fbac52eb8)

  > Note: please note that on Windows, need to use `source env/Scripts/activate` in order to activate the virtual environment.
  - After activating the environment, you need to proceed by installing Django using `pip`:
    ```python
    $ pip install django
    ```
    ![image](https://github.com/drshahizan/SECP3843/assets/92329710/fed732ad-4e93-4466-9613-49bd6c320b0c)

  - If the framework is successfully installed, the Django management commands now can be used to create and work with the Django project.
  - Next, install mysql-client using:
    ```python
    $ pip install mysqlclient
    ```
- <strong>Creating a MySQL Database to Store Authentication Info</strong>
  - In the command prompt invoke the `mysql` client using the following command:
    ```
    $ mysql -u root -p
    ```
  - The command prompt will ask the MySQL password then enter the password and hit Enter.
  - After that, run the following SQL statement to create a database:
    ```
    mysql> create database dbAA;
    ```
- <strong>Creating a Django Project</strong>
  - Let's now create the project using `django-admin.py`. In the terminal, run the following command:
    ```
    $ django-admin.py startproject AA
    ```
  - Next, open the `settings.py` of your project and add the database address and credentials inside the `DATABASES` object.
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbauth',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
    }
}
    ```
- <strong>Creating the `users` Application for User Authentication</strong>
  - Apps are the Django way of organizing a project. Think of them as modules. Let's encapsulate the authentication logic needed in our project into an accounts application. You obviously use any valid       name you see fit. Go to command prompt and navigate to the project's folder directory:
    ```
    $ cd authsysproject
    ```
  - Next, create the application using `manage.py`:
    ```
    $ python manage.py startapp users
    ```
- <strong>Configure models.py</strong>
  - Next, configure the `models.py` file in users app and add the following code:
    ```
    from django.db import models
    from django.contrib.auth.models import AbstractUser, Group, Permission
    # Create your models here.
    
    class User(AbstractUser):
        is_customers = models.BooleanField(default=False)
        is_technical_workers = models.BooleanField(default=False)
        is_senior_management = models.BooleanField(default=False)
    
        groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    
        user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')

    ```
  - Make sure `django.contrib.auth` is in `INSTALLED_APPS` in the `settings.py`.
  - `manage.py` is another Django management script that may be found in the root project's folder. It's a great wrapper for the most commonly used Django administrative commands. The preceding command         will generate a Django application with a standard file structure. To include this app in your project, visit the `settings.py` file and add it to the `INSTALLED_APPS` array:
    ```
    INSTALLED_APPS = [
    # [...]
    'users'
    ]
    ```
  - That's it, now create the database and run Django development server using the following commands:
    ```
    $ python manage.py migrate
    $ python manage.py runserver
    ```
  - The command prompt will provide the link address at http://127.0.0.1:8000/. Paste the link address into the web browser to see the web application up and running.
- <strong>urls.py</strong>
  - Next, configure the `urls.py` file in users app and add the following code:
    ```
    from django.urls import path
    from . import views
    from django.contrib.auth import views as auth_view
    
    urlpatterns = [
      path('', views.home, name='home'),
      path('register/', views.register, name='register'),
      path('profile/', views.profile, name='profile'),
      path('login/', views.user_login, name='login'),
      path('customerindex/', views.customerindex, name='customerindex'),
      path('technicalindex/', views.technicalindex, name='technicalindex'),
      path('seniorindex/', views.seniorindex, name='seniorindex'),
      path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    ]
    ```
  - Make sure `django.contrib.auth` is in `INSTALLED_APPS` in the `settings.py`.
- <strong>views.py</strong>
  - Next, configure the `views.py` file in users app and add the following code:
    ```
    from django.shortcuts import render, redirect
    from django.contrib.auth.forms import UserCreationForm
    from . forms import UserRegisterForm
    from django.contrib import messages
    from django.contrib.auth.decorators import login_required
    from django.contrib.auth import authenticate, login
    # Create your views here.
    
    
    def home(request):
        return render(request, 'users/home.html')
    
    def user_login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                username = user.username
                message = f"Hello {username}!"
                if user.is_customers == 1:
                    messages.success(request, message)
                    return redirect('customerindex')
                elif user.is_technical_workers == 1:
                    messages.success(request, message)
                    return redirect('technicalindex')
                elif user.is_senior_management == 1:
                    # Redirect to a success page.
                    messages.success(request, message)
                    return redirect('seniorindex')
            else:
                # Return an 'invalid login' error message.
                ...
                messages.success(request, "Wrong Username or Password!")
                return redirect('login')
        else:
            return render(request, 'users/login.html', {})
    
    def register(request):
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Hi {username}, your account was created successfully')
                return redirect('home')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    @login_required()
    def profile(request):
        return render(request, 'users/profile.html')
    
    def customerindex(request):
        return render(request, 'users/customerindex.html')
    
    def technicalindex(request):
        return render(request, 'users/technicalindex.html')
    
    def seniorindex(request):
        return render(request, 'users/seniorindex.html')
    ```
- <strong>Register Page</strong>
  - So let's create a simple register view first.
  - Create `register.html` under `templates/users` folder.
    ```
    {% extends 'users/base.html' %}
    {% load crispy_forms_tags %}
    {% load static %}
    
    
    {% block content %}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
        <div class="container" style="margin-top: 30px;">
        <form action="" method="POST">
          {% csrf_token %}
          <fieldset class="form-group">
              <legend class="border-bottom mb-4" style="color: white;">Join Now</legend>
              {{ form|crispy }}
          </fieldset>
          <div class="form-group" id="signup-button">
              <button class="btn ">Sign Up</button>
          </div>
          <div class="form-group">
              <small class="text-muted ml-3" >Already have an account? <a href="">Sign In</a></small>
          </div>
        </form>
        </div>
    {% endblock content %}
    ```
  - Here is how the register looks like:
  ![image](https://github.com/drshahizan/SECP3843/assets/92329710/280af21e-4c74-473e-9ee2-0b11641f3b85)
- <strong>Login Page</strong>
  - So let's create a simple login view first.
  - Create `login.html` under `templates/users` folder.
    ```
    {% extends 'users/base.html' %}
    {% load crispy_forms_tags %}
    {% load static %}
    
    
    {% block content %}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
        <div class="container" style="margin-top: 30px;">
        <form action="" method="POST">
          {% csrf_token %}
          <fieldset class="form-group">
              <legend class="border-bottom mb-4" style="color: white;">Join Now</legend>
              {{ form|crispy }}
          </fieldset>
          <div class="form-group" id="signup-button">
              <button class="btn ">Sign Up</button>
          </div>
          <div class="form-group">
              <small class="text-muted ml-3" >Already have an account? <a href="">Sign In</a></small>
          </div>
        </form>
        </div>
    {% endblock content %}
    ```
  - Here is how the login page looks like:
  ![image](https://github.com/drshahizan/SECP3843/assets/92329710/2d01b714-7ad2-42e6-8cb8-c575a41a01bd)




  






    


    
    
    
    
  
## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



