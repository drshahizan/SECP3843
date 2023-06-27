
<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: AHMAD AIMAN HAFIZI BIN MUHAMMAD
#### Matric No.: A20EC0177
#### Dataset: ANALYTICS DATASET

## Question 3 (a)

### Step 1: Navigate to Desktop

```python
cd Deskstop
```

### Step 2: Create virtual environment

```python
python -m venv envq3
```

### Step 3: Activate virtual environment

```python
envq3\Scripts\activate
```

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image1.png)

### Step 4: Create new Project and App

1. Go to  command prompt to creat new Django Project. Create a new app called mflixportal inside the project

2. Create project called `AnalyticsQ3`

```python
django-admin startproject AnalyticsQ3
```

3. Change directory

```python
cd AnalyticsQ3
```

4. Creata app called `AnalyticsQ3_app`

```python
py manage.py startapp AnalyticsQ3_app
```

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image2.png)

### Step 5: Configure settings.py

1. Go to `Desktop` > `AnalyticsQ3` > `AnalyticsQ3` > `settings.py`

2. Add `AnalyticsQ3_app` app inside *INSTALLED_APPS* section

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AnalyticsQ3_app'
]
```

3. Replace the original code with this one inside *DATABASE* section

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'analytics_q3',
	'USER': 'root',
	'HOST': 'localhost',
	'PORT': '3306',
    }
}
```

### Step 6: Configure models.py

1. Go to `Desktop` > `AnalyticsQ3` > `AnalyticsQ3_app` > `models.py`

2. Modify the existing code with this one

```python
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technical_worker = models.BooleanField(default=False)
    is_senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')
```

### Step 7: Configure views.py

1. Go to `Desktop`> `AnalyticsQ3` > `AnalyticsQ3_app` > `views.py`

2. Open `views.py` file using Microsot Visual Studio Code

3. Include the necessary library and place in at the top of the file

```python
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import is_customer, is_technical_worker, is_senior_management
from django.contrib.auth.decorators import user_passes_test
```

4. Define a function called `user_login` to handle the user login process below the library

```python
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

5. Define a function called `register` to handle the user registration process below the `user_login` function

```python
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

6. Define three dashbord views page based on their respective roles below the `register` function

```python
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

7. Define a function called `redirect_dashboard` to redirect each views page based on their respective roles

```python
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

7. Define a function called `user_logout` to handle user logging out if the system

```python
def user_logout(request):
    logout(request)
    return redirect('login')
```

### Step 8: Create a Registration Form

1. Open Visual Studio Code and go to `Desktop` > `AnalyticsQ3` > `AnalyticsQ3_app`

2. Create a new file called `forms.py`. The file must be place inside the `AnalyticsQ3_app`

3. Write down the code below inside the newly created `forms.py`

```python
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

### Step 9: Configure urls.py file

1. Go to `Desktop` > `AnalyticsQ3` > `AnalyticsQ3`

2. Open urls.py file using Microsoft Visual Studio Code

3. Replace the default codes with the codes below
   
```python
from django.contrib import admin
from django.urls import path
from AnalyticsQ3_app.views import register, user_login, redirect_dashboard, customer_dashboard, technical_worker_dashboard, senior_management_dashboard, user_logout

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

### Step 10: Create User Interface

1. Go to `Desktop` > `AnalyticsQ3` > `AnalyticsQ3_app`
   
2. Create a file called `login.html`

3. Type in the follwing code

```python
{% extends 'base.html' %} {% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```

4. Create a file called `register.html`

5. Type in the follwing code

```python
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

### Step 11: Install mysqlclient

1. Type in `pip install mysqlclient` in the command prompt

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image3.png)

### Step 12: Install decorators

2. Type in `pip install decorator` in the command prompt

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image4.png)

### Step 13: Create decorator.py file

```python
# decorators.py
from django.contrib.auth.decorators import user_passes_test

def is_customer(user):
    return user.is_authenticated and user.is_customer

def is_technical_worker(user):
    return user.is_authenticated and user.is_technical_worker

def is_senior_management(user):
    return user.is_authenticated and user.is_senior_management
```

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image4.png) 

### Step 14: Move files

1. Go to `Desktop` > `AnalyticsQ3` > `AnalyticsQ3_app`

2. Creata a folder called `templates`

3. Relocate the previous `registeration` and `login` files into this folder

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image9.png) 

### Step 15: Migrate Model

1. Go to command prompt.

2. Make migrations for the User model

```python
py manage.py makemigrations
```

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q4%20image5.png) 

3. Run migrations to apply changes in the MySql database

```python
py manage.py migrate
```

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image6.png) 

3. Check phpMyAdmin database if there is any changes

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image7.png) 

###Step 15: Go to page

1. Run server at the command prompt by typing in the code below

```python
py manage.py runserver
```

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image8.png) 

2. Register as a new user

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image10.png)

3. Log in as a user

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image11.png)

## Question 3 (b)

**MySql Replication**

> Data Replication is the process of storing data in more than one site or node.

> It is simply copying data from a database from one server to another server so that all the users can share the same data without any inconsistency.

> The result is a distributed database in which users can access data relevant to their tasks without interfering with the work of others.

> Replication allows the contents of the master database server to be replicated to the other database server

**Step 1**

- Login to phpMyAdmin panel and then click the `replication` tab on the top ribbon

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image12.png)

**Step 2**

- Click on the *configure* option under the `Primary replication` section

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image13.png)

The primary replication section will expand

**Step 3**

- Select the option `Ignore all database; Replicate:

- Then select the database named `analytics_q3` or whatever database that needs to be replicated

- Copy the lines shown belown the list. In this case, this is my server-id

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image14.png)

```python
server-id=4833576
log_bin=mysql-bin
log_error=mysql-bin.err
binlog_do_db=analytics_q3
```

**Step 4**

- Open Xampp Control Panel

- Click the `Config` button and choose the `my.ini` option

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image15.png)

**Step 5**

- A notepad will open

- Navigate further down and look  for `log_error` parameter

- Paste the server-id code from phpMyAdmin

- Change the `max_allowed-packet` from `1M` to `16M`

![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%203/files/images/Q3%20image16.png)











## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



