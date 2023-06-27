<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kelvin Ee
#### Matric No.: A20EC0195
#### Dataset: City Inspection

## Question 3 (a)

### 1. To install and set up Django, follow these steps:

a. Open the command prompt or terminal.

b. Run the command `pip install Django` to install Django using pip, the Python package manager. Make sure you have Python and pip installed on your system.

c. After the installation is complete, you can create a new Django project by running the following command:   
```python
django-admin startproject q3
```
This command will create a new Django project with the name "q3". You can replace "q3" with your desired project name.

d.Once the project is created, navigate to the project folder using the cd command. In this case, run:
<img src="./files/image/q3.png">

### MySQL setup

1. To set up MySQL for your Django project, follow these steps:

Install the MySQL connector for Python by running the command `pip install mysql-connector-python`. This package allows Django to communicate with the MySQL database.

<img src="./files/image/mysql.png">

2. After the installation is complete, create a new database named q3 in phpMyAdmin. This will be the database where your Django project will store its data.

3. Open the `settings.py` file in your Django project and locate the DATABASES configuration. Modify it to match the following configuration:

```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'q3',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Create a Django app

1. Create Django app by running
```bash
python manage.py startapp q3_app
```

2. Go to setting and update this part:
```kotlin
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'q3_app',
]
```
### Define the User model

1. Go to `model.py` file in q3_app and define the User model for authentication

```ruby
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    # Add any additional fields you need for each user type

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
```
2. Run the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
<img src="./files/image/migrate.png">

### Create registrations views and templates

1. Create new file called `forms.py`

```python
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=User.USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'user_type']
```

2. Create a new view in your app's views.py file to handle registration:

```python
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Replace 'login' with the URL name of your login page
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})
```
3. Create new direcotry and file

```kotlin
q3_app/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── urls.py
├── views.py
└── templates/
    └── registration/  <--- New directory
        └── user_registration.html  <--- New file
```

4. User registration form `user_registration.html`

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Register</button>
</form>
```
5. Go to setting.py and initiallize path:

```rust
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'q3_app/templates/registrations'),
            os.path.join(BASE_DIR, 'q3_app/templates/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
### Create login views and templates

1. Add a new class inside `forms.py`

```python 
class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
```

2. Add a new method inside views.py file to handle login:

```python 
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

  def customer_dashboard_view(request):
    return render(request, 'customer_dashboard.html')

  def technical_worker_dashboard_view(request):
        return render(request, 'technical_worker_dashboard.html')
    
  def management_dashboard_view(request):
        return render(request, 'management_dashboard.html')
```

3. Create login form:

```html
<div style="background-color: rgb(86, 86, 175); padding: 20px;">
    <div style="max-width: 400px; margin: 0 auto; background-color: white; padding: 20px;">
        <h1 style="text-align: center; font-family: 'Comic Sans MS', cursive; color: navy;">Login</h1>

        <form method="POST" action="{% url 'login' %}">
            {% csrf_token %}

            <div style="margin-bottom: 10px;">
                <label for="id_username">Username:</label>
                <input type="text" id="id_username" name="username" class="form-control">
            </div>

            <div style="margin-bottom: 10px;">
                <label for="id_password">Password:</label>
                <input type="password" id="id_password" name="password" class="form-control">
            </div>

            <div style="text-align: center;">
                <button type="submit" class="btn btn-primary">Login</button>
            </div>

            {% if messages %}
            <div style="text-align: center; color: red; margin-top: 10px;">
                {% for message in messages %}
                <p>{{ message }}</p>
                {% endfor %}
            </div>
            {% endif %}
        </form>

        <p style="text-align: center; font-family: 'Comic Sans MS', cursive; color: navy;">
            Don't have an account? <a href="{% url 'user_registration' %}">Register</a>
        </p>
    </div>
</div>

```

4. Create 3 dashboard for each user:

`customer_dashboard.html`
`management_dashboard.html`
`technical_worker_dashboard.html`

### Path setting and run the App

1. Go to urls.py and add necessary path for each page

```python
from django.contrib import admin
from django.urls import path, include
from q3_app.views import user_registration, login_view, customer_dashboard_view, technical_worker_dashboard_view, management_dashboard_view

urlpatterns = [
    path('customer_dashboard/', customer_dashboard_view, name='customer_dashboard'),
    path('technical_worker_dashboard/', technical_worker_dashboard_view, name='technical_worker_dashboard'),
    path('management_dashboard/', management_dashboard_view, name='management_dashboard'),
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('register/', user_registration, name='user_registration'),
]

```

2. Open terminal and run `python manage.py runserver`

   

## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




