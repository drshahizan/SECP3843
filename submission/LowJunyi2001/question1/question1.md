<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Low Junyi
#### Matric No.: A20EC0071
#### Dataset: [Airbnb](https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb)


### Prerequisites
Download and Install All Required Software.
- [MongoDB Community Server](https://www.mongodb.com/try/download/community)<br>
Create a database with the name `AAQ1`


 <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/34949a42-f886-43e3-883f-f7bde08d25c4"></img>


- [XAMPP for Window](https://www.apachefriends.org/download.html) <br>
Create a database with the name `AAQ1`.

 <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/3f261f0f-3fd1-4909-adee-651a1429f5d1"></img>

Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/204ed4f0-6611-4c97-b5dd-5423d1b913cd"></img>




## Question 1 (a)

Five servers used in this project.
- Django Application Server
- MySQL Database Server
- MongoDB Database Server
- Load Balancer
- File Server


### Step 1: Set up environment and install Django

a) Open Command Prompt:


  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/086f550c-8f6d-4e35-ae96-9ac80744621f"></img>


b) Redirect to the correct path.
```
cd Downloads\AA MSO\Question 1
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/e736e36f-2e2f-4a44-86e3-abcd5491c3e2"></img>

c) Create and activate virtual environment in Python by using the following code.
```
py -m venv env
```
and
```
env\Scripts\activate
```
  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/c7670804-64eb-445f-805d-5219004c63a8"></img>


d) Install Django with the following code.
```
pip install Django
```
  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/e24f7c69-a210-4721-b2cf-442ab5dc3ee3"></img>


e) Necessary packages for MySQL and MongoDB connectivity need to be install by using the code below.
```
pip install mysql-connector-python djongo pymongo
```
  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/18b4df91-4f8b-4e50-b05e-a853b49d6132"></img>


f) Install the mysqlclient in the command prompt using the code below.
```
pip install mysqlclient
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/995d9692-ba1d-4625-adb3-44ad79252fc1"></img>



### Step 2: Create Django project
a) Create the project by using the code below.
```
django-admin startproject AA_Q1
```
  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/a1f73264-e89d-4265-8568-48c5c08d22ad"></img>
  

b) Direct to the created project by using the code below.
```
cd AA_Q1
```
  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/0e890e78-7df8-4e4a-a133-3cb62be9b20a"></img>
  

c) Create a new Django app within the project by using the code below.
```
python manage.py startapp app
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/b392cebe-6110-46de-942c-0b7fcd89b14b"></img>



### Step 3: Configure the Django database settings
a) Open the Django project's `settings.py` file.

b) Define the database settings for both MySQL and MongoDB.
```python
 DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'AAQ1',
             'USER': 'root',
             'PASSWORD': '',
             'HOST': 'localhost',
             'PORT': 3306,
         },
         'mongodb': {
             'ENGINE': 'djongo',
             'ENFORCE_SCHEMA': False,
             'NAME': 'AAQ1',
             'CLIENT': {
                 'host': 'localhost:27017',
                 'port': 27017,
                 'username': '',
                 'password': '',
             }
         }
     }
```


### Step 4: Configuring Django models
a) In `models.py` file from the app folder, define the models according to its data structure and data types.


```python
from django.db import models

class room_details(models.Model):
    _id = models.CharField(max_length=255, primary_key=True)
    listing_url = models.URLField()
    name = models.CharField(max_length=255)
    summary = models.TextField()
    space = models.TextField()
    description = models.TextField()
    neighborhood_overview = models.TextField()
    notes = models.TextField()
    transit = models.TextField()
    access = models.TextField()
    interaction = models.TextField()
    house_rules = models.TextField()
    property_type = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    bed_type = models.CharField(max_length=255)
    minimum_nights = models.CharField(max_length=255)
    maximum_nights = models.CharField(max_length=255)
    cancellation_policy = models.TextField()
    calendar_last_scraped = models.DateField()
    first_review = models.DateField()
    last_review = models.DateField()
    accommodates = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    number_of_reviews = models.IntegerField()
    bathrooms = models.IntegerField()
    amenities = models.TextField()
    price = models.DecimalField()
    security_deposit = models.DecimalField()
    cleaning_fee = models.DecimalField()
    extra_people = models.DecimalField()
    guests_included = models.DecimalField()
    images = models.URLlField()
    host = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    review_scores = models.CharField(max_length=255)
    reviews = models.CharField(max_length=255)
   
    def __str__(self):
        return self.name

```

### Step 5: Migrate database to phpmyadmin and MongoDB (Data Storage)
a) Before migrate, make the pathway is correct in the `models.py`.


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/401c2c32-4b90-4d95-8ed9-8a16d5efe7d2"></img>


b) Migrate all the tables into each database by using the code below
```
python manage.py makemigrations
```
```
python manage.py migrate
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/1809f566-5fa7-43c0-a734-6424502a21ff"></img>


There will be changes in Myphpadmin:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/0411e9d5-367c-4cd7-8bd5-c2e503ac3723"></img>


