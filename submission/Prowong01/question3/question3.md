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

## Question 3 (a)
### Step 1: Set up Django Project & App
To set up Django project & app, I need to create and activate the virtual environment first

```
python -m venv env
env\Scripts\activate
```

Then, install the django package
```
pip install django
```

Create new Django project called question 3 and a new app called q3 through command prompt.
```
django-admin startproject question3
cd question3
python manage.py startapp q3
```

Command Prompt:
<img  src="./files/images/django.png"></img>

### Step 2: Install MySQL Python Driver & Configure Database Setting
Install the mysqlclient as this is a library that allows Django to connect and communicate with the MySQL database.
```
pip install mysqlclient
```
<img  src="./files/images/mysqlclient.png"></img>

Next, update the settings.py file in question3 project folder. I change the DATABASES dictionary to configure the MySQL database values.
<img  src="./files/images/setting.png"></img>


### Step 3: Configure models.py
I need to define the models for q3 app that represent the data that I want to store in the database.
<img  src="./files/images/model.png"></img>

### Step 4: Migrate Database
Apply the database migrations to create the necessary tables for the user model in the MySQL database.
```
python manage.py makemigrations Q3_analytics_app
python manage.py migrate
```
<img  src="./files/images/model.png"></img>

SQL Result:
<img  src="./files/images/mysql_result.png"></img>

### Step 5: Create Form for User
Import the User model from  models.py file, which defines the attributes and methods of the user class
<img  src="./files/images/forms.png"></img>

### Step 6: Create View File and Template
Define a login_view function 
<img  src="./files/images/login_view.png"></img>

Define a user_registration function 
<img  src="./files/images/user_register.png"></img>

Locate each user type to view to the related the template.
<img  src="./files/images/all.png"></img>

Create new directories at the app and put all the template inside one folder.
<img  src="./files/images/template.png"></img>

In your settings.py file, update the TEMPLATES setting to include the directory and remember to import the os module also.
<img  src="./files/images/include_template.png"></img>

### Step 6: Configure URL
<img  src="./files/images/url.png"></img>

## Ouput:

### Home Page
<img  src="./files/images/homepage.png"></img>

### Home Page
<img  src="./files/images/login.png"></img>

### Registration Page
<img  src="./files/images/register.png"></img>

### Customer Page
<img  src="./files/images/customer.png"></img>

### Technical Worker Page
<img  src="./files/images/worker.png"></img>

### Senior Management Page
<img  src="./files/images/management.png"></img>

### MySQL Database
<img  src="./files/images/after_login.png"></img>

## Question 3 (b)
MySQL and MongoDB are two different types of database management systems. MySQL is a relational database that uses SQL to store and query structured data in tables. MongoDB is a document-oriented database that uses JSON-like documents to store and query semi-structured data in collections. 

## Replication Technique
### 1. Configure Database Setting   
<img  src="./files/images/setup_database.png"></img>

### 2. Implement Replication Technique
 a. Open XAMPP Controler panel and click config for MySQL to open my.ini
 <img  src="./files/images/my_ini.png"></img>
 b. Uncomment ``` log-bin=mysql-bin ```
 <img  src="./files/images/uncomment.png"></img>
 c. Setup a new MongoDB database
<img  src="./files/images/new_db.png"></img>
 d. Create a new folder and a python file
 <img  src="./files/images/create.png"></img>

### 3. Implementation
a. Import SQL connector and MongoClient
```
import mysql.connector
from pymongo import MongoClient
```

b. MySQL: Create Connection
```
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='q3'
)
mysql_cursor = mysql_connection.cursor()
```

c. MongoDB: Create Connection
```
mongo_client = MongoClient('mongodb+srv://eddiewong:prowong42@cluster0.ytff2so.mongodb.net')
mongo_db = mongo_client['Q3']
mongo_collection = mongo_db['replication']
```

d. MySQL: Read Data
```
mysql_cursor.execute("SELECT * FROM app_user")
results = mysql_cursor.fetchall()
```

e. Import data to MongoDB
```
for row in results:
    row_data = {
        'id': row[0],
        'password': row[1],
        'last_login': row[2],
        'is_superuser': row[3],
        'username': row[4],
        'first_name': row[5],
        'last_name': row[6],
        'email': row[7],
        'is_staff': row[8],
        'is_active': row[9],
        'date_joined': row[10],
        'user_type': row[11]
    }
    mongo_collection.insert_one(row_data)
    print("Inserted row with ID:", row[0])
```

f. Log binary log events
```
mysql_cursor.execute("SHOW BINARY LOGS")
binary_logs = mysql_cursor.fetchall()

latest_log = binary_logs[-1]
log_filename, log_position = latest_log[0], latest_log[1]

mysql_cursor.execute(f"SHOW BINLOG EVENTS IN '{log_filename}' FROM {log_position}")
for binlog_event in mysql_cursor:
    event_type = binlog_event[7]

    if event_type == 2:
        query = binlog_event[8]

        query_parts = query.split()
        table_name = query_parts[2]
        operation = "INSERT"

        if table_name == 'app_user':
            print("Binary Log Event:")
            print("Query:", query)  # Logging statement

            if operation == 'INSERT':
                values_start = query.index("VALUES") + 7
                values_end = query.index(")", values_start)
                values = query[values_start:values_end].split(",")

                row_data = {
                    'id': int(values[0]),
                    'password': values[1].strip("'"),
                    'last_login': values[2].strip("'"),
                    'is_superuser': bool(int(values[3])),
                    'username': values[4].strip("'"),
                    'first_name': values[5].strip("'"),
                    'last_name': values[6].strip("'"),
                    'email': values[7].strip("'"),
                    'is_staff': bool(int(values[8])),
                    'is_active': bool(int(values[9])),
                    'date_joined': values[10].strip("'"),
                    'user_type': values[11].strip("'")
                }

                mongo_collection.insert_one(row_data)
                print("Inserted row with ID:", row_data['id'])  # Logging statement

            elif operation == 'UPDATE':
                set_start = query.index("SET") + 4
                set_end = query.index("WHERE", set_start)
                set_clause = query[set_start:set_end]

                where_start = query.index("WHERE") + 6
                where_clause = query[where_start:]

                set_pairs = set_clause.split(",")
                update_data = {}
                for pair in set_pairs:
                    column, value = pair.split("=")
                    column = column.strip()
                    value = value.strip("'")
                    update_data[column] = value

                where_parts = where_clause.split("=")
                condition_column = where_parts[0].strip()
                condition_value = where_parts[1].strip("'")

                filter_condition = {condition_column: condition_value}

                mongo_collection.update_one(filter_condition, {'$set': update_data})
                print("Updated row matching condition:", filter_condition)  

            elif operation == 'DELETE':
                where_start = query.index("WHERE") + 6
                where_clause = query[where_start:]

                where_parts = where_clause.split("=")
                condition_column = where_parts[0].strip()
                condition_value = where_parts[1].strip("'")

                filter_condition = {condition_column: condition_value}

                mongo_collection.delete_one(filter_condition)
                print("Deleted row matching condition:", filter_condition) 
```
g. MySQL: Close Connection
```
mysql_cursor.close()
mysql_connection.close()
```
h. MongoDB: Close Connection
```
mongo_client.close()
```

### 4.Result
MYSQL
<img  src="./files/images/mysql_r.png"></img>

MongoDB
<img  src="./files/images/insert_mongodb.png"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



