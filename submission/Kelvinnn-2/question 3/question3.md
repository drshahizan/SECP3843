<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kelvin Ee
#### Matric No.: A20EC0195
#### Dataset: City Inspection

## Question 3 (a)

### 1. To install and set up Django, follow these steps:

a. Create Virtual Environment
```
virtualenv env
```

Once you have created the virtual environment, you can activate it by running the following command.
```
env\Scripts\activate
```

b. Run the command `pip install Django` to install Django using pip, the Python package manager. Make sure you have Python and pip installed on your system.

c. After the installation is complete, you can create a new Django project by running the following command:   
```python
django-admin startproject q3
```
This command will create a new Django project with the name "q3". You can replace "q3" with your desired project name.

d.Once the project is created, navigate to the project folder using the cd command. In this case, run:
<img src="./files/image/q3.png">

### 2. MySQL setup

a. To set up MySQL for your Django project, follow these steps:

Install the MySQL connector for Python by running the command `pip install mysql-connector-python`. This package allows Django to communicate with the MySQL database.

<img src="./files/image/mysql.png">

b. After the installation is complete, create a new database named q3 in phpMyAdmin. This will be the database where the Django project will store its data.

c. Open the `settings.py` file in  Django project and locate the DATABASES configuration. Modify it to match the following configuration:

```python 
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

### 3. Create a Django app

a. Open the command prompt and navigate to the root directory of  Django project. Then run the following command:
```bash
python manage.py startapp q3_app
```
This will create a new Django app named q3_app within the project directory. The app will have a basic structure and files.

b. Open the settings.py file in the Django project and locate the INSTALLED_APPS configuration. Add 'q3_app' to the list of installed apps as shown below:
```kotlin
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'q3_app',
]
```
By adding 'q3_app' to the INSTALLED_APPS,  the q3_app Django app are registered to be used in your project.


### 4. Define the User model

a. Open the models.py file in the q3_app directory and add the following code:

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
b. To apply the model changes to the database, run the following commands in the command prompt:

```bash
python manage.py makemigrations
python manage.py migrate
```
<img src="./files/image/migrate.png">

<img src="./files/image/q3migrate.png">

After running the migrations, the User model will be created in the database with the defined fields and relationships.

### 5. Create registrations views and templates

a. Create a new file called `forms.py` in your q3_app directory. Add the following code to define the UserRegistrationForm:

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

b. Open app's views.py file and add the following code to create a view function for user registration:

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
c. Create new direcotry and file:

```kotlin
q3_app/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── urls.py
├── views.py
└── templates/
    └── registration/  <--- New directory
        └── user_registration.html  <--- New file
```

d.  Inside the registration directory, create a file named user_registration.html with the following content:

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Register</button>
</form>
```
e. In your settings.py file, update the TEMPLATES setting to include the directory where the user_registration.html template is located. Add the following paths to the DIRS list:

```rust
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'q3_app/templates/registrations'),
            os.path.join(BASE_DIR, 'q3_app/templates/'),
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

### 6. Create login views and templates

a.  Inside  forms.py file, add a new class called LoginForm to handle the login form:
```python 
class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
```
The LoginForm class defines two fields, username and password, which will be displayed in the login form.

b. In views.py file, add the following code to handle the login view:

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

c. Create the login template login.html with the following content:

```html
<div style="background-color: rgb(86, 86, 175); padding: 20px;">
    <div style="max-width: 400px; margin: 0 auto; background-color: white; padding: 20px;">
        <h1 style="text-align: center; font-family: 'Comic Sans MS', cursive; color: navy;">Login</h1>

        <form method="POST" action="{% url 'login' %}">
            {% csrf_token %}

            <div style="margin-bottom: 10px;">
                <label for="id_username">Username:</label>
                <input type="text" id="id_username" name="username" class="form-control">
            </div>

            <div style="margin-bottom: 10px;">
                <label for="id_password">Password:</label>
                <input type="password" id="id_password" name="password" class="form-control">
            </div>

            <div style="text-align: center;">
                <button type="submit" class="btn btn-primary">Login</button>
            </div>

            {% if messages %}
            <div style="text-align: center; color: red; margin-top: 10px;">
                {% for message in messages %}
                <p>{{ message }}</p>
                {% endfor %}
            </div>
            {% endif %}
        </form>

        <p style="text-align: center; font-family: 'Comic Sans MS', cursive; color: navy;">
            Don't have an account? <a href="{% url 'user_registration' %}">Register</a>
        </p>
    </div>
</div>

