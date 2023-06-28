<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Vincent Boo Ee Khai
#### Matric No.: A20EC0231
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 3 (a)
### 1. Setup Environment
1. Create a and activate the Virtual Environment:
```
py -m venv myenv
myenv\Scripts\activate
```

2.Install all the needed package:
```
python pip install django
pip install mysql-connector-python
```

3. Create new Django project with the following code:
```
django-admin startproject q3
py manage.py startapp app
```

### 2. Configure Database
1. Create a new database in MySQL
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/51284dba-093a-426e-a396-9b50a10243c9"/>

2. Configure the database setting in `setting.py` to connect with MySQL.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'q3',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Define Model 
Created a model in Django by extending the AbstractUser class. This customization allows to tailor the user model fields for three user types: customers, technical workers, and senior management.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/cacec9c3-b84c-47ba-a2be-a534e3f4cbe4"/>

Then, set the model as default authentication model in `setting.py` as the following code:
```
AUTH_USER_MODEL = 'app.User'
```

### 4. Migrate Database
Migrate and create the databse table with these code:
```
python manage.py makemigrations 

python manage.py migrate
```
The output from terminal:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/fa0ff521-58ed-4785-8b97-4fab57c3d737"/>

The result in MySQl:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/85c9aa43-d8c2-4d95-968a-732e56a1b599"/>

### 5. Create Forms for User
Create a new file named 'form.py' in the app that are newly created.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/2fb1e2e7-60ec-4ed0-8012-563fb556aac3"/>

### 6. Define Views that Handle the User Registration and Login.
These views will be responsible for managing the registration and login forms, validating user input, and interacting with the MySQL database. To begin, necessary libraries is needed to be import.
```
from app.form import UserRegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
```
We will need to write these following code to define Login for user:
```
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
```
Then, define register user
```
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})
```
Lastly, locate each user type to view to the related the template.
```
def customer_dashboard_view(request):
    return render(request, 'customer_dashboard.html')

def technical_worker_dashboard_view(request):
    return render(request, 'technical_worker_dashboard.html')

def management_dashboard_view(request):
    return render(request, 'management_dashboard.html')
```

### 7. Create Template for Create User Registration and Login
1. Login:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/b22cccfd-5346-4978-9265-dc54f5284716"/>

2. Register
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/5d1564f0-98ed-4e89-ae6e-a20667e96d62"/>

### 8. Configure the URL
1. URL path for login and user registration.
```
from django.contrib import admin
from django.urls import path, include
from app.views import user_registration, login_view, customer_dashboard_view, technical_worker_dashboard_view, management_dashboard_view

urlpatterns = [
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', user_registration, name='user_registration'),
]
```

2. URL path for dashboard view for each user type
```
path('customer_dashboard/', customer_dashboard_view, name='customer_dashboard'),
path('technical_worker_dashboard/', technical_worker_dashboard_view, name='technical_worker_dashboard'),
path('management_dashboard/', management_dashboard_view, name='management_dashboard'),
```

### User Interface
1. Login
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/af501f19-f79a-4169-9b96-d269f7d623cb"/>

2. Register
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/c4551943-55e4-4665-a516-19b1c4b2b25e"/>

#### Dashboard
1. Customer 
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/00a01dd0-a4a2-49a4-8403-46460d70e8f6"/>

2. Technical Worker
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/ce4098cd-5872-46f4-a3a1-c31a10eaa6cb"/>

3. Management
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/cbb73235-1106-4aa8-8242-50b0b95782c2"/>

## Question 3 (b)
### 1. Understand and Identify
When working with both MySQL and MongoDB databases, it is important to have an understanding of the data models for each database. This knowledge helps identify the entities and data fields that need to be synchronized between the two databases to ensure data consistency. 

To overcome the challenge of data replication and synchronization, developers can explore database-specific replication techniques or utilize external tools that facilitate real-time updates and seamless interaction between the databases. By following these steps, it becomes possible to effectively manage data replication and synchronization between MySQL and MongoDB databases.

### 2. Configure Database Setting 
We will need to define the the connection for MongoDB and MySql in `setting.py`.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stories',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306,
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'NAME': 'Question3b',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
            'port': 27017,
            'username': '',
            'password': '',
        }
    }
}
```

### 3. Implement Replica Technique
1. Open Xampp Controller.
2. Go to MySQl column and click on the Config button and select on 'my.ini'
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/676ed048-e571-4c0b-9cb4-ee73da212d6f"/>
3. Uncomment or add the line `log-bin=mysql-bin` in the file.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/f3667c64-99d0-4868-a205-2ca243dfa3ce"/>
4. Save and restart the MySQL

### 4. Set Up MongoDB
Open MongDB and create a database named `Question3` and collection as `q3`.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/28382b7f-d4bc-4610-a2f0-5e53403cf608"/>

### 5. Create a New folder and File
New folder name as `MySQL-to-MongoDB-Replication` and a new python file as `mysql_to_mongodb_replication.py`
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/300e1bb7-434c-4aa2-b577-61e48be99f75"/>

### 6. Code Explaination 
There are two techniques that had been used in this file is MySQL binary log replication and MySQL triggers.
MySQL binary log replication is a feature in MySQL that allows you to replicate changes made to a MySQL database from one server to another.
MySQL triggers are database objects that are associated with a table and automatically execute in response to specific events or actions performed on that table.
1. Import SQL connector and MongoClient
```
import mysql.connector
from pymongo import MongoClient
```
2. MySQL: Create Connection
```
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='q3'
)
mysql_cursor = mysql_connection.cursor()
```

3.MongoDB: Create Connection
```
mongo_client = MongoClient('mongodb+srv://mincridible:minzpro1@min.tan7fdn.mongodb.net/')
mongo_db = mongo_client['Question3b']
mongo_collection = mongo_db['q3']
```

4. MySQL: Read Data
```
mysql_cursor.execute("SELECT * FROM app_user")
results = mysql_cursor.fetchall()
```

5. Import data to MongoDB
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

6. Log binary log events
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

7. MySQL: Close Connection
```
mysql_cursor.close()
mysql_connection.close()
```
8. MongoDB: Close Connection
```
mongo_client.close()
```

### 7. Run the program
1. Before we run the program, we will need to download the package `pip install mysql-connector-python`
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/e6409e6a-d5da-4567-908d-1038b41c611b"/>
2. Use the code to run python file `mysql_to_mongodb_replication.py`
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/7d0c4a91-4ffe-4f1e-8f97-c91080cf4cd4"/>

### 8. Results
#### 1. MySQL
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/fc58be3b-097d-477b-bdf1-2543b0f4eba1"/>

#### 2. MongoDB
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/efd9db29-c2fd-47a2-8b6c-09407b68aff7"/>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



