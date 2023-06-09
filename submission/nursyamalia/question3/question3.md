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

## Question 3 (a)

1. Setting up Django:
- Install Django framework on the web server using the `pip install django` command.
- Create virtual environment and activate it.
```python
python -m venv myenv
myenv\Scripts\activate
```
- Create a new Django project using the `django-admin startproject user` command.
- Install MySQL using the `pip install mysqlclient` command.

2. Configure MySQL Database:
- Open the Django project's settings file (`settings.py`).
- Set up the MySQL database connection by providing the database name, user, password, and host.
- Specify the database engine as `'django.db.backends.mysql'`.
```python
DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'user',
     'USER': 'root',
     'PASSWORD': '',
     'HOST': 'localhost',
     'PORT': '3306'
 }
}
```

3. Define the User Model:
- Create a new app by using the `python manage.py startapp app` command.
- Open the Django project's settings file (`settings.py`) and add  `app` in INSTALLED_APP.
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
- In the Django app, open the `models.py` file and define the User model class.
- Add fields like username, password, email, etc. to represent the user's information.
- Implement any additional fields required for customer, technical workers, and senior management.
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
 USER_TYPES = (
     ('customer', 'Customer'),
     ('technical_worker', 'Technical Worker'),
     ('senior_management', 'Senior Management'),
 )
 user_type = models.CharField(max_length=20, choices=USER_TYPES)
 # Add any additional fields you need for each user type

 groups = models.ManyToManyField(
     'auth.Group',
     related_name='custom_user_set',
     blank=True,
     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
     verbose_name='groups',
 )

 user_permissions = models.ManyToManyField(
     'auth.Permission',
     related_name='custom_user_set',
     blank=True,
     help_text='Specific permissions for this user.',
     verbose_name='user permissions',
 )
```

4. Generate Database Tables:
- Create new database name `user` in MySQL.
- Run the migrations to create the necessary database tables based on the defined models.
- Use the `python manage.py makemigrations` command to generate migrations.
- Apply the migrations using the `python manage.py migrate` command.
- After migrations, the tables can be seen like below:

   <img  src="./files/images/mysql.png"></img>

5. Implement User Registration and Login Views:
   
- In views.py:
  
```python
from .forms import UserRegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Handle login and registration form
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login') 
    else:
        form = UserRegistrationForm()
        
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f"Logged in as {username}")
            print(f"User type: {user.user_type}")
            
            if user.user_type == 'customer':
                print("Redirecting to customer dashboard")
                return redirect('customer_dashboard')
            elif user.user_type == 'technical_worker':
                print("Redirecting to technical worker dashboard")
                return redirect('technical_worker_dashboard')
            elif user.user_type == 'senior_management':
                print("Redirecting to management dashboard")
                return redirect('management_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

# Handle dashboard views for all user types
def customer_dashboard_view(request):
    return render(request, 'customer_dashboard.html')

def technical_worker_dashboard_view(request):
    return render(request, 'technical_worker_dashboard.html')

def management_dashboard_view(request):
    return render(request, 'management_dashboard.html')
```

- In forms.py:
  
```python
from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=User.USER_TYPES)

class Meta:
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name', 'user_type']
```

- .html for:
   - User registration page:
   
   <img  src="./files/images/reg.png"></img>
   
   - Login page:
   
   <img  src="./files/images/log.png"></img>
   
   - Customer dashboard page:
   
   <img  src="./files/images/cs.png"></img>
   
   - Senior management dashboard page:
   
   <img  src="./files/images/sm.png"></img>
   
   - Technical worker dashboard page:
   
   <img  src="./files/images/tw.png"></img>


6. Set URLs and Templates:
- Define URL patterns in the app's `urls.py` file to map views to URLs.

```python
from django.contrib import admin
from django.urls import path, include
from app.views import registration, login_view, customer_dashboard_view, technical_worker_dashboard_view, management_dashboard_view

