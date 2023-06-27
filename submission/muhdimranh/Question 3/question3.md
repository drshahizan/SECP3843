<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: MUHAMMAD IMRAN HAKIMI BIN MOHD SHUKRI
#### Matric No.:A20EC0213
#### Dataset:AIRBNB

## Question 3 (a)

This module are divided into two parts which include Register and Login. In order to create this module on Django:

### Step 1: Database Configuration

To start developing the User module for the Airbnb Booking Portal, the first step is to configure the database settings. In this project, MySQL is used as the database engine. Below is the code that I have used to configure the database in `settings.py`:

```
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
		'NAME': 'airbnbportal',
		'USER': 'root',
		'HOST':'localhost',
		'PORT':'3306',     
        },

	'mongodb': {
		'ENGINE': 'djongo',
        'NAME': 'airbnbportal',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
        'host': 'mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/'
	}
}
}
```

### Step 2: Defining User Model

The next step is to define the User model for the Airbnb Booking Portal. The User model will extend Django's AbstractUser model and include additional fields to represent user roles. In `models.py`,

```
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technical_worker = models.BooleanField(default=False)
    is_senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')
```

### Step 3: Creating Views

After defining the User model, the next step is to create the views that handle user registration, login, profile, and role-based dashboards. In `views.py`,

> Importing necessary libraries

```
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import is_customer, is_technical_worker, is_senior_management
from django.contrib.auth.decorators import user_passes_test
```

> Implement the `user_login` view function to handle user login

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

> Implement the `register` view function to handle user registration

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

> Implement separate dashboard views for each user role (`customer_dashboard`, `technical_worker_dashboard`, `senior_management_dashboard`)

```
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

> Implement the `redirect_dashboard` view function to redirect the user to their respective dashboard based on their role

```
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

> Implement the `user_logout` view function to handle user logout

```
def user_logout(request):
    logout(request)
    return redirect('login')
```

### Step 4: Define Registration Form

In order to register users with their selected roles, a custom registration form needs to be created. In `forms.py`,

```
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

### Step 5: Configure URLs

The next step is to configure the URL patterns for the User module in the `urls.py` file.

```
from django.contrib import admin
from django.urls import path
from AirbnbBookingPortal.views import register, user_login, redirect_dashboard, customer_dashboard, technical_worker_dashboard, senior_management_dashboard, user_logout

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

### Step 6: Create Templates

Create the required HTML templates for user registration, login, profile, and role-based dashboards.

> `login.html`: Render the login form.

```
{% extends 'base.html' %} {% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```

> `register.html`: Render the registration form.

```
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

> `profile.html`: Display the user's profile information.
> `customer_dashboard.html`: Dashboard for customers.
> `technical_worker_dashboard.html`: Dashboard for technical workers.
> `senior_management_dashboard.html`: Dashboard for senior management.

### Step 7: Apply Migrations

To apply the changes made to the database models, run the following command in the terminal:

```
python manage.py makemigrations
python manage.py migrate
```

### Below shows the full implementation of user module.

> After defining User model, a custom User table will be created. In this case, there will be three tables created that follows django user authentication.

![Q3](files/images/q3.1.png)

> Run migration to apply changes to database.

![Q3](files/images/q3.2.png)

> In the register page, enter all required fields and click on Submit. This will proceed with registration and store information in database.

![Q3](files/images/q3.3.png)

![Q3](files/images/q3.8.png)

> In the login page, enter all required fields and click on Login. This will redirect users to different dashboards or pages depending on the role.

![Q3](files/images/q3.4.png)

![Q3](files/images/q3.5.png)

![Q3](files/images/q3.6.png)

![Q3](files/images/q3.7.png)

> Click on Logout to logout from session.



## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




