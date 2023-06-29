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

## Question 3 (a)

<h4>Step 1 - Create and connect database</h4>

Create a database, 'aa_system' in MySQL database. In the aa_system VS code project file, connect to the database in the settings.py file.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa_system',
        'USER': 'root',
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}
```
<h4>Step 2 - Migrate into database</h4>

Create a new file named 'urls.py' to create the urls that direct users to different view page. 

```
from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name= 'index'),
      path('login/', views.login_view, name='login_view'),
      path('register/', views.register, name='register'),
      path('admin/', views.admin, name='admin'),
      path('customer/', views.customer, name='customer'),
      path('technical/', views.technical, name='technical'),
      path('senior/', views.senior, name='senior'),
]
```

After that, create models consist of users (Admin, Customer, Technical Workers, Senior Manager) in the models.py file.

```
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_technical = models.BooleanField('Is technical', default=False)
    is_senior = models.BooleanField('Is senior', default=False)
```

In the terminal, migrate using ```py manage.py makemigrations``` and ```py manage.py migrate```. The database will be update in the MySQL database.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/database.png" />
</p>

<h4>Step 3 - Create file for each view page</h4>

The image below shows the view file for each page.
<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/templates.png" />
</p>

- admin.py
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin page</title>
</head>
<body>
    <h1> hello {{ user.username }} Your user role is Admin</h1>
</body>
</html>
```

- base.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js" integrity="sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS" crossorigin="anonymous"></script>
    <!-- Add your additional CSS links or stylesheets here -->
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <!-- Add your additional JavaScript scripts or links here -->
</body>
</html>
```

- customer.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Customer page</title>
</head>
<body>
    <h1> hello {{ user.username }}  Your user role is Customer</h1>
</body>
</html>
```

- index.py

```
{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to your homepage!</h1>
    
{% endblock %}
```

- login.py

```
<!doctype html>
{% load static %}
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="{% static 'fonts/icomoon/style.css' %}">

    <link rel="stylesheet" href="{% static 'css/owl.carousel.min.css' %}">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">

    <!-- Style -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

    <title>Multiple user login</title>
  </head>
  <body>
  <div class="content">
    <div class="container">
      <div class="row justify-content-center">
        <!-- <div class="col-md-6 order-md-2">
          <img src="images/undraw_file_sync_ot38.svg" alt="Image" class="img-fluid">
        </div> -->
        <div class="col-md-6 contents">
          <div class="row justify-content-center">
            <div class="col-md-12">
              <div class="form-block">
                  <div class="mb-4">
                </div>

              <span class="mb-0 text-muted">
                {% if msg %}
                    {{ msg | safe }}
                {% else %}
                    Login page
                {% endif %}
              </span>
                <form  method="post">
                    {% csrf_token %}
                  <div class="form-group first">
                    <label for="username">Username</label>
                      {{ form.username }}
                  </div>
                  <div class="form-group last mb-4">
                    <label for="username">Password</label>
                    {{ form.password }}
                  </div>

                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">Remember me</span>
                      <input type="checkbox" checked="checked"/>
                      <div class="control__indicator"></div>
                    </label>
                    <span class="ml-auto"><a href="#" class="forgot-pass">Forgot Password</a></span>
                  </div>

                  <input type="submit" value="Log In" class="btn btn-pill text-white btn-block btn-primary">
                </form>
              </div>
            </div>
          </div>

        </div>

      </div>
    </div>
  </div>


    <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'js/popper.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>
  </body>
</html>
```

- register.py

```
<!doctype html>
{% load static %}
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="{% static 'fonts/icomoon/style.css' %}">

    <link rel="stylesheet" href="{% static 'css/owl.carousel.min.css' %}">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">

    <!-- Style -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

    <title>Multiple user login</title>
  </head>
  <body>
  <div class="content">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-6 contents">
          <div class="row justify-content-center">
            <div class="col-md-12">
              <div class="form-block">
                  <div class="mb-4">
                      <h1>User Registration page</h1>
                </div>
                  <span class="mb-0 text-muted">
                {% if msg %}
                    {{ msg | safe }}
                {% else %}
                    Login page
                {% endif %}
              </span>
                <form  method="post">
                    {% csrf_token %}
                  <div class="form-group first">
                    <label for="username">Username</label>
                      {{ form.username }}
                  </div>
                  <div class="form-group first">
                    <label for="email">Email</label>
                      {{ form.email}}
                  </div>
                  <div class="form-group last mb-4">
                    <label for="password">Password</label>
                      {{ form.password1 }}
                  </div>
                  <div class="form-group last mb-4">
                    <label for="password">confirm Password</label>
                      {{ form.password2 }}
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">Admin</span>
                        {{ form.is_admin }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">customer</span>
                        {{ form.is_customer }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">technical worker</span>
                        {{ form.is_technical }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                  <div class="d-flex mb-5 align-items-center">
                    <label class="control control--checkbox mb-0"><span class="caption">Senior Management</span>
                        {{ form.is_senior }}
                      <div class="control__indicator"></div>
                    </label>
                  </div>
                    <span class="text-error">{{ form.errors }}</span>
                  <input type="submit"  value="Register" class="btn btn-pill text-white btn-block btn-primary">
                </form>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>


    <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'js/popper.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>
  </body>
</html>
```

