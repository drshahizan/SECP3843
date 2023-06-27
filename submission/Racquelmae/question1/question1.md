<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Chloe Racquelmae Kennedy
#### Matric No.: A20EC0026
#### Dataset: City Inspections	

## Question 1 (a)
#### Prerequisites
To utilize Django, a Python installation is required which can be obtained by downloading it from the [official website](https://www.python.org/downloads/).

### 1. Create & activate virtual environment
To create a virtual environment, run `python -m venv env` in your command prompt. Once the virtual environment is created, activate it by typing `env\Scripts\activate`.
<img  src="./files/images/env.jpg"></img>

### 2. Install Django
With the virtual environment activated, type `pip install django` to install Django.
<img  src="./files/images/pip.jpg"></img>

### 3. Create project & app
Use `django-admin startproject portalproject` to create the Django project. Then, navigate to the project directory and create a new app by running `python manage.py startapp portalapp`. 
<img  src="./files/images/project.jpg"></img>

Once the app is created, add the app name in the INSTALLED_APPS array of settings.py file.<br>
<img  src="./files/images/portalapp.jpg"></img>

### 4. Install package 
After creating the database in both MongoDB and MySQL database servers, install the required package by running these 3 commands: 
- `pip install djongo`
- `pip install mysqlclient` 
- `pip install pytz`<br>

<img  src="./files/images/package.jpg"></img>

### 5. Configure the database
To use MongoDB and MYSQL as the database, modify the settings.py file in the project folder.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AA',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'AA',
        'CLIENT': {
            'host': 'mongodb+srv://Chloe:Racq0711@atlascluster.uwqwdbv.mongodb.net/',
        },
    },
}
```

### 6. Define model
In the models.py, define the model that represents the data in Django.
```
from django.db import models

class City(models.Model):
    _id = models.CharField(max_length=255, primary_key=True)
    id = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    sector = models.CharField(max_length=255, null=True)
    address = models.JSONField()
```

### 7. Migrate database
Once the models are defined, create the database tables by running `python manage.py makemigrations`.

Then, apply the migration by using these 2 commands:
- MySQL: `python manage.py migrate`
- MongoDB: `python manage.py migrate --database=mongodb`
<img  src="./files/images/migrate.jpg"></img>

### 8. Load dataset
Modify the city_inspections.json dataset in Jupyter notebook to convert the format into JSON array structure and download the [new_city_inspections.json](./files/code/new_city_inspections.json).
```
import json

# Open the original JSON file with the correct encoding
with open('city_inspections.json', 'r', encoding='utf-8') as file:
    data = file.readlines()

# Modify the data to add square brackets
modified_data = '[' + ','.join(data) + ']'

# Write the modified data to a new file with the correct encoding
with open('new_city_inspections.json', 'w', encoding='utf-8') as file:
    file.write(modified_data)
```

Create a load_data.py file under management folder and add the following code in the file.
```
from django.core.management.base import BaseCommand
import json
from portalapp.models import City

class Command(BaseCommand):
   help = 'Loads JSON data into the AA model'

   def add_arguments(self, parser):
       parser.add_argument('json_file', type=str, help='Path to the JSON file')

   def handle(self, *args, **options):
       json_file = options['json_file']
       with open(json_file, encoding='utf-8') as f:
           data = json.load(f)
           for item in data:
               city = City(
                   _id=item['_id'],
                   id=item['id'],
                   certificate_number=item['certificate_number'],
                   business_name=item['business_name'],
                   date=item['date'],
                   result=item['result'],
                   sector=item['sector'],
                   address=item['address'],
               )
               city.save()
               city.save(using='mongodb')
               self.stdout.write(self.style.SUCCESS(f'Successfully loaded data for city with id {city.id}'))
```

Then, run `python manage.py load_data new_city_inspections.json` to import the JSON dataset into the databases.

### 9. Data retrieval
Run the following code to retrieve data from the databases:
```
AA_mysql = City.objects.using('default').get(id="34557-2015-ENFO")
AA_mongodb = City.objects.using('mongodb').get(id="34557-2015-ENFO")
```
<img  src="./files/images/retrieve.jpg"></img>

## Question 1 (b)
<img  src="./files/images/architecture.jpeg"></img>

### User
Have access to the portal and contribute to the driving of flow as well as functionality of the application by performing tasks within the system.

### User Interface 
Presents the portal's visual interface to users which includes presentation of information, data entry forms, navigation and menu.

### Web Server (Django)
- Manages incoming user requests over the HTTP protocol and directs them to the relevant views for further handling.
- Performs data processing and transformation operations.
- Object-Relational Mapping (ORM) layer facilitate interactions with the databases.

### Databases
- MySQL: stores structured data such as users login and registration credentials.
- MongoDB: stores unstructured or semi-structured data such as the new_city_inspections.json dataset.

### Dataset (JSON)
The new_city_inspections.json is the JSON dataset used in this project and is processed by Django app for integration with the database.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