```

d. Create three dashboard templates for each user type: customer_dashboard.html, technical_worker_dashboard.html, and management_dashboard.html. These templates  contain the HTML code specific to each user type's dashboard.

`customer_dashboard.html`
`management_dashboard.html`
`technical_worker_dashboard.html`

### 7. Path setting and run the App

a. Open the urls.py file in your Django project. This file is usually located in the main project directory. Import the views you need to map to the URL paths.

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

b. Run the following command to start the Django development server: `python manage.py runserver`
<img src="./files/image/runserver.png">

### Results:   
- Register:
<img src="./files/image/register.png">

- Login:
<img src="./files/image/login.png">

- Customer Dashboard:
<img src="./files/image/customer.png">
<img src="./files/image/customerdashboard.png">

- Technical Worker Dashboard:
<img src="./files/image/technicalworkerdashboard.png">

- Senior Management Dashboard:
<img src="./files/image/seniormanagementdashboard.png">

## Question 3 (b)
To ensure data synchronization between MySQL and MongoDB databases, it is important to understand their respective data models. MySQL follows a relational data model, while MongoDB follows a document-based data model.

When choosing database-specific replication techniques, we can consider the following options:

#### 1. MySQL Binary Log Replication:

- Enable binary logging in the MySQL server configuration. This allows the server to generate binary log files capturing data changes.
- Set up a replica MongoDB instance. This will serve as the target database for data synchronization.

#### 2. MySQL Triggers:

- Create triggers in MySQL to capture data changes such as INSERT, UPDATE, and DELETE operations.
- Implement logic in the triggers to handle the captured data changes and propagate them to the MongoDB database.

To implement the chosen replication technique: 

1. Open the XAMPP Control Panel and navigate to the MySQL configuration file (my.ini).
   <img src="./files/image/myini.png">
   
2. Uncomment or add the line `log-bin=mysql-bin` in the my.ini file to enable binary logging
   <img src="./files/image/logbin.png">
   
3. Save the my.ini file and restart the MySQL server to apply the configuration changes.
4. Set up a replica MongoDB instance to serve as the target database for data synchronization.

<ul>
<li>Connect to MongoDB Atlas</li>
<li>Create new Database using MongoDB Compass and new Collection named `Q3`</li>
</ul>

5. Download necessary packages `pip install mysql-connector-python`

6.  Create a new folder name `MySQL-to-MongoDB-Replication` and a new python file name `mysql_to_mongodb_replication.py`
```python
import mysql.connector
from pymongo import MongoClient

# MySQL connection
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='q3'
)
mysql_cursor = mysql_connection.cursor()

# MongoDB connection
mongo_client = MongoClient('mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/')
mongo_db = mongo_client['Q3']
mongo_collection = mongo_db['q3user']

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
    database='q3'
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
7.   Run the python code `python mysql_to_mongodb_replication.py`
   <img src="./files/image/synchronous.png">

### Code Explaination
The provided code performs data synchronization between a MySQL database and a MongoDB database.

Firstly, the code establishes connections to both databases using the `mysql.connector` and `pymongo libraries` for MySQL and MongoDB, respectively. It then retrieves data from a specific table (`q3_app_user`) in the MySQL database.

Next, the code iterates over the fetched rows and transforms the data into a suitable format for MongoDB. Each row is converted into a dictionary, with field names and corresponding values mapped accordingly.The transformed data is then inserted into a MongoDB collection named `q3user` within the` Q3` database using the `insert_one` method. As each row is inserted, the code logs the ID of the inserted row.

After completing the data insertion process, the code closes the MySQL connection and re-establishes it to perform binlog monitoring. It retrieves the binary log events using the `SHOW BINLOG EVENTS` statement and filters out events related to the `q3_app_user` table. For each relevant binlog event, the code determines the type of operation (INSERT, UPDATE, DELETE) and extracts the corresponding SQL query.

If the operation is an INSERT, the code parses the values from the SQL query, constructs a dictionary, and inserts the data into the MongoDB collection. The ID of the inserted row is logged.

In the case of an UPDATE operation, the code extracts the SET clause and WHERE clause from the SQL query. It creates an update_data dictionary based on the SET clause and updates the matching document in the MongoDB collection using the `update_one` method.

For DELETE operations, the code extracts the WHERE clause, constructs a filter_condition dictionary, and deletes the matching document from the MongoDB collection using the `delete_one` method.

Throughout the process, the code logs the performed actions, including inserted, updated, or deleted rows.mFinally, the code closes the MySQL connection, ensuring the completion of the synchronization process between the two databases.

Proof:
### Figure below shows data in mysql
<img src="./files/image/usersql.png">

### Figure below shows data in mongodb
<img src="./files/image/usermongo.png">

   
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




