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
   - Install Django framework on the web server.
   - Create a new Django project using the `django-admin startproject` command.
   - Create a new Django app using the `python manage.py startapp` command.

2. Define the User Model:
   - In the Django app, open the `models.py` file and define the User model class.
   - Add fields like username, password, email, etc. to represent the user's information.
   - Implement any additional fields required for customer, technical workers, and senior management.

   Example code snippet:
   ```python
   from django.db import models
   from django.contrib.auth.models import AbstractUser

   class User(AbstractUser):
       is_customer = models.BooleanField(default=False)
       is_technical_worker = models.BooleanField(default=False)
       is_senior_management = models.BooleanField(default=False)

       # Additional fields for each user type
       # ...
   ```

3. Configure MySQL Database:
   - Open the Django project's settings file (`settings.py`).
   - Set up the MySQL database connection by providing the database name, user, password, and host.
   - Specify the database engine as `'django.db.backends.mysql'`.

   Example code snippet:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'your_mysql_host',
           'PORT': 'your_mysql_port',
       }
   }
   ```

4. Generate Database Tables:
   - Run the migrations to create the necessary database tables based on the defined models.
   - Use the `python manage.py makemigrations` command to generate migrations.
   - Apply the migrations using the `python manage.py migrate` command.

5. Implement User Registration and Login Views:
   - Create views for user registration and login functionality.
   - These views handle form submissions, validate user input, and interact with the database.
   - Use Django's built-in authentication views and forms or create custom views and forms.

   Example code snippet for user registration view:
   ```python
   from django.contrib.auth.forms import UserCreationForm
   from django.shortcuts import render, redirect

   def register(request):
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')
       else:
           form = UserCreationForm()
       return render(request, 'registration/register.html', {'form': form})
   ```

6. Create Templates and URLs:
   - Create HTML templates for user registration and login forms.
   - Define URL patterns in the app's `urls.py` file to map views to URLs.

   Example code snippet for URL patterns:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('register/', views.register, name='register'),
       # Other URL patterns for login, logout, etc.
       # ...
   ]
   ```

7. Implement User Authentication and Authorization:
   - Customize authentication and authorization settings based on user types (customers, technical workers, senior management).
   - Use Django's built-in authentication and authorization features to restrict access to specific views or functionalities.

   Example code snippet for authorization in views:
   ```python
   from django.contrib.auth.decorators import login_required

   @login_required
   def restricted_view(request):
       # Only authenticated users can access this view
       # ...
   ```

## Question 3 (b)
The challenges in addressing Data Replication and Synchronization between MySQL and MongoDB:
1. Evaluate Database-Specific Replication Techniques:
   - Research and evaluate database-specific replication techniques provided by MySQL and MongoDB.
   - Determine if their built-in replication mechanisms meet the project requirements.
   - Identify the replication type, such as master-slave replication, multi-master replication, or sharding.

2. Select an External Tool:
   - Explore external tools that facilitate real-time updates and seamless interaction between MySQL and MongoDB.
   - Identify tools such as Apache Kafka, Debezium, or similar solutions that support data replication and synchronization.

3. Implement Replication Solution:
   - Install and configure the selected tool or replication mechanism on the server.
   - Configure the replication settings to connect to both MySQL and MongoDB databases.
   - Specify the replication rules, such as which tables or collections need to be synchronized.

4. Test and Monitor:
   - Execute tests to verify the replication and synchronization process.
   - Monitor the replication process for any errors or inconsistencies.
   - Set up monitoring tools or alerts to ensure data consistency and identify any issues promptly.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



