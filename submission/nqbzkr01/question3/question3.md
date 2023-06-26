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
    $ python -m venv env
    ```
  - Next, activate the virtual environment using:
    ```
    $ source env/bin/activate
    ```
  > Note: please note that on Windows, need to use `source env/Scripts/activate` in order to activate the virtual environment.
  - After activating the environment, you need to proceed by installing Django using `pip`:
    ```python
    $ pip install django
    ```
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
    mysql> create database moviedb;
    ```
- <strong>Creating a Django Project</strong>
  - Let's now create the project using `django-admin.py`. In the terminal, run the following command:
    ```
    $ django-admin.py startproject demoproject
    ```
  - Next, open the `settings.py` of your project and add the database address and credentials inside the `DATABASES` object.
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'moviedb',
        'USER': 'root',
        'PASSWORD': 'YOUR_DB_PASSWORD',
        'HOST': 'localhost',   
        'PORT': '3306',
        }    
    }
    ```
- <strong>Creating the `accounts` Application for User Authentication</strong>
  - Apps are the Django way of organizing a project. Think of them as modules. Let's encapsulate the authentication logic needed in our project into an accounts application. You obviously use any valid       name you see fit. Go to command prompt and navigate to the project's folder directory:
    ```
    $ cd demoproject
    ```
  - Next, create the application using `manage.py`:
    ```
    $ python manage.py startapp accounts
    ```
  - `manage.py` is another Django management script that may be found in the root project's folder. It's a great wrapper for the most commonly used Django administrative commands. The preceding command         will generate a Django application with a standard file structure. To include this app in your project, visit the `settings.py` file and add it to the `INSTALLED_APPS` array:
    ```
    INSTALLED_APPS = [
    # [...]
    'accounts'
    ]
    ```
  - That's it, now create the database and run Django development server using the following commands:
    ```
    $ python manage.py migrate
    $ python manage.py runserver
    ```
  - The command prompt will provide the link address at http://127.0.0.1:8000/. Paste the link address into the web browser to see the web application up and running.
- <strong>urls.py</strong>
  - Next, create the `urls.py` file in accounts app and add the following code:
    ```
    from django.contrib.auth import views
    from django.urls import path
    
    urlpatterns = [
    ]
    ```
  - Make sure `django.contrib.auth` is in `INSTALLED_APPS` in the `settings.py`.
- <strong>Create the Register View</strong>
  - Inside the `account` app, there is a file named `views.py`.
  - The views in views.py play a crucial role in defining the application logic and controlling the behavior of the web application in response to user interactions. They bridge the gap between the URL routing, data models, and templates, enabling Django to handle requests and generate responses effectively.
  - So let's create a simple register view first.
    ```
    from django.shortcuts import render, redirect
    from django.contrib.auth import login, authenticate
    from django.contrib import messages
    from django.contrib.auth.forms import UserCreationForm
    
    def home(request):
        return render(request, 'users/home.html')
    
    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
    
                messages.success(request, f'Your account has been created. You can log in now!')    
                return redirect('login')
        else:
            form = UserCreationForm()
    
        context = {'form': form}
        return render(request, 'users/register.html', context)
    ```
  - <strong>Templates</strong>
    - Inside the users app, we will create our templates. Inside the users directory, we will create a directory called templates. Then inside the templates directory, we will create another directory named users. Here we will put the html files. In this case home.html and register.html.
    ![Screenshot 2023-06-26 205311](https://github.com/drshahizan/SECP3843/assets/92329710/ee559aa0-82e6-4d3a-bf3a-30629bc717c6)
  - <strong>register.html</strong>
    ![Screenshot 2023-06-26 210048](https://github.com/drshahizan/SECP3843/assets/92329710/6084c90c-7aaf-46fb-a768-56249644d999)
  - <strong>urls.py</strong>
    - Modify the `urls.py` in `AA`.
      ![image](https://github.com/drshahizan/SECP3843/assets/92329710/b2d298c1-8624-4fab-8bda-25cf541122b0)





    


    
    
    
    
  
## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