- senior.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Senior Manager page</title>
</head>
<body>
    <h1> hello {{ user.username }}  Your user role is Senior Manager</h1>
</body>
</html>
```

- technical.py

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Technical Worker page</title>
</head>
<body>
    <h1> hello {{ user.username }}  Your user role is Technical Worker</h1>
</body>
</html>
```

<h4>Step 4 - Create registration form</h4>

```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_customer', 'is_technical', 'is_senior')
```

<h4>Step 5 - Create superuser for testing system</h4>

Use this command line ```python manage.py createsuperuser``` to create a new superuser.

User Interfaces

- Registration Page
  
<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/register%20page.png" />
</p>

- Login Page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/Screenshot%202023-06-29%20015540.png" />
</p>

- Customer Page

<p align="center">
  <img height="100px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/customer.png" />
</p>

- Technical Workers Page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/technical.png" />
</p>

- Senior Manager Page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/senior%20manager.png" />
</p>

- Superuser view users page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/user%20view%20page.png" />
</p>

- Edit users page

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/edit%20user.png" />
</p>




## Question 3 (b)

<h4>Step 1 - Set Up Replication in MySQL</h4>

In the Xampp, open the configuration file of phpmyadmin by clicking the 'my.ini'.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/my.ini.png" />
</p>

Uncomment the line 'log-bin=mysql-bin' in the configuration file.

From this

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/comment.png" />
</p>

To this

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/uncomment.png" />
</p>

<h4>Step 2 - Create a database in MongoDB Compass</h4>

Create a new database named 'aa_system' and collection 'app_user' in MongoDB compass.

<p align="center">
  <img height="100px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/databasename.png" />
</p>

<h4>Step 3 - Create a mongoDB.py file in VS code</h4>

<p align="center">
  <img height="100px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/mongoDB.py.png" />
</p>

The following code in the mongoDB.py is to connect to both MySQL and MongoDB local database. The row_data reprsents all the rows need to be defined to be insert into the MongoDB database. The structure is same as the aa_app_user table in MySQL database. 

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/Screenshot%202023-06-29%20130159.png" />
</p>

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/Screenshot%202023-06-29%20130212.png" />
</p>

```
import mysql.connector
from pymongo import MongoClient

# Connect to MySQL database
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='aa_system'
)
mysql_cursor = mysql_connection.cursor()

# Connect to MongoDB database
mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_database = 'aa_system'
mongodb_collection = 'app_user'

mongo_client = MongoClient('localhost', 27017)
mongodb = mongo_client['aa_system']
mongo_collection = mongodb['app_user']

# Read data from the MySQL table
mysql_cursor.execute("SELECT * FROM aa_app_user")
results = mysql_cursor.fetchall()

# Import data to MongoDB
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
        'is_admin': row[11],
        'is_customer': row[12],
        'is_technical': row[13],
        'is_senior': row[14],
    }
    mongo_collection.insert_one(row_data)
    print("Inserted row with ID:", row[0])

# Close MySQL connection
mysql_cursor.close()
mysql_connection.close()

# Close MongoDB connection
mongo_client.close()

# Log the binary log events
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='aa_system'
)
mysql_cursor = mysql_connection.cursor()

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

        if table_name == 'aa_app_user':
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
                    'is_admin': bool(int(values[11])),
                    'is_customer': bool(int(values[12])),
                    'is_technical': bool(int(values[13])),
                    'is_senior': bool(int(values[14])),
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
                print("Updated row matching condition:", filter_condition)  # Logging statement

            elif operation == 'DELETE':
                where_start = query.index("WHERE") + 6
                where_clause = query[where_start:]

                where_parts = where_clause.split("=")
                condition_column = where_parts[0].strip()
                condition_value = where_parts[1].strip("'")

                filter_condition = {condition_column: condition_value}

                mongo_collection.delete_one(filter_condition)
                print("Deleted row matching condition:", filter_condition)  # 

# Close MySQL connection
mysql_cursor.close()
mysql_connection.close()

mongo_client.close()
```

Then, run the command in the terminal to migrate the data. ```python C:\Users\User\Desktop\aa_system\aa_system\aa_system\mongoDB.py```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/command.png" />
</p>

Result:

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/Screenshot%202023-06-29%20123212.png" />
</p>

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question3/files/images/mongo.png" />
</p>



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


