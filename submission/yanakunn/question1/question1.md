<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURARISSA DAYANA BINTI MOHD SUKRI
#### Matric No.: A20EC0120
#### Dataset: SALES

## Question 1 (a)
Integrating the Django framework, JSON data, MySQL, and MongoDB can be achieved by running Django on a web server and using separate servers for MySQL and MongoDB databases. Depending on the project's specific needs, it may require additional servers for specialized purposes such as load balancing, caching, or scaling. The five servers in this project have the following functions:

1. Web Server: A web server such as Apache will host your Django application, handle HTTP requests, and create dynamic web pages.
2. MySQL Server: MySQL RDBMS that can handle structured data storage.
3. MongoDB Server: NoSQL database that can store and retrieves data using JSON-like documents.
4. Django Application Server: This server will run the Django application and connect to MySQL and MongoDB. It will process requests and generate responses.
5. Development/Testing Server: A separate server for development or testing.

### Steps required to integrate Django with the JSON dataset, MySQL, and MongoDB:

#### Step 1: Install Django and setup the Django project

1. Create and activate a new virtual environment called `.venv` in the Django project directory. VVirtual environments enable the creation and management of separate spaces for individual Python projects on a single computer.
  ``` ruby
  % python3 -m venv .venv
  % source .venv/bin/activate
```
2. Install Django, then create a new project called `project`.
  ``` ruby
  (.venv) % python3 -m pip install django
  (.venv) % django-admin startproject project
  ```

3. To use MySQL and MongoDB in this Django project, we will utilized XAMPP's phpmyadmin and MongoDB Atlas. There are other options besides XAMPP for setting up your Django project such as installing the MySQL server separately and configuring it within the project's settings.

- XAMPP
  - Open `http://localhost/phpmyadmin/` and create a new database.
  - <img width="300" alt="Screenshot 2023-06-29 at 7 50 29 AM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/70b6950b-e627-4cbe-ae2e-4084b5372d82">


- MongoDB Atlas
  - Go to `https://cloud.mongodb.com/`, sign in to your account, and create a new project.
  - Build a new database cluster in the project and follow the instructions.
  - Browse the collection and create a new database and collection.
  - <img width="300" alt="Screenshot 2023-06-29 at 7 58 48 AM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/97164025-4e91-49cc-882d-65ad7a9d9179">

4. Configure the project's `settings.py` file and provide the database connection details for MySQL and MongoDB. Make sure to use MySQLClient as the database backend for the MySQL database, and utilize Djongo as the MongoDB connector for Django.
  ```ruby
  (.venv) project % pip3 install mysqlclient
  (.venv) project % pip3 install djongo
  ```
In `settings.py`, define the databases,
  ```ruby
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': '<db_name>',
          'USER': '<username>',
          'PASSWORD': '<password>',
          'HOST': 'localhost',
          'PORT': '3306',
          'OPTIONS': {
              'unix_socket': 'your_path/to/mysql.sock',
          },
      },
      'mongodb': {
          'ENGINE': 'djongo',
          'NAME': '<db_name>',
          'CLIENT': {
              'host': '<mongodb_connection_string>',
              'username': '<username>',
              'password': '<password>',
              'authMechanism': 'SCRAM-SHA-1',
              'authSource': 'admin',
          },
      },
  }
  ```
#### Step 2: Define Django models that represent the structure of the project's data
1. Define a Django model called `Sale` based on the given JSON data structure
  ```ruby
  from django.db import models
  
  class Sale(models.Model):
      _id = models.CharField(max_length=24)
      saleDate = models.DateTimeField()
      items = models.JSONField()
      storeLocation = models.CharField(max_length=255)
      customer= models.JSONField()
      couponUsed = models.BooleanField()
      purchaseMethod = models.CharField(max_length=255)
  
      class Meta:
          db_table = 'sales'
          app_label = 'home'
  ```
2. Define a model for user by extending Django's built-in AbstractUser model
  ```ruby
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      USER_TYPE_CHOICES = (
          ('customer', 'Customer'),
          ('technical_worker', 'Technical Worker'),
          ('senior_management', 'Senior Management'),
      )
  
      user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
  
      class Meta:
          db_table = 'users'
          app_label = 'home'
  ```
3. Make migrations
  ```ruby
  (.venv) project % python3 manage.py makemigrations
  (.venv) project % python3 manage.py migrate
  ```

#### Step 3: Prepare and import the JSON data file
1. Write a Python code that transforms the JSON sales dataset into a structure compatible with MongoDB, save it to a new JSON file, and insert the data into MongoDB using the `pymongo` library.
  ```ruby
  from pymongo import MongoClient
  import json
  
  uri = "mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/?retryWrites=true&w=majority"
  
  # Read the new JSON file
  with open('/Documents/stde/newsales.json') as file:
      json_data = json.load(file)
  
  # Establish a connection to the MongoDB server
  client = MongoClient(uri)
  db = client['<db_name>']
  collection = db['<collection_name>']
  
  # Insert each sale record into the collection
  for sale in json_data:
      collection.insert_one(sale)
  ```
