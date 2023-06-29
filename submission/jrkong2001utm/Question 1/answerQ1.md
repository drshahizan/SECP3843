<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kong Jia Rou
#### Matric No.: A20EC0198
#### Dataset: Supply store 

## Question 1 (a)
First, we need to define and assign specific roles to each of the five servers. The distribution of the roles to each servers can be as below:

| Server | Server Type | Description |
| --- | --- | --- |
| Server 1 | Django Web Server | This server is responsible for handling Django web framework and serving dynamic web pages to users. It handles incoming HTTP requests and send the requests to the Django application by configuring the web server software such as Apache. |
| Server 2 | MySQL Database Server | As the main MySQL database server, it is reponsible for storing and managing the relational data of the application. |
| Server 3 | MongoDB Database Server | This server acts as the main MongoDB databse server which is used to store and manage the NoSQL data of the application. The data stored in JSON file type is usually saved in this database server. |
| Server 4 | Load Balancer | This server takes the incoming web requests and distribute them across different web servers. By having this server, the incoming traffic can be distributed evenly and prevent system down problem when high load and busy traffic occurs. |
| Server 5 | Backup Server | The role of this server is to perform backup and replication process for the databases in MySQL and MongoDB which will help to maintain data integrity and data availability. |

After that, we can start to integrate Django with the JSON dataset, ensuring data storage and retrieval from both MySQL and MongoDB databases. The steps are as below:

## Step 1:
### Install the servers
| Server | Server Type | Steps |
| --- | --- | --- |
| Server 1 | Django Web Server | To install Django, run the command `pip install django` |
| Server 2 | MySQL Database Server | To install MySQL, run the command `pip install mysqlclient` |
| Server 3 | MongoDB Database Server | To install MongoDB, run the command `pip install djongo` |

<br>

### Create Django project and Django app
To create a Django project, run the command below.
```
django-admin startproject AA_SupplyStore
```
Modify the directory to the project folder.
```
cd AA_SupplyStore
```
Then, create a Django app by running the command.
```
python manage.py startapp SupplyStore
```

<img src="..\Question 1\files\images\createproj.png" >
<br>
<br>

### Configuring Django settings
Go to settings.py in the AA_SupplyStore folder to set up the database connection for both MySQL and MongoDB.

For MySQL:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_supplysales',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

For MongoDB:
```
DATABASES['mongodb'] = {
    'ENGINE': 'djongo',
    'NAME': 'SupplySales',
    'CLIENT': {
        'host': 'mongodb://localhost:27017'
    }
}
```
<br>

### Define model
Then, we need to define the model. Based on the dataset given, the database contains a single collection called `sales`. It has `items` and `customer` fields which contains nested attributes. Therefore, when creating a model, we need to use `JSONField`. The code are as follows:

```
from django.db import models

class Sale(models.Model):
    saleDate = models.DateTimeField()
    storeLocation = models.CharField(max_length=100)
    couponUsed = models.BooleanField()
    purchaseMethod = models.CharField(max_length=20)
    items = models.JSONField()
    customer = models.JSONField()

    def __str__(self):
        return str(self.id)
```
<br>

### Load JSON file to the model's database
Import the module and libraries.
```
import json
from django.core.management.base import BaseCommand
from SupplyStore.models import Sale
```

Load the JSON data and save to the database.
```
with open('sales.json') as json_file:
    data = json.load(json_file)
    for item in data:
        sale = Sale(
            saleDate=item['saleDate'],
            storeLocation=item['storeLocation'],
            couponUsed=item['couponUsed'],
            purchaseMethod=item['purchaseMethod'],
            items=item['items'],
            customer=item['customer']
        )
        sale.save()
```
<br>

### Migration
Now, we can start to migrate the `Sale` model to the `SupplyStore` app.To perform initial migration for the app, run the code below:
```
python manage.py makemigrations SupplyStore
```

Then, perform migration to create the database table.
```
python manage.py migrate
```
<br>

### Retrieve Data
After performing the migration, we can try to access the data. First, we need to import the `Sale` model. 
```
from SupplyStore.models import Sale
```

Get all sales by running the code below:
```
sales = Sale.objects.all()
```

To access each record of the sale, we need to iterate though the query set.
```
for sale in sales:
    sale_id = sale.id
    sale_date = sale.saleDate
    store_location = sale.storeLocation
    coupon_used = sale.couponUsed
    purchase_method = sale.purchaseMethod
    items = sale.items
    customer = sale.customer

    # This code will print the sale details
    print("Sale ID:", sale_id)
    print("Sale Date:", sale_date)
    print("Store Location:", store_location)
    print("Coupon Used:", coupon_used)
    print("Purchase Method:", purchase_method)
    print("Items:", items)
    print("Customer:", customer)
    print("-----------------------------")
```
<br>

## Question 1 (b)
The system architecture focusing on the seamless integration between the web server (Django), dataset (JSON), and databases (MySQL and
MongoDB) can be illustrated as below:

<img src="..\Question 1\files\images\systemarch.png" >

<div style="text-align: justify;">
The user interacts with Django web server thorugh the web interfaces (front-end). The Django web server will take the HTTP requests, process the user input and provide responses by displaying dynamic web pages using Django. It interacts with the databases which is stored in MySQL and MongoDB to manage data storage and data retrieval. MySQL is mainly used to store structured relational data in tables with predefined schemas while MongoDB is primary used to store NoSQL document data in Binary JSON. Django ORM will responsible for communicating with the database to perform database operations such as create, update, view and delete. The models is used to define the data structure and relationships in the JSON file. 
</div>
<br>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



