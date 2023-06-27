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

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/django.png)

#### 2. Create a new project

Then, create a new project. Write the code below.

```
django-admin startproject airbnb
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/project.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/project2.png)

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
```

#### 5. Migrate the data models to both MySQL and MongoDB

Next, perform database migrations to both MySQL and MongoDB.

```
python manage.py makemigrations Listings
python manage.py migrate
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/migrate.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/migrate2.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/mysql.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/mysql2.png)

#### 6. Load the JSON dataset into MySQL and MongoDB

To load the JSON dataset into MySQL and MongoDB through Django is by reading the data in JSON file and assign it as array. Then, insert the array into the databases. Refer the code below. 

##### - MySQL

```
from django.core.management.base import BaseCommand
from Listings.models import Listing  # Import your Listing model here
import json


class Command(BaseCommand):
    help = 'Load JSON data into MySQL database'

    def handle(self, *args, **options):
        # Read the JSON file
        with open('C:/Users/User/Downloads/listings.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            listing = Listing(
                _id=item['_id'],
                listing_url=item['listing_url'],
                name=item['name'],
                summary=item['summary'],
                space=item['space'],
                description=item['description'],
                neighborhood_overview=item['neighborhood_overview'],
                notes=item['notes'],
                transit=item['transit'],
                access=item['access'],
                interaction=item['interaction'],
                house_rules=item['house_rules'],
                property_type=item['property_type'],
                room_type=item['room_type'],
                bed_type=item['bed_type'],
                minimum_nights=item['minimum_nights'],
                maximum_nights=item['maximum_nights'],
                cancellation_policy=item['cancellation_policy'],
                last_scraped=item['last_scraped'],
                calendar_last_scraped=item['calendar_last_scraped'],
                accommodates=item['accommodates'],
                bedrooms=item['bedrooms'],
                beds=item['beds'],
                number_of_reviews=item['number_of_reviews'],
                bathrooms=item['bathrooms'],
                amenities=item['amenities'],
                price=item['price'],
                weekly_price=item['weekly_price'],
                monthly_price=item['monthly_price'],
                cleaning_fee=item['cleaning_fee'],
                extra_people=item['extra_people'],
                guests_included=item['guests_included'],
                images=item['images'],
                host=item['host'],
                address=item['address'],
                availability=item['availability'],
                review_scores=item['review_scores'],
                reviews=item['reviews']
            )

            listing.save()

        self.stdout.write(self.style.SUCCESS(
            'JSON data has been loaded into the database.'))
```

##### - MongoDB

```
import json
from django.core.management.base import BaseCommand
from Listings.models import Listing
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Load JSON data into MongoDB'

    def handle(self, *args, **options):
        with open('C:/Users/User/Downloads/listings.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        client = MongoClient('mongodb+srv://arasayooo:<password>@listings.rdxcnj3.mongodb.net/test')
        db = client['airbnb']
        collection = db['listings']

        for item in json_data:
            MongoDBModel.objects.create(
                _id=item['_id'],
                listing_url=item['listing_url'],
                name=item['name'],
                summary=item['summary'],
                space=item['space'],
                description=item['description'],
                neighborhood_overview=item['neighborhood_overview'],
                notes=item['notes'],
                transit=item['transit'],
                access=item['access'],
                interaction=item['interaction'],
                house_rules=item['house_rules'],
                property_type=item['property_type'],
                room_type=item['room_type'],
                bed_type=item['bed_type'],
                minimum_nights=item['minimum_nights'],
                maximum_nights=item['maximum_nights'],
                cancellation_policy=item['cancellation_policy'],
                last_scraped=item['last_scraped'],
                calendar_last_scraped=item['calendar_last_scraped'],
                accommodates=item['accommodates'],
                bedrooms=item['bedrooms'],
                beds=item['beds'],
                number_of_reviews=item['number_of_reviews'],
                bathrooms=item['bathrooms'],
                amenities=item['amenities'],
                price=item['price'],
                weekly_price=item['weekly_price'],
                monthly_price=item['monthly_price'],
                cleaning_fee=item['cleaning_fee'],
                extra_people=item['extra_people'],
                guests_included=item['guests_included'],
                images=item['images'],
                host=item['host'],
                address=item['address'],
                availability=item['availability'],
                review_scores=item['review_scores'],
                reviews=item['reviews']
            )
            collection.insert_one(item)
```

#### 7. Query and retrieve data

```
from Listings.models import MySQLModel
from Listings.models import MongoDBModel

mysql_objects = MySQLModel.objects.all()
mongodb_objects = MongoDBModel.objects.using('mongodb').all()
```

## Question 1 (b)

### System Architecture

Below is the system architecture for the integration between the web server (Django), dataset (JSON) and databases (MySQL and MongoDB).

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question1/files/images/architecture.png)

### Detailed Explanations of System Architecture

#### 1. User
User is the one who will be using this system. For this project, the users are customers, technical workers and senior management.

#### 2. User Interface
The user interface layer represents the frontend components that users interact with, including web pages such as home and dashboard pages, forms such as register and login forms, and user inputs. It is responsible for rendering the views and capturing user actions.

#### 3. Web Server

##### - URLs
The URL maps URLs to the corresponding views. It determines which view should handle a particular request based on the URL patterns defined in the Django project's URL configuration.

##### - Views
Views handle user requests and serve as the intermediary between the user interface and the backend. It will receive HTTP requests from the user interface, process the data, interact with the models and databases, and generate appropriate responses.

##### - Models
Models represent the data structure and define how data is stored in the database. Models are typically defined as Python classes using Django's ORM, which abstracts the database operations.

##### - Templates
Templates provide the structure and layout for the generated web pages. They utilize Django's template system, which allows embedding dynamic content and data retrieved from the backend into the HTML pages.

#### 4. Database Server
The database component stores the application's data persistently. In the provided architecture, it represents a relational database system (RDBMS) such as MySQL and MongoDB. Django's ORM handles the communication with the database, allowing developers to work with data using Python objects instead of writing raw SQL queries.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