c) To migrate in MongoDB, use the code below
```
python manage.py migrate --database=mongodb
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/95b09483-498e-4e8c-aeb9-64838ab8b04b"></img>


There will be changes in MongoDB:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/4e57fabb-5ec3-41ee-92ed-18ea535e5111"></img>


### Step 6: Load Data 
- To load data in Django, create a new file called `load_data.py` in the Django app's management/commands directory.
- Insert the code below inside the `load_data.py.
```python
import json
from django.core.management.base import BaseCommand
from app.models import room_details


class Command(BaseCommand):
    help = 'Loads JSON data into the database.'

    def handle(self, *args, **options):
        listing_file = 'C:\\Users\\user\\Downloads\\AA MSO\\Question 1\\AA_Q1\\listingAndReviews.json'


        # Load listing JSON data    
        with open(listing_file) as file:
            listing_data = json.load(file)

            for item in listing_data:

                _id = item['_id']['$oid']
                listing_url = item['listing_url']
                name = item['name']
                summary = item['summary']
                space = item['space']
                description = item['description']
                neighborhood_overview = item['neighborhood_overview']
                notes = item['notes']
                transit = item['transit']
                access = item['access']
                interaction = item['interaction']
                house_rules = item['house_rules']
                property_type = item['property_type']
                room_type = item['room_type']
                bed_type = item['bed_type']
                minimum_nights = item['minimum_nights']
                maximum_nights = item['maximum_nights']
                cancellation_policy = item['cancellation_policy']
                calendar_last_scraped = item['calendar_last_scraped']
                first_review = item['first_review']
                last_review = item['last_review']
                accommodates = item['accommodates']
                bedrooms = item['bedrooms']
                beds = item['beds']
                number_of_reviews = item['number_of_reviews']
                bathrooms = item['bathrooms']
                amenities = item['amenities']
                price = item['price']
                security_deposit = item['security_deposit']
                cleaning_fee = item['cleaning_fee']
                extra_people = item['extra_people']
                guests_included = item['guests_included']
                images = item['images']
                host = item['host']
                address = item['address']
                availability = item['availability']
                review_scores = item['review_scores']
                reviews = item['reviews']
            listing.save()
            listing.save(using='mongodb')
        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
```

- Run the following command to load the data.
```
python manage.py load_data
```


### Step 7: Retrieve Data 
- To retrieve data in Django, create a new file called `retrieve_data.py` in the Django app's management/commands directory.
- Insert the code below inside the `retrieve_data.py.
```python
from django.core.management.base import BaseCommand
from app.models import room_details

class Command(BaseCommand):
    help = 'Retrieve data from MySQL and MongoDB databases.'

    def handle(self, *args, **options):
        # Retrieve data from MySQL database with a filter
        AAQ1 = room_details.objects.using('default').filter(limit__gt=1000)

        # Print MySQL data
        print("MySQL Data:")
        for room_details in AAQ1:
            print(f"room_details ID: {room_details._id}, Limit: {room_details.limit}")

        # Retrieve data from MongoDB database with a filter
        AAQ1 = room_details.objects.using('mongodb').filter(limit__gt=1000)

        # Print MongoDB data
        print("MongoDB Data:")
        for room_details in AAQ1:
            print(f"room_details ID: {room_details._id}, Limit: {room_details.limit}")
```

- Run the following command to retrieve the data.:
```
python manage.py retrieve_data
```

## Question 1 (b)
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/a0f4a6db-8097-4cd7-95aa-b3757f7fb76a"></img>

## Component details

### User
The user interacts with the web application by sending HTTP requests and receiving HTTP responses. The user's requests are transmitted to the Django web server, which processes them and generates responses. The seamless integration between the web server and the user ensures smooth communication and interaction.

### Web Server (Django)
Django is a high-level Python web framework that acts as the web server in this scenario. It receives HTTP requests from the user and routes them to the appropriate view in the web application. Django seamlessly integrates with the view layer, allowing the processing of user requests and generating HTTP responses.

### Web Application

#### View
The view layer handles the logic for processing user requests and generating responses. It interacts with the model layer to retrieve or manipulate data from the databases. The view layer seamlessly communicates with both the model layer and the template layer to gather necessary data and pass it for rendering.

#### Template
The template layer is responsible for rendering HTML templates. It receives data from the view layer and combines it with the appropriate HTML templates to generate the final HTML response that will be sent back to the user. The seamless integration between the template layer and the view layer ensures that the necessary data is passed correctly for rendering.

#### Model
The model layer represents the application's data models and business logic. It acts as an intermediary between the databases and the web application. The model layer seamlessly interacts with both MongoDB and MySQL databases, utilizing the appropriate database connectors or ORM depending on the database type.

### Databases

#### MySQL
MySQL is a relational database management system (RDBMS) that follows the traditional relational data model. In the scenario, the MySQL database is integrated with the web application through the ORM (Object-Relational Mapping) provided by Django. The ORM translates between the relational structure of the MySQL database and the object-oriented model used in the web application's model layer.

#### MongoDB
MongoDB is a NoSQL database that stores data in a flexible, document-oriented format. The JSON dataset is seamlessly integrated with MongoDB, allowing efficient storage and retrieval of data using MongoDB's query language.

### JSON Dataset
The JSON dataset contains structured data in JSON format. It serves as a data source for the web application. In this scenario, the JSON dataset is integrated with MongoDB database.



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


