<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURFARRAHIN BINTI CHE ALIAS
#### Matric No.: A20EC0121
#### Dataset: Mflix

## Question 3 (a)
On this project, the module for managing user registration and login will be placed in the mySQL database. This system is used by three types of people: customers, technical workers, and senior management. Describe in detail the creation of this module on the web server (Django) and the database (mySQL).

**PREQUISITES**
- install Visual Studio Code
- Install Python in your computer

**create a file project for Mflix**

![Screenshot (291)](https://github.com/drshahizan/SECP3843/assets/121208097/1122a1bd-1ca8-4bea-bb35-e258e16700fe)

1. setup your virtual environment

![Screenshot (294)](https://github.com/drshahizan/SECP3843/assets/121208097/32bc8a5d-e9ba-41f1-9a52-8a0885b55f70)

2. To start a Django project, enter django-admin startproject mflix. Inside the project, create a new application called mflixportal.

![Screenshot (296)](https://github.com/drshahizan/SECP3843/assets/121208097/1bbbaab1-4cb5-43eb-982f-67f0486fbf0a)

3. Open the settings.py file inside the Mflix project, set the MySQL database to my settings, and add the new app under INSTALLED_APPS.


![Screenshot (299)](https://github.com/drshahizan/SECP3843/assets/121208097/9d4247e5-087c-4f97-8fdd-777286b2bfb8)

 ![Screenshot (300)](https://github.com/drshahizan/SECP3843/assets/121208097/b5fad6f6-7265-489d-928b-a54111e1e971)

 4. Design the models

```
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    cust = models.BooleanField(default=False)
    TechnicalWorker = models.BooleanField(default=False)
    SeniorManagement = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')
```

 5. create views

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
 
 6. for the registration code

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
 
 7. as for the dashboard, i will be using seperate ones
 
 ```
 @login_required
def profile(request):
    user = request.user
    
    return render(request, 'profile.html', {'user': user})

@user_passes_test(Cust)
def customer_dashboard(request):
    
    return render(request, 'customer_dashboard.html')

@user_passes_test(TechnicalWorker)
def technical_worker_dashboard(request):
    
    return render(request, 'technical_worker_dashboard.html')

@user_passes_test(SeniorManagement)
def senior_management_dashboard(request):
    
    return render(request, 'senior_management_dashboard.html')
def redirect_dashboard(request):
    user = request.user
    if user.Cust:
        return redirect('customer_dashboard')
    elif user.TechnicalWorker:
        return redirect('technical_worker_dashboard')
    elif user.SeniorManagement:
        return redirect('senior_management_dashboard')
    else:
        
        return redirect('profile')
```
 8.  Create a manage registration form

```
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Cust', 'Customer'),
        ('TechnicalWorker', 'Technical Worker'),
        ('SeniorManagement', 'Senior Management'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')

        if role == 'Customer':
            user.Cust = True
        elif role == 'TechnicalWorker':
            user.TechnicalWorker = True
        elif role == 'SeniorManagement':
            user.SeniorManagement = True

        if commit:
            user.save()
        return user
```

9. manage logout

```
def user_logout(request):
    logout(request)
    return redirect('login')
```

10.  inside the url.py
 
```
from django.contrib import admin
from django.urls import path
from dashboard.views import register, user_login, redirect_dashboard, customer_dashboard, technical_worker_dashboard, senior_management_dashboard, user_logout

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
 10.  **Create the basic html page to view the login view and dashboard**

**Register**

  ```
  {% extends 'Index.html' %} {% block content %}
<h3>Register</h3>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">REGISTER</button>
</form>
<br />
<text>Have an account?</text><a href="{% url 'login' %}">Sign In</a>
{% endblock %}

```

**Login**

```
{% extends 'Index.html' %} {% block content %}
<h3>LOGIN</h3>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
```


 11.  Lastly,migrate the dataeset using this command

     ```
     python manage.py makemigrations
    python manage.py migrate


## Question 3(b)

The difficulty of Data Replication and Synchronisation between the MySQL and MongoDB databases occurs while working with two separate databases. To ensure data consistency between the two systems, it is necessary to make sure that any changes made in one database are appropriately reflected in the other. It is advised to investigate database-specific replication solutions or make use of outside tools that provide real-time updates and flawless communication across the databases in order to resolve this problem. Give a thorough breakdown of the procedures you used to solve this problem in your response. You can add pertinent screenshots and snippets of code that show how the solution was used.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


