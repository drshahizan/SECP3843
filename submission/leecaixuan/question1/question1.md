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

Create a new database named aa_project in MySQL database. Includes the code below in the settings.py file in VS code. 

<p align="center">
  <img height="100px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question1/files/images/Screenshot%202023-06-26%20173526.png" />
</p>

Make sure the database name, username, password, host and port are correct to connect to MySQL database.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa_project',
        'USER': 'root',
        'PASSWORD': '',
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

<h4>Step 4 - Import JSON file into database</h4>

- MySql database

Create a load_data.py file to import the JSON file into database.

```
import json
from django.core.management.base import BaseCommand
from AA_DjangoApp.models import Account, Customer, Transaction

class Command(BaseCommand):
    help = 'Loads JSON data into the database.'

    def handle(self, *args, **options):
        account_file = '"c:\Users\User\Downloads\AA_SpecialTopic\accounts.json"'
        customer_file = 'c:\Users\User\Downloads\AA_SpecialTopic\customers.json'
        transaction_file = 'c:\Users\User\Downloads\AA_SpecialTopic\transactions.json'

        # Load Accounts JSON data
        with open(account_file) as file:
            account_data = json.load(file)

            for item in account_data:
                account = Account(account_id=item['account_id'], limit=item['limit'], products=item['products']])
                account.save()

        # Load Customers JSON data
        with open(customer_file) as file:
            customer_data = json.load(file)

            for item in customer_data:
                customer = Customer(username=item['username'], name=item['name'], address=item['address'], birthdate=item['birthdate'], email=item['email'], tier_and_details=item['tier_and_details'])
                customer.save()

        # Load Transactions JSON data
        with open(transaction_file) as file:
            transaction_data = json.load(file)

            for item in transaction_data:
                transaction = Transaction(account=item['account'], transaction_count=item['transaction_count'], bucket_start_date=item['bucket_start_date'], bucket_end_date=item['bucket_end_date'])
                transaction.save()
```

Then, run the command below.

```
python manage.py load_data C:\Users\User\Downloads\AA_SpecialTopic\accounts.json c:\Users\User\Downloads\AA_SpecialTopic\customers.json c:\Users\User\Downloads\AA_SpecialTopic\transactions.json
```

- MongoDB

Install PyMongo library

```
pip install pymongo
```

Create a new file named 'mongodb.py' in VS code to import JSON file into MongoDB database.

```
import json
from pymongo import MongoClient

# MongoDB connection details
mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_database = 'aa_project'
mongodb_collection_account = 'accounts'
mongodb_collection_customer = 'customers'
mongodb_collection_transaction = 'transactions'

# JSON file paths
account_json_file = '"C:\Users\User\Downloads\AA_SpecialTopic\accounts.json"'
customer_json_file = '"C:\Users\User\Downloads\AA_SpecialTopic\customers.json"'
transaction_json_file = '"C:\Users\User\Downloads\AA_SpecialTopic\transactions.json"'

# Connect to MongoDB
client = MongoClient(mongodb_host, mongodb_port)
db = client[mongodb_database]
collection_account = db[mongodb_collection_account]
collection_customer = db[mongodb_collection_customer]
collection_transaction = db[mongodb_collection_transaction]

# Load Account JSON data
with open(account_json_file) as file:
    account_data = json.load(file)

# Insert Account JSON data into MongoDB
collection_account.insert_many(account_data)

# Load Customer JSON data
with open(customer_json_file) as file:
    customer_data = json.load(file)

# Insert Customer JSON data into MongoDB
collection_customer.insert_many(customer_data)

# Load Transaction JSON data
with open(transaction_json_file) as file:
    transaction_data = json.load(file)

# Insert Transaction JSON data into MongoDB
collection_transaction.insert_many(transaction_data)

# Close the MongoDB connection
client.close()
```

<h4>How to Retrieve Data from database</h4>

- MySql database

Example: Retrieve data from the Accounts table

```
# Import the model representing the account table
from myapp.models import Account

def retrieve_accounts_data():
    # Retrieve all records from the account table
    accounts = Account.objects.all()

    # Iterate over the retrieved accounts
    for account in accounts:
        account_id = account.account_id
        limit = account.limit
        products = account.products

        # Print data
        print(f"Account ID: {account_id}")
        print(f"Limit: {limit}")
        print(f"Products: {products}")

retrieve_accounts_data()
```

- MongoDB

Example: Retrieve data from Accounts table

```
from pymongo import MongoClient

def retrieve_accounts_data():
    # Establish a connection to MongoDB
    client = MongoClient('mongodb://localhost:27017')

    # Access the database
    db = client['aa_project']

    # Access the "accounts" collection
    collection = db['accounts']

    # Define the query
    query = {'status': 'active'}  # Example query to retrieve active accounts

    # Execute the query and retrieve the documents
    accounts = collection.find(query)

    # Iterate over the retrieved accounts
    for account in accounts:
        account_id = account['_id']
        limit = account['limit']
        products = account['products']

        # Print the data
        print(f"Account ID: {account_id}")
        print(f"Limit: {limit}")
        print(f"Products: {products}")

    # Close the MongoDB connection
    client.close()

retrieve_accounts_data()
```


## Question 1 (b)

<p align="center">
  <img height="600px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question1/files/images/System%20Architecture.png" />
</p>

The system architecture consists of Django web server, JSON dataset, MySQL and MongoDB database. The model is created and the data is loaded into MYSQL and MongoDB database. JSON file is imported into MongoDB database. User must login to the system that consists of the user interface that can interact to view the data information. To retrieve data, Django is used to process and communicate with databases that stored all the data.  


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


