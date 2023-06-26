<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nur Syamalia Faiqah Binti Mohd Kamal
#### Matric No.: A20EC0118
#### Dataset : [Analytics Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 1 (a)
In This questions, I will use 3 servers which are:
- Server 1: MongoDB Database Server
- Server 2: MySQL Database Server
- Server 3: Django Application Server

<p>To begin, allocating a separate web server guarantees that the Django web application has the resources to process user requests, generate dynamic web pages, and connect with databases. Isolating the web server from the database servers enables better resource management and prevents any database performance issues from affecting the responsiveness of the online application.</p>

<p>Having separate servers for MySQL and MongoDB databases improves database administration and optimisation. The MySQL database server processes SQL queries from the Django application and concentrates on storing structured data from the JSON dataset. Likewise, the MongoDB database server specialises in storing semi-structured data from JSON datasets and answers MongoDB queries. This division guarantees that each database technology is used to its full potential, allowing for efficient data storage and retrieval.</p>


### Prerequisites
Install the following below:
- [Python](https://www.python.org/downloads/)

### Steps
Step 1: Install Django:
 - Open command prompt.
 - Install Django using pip: `pip install django`.

Optional: Set up the virtual environment:
- A virtual environment is a self-contained environment that allows you to install packages without changing the overall Python installation on your machine. Run the following command in your terminal to establish a virtual environment:
  ```python
      python -m venv myenv
      myenv\Scripts\activate
  ```
- Activate virtual environment
  ```python
      myenv\Scripts\activate
  ```

Step 2: Set up the Django project:
- Create a new Django project using the command: `django-admin startproject analytics`.
- Navigate into the project directory: `cd analytics`.
  
<img  src="./files/images/envproject.png"></img>

Step 3: Set up the Django app and install required packages:
- Create a new Django project using the command: `django-admin startapp app`.
- Install the Django MySQL package: `pip install mysqlclient`.
- Install the Django MongoDB package: `pip install djongo`.
- Install any other necessary dependencies based on your specific project requirements.
   
  <img  src="./files/images/app.png"></img>

- Open the `settings.py` file located in the project 'analytics' directory.
- Add in the `INSTALLED_APPS` configuration to include 'app'.
  ```python
     INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'app',
    ]
  ```
  
Step 4: Configure the database in project settings:
- Open the `settings.py` file located in the project 'analytics' directory.
- Set the `DATABASES` configuration to include both MySQL and MongoDB settings. Here's an example:

   ```
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'analytics',
             'USER': 'root',
             'HOST': 'localhost',
             'PORT': '3306',
         },
         
         'mongodb': {
             'ENGINE': 'djongo',
             'ENFORCE_SCHEMA': False,
             'NAME': 'analytics',
             'CLIENT': {
                 'host': 'mongodb://localhost:27017'
             }
         }
     }
     ```

Step 5: Define Django models:
- Open the `models.py` file in the 'app' directory.
- Define your models according to the JSON dataset's structure. Use Django's model fields to map the JSON data fields to the database fields.

    ```
       from django.db import models

       # Create your models here.
       class Account(models.Model):
           account_id = models.IntegerField(primary_key=True)
           limit = models.IntegerField()
           products = models.JSONField()
           
           def __str__(self):
               return f"Account ID: {self.account_id}"
           
       class Customer(models.Model):
           username = models.CharField(max_length=255)
           name = models.CharField(max_length=255)
           address = models.TextField()
           birthdate = models.DateTimeField()
           email = models.EmailField()
           active = models.BooleanField()
           accounts = models.JSONField()
           tier_and_details = models.JSONField()
       
           def __str__(self):
               return self.username
       
       
       class Transaction(models.Model):
           account_id = models.IntegerField()
           transaction_count = models.IntegerField()
           bucket_start_date = models.DateTimeField()
           bucket_end_date = models.DateTimeField()
           transactions = models.JSONField()
       
           def __str__(self):
               return f"Transactions for Account ID: {self.account_id}"
    ```
 

Step 6: Migrate the models:
 - Apply the initial migrations for both MySQL and MongoDB databases using the command.
   ```python
   python manage.py makemigrations
   ```
 - Django will create the necessary tables and collections in the databases based on your model definitions.
 - Once you have created the migration file, you can apply the migrations by running the following command.
   ```python
   python manage.py migrate
   ```

Step 7: Load the JSON dataset into databases:
 - Write a script or use Django's management command to load the JSON dataset into the MySQL and MongoDB databases.
 - In the script or management command, parse the JSON dataset, create Django model instances, and save them to the respective databases.

## Question 1 (b)

```
            +---------------------+
            |      Web Server     |
            |       (Django)      |
            +----------+----------+
                       |
                       |
            +----------v----------+
            |        JSON         |
            |       Dataset       |
            +----------+----------+
                       |
                       |
            +----------v----------+
            |    MySQL Database   |
            +----------+----------+
                       |
                       |
            +----------v----------+
            |    MongoDB Database |
            +----------+----------+
                       |
                       |
            +----------v----------+
            |    Django Models    |
            +----------+----------+
                       |
                       |
            +----------v----------+
            | Data Processing and |
            |    Integration      |
            +---------------------+
```

In the system architecture, the web server (Django) interacts with the JSON dataset, MySQL, and MongoDB databases through appropriate connectors and libraries. Django models provide an abstraction layer to handle data operations, and data processing components ensure seamless integration between the web server and the databases. This architecture enables efficient storage, retrieval, and visualization of data from the JSON dataset using Django, MySQL, and MongoDB.

1. Web Server (Django):
The web server component is responsible for handling user requests, generating dynamic web pages, and serving the portal's functionality. Django, a Python-based web framework, is used as the foundation for the web server. It provides a high-level abstraction layer for building web applications and integrates well with both MySQL and MongoDB databases.

2. JSON Dataset:
The JSON dataset contains the data that will be displayed and visualized on the portal. It consists of structured and semi-structured data that represents various entities, such as accounts, customers, and transactions. The dataset serves as the primary source of information for the portal's dashboard visualizations and data views.

3. MySQL Database:
MySQL is a widely used relational database management system (RDBMS) that excels at storing structured data. In this architecture, MySQL is used to store and manage structured data from the JSON dataset. Django interacts with the MySQL database using the Django ORM (Object-Relational Mapping) to perform CRUD (Create, Read, Update, Delete) operations on the data.

4. MongoDB Database:
MongoDB is a NoSQL database that specializes in storing and retrieving semi-structured and unstructured data. It is well-suited for handling the flexibility and scalability required by JSON datasets. In this architecture, MongoDB is used to store and manage the semi-structured data from the JSON dataset. Django communicates with the MongoDB database using the Djongo package, which provides a bridge between Django and MongoDB.

5. Django Models:
Django models define the structure of the data stored in the databases. Models are Python classes that map to database tables or collections. In this architecture, Django models are defined based on the structure of the JSON dataset. Each model represents an entity (e.g., accounts, customers, transactions) and its fields correspond to the attributes in the dataset. The models act as an abstraction layer between the application and the databases, allowing seamless interaction with the data.

6. Data Processing and Integration:
The integration process involves parsing the JSON dataset, transforming it into Django model instances, and storing them in the MySQL and MongoDB databases. This can be achieved by writing scripts or using Django's management commands. The data processing component reads the JSON dataset, maps its fields to the appropriate model fields, and saves the instances to the respective databases. The processing ensures that the data is correctly structured and stored in the databases for efficient retrieval.




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