`sales.json`

<img width="900" alt="Screenshot 2023-06-29 at 5 56 15 AM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/9c5a811d-994d-41a1-984b-a00f7a51c116">

`newsales.json`

<img width="300" alt="Screenshot 2023-06-29 at 5 57 01 AM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/287a025b-fcea-47b1-9526-09ad04779e25">

#### Step 4: Build web pages for user interface
1. Define Django views for retrieving data using Django's built-in Object-Relational Mapping system as required. In this example, we will retrieve the store locations for the dataset
  ```ruby
  from home.models import Sale
  
  def salesReport(request):
      location = Sale.objects.using('mongodb').values('storeLocation').distinct()
  
      context = {
          'location': location,
      }
      return render(request, 'salesReport.html', context)
  ```
2. Create Django templates that define the structure and presentation of the dynamic web pages. Generate the content by retrieving data from MySQL and MongoDB databases and use it in the templates. For this example, the file is named as `salesReport.html`.
  ```ruby
  <!DOCTYPE html>
  <html>
  <head>
      <title>Sales Page</title>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.1/js/bootstrap.min.js"></script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.1/css/bootstrap.min.css">
  </head>
  <body>
      <main>
          <div class="container">
              <div class="col-3 p-5">
                  <table class="table">
                      <thead>
                          <tr>
                              <th>Store Location</th>
                          </tr>
                      </thead>
                      <tbody>
                          {% for s in location %}
                          <tr>
                              <td>{{s.storeLocation}}</td>
                          </tr>
                          {% endfor %}
                      </tbody>
                  </table>
              </div>
              
          </div>
      </main>
  </body>
  </html>
  ```
4. Map the URLs in your Django project to the corresponding views. Update the `urls.py` file in the Django project to define the URL patterns and associate them with the appropriate views.
  ```ruby
  path('salesReport', views.salesReport, name='salesReport')
  ```
#### Step 5: Run the Django application
  ```ruby
  (.venv) project % python3 manage.py runserver
  ```
#### Result of the page
<img width="300" alt="Screenshot 2023-06-29 at 7 41 29 AM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/bea00364-4a34-4859-9c20-81b8ebe32753">


## Question 1 (b)
<img width="1000" alt="Screenshot 2023-06-28 at 12 11 32 PM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/de697f28-c2e8-4809-95d7-c4be00f5f974">

This system architecture seamlessly integrates Django with MySQL and MongoDB databases to create a dashboard visualization and data viewing platform. It consists of several tiers and components:

<table>
  <tr>
    <th>Tiers</th>
    <th>Components Description</th>
  </tr>
  <tr>
    <td>Client Tier</td>
    <td>Web Browser</td>
  </tr>
  <tr>
    <td>Web Server Tier</td>
    <td>Hosts the Django application and handles incoming client HTTP requests.</td>
  </tr>
  <tr>
    <td>Application Tier</td>
    <td>
      <ol>
        <li>Django Web Framework: Main framework for handling business logic, requests, and responses.</li>
        <li>MySQL Database: Hosts the relational database for storing data of users to the Django application.</li>
        <li>MongoDB Database: Stores the JSON sales data.</li>
        <li>JSON Data: Sales dataset in JSON file.</li>
        <li>Data Preparation: Prepare the JSON data to follow the MongoDB documents structure.</li>
      </ol>
    </td>
  </tr>
  <tr>
    <td>Dashboard Tier</td>
    <td>
      <ol>
        <li>
          Dashboard: Visual representations of the data into the application's front end.
        </li>
        <li>
          User Interaction: Enables users to interact with the dashboard.
        </li>
    </td>
  </tr>
</table>

In this system architecture:
- Clients send HTTP requests to the web server.
- The web server uses a Web Server Gateway Interface to communicate with the application server.
- The application server receives requests and forwards them to the Django web framework.
- Python code to prepare and load JSON data into the databases. 
- The Django web framework runs on the application server and communicates with the MySQL and MongoDB databases using its built-in Object-Relational Mapping system. Django models are used to define the structure and behaviors of corresponding database tables, which are Python classes. The Django ORM handles the translation between Python objects and database rows, allowing object-oriented syntax to be used for database operations.
- Visualization tools are utilized to create dashboard visualizations based on the retrieved data. The frontend integration then integrates these visualizations into the Django templates. 
- Users can interact with the dashboard that allows them to filter and select data.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


