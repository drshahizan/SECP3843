<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Madihah binti Che Zabri
#### Matric No.: A20EC0074
#### Dataset: <a href="https://github.com/drshahizan/dataset/blob/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/07-stories/stories.json">stories.json</a>

## Question 3 (a)
#### Set up Django project

1. If Django is not intalled yet, open command prompt and run `pip install Django` to install Django framework 
2. Create a new Django project and redirect to your prefered directory
   
```python
cd Desktop
C:\Users\madih\AppData\Local\Microsoft\WindowsApps\python.exe -m django startproject project 
```
3. go to newly create project folder by typing `cd project`

<img src="../question3/files/images/Q3a(1).png">


#### Setup DB connection (MySQL)

1. Install MySQL connector for Python by running `pip install mysql-connector-python`
<img src="../materials/Q3a(2).png">

2. Create a new database named `project` in phpMyAdmin

3. Go to setting.py and configure the MySQL database

```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Create a Django app

1. Create Django app by running
```bash
python manage.py startapp projectapp
```

2. Go to project > settings.py to add 'projectapp' in the the code:
```kotlin
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projectapp',
]
```
#### Define the User model

1. Go to projectapp > `models.py` and define the User model for authentication

```ruby
from django.db import models
from django.contrib.auth.models import AbstractUser

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

2. Run the database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
<img src="../materials/Q3_3.png">

#### Create registrations and login views

1. Create a new file called `forms.py` under projectapp

```python
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=User.USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'user_type']
```

2. Update views.py under projectapp

```python
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Replace 'login' with the URL name of your login page
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})
```

3. Create new folder named templates

```kotlin
projectapp/
├── __pycache__
├── migrations
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── views.py
└── templates/
```

4. Under templates, create folder registration
   
6. Update setting.py in project:

```rust
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'projectapp/templates/registration'),
            os.path.join(BASE_DIR, 'projectapp/templates/'),
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

#### Create login views and templates

1. Add new class inside `forms.py`

```python 
class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
```

2. Add a new method inside views.py file to handle login:

```python 
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

  def customer_dashboard_view(request):
    return render(request, 'customer_dashboard.html')

  def technical_worker_dashboard_view(request):
        return render(request, 'technical_worker_dashboard.html')
    
  def management_dashboard_view(request):
        return render(request, 'management_dashboard.html')
```

3. Create login form:

```html
<form method="POST" action="{% url 'login' %}">
   {% csrf_token %}

   <div>
      <label for="id_username">Username:</label>
      <input type="text" id="id_username" name="username">
   </div>

   <div>
      <label for="id_password">Password:</label>
      <input type="password" id="id_password" name="password">
   </div>

   <div>
      <input type="submit" value="Login">
   </div>

   {% if messages %}
   <div>
      {% for message in messages %}
      <p>{{ message }}</p>
      {% endfor %}
   </div>
   {% endif %}
</form>

<a href="{% url 'user_registration' %}">Register</a>

```

4. Create 3 simple dashboard for each user for three types of people: customers, technical workers, and senior management.

#### Define URL patterns:

1. Map the views to specific URL patterns in projectapp's urls.py file.

```python
from django.contrib import admin
from django.urls import path, include
from q3_app.views import user_registration, login_view, customer_dashboard_view, technical_worker_dashboard_view, management_dashboard_view

urlpatterns = [
    path('customer_dashboard/', customer_dashboard_view, name='customer_dashboard'),
    path('technical_worker_dashboard/', technical_worker_dashboard_view, name='technical_worker_dashboard'),
    path('management_dashboard/', management_dashboard_view, name='management_dashboard'),
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('register/', user_registration, name='user_registration'),
]

```

2. Run `python manage.py runserver` in command prompt

   
### Ouput:

#### Login Page

<img src="../question3/files/images/Q3_4.png">

#### Registeration Page

<img src="../question3/files/images/Q3_5.png">

#### Customer Dashboard

<img src="../question3/files/images/Q3_dashboardcust.png">

#### Management Dashboard

<img src="../question3/files/images/Q3_dashboard.png">

#### Technical Worker Dashboard

<img src="../question3/files/images/Q3_dashboardtech.png">

#### Link to the project folder

<a href="./question3">Souce Code Folder</a>

### Question 3 (b)
### Understand data models

1. Since we are using MySQL and MongoDB databases, we need to understand both data models.
2. Identify the entities and data feild that eed to be synchronized between the databases.

### Choose database-specific replication techniques

1. Database-Specific Replication Techniques (MySQL):

    MySQL provides built-in replication mechanisms that can be utilized to synchronize data between MySQL and MongoDB.

    a. MySQL Binary Log Replication:

        Enable binary logging in MySQL server configuration.
        Set up a replica MongoDB instance.

    b. MySQL Triggers:

        Create triggers in MySQL to capture data changes (INSERT, UPDATE, DELETE).

### Implement Logic

1. Open XAMPP Controler panel and click config for MySQL to open `my.ini`

2. Uncomment or add this line of code inside `my.ini` and saved the file

```bash
log-bin=mysql-bin
```

3. Setup a replica MongoDB instance

<ul>
<li>Connect to MongoDB Atlas</li>
<li>Create new Database using MongoDB Compass and new Collection named Question3</li>
</ul>

4. Download necessary packages `pip install mysql-connector-python`

5. Create a new folder name `MySQL-to-MongoDB-Replication` and a new python file name `mysql_to_mongodb_replication.py`

```python
import mysql.connector
from pymongo import MongoClient

# MySQL connection
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='question3'
)
mysql_cursor = mysql_connection.cursor()

# MongoDB connection
mongo_client = MongoClient('mongodb+srv://mincridible:minzpro1@min.tan7fdn.mongodb.net/')
mongo_db = mongo_client['Question3b']
mongo_collection = mongo_db['q3']

# Read data from the MySQL table
mysql_cursor.execute("SELECT * FROM q3_app_user")
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
        'user_type': row[11]
    }
    mongo_collection.insert_one(row_data)
    print("Inserted row with ID:", row[0])  # Logging statement

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
    database='question3'
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

        if table_name == 'q3_app_user':
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

```

6. Run the python code `python mysql_to_mongodb_replication.py`

<img src="../question3/files/images/Q3b_4.png">

### Explanation:

In the above code, firstly I imported my current data from MySQL table to my newly created MongoDB database.

#### MySQL data:

<img src="../question3/files/images/Q3b_2.png">

#### MongoDB view: 

<img src="../question3/files/images/Q3b_3.png">

Afterwards, the purpose of the code is to initiate an action whenever data is inserted, updated, or deleted from MySQL. This action ensures that the MongoDB database is automatically updated.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




