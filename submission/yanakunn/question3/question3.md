<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURARISSA DAYANA BINTI MOHD SUKRI
#### Matric No.: A20EC0120
#### Dataset: SALES

## Question 3 (a)
This project will incorporate a user registration and login module into the MySQL database. This module will serve three different types of users: customers, technical workers, and senior management. To build this module, we will use Django as the web server framework and MySQL as the database.

#### Step 1: Configure the MySQL database.
1. Install the MySQL client for Python in the virtual environment inside the project's directory.
  ``` ruby
  (.venv) project % pip3 install mysqlclient
  ```
2. To use MySQL in this Django project, we will utilized XAMPP's PHPMyAdmin

- XAMPP
  - Open `http://localhost/phpmyadmin/` and create a new database.
  - <img width="300" alt="Screenshot 2023-06-29 at 7 50 29 AM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/70b6950b-e627-4cbe-ae2e-4084b5372d82">

2. In the project's core folder, go to settings.py file, update the `DATABASES` setting to use MySQL.
  ```ruby
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'NAME': 'your_database_name',
               'USER': 'your_username',
               'PASSWORD': 'your_password',
               'HOST': 'localhost',
               'PORT': '3306',
           }
       }
  ```

#### Step 2: Create a custom User model.
1. In the `models.py` file, import the necessary modules and create a custom User model by extending Django's AbstractUser class.
  ```ruby
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
  USER_TYPE_CHOICES = (
      ('customer', 'Customer'),
      ('technical_worker', 'Technical Worker'),
      ('senior_management', 'Senior Management'),
  )
  
  user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
  
  # Override the 'groups' field
  groups = models.ManyToManyField(
      'auth.Group',
      related_name='home_users',
      blank=True,
      help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
      verbose_name='groups',
  )
  
  # Override the 'user_permissions' field
  user_permissions = models.ManyToManyField(
      'auth.Permission',
      related_name='home_users',
      blank=True,
      help_text='Specific permissions for this user.',
      verbose_name='user permissions',
  )
  
  class Meta:
      db_table = 'users'
      app_label = 'home'
  ```

2. In the project's `settings.py` file, add the following setting to specify the custom user model:
  ```ruby
  AUTH_USER_MODEL = '<appname>.CustomUser'
  ```

#### Step 3: Generate database migrations

1. Run the following command to generate the initial migrations
  ```ruby
  python manage.py makemigrations
  ```
3. Apply the migrations to create the corresponding database tables
  ```ruby
  python manage.py migrate
  ```

#### Step 4: Create user registration and login views with Django's built-in authentication views and forms.

1. Define the URL in the `urls.py` file:
  ```ruby
  from django.contrib.auth import views as auth_views
  
  urlpatterns = [
     # Login and logout views
     path('login/', auth_views.LoginView.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     # Registration view and URL
     path('register/', views.register, name='register'),
  ]
  ```
2. Create a register view in the `views.py` file to handle user registration.
  ```ruby
  from django.shortcuts import render, redirect
  from .forms import RegistrationForm
  
  def register(request):
     if request.method == 'POST':
         form = RegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('login')
     else:
         form = RegistrationForm()
     return render(request, 'registration/register.html', {'form': form})
  ```

3. Create a registration form in the `forms.py` file that inherits from Django's UserCreationForm and includes an additional field for the role.
  ```ruby
  from django import forms
  from .models import CustomUser
  from django.contrib.auth.forms import UserCreationForm
  
  class RegistrationForm(UserCreationForm):
     role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
     
     class Meta:
         model = CustomUser
         fields = ('username', 'password1', 'password2', 'role')
  ```


### Step 6: Start the Django development server
  ```ruby
  (.venv) $ python manage.py runserver
  ```

## Question 3 (b)
In this project, we use MongoDB to store JSON datasets and MySQL to manage user information. These databases are not interconnected, and thus data synchronization between them is unnecessary. Any modifications to one database will only impact the other if a business requirement or logic necessitates synchronization.

However, there are certain cases where we need to combine data from both databases. For instance, MySQL database can be used as a backup to store the sales data. In that case, we can perform data retrieval and integration operations in the application logic, fetching relevant data from MongoDB and MySQL separately and combining them as needed.

### Steps to synchronize data between MySQL and MongoDB databases in Django
#### Step 1: Define the models for both databases according to the JSON sales data fields.
  ```ruby
  from django.db import models
  
  # MongoDB Model (Main)
  class Sale(models.Model):
      _id = models.CharField(max_length=24, primary_key=True)
      saleDate = models.DateTimeField()
      items = models.JSONField()
      storeLocation = models.CharField(max_length=255)
      customer = models.JSONField()
      couponUsed = models.BooleanField()
      purchaseMethod = models.CharField(max_length=255)
  
      class Meta:
          db_table = 'sales'
          app_label = 'home'
  
  # MySQL Model (Backup)
  class SaleBackup(models.Model):
      _id = models.CharField(max_length=24, primary_key=True)
      saleDate = models.DateTimeField()
      items = models.JSONField()
      storeLocation = models.CharField(max_length=255)
      customer = models.JSONField()
      couponUsed = models.BooleanField()
      purchaseMethod = models.CharField(max_length=255)
  
      class Meta:
          db_table = 'sales_backup'
          app_label = 'home'
  ```
#### Step 2: Create the synchronization function.
This function retrieves data from MongoDB and synchronizes it with the MySQL database as a backup. To retrieve all sales records from MongoDB, this function establishes a connection to the database and iterates through each record. For each sale record, a corresponding SaleBackup record is created in MySQL if the record does not exist.

  ```ruby
from .models import Sale, SaleBackup

def sync_data():
    mongodb_sales = Sale.objects.using('mongodb').all()

    # Synchronize data from MongoDB to MySQL
    for sale in mongodb_sales:
        try:
            backup = SaleBackup.objects.get(_id=sale._id)
            # Update existing record in MySQL
            backup.saleDate = sale.saleDate
            backup.items = sale.items
            backup.storeLocation = sale.storeLocation
            backup.customer = sale.customer
            backup.couponUsed = sale.couponUsed
            backup.purchaseMethod = sale.purchaseMethod
            backup.save()
        except SaleBackup.DoesNotExist:
            # Create new record in MySQL
            backup = SaleBackup(
                _id=sale._id,
                saleDate=sale.saleDate,
                items=sale.items,
                storeLocation=sale.storeLocation,
                customer=sale.customer,
                couponUsed=sale.couponUsed,
                purchaseMethod=sale.purchaseMethod
            )
            backup.save()

    # Delete records in MySQL that are not present in MongoDB
    mysql_sales = SaleBackup.objects.all()
    mysql_ids = [sale._id for sale in mongodb_sales]
    mysql_sales.filter(~models.Q(_id__in=mysql_ids)).delete()
  ```
#### Step 3: Trigger the synchronization process every time there is a change in the main model.
  ```ruby
  sync_data()
  ```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



