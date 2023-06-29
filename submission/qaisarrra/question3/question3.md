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
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_technical_worker = models.BooleanField(default=False)
    is_senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set', related_query_name='user')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set', related_query_name='user')

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


**Create Registration and Login View** 

Here is the code for my DjangoApp **views.py** file that defines the user registration and login processes.

The **Login** functionality
```bash
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import is_customer, is_technical_worker, is_senior_management
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('User: ', user)
            if user is not None:
                 login(request, user)
                 print('User logged in')
                 return redirect('home')
            else:
                 print("Invalid username or password.")
                 return redirect('login')
            
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
```

The **Register** functionality
```bash
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
```

These are other **views** processes that will help users to navigate arounf the portal

```bash
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
    
def user_logout(request):
    logout(request)
    return redirect('login')

```

**Create Registration Form** 

In the DjangoApp folder, create a registration form file named **forms.py**
```bash
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
        fields = ['username', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        role = self.cleaned_data['role']
        
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

## Question 3 (b)
The difficulty of Data Replication and Synchronisation between the MySQL and MongoDB databases occurs while working with two separate databases. This issue entails making sure that any changes made in one database are appropriately mirrored in the other, ensuring data consistency across both systems. To address this issue, we can do as follows:

**Open phpMyAdmin**

Once you're directed to the main page of phpMyAdmin, click on the **Replication** tab on the ribbon navigation bar. Here, in the **Primary Replication** container, click **configure**.
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Open%20PHPMyAdmin.png">
</p>

You will then be directed to **Replication** page. Ensure that you have chose **Ignore all databases: Replicate**
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Primary%20configuration.png">
</p>
<br></br>

**Open XAMPP Control Panel**

From the control panel, click on MySQL's **config** button, then click on the **my.ini** file. From the primary configuration page, copy the four lines to be pasted in the my.ini file.
```bash
server-id=5182973
log_bin=mysql-bin
log_error=mysql-bin.err
binlog_do_db=aa
```

<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/My%20Ini%20file.png">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Log%20Error.png">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Save%20file.png">
</p>
     
<br></br>

**Restart Apache and MySQL**

After restarting both Apache and MySQL, reload the replication page and explore it's functionalities


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



