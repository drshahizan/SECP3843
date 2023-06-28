<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Sakinah Al'izzah Binti Mohd Asri
#### Matric No.: A20EC0142
#### Dataset: [Analytics](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 3 (a)

Here's an overview of the step-creating module that manages user registration and login:

### Step 1: Start with set up the environment, Django project and Django App

1. Creating a virtual environment using the command `virtualenv env`.

2. Activating the virtual environment using the command `.\env\Scripts\activate`.

3.  Check if Django is installed using `pip show django`. If not, install it with `pip install django`.

    <img src="https://github.com/drshahizan/SECP3843/assets/99240177/3dfa2840-536e-4e8d-91b3-7e2f6c2b685c" />

4. Create a new Django Project using the command `django-admin startproject analytics`

5. Create a new Django app within the analytics directory, and execute the command `python manage.py startapp financialAnalytics`.

   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/d523bb25-d9f3-4b97-903f-8452ee38584d" />

6. Define the created app at settings.py file under the INSTALLED_APPS configuration.

 ```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'financialAnalytics',
]
```

### Step 2: Django Configuration

1. Install the mysqlclient package using the command `pip install mysqlclient` to connect MySQL database and Python.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/04c1b71f-2efe-4bbe-961f-9ca95d44506f" />

### Step 3: Setting Database configuration

1.  To update the database setting, navigate to the setting.py file.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_analytics',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'unix_socket': '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
        },
    },
}
 ```
### Step 4: Create User Model

1.  In the financialAnalytics App insert the custom user model and import Django's AbstractUser class.

```
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
   ROLE_TYPES = (
       ('customer', 'Customer'),
       ('technical_worker', 'Technical Worker'),
       ('senior_management', 'Senior Management'),
   )
   
   roleTypes = models.CharField(max_length=20, choices = ROLE_TYPES)

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
2. Specify the custom user model in the project's settings.py file.
```
AUTH_USER_MODEL = 'financialAnalytics.CustomUser'
```

### Step 5: Run Database Migrations

1. To apply the database migrations and create the required tables for the user model, execute the following command.

```
python manage.py makemigrations
python manage.py migrate
```
<img src="https://github.com/drshahizan/SECP3843/assets/99240177/8c28411e-cd8d-4516-bb3d-85e103064ce4" />
<img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/d04788ea-5681-43b5-bd87-642cb547821e" />

### Step 6: Create registration and login Views with applied templates

1.  create `forms.py` file inside the Django App directory. The following code defines both registration and login forms.

```
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'}),
  )
  password2 = forms.CharField(
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm your password'}),
  )
  role = forms.ChoiceField(choices=CustomUser.ROLE_TYPES)

  class Meta:
    model = User
    fields = ('name', 'email', 'password1', 'password2', 'role')

    widgets = {
      'name': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'enter your name'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control',
          'placeholder': 'enter your email'
      })
    }

class LoginForm(AuthenticationForm):
  email = EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your email"}))
  password = forms.CharField(
      label=_("Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your email password"}),
  )

```
2. Open `views.py` file inside the Django App directory. The following code defines both registration and login views.

```
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import logout

class UserLoginView(LoginView):
  template_name = 'login.html'
  form_class = LoginForm

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = RegistrationForm()
    return render(request, 'register.html', { 'form': form })

def logout_view(request):
  logout(request)
  return redirect('login')
```
   
3. Open `settings.py` file, update the TEMPLATES as follows:
```
ANALYTICS_TEMPLATES = os.path.join(BASE_DIR, 'financialAnalytics', 'templates')

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ANALYTICS_TEMPLATES],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

### Step 7: Define the URL

1. Open `urls.py` file to map the registration and login views to their respective URLs.
```
from django.urls import path
from finanAnalytics import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
```

### Step 8: Start Django development server

1. Run `python manage.py runserver`

### User Interfaces (output)
1. Register page
   
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/6fe3193d-07ca-49ce-b1f7-d9cecf6bbb75" width="400" alt="Image">
   
2. Login Page

   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/f04f3db1-6ea9-48a5-b140-dbbd693b5811" width="400" alt="Image">
   
4. Customer page

   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/d0ccdec2-b757-4c7c-bc90-4e4d7bb6dd66" width="400" alt="Image">

6. Technical workers page

    <img src="https://github.com/drshahizan/SECP3843/assets/99240177/0aa880cc-3b5a-4415-8143-dcf9c131a9c9" width="400" alt="Image">
   
8. Senior Management page

    <img src="https://github.com/drshahizan/SECP3843/assets/99240177/02fbc075-83ff-4a99-b232-3a3d35add7b4" width="400" alt="Image">
   
## Question 3 (b)




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



