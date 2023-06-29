<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Qaisara binti Rohzan
#### Matric No.: A20EC0133
#### Dataset: 04 - Companies

## Question 3 (a)
This segment of Question 3. (a) is similar to Question 1. (a) and is divided into several parts:
* [Prerequisites](#-prerequisites)
* [Setting Up A Django Project](#️-setting-up-a-django-project)

### Prerequisites
To carry out this segment of the question, it it crucial me for to do the following:
1. Install [Python](https://www.python.org/downloads/)
2. Install [Visual Studio Code](https://code.visualstudio.com/download)
<br></br>


### Setting Up A Django Project

**Django Installation** 

1. Create a Django Project Folder. For this project I created a folder named **AA** on my **Desktop**, where it is easily accessible.
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Create%20Project%20Folder.png">
</p>
     
<br>

2. Set up a virtual environment. In your current working directory, this command creates a new virtual environment called ``environment``. 
```bash
python -m venv environment
```
<br>

3. Activate the virtual environment. When the process is finished, you must additionally activate the virtual environment.
```bash
environment\Scripts\activate
```
<br>
   
4. Install Django.
```bash
pip install django
```
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Django%20Installation.png">
</p>
<br>

5. Install necessary packages. Here we are installing  packages that allows integration between our Django App and MongoDB, those packages are **MySQL Client PyMongo** and **Djongo**. Djongo is a smarter approach to database querying. It maps python objects to MongoDB documents. 
```bash
pip install django mysqlclient pymongo
pip install djongo
```
Below are the output when running the commands:
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Install%20Django%20MySQLClient%20PyMongo.png">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Install%20Djongo.png">
</p>
<br></br>

**Create A Django Project** 

You can now create a new project after setting up, activating your virtual environment and installing Django. To start a new Django project, open a new terminal in Visual Studio Code and run the following command. The project is named **Companies** in the code below, but it can be changed to any name you like.
```bash
python -m django startproject Q3
```
Navigate yourself to the project directory by inputing the command below:
```bash
cd Q3
```

<br></br>

**Create A Django Application** 

The  ``startapp `` command generates a default folder structure for a Django app. This tutorial uses **DjangoApp** as the name for the app:
```bash
python manage.py startapp DjangoApp
```
<br></br>

**Configure Database Connection** 

Set up the MySQL and MongoDB connections. Alter the code for the databases and installed apps in the Django project's **settings.py** file as shown below.
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_login_required',
    'DjangoApp'
]
```
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}
```
<br></br>

 **Create Model** 
 ```bash
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups',
        blank=True, 
        related_name='user_set', 
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='user_set',
        related_query_name='user',
    )

    def __str__(self):
        return self.username
```
In **settings.py**, set AUTH_USER_MODEL to the custom user model to make it the default authentication model.
```bash
AUTH_USER_MODEL = 'DjangoApp.CustomUser'
```
<br></br>

**Perform Database Migration** 

**makemigrations** provides SQL instructions for preinstalled apps and my **CustomUser model**, meanwhile **migrate** runs the SQL commands stored in the database file. So, after running migrate, all of my CompaniesApp's tables are created in the database file. Please establish an empty MySQL database named **aa** beforehand to assure this.
```bash
 python manage.py makemigrations
 python manage.py migrate
```
Check your MySQL database (XAMPP > MySQL > Start > Admin) to confirm this migration procedure.

<br></br>

**Create Admin Site** 

Go to **admin.py** to classify your own admin site. This will allow admins to register on a site of their own.
```bash
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('user_type',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
```
<br></br>

**Create Registration Login View** 

Here is the code for my DjangoApp **views.py** file that defines the user registration and login processes.
```bash
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required

def registerUser(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'customer'
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)

            msg = "User created."
            success = True
            return redirect('login')
        else:
            msg = "Form is not valid."
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success})

def loginView(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if user.user_type == 'customer':
                    return redirect('customer_home')
                elif user.user_type == 'technical_worker':
                    return redirect('technical_worker_home')
                elif user.user_type == 'senior_management':
                    return redirect('management_home')
                else:
                    return redirect('home')
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

@login_required(login_url="/login/")
def customer(request):
    context = {'segment': 'index'}
    return render(request, "home/customer_home.html", context)

@login_required(login_url="/login/")
def technical_worker(request):
    context = {'segment': 'index'}
    return render(request, "home/technical_worker_home.html", context)

@login_required(login_url="/login/")
def management(request):
    context = {'segment': 'index'}
    return render(request, "home/management_home.html", context)
```


## Question 3 (b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



