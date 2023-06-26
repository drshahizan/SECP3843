<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Cai Xuan
#### Matric No.: A20EC0062
#### Dataset: Analytics Dataset

## Question 1 (a)
<h4>Step 1 - Install Django and create project in Visual Studio Code</h4>

Install Django 

```
pip install django
```
Create project named AA_project

```
django-admin startproject AA_project
python manage.py migrate
cd AA_project
code .
```

Create a Django App named AA_DjangoApp

```
python manage.py startapp AA_DjangoApp
```

<h4>Step 2 - Connect to MySQL database</h4>

Create a new database named aa_project in MySQL database. Includes the code below in the settings.py file in VS code. Make sure the database name, username, password, host and port are correct.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa_project',
        'USER': 'root',
        'PASSWORD': '',  # Leave this empty
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

<h4>Step 3 - Define Django Models</h4>

Based on the dataset, the models consist of 3 classes which are Account, Customer and Transaction. 

```
from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.IntegerField(unique=True)
    limit = models.IntegerField()
    products = models.ArrayField(models.CharField(max_length=255))

class Customer(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birthdate = models.DateTimeField()
    email = models.EmailField()
    accounts = models.ManyToManyField(Account)
    tier_and_details = models.JSONField()

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_count = models.IntegerField()
    bucket_start_date = models.DateTimeField()
    bucket_end_date = models.DateTimeField()
```

After creating the models, run the migrations to create tables in the aa_project database.

```
python manage.py makemigrations
python manage.py migrate
```

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