urlpatterns = [
    path('customer_dashboard/', customer_dashboard_view, name='customer_dashboard'),
    path('technical_worker_dashboard/', technical_worker_dashboard_view, name='technical_worker_dashboard'),
    path('management_dashboard/', management_dashboard_view, name='management_dashboard'),
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('register/', registration, name='registration'),
]
```
- Open the Django project's settings file (`settings.py`) and edit in TEMPLATES.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'app/templates/'),
            os.path.join(BASE_DIR, 'app/templates/authentication'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

7. Run server:
- In command prompt, run below:
```python
python manage.py runserver
```
- User registration page:

   <img  src="./files/images/register.png"></img>
   
- Login page:

  <img  src="./files/images/login.png"></img>

## Question 3 (b)
<p>When working with two different databases, such as MySQL and MongoDB, there are several approaches to address the challenge of data replication and synchronization. 
One possible solution is to use an external tool or library that facilitates real-time updates and seamless interaction between the databases. 
This is the general outline of the steps involved I use in implementing the solution:</p>

1. Create MySQL trigger by opening XAMPP and click on the **Config**. Choose the **my.ini** file. In here, it contains various settings and parameters that control the behavior and functionality of the MySQL server. 
  <img  src="./files/images/xampp.png"></img>
  
2. Configure the database by uncomment the `log-bin=mysql-bin`. When I set log-bin=mysql-bin in the my.ini file, it instructs MySQL to enable binary logging and store the binary log files with a base name of mysql-bin.
  <img  src="./files/images/uncomment.png"></img>

3. Install related packages to do integration for both MySQL to MongoDB.
 ```python
 pip install mysql-connector-python
 ```
4. Create a folder to store replication python file. Make a new folder called **replication** and put a file called **replication.py** in it. This file defines the connection for both databases, retrieving data from the MySQL table and inserting it into the MongoDB collection. Define code to read the binary logs to determine the kind of operation (INSERT, UPDATE, DELETE), and then perform the appropriate action on the MongoDB collection to maintain it synchronised with the MySQL database. 

For MySQL (Django models):
```python
import mysql.connector
from pymongo import MongoClient

# MySQL connection
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='analytics'
)
mysql_cursor = mysql_connection.cursor()

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017')
mongo_db = mongo_client['analytics']
accounts_collection = mongo_db['accounts']
customers_collection = mongo_db['customers']
transactions_collection = mongo_db['transactions']

# Read data from the MySQL tables
mysql_cursor.execute("SELECT * FROM accounts")
accounts_results = mysql_cursor.fetchall()

mysql_cursor.execute("SELECT * FROM customers")
customers_results = mysql_cursor.fetchall()

mysql_cursor.execute("SELECT * FROM transactions")
transactions_results = mysql_cursor.fetchall()

# Import data to MongoDB - accounts
for account_row in accounts_results:
    account_data = {
        'account_id': account_row[0],
        'limit': account_row[1],
        'products': account_row[2].split(",")
    }
    accounts_collection.insert_one(account_data)
    print("Inserted account with account_id:", account_data['account_id'])

# Import data to MongoDB - customers
for customer_row in customers_results:
    customer_data = {
        'username': customer_row[0],
        'name': customer_row[1],
        'address': customer_row[2],
        'birthdate': customer_row[3],
        'email': customer_row[4],
        'accounts': customer_row[5].split(","),
        'tier_and_details': customer_row[6]
    }
    customers_collection.insert_one(customer_data)
    print("Inserted customer with username:", customer_data['username'])

# Import data to MongoDB - transactions
for transaction_row in transactions_results:
    transaction_data = {
        'account_id': transaction_row[0],
        'transaction_count': transaction_row[1],
        'bucket_start_date': transaction_row[2],
        'bucket_end_date': transaction_row[3],
        'transactions': transaction_row[4]
    }
    transactions_collection.insert_one(transaction_data)
    print("Inserted transaction with account_id:", transaction_data['account_id'])

