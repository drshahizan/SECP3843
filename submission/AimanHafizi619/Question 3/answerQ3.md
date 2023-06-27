
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


### Step 2: Setup Database

1. Go to `Analytics` > `Analytics` > `settings.py` and open the file

2. MySQL database will be use to build the user registration and login module.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'analytics',
        'USER': 'root',
	'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
     'mongodb': {
        'ENGINE': 'django',
        'NAME': 'Analytics',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://admin:admin@projectcluster.7sndifd.mongodb.net/',
    }   
}
}
```

### Step 3: Create User Model

> User Model uses AbstractUser class to apply the authentication and role designation feature

> Among all three JSON files, customers.json will be use for handling user authentication

> Go to `Desktop` > `Analytics` > `Customers` > `model.py` and update the files

```python
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, Group, Permission

class Customers(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    birthdate = models.DateField()
    email = models.EmailField()
    accounts = models.ArrayField(models.IntegerField())
    tier_and_details = models.JSONField()

class User(AbstractUser):
    customer_user = models.BooleanField(default=False)
    worker_user = models.BooleanField(default=False)
    management_user = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    user_permission = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')
```

## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



