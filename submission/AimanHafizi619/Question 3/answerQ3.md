
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
myenv\Scripts\activate
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

1. Include the necessary library

```python
from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib.auth. forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from decorators import is_customer, is_technical _worker, is_senior_management
from django.contrib.auth.decorators import user_passes_test
```

2. Define a function name `user_login















## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