# Log the binary log events
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
        operation = query_parts[0].upper()

        print("Binary Log Event:")
        print("Query:", query)

        if table_name == 'accounts':
            if operation == 'INSERT':
                values_start = query.index("VALUES") + 7
                values_end = query.index(")", values_start)
                values = query[values_start:values_end].split(",")

                account_data = {
                    'account_id': int(values[0]),
                    'limit': int(values[1]),
                    'products': [p.strip().strip("'") for p in values[2].split(",")]
                }

                accounts_collection.insert_one(account_data)
                print("Inserted account with account_id:", account_data['account_id'])

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
                    if column == 'products':
                        value = [p.strip().strip("'") for p in value.split(",")]
                    update_data[column] = value

                where_parts = where_clause.split("=")
                condition_column = where_parts[0].strip()
                condition_value = where_parts[1].strip("'")

                filter_condition = {'account_id': int(condition_value)}

                accounts_collection.update_one(filter_condition, {'$set': update_data})
                print("Updated account matching condition:", filter_condition)

            elif operation == 'DELETE':
                where_start = query.index("WHERE") + 6
                where_clause = query[where_start:]

                where_parts = where_clause.split("=")
                condition_column = where_parts[0].strip()
                condition_value = where_parts[1].strip("'")

                filter_condition = {'account_id': int(condition_value)}

                accounts_collection.delete_one(filter_condition)
                print("Deleted account matching condition:", filter_condition)

        elif table_name == 'customers':
            if operation == 'INSERT':
                values_start = query.index("VALUES") + 7
                values_end = query.index(")", values_start)
                values = query[values_start:values_end].split(",")

                customer_data = {
                    'username': values[0].strip("'"),
                    'name': values[1].strip("'"),
                    'address': values[2].strip("'"),
                    'birthdate': values[3].strip("'"),
                    'email': values[4].strip("'"),
                    'accounts': values[5].strip("'").split(","),
                    'tier_and_details': values[6].strip("'")
                }

                customers_collection.insert_one(customer_data)
                print("Inserted customer with username:", customer_data['username'])

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

                filter_condition = {'username': condition_value}

                customers_collection.update_one(filter_condition, {'$set': update_data})
                print("Updated customer matching condition:", filter_condition)

            elif operation == 'DELETE':
                where_start = query.index("WHERE") + 6
                where_clause = query[where_start:]

                where_parts = where_clause.split("=")
                condition_column = where_parts[0].strip()
                condition_value = where_parts[1].strip("'")

                filter_condition = {'username': condition_value}

                customers_collection.delete_one(filter_condition)
                print("Deleted customer matching condition:", filter_condition)

        elif table_name == 'transactions':
            if operation == 'INSERT':
                values_start = query.index("VALUES") + 7
                values_end = query.index(")", values_start)
                values = query[values_start:values_end].split(",")

                transaction_data = {
                    'account_id': int(values[0]),
                    'transaction_count': int(values[1]),
                    'bucket_start_date': values[2].strip("'"),
                    'bucket_end_date': values[3].strip("'"),
                    'transactions': []
                }

                transactions_collection.insert_one(transaction_data)
                print("Inserted transaction with account_id:", transaction_data['account_id'])

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

                filter_condition = {'account_id': condition_value}

                transactions_collection.update_one(filter_condition, {'$set': update_data})
                print("Updated transaction matching condition:", filter_condition)

            elif operation == 'DELETE':
                where_start = query.index("WHERE") + 6
                where_clause = query[where_start:]

                where_parts = where_clause.split("=")
                condition_column = where_parts[0].strip()
                condition_value = where_parts[1].strip("'")

                filter_condition = {'account_id': condition_value}

                transactions_collection.delete_one(filter_condition)
                print("Deleted transaction matching condition:", filter_condition)

# Close MySQL connection
mysql_cursor.close()
mysql_connection.close()

# Close MongoDB connection
mongo_client.close()
```

5. Run the file in command prompt to replicate the data in MySQL and MongoDB.
```python
python replication.py
```


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



