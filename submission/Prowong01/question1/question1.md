<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Eddie Wong Chung Pheng
#### Matric No.: A20EC0031
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies" >Companies</a>

## Question 1 (a)
### Step 1: Install Python & Django
Install Python 3 from the <a href=" www.python.org"> official website </a> according to your operating system. <br/>
Command: 
```
python --version
```

Open cmd and  verify that Django is installed by importing it in Python and printing its version.
Command: 
```
python
>>> import django
>>> print(django.get_version())
```
<img  src="./files/images/install.png"></img>

### Step 2: Create & activate virtual environment
After successfully installed Python and Django. I need to create Django project and activate virtual environment. 
Direct to project directory first and create a virtual environment for your Django project.

Command: 
```
python -m venv env
```

Activate your virtual environment. This will ensure that any packages you install will be isolated from the rest of your system

Command: 
```
env\Scripts\activate
```

### Step 3: Install Django Package 
After activate virtual environment, next is to install Django by using the pip command and install the latest Django release from the Python

Command: 
```
pip install django
```
<img  src="./files/images/install_django.png"></img>

### Step 4: Create Django Project & App
Next, create a new Django project with the name AA_project. This will create a AA_project directory with some files inside it, such as manage.py, settings.py, urls.py, asgi.py, and wsgi.py. These files are responsible for configuring the project and setting up the web server interface.

Command: 
```
django-admin startproject AA_project

```

 Before create the Django app, cd to the project directory and this will be the container for the project and its apps. This will create a polls directory with some files inside it, such as models.py, views.py, tests.py, admin.py, apps.py, and migrations. These files are responsible for defining your app's data models, views, tests, admin interface, configuration, and database migrations.

Command:
```
cd AA_project
python manage.py startapp companies_analytics
```
<img  src="./files/images/create_project.png"></img>

### Step 5: Configure the Database
To configure both MySQL and MongoDB databases in Django project, ppen the settings.py file located in the project's directory and update the DATABASES setting to configure both MySQL and MongoDB databases. You need to specify the database engine, name, user, password, host, and port for each database as shown below.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AA',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },

    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'AA',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost:27017',
            'port': 27017,
            'username': '',
            'password': '',
        }
    }
}
```

### Step 6: Define Django Models
To create a model, you need to subclass django.db.models.Model and declare the fields as class attributes. Open the models.py file in ```companies_analytics``` app directory.

Command:
```
from django.db import models

# Create your models here.
class Company(models.Model):

    name = models.CharField(max_length=200)
    permalink = models.CharField(max_length=200)
    crunchbase_url = models.URLField()
    homepage_url = models.URLField()
    blog_url = models.URLField()
    blog_feed_url = models.URLField()
    twitter_username = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # A foreign key field that references the Category model
    number_of_employees = models.IntegerField()
    founded_year = models.IntegerField()
    founded_month = models.IntegerField()
    founded_day = models.IntegerField()
    deadpooled_year = models.IntegerField(null=True) # A nullable field that allows empty values
    tag_list = models.TextField() # A text field that can store long strings
    alias_list = models.TextField()
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    overview = models.TextField()

```
### Step 7:Create Migration
To create migrations for these models, I need to use the manage.py command with the makemigrations option.

```
python manage.py makemigrations
```

## Question 1 (b)
<img  src="./files/images/system_architecture.png"></img>

#### User
User can send requests to the web server, such as viewing a web page, submitting a form, or calling an API. The web server then responds to the user by sending back the requested data or content. The user can also provide feedback to the web server, such as rating, commenting, or liking a web page or an API response. The user component is important for understanding the user needs, preferences, and behaviors, which can help improve the usability and functionality of the web application.

#### Django Web Server
This is the component that handles the requests from the clients and serves the web pages or API responses. You can use Django as your web framework to build your web server, as it provides a high-level abstraction of common web development tasks, such as URL routing, template rendering, authentication, etc. Django also supports multiple database backends, which allows you to use MySQL and MongoDB in your system.

#### Database (MySQL & MongoDB)
These are the components that persistently store and manage data.
-MySQL: MySQL is a relational database that uses tables, rows, and columns to store structured data. It supports SQL queries, transactions, and joins, which can be useful for performing complex operations on data.
-MongoDB: MongoDB is a document database that uses collections, documents, and fields to store unstructured or semi-structured data. It supports dynamic schemas, flexible queries, and aggregation pipelines, which can be useful for handling large amounts of data or data with varying structures.

#### Dataset (JSON)
This is the component that stores the data that want to use in web application. I use JSON as the data format, as it is a lightweight and human-readable format that can be easily parsed and manipulated by Python. JSON also supports nested structures, which can be useful for storing complex data. 

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


