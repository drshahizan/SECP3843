<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: FARAH IRDINA BINTI AHMAD BAHARUDIN
#### Matric No.: A20EC0035
#### Dataset: AIRBNB LISTINGS DATASET

## Question 1 (a)

The servers that I will be using to accomplish this Alternative Assignment are Django web server, MongoDB database server and MySQL database server. 

#### 1. Set up the Django project

Firstly, open command prompt and install Django. Write the code below.

```
pip install Django
```

#### 2. Create a new project

Then, create a new project. Write the code below.

```
django-admin startproject airbnb
```

#### 3. Configure database connections

Open your project folder inside Visual Studio Code and open settings.py file to configure the dataabase connections.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'airbnb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'airbnb',
        'CLIENT': {
            'host': 'mongodb+srv://arasayooo:<password>@listings.rdxcnj3.mongodb.net/test',
        },
    }
}
```

#### 4. Define the data models

Create a file named 'models.py' inside the folder and write the code below to define the data models.

```
from django.db import models

class MySQLModel (models.Model):
    _id = models.CharField(max_length=50)
    listing_url = models.URLField()
    name = models.CharField(max_length=200)
    summary = models.TextField()
    space = models.TextField()
    description = models.TextField()
    neighborhood_overview = models.TextField()
    notes = models.TextField()
    transit = models.TextField()
    access = models.TextField()
    interaction = models.TextField()
    house_rules = models.TextField()
    property_type = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50)
    bed_type = models.CharField(max_length=50)
    minimum_nights = models.CharField(max_length=10)
    maximum_nights = models.CharField(max_length=10)
    cancellation_policy = models.CharField(max_length=50)
    last_scraped = models.DateTimeField()
    calendar_last_scraped = models.DateTimeField()
    accommodates = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    number_of_reviews = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    amenities = models.JSONField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    weekly_price = models.DecimalField(max_digits=7, decimal_places=2)
    monthly_price = models.DecimalField(max_digits=7, decimal_places=2)
    cleaning_fee = models.DecimalField(max_digits=7, decimal_places=2)
    extra_people = models.DecimalField(max_digits=7, decimal_places=2)
    guests_included = models.IntegerField()
    images = models.JSONField()
    host = models.JSONField()
    address = models.JSONField()
    availability = models.JSONField()
    review_scores = models.JSONField()
    reviews = models.JSONField()
    
    class Meta:
        db_table = 'airbnb'

class MongoDBModel (models.Model):
    _id = models.CharField(max_length=50)
    listing_url = models.URLField()
    name = models.CharField(max_length=200)
    summary = models.TextField()
    space = models.TextField()
    description = models.TextField()
    neighborhood_overview = models.TextField()
    notes = models.TextField()
    transit = models.TextField()
    access = models.TextField()
    interaction = models.TextField()
    house_rules = models.TextField()
    property_type = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50)
    bed_type = models.CharField(max_length=50)
    minimum_nights = models.CharField(max_length=10)
    maximum_nights = models.CharField(max_length=10)
    cancellation_policy = models.CharField(max_length=50)
    last_scraped = models.DateTimeField()
    calendar_last_scraped = models.DateTimeField()
    accommodates = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    number_of_reviews = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    amenities = models.JSONField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    weekly_price = models.DecimalField(max_digits=7, decimal_places=2)
    monthly_price = models.DecimalField(max_digits=7, decimal_places=2)
    cleaning_fee = models.DecimalField(max_digits=7, decimal_places=2)
    extra_people = models.DecimalField(max_digits=7, decimal_places=2)
    guests_included = models.IntegerField()
    images = models.JSONField()
    host = models.JSONField()
    address = models.JSONField()
    availability = models.JSONField()
    review_scores = models.JSONField()
    reviews = models.JSONField()
    
    class Meta:
        db_table = 'listings'
```

#### 5. Migrate the data models to MySQL



#### 5. Load the JSON dataset into MySQL

#### 6. Connect Django to MongoDB

#### 7. Migrate the data models to MongoDB

#### 8. Load the JSON dataset into MongoDB

#### 9. Query and retrieve data

## Question 1 (b)

### System Architecture

Below is the system architecture for the integration between the web server (Django), dataset (JSON) and databases (MySQL and MongoDB).

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/architecture.png)

### Detailed Explanations of System Architecture

#### 1. User
User 
#### 2. User Interface
The user interface layer represents the frontend components that users interact with, including web pages such as home and dashboard pages, forms such as register and login forms, and user inputs. It is responsible for rendering the views and capturing user actions.

#### 3. Web Server

#### 4. Database Server

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


