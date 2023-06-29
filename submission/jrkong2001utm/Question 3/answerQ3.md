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

## Question 3 (a)
To create a role-based registration system using Django with MySQL, first we need to create a project.
```
django-admin startproject AA_user
```
Modify the directory to the project folder.
```
cd AA_user
```
Then, create a Django app by running the command.
```
python manage.py startapp user
```

Step 1: Configure Settings.py
Go to Settings.py under the AA_user folder.

Add the app name in `INSTALLED_APPS`
```
INSTALLED_APPS = [
    'user',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Add AUTH_USER_MODEL 
```
AUTH_USER_MODEL='user.User'
```

Modify the database information
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'db_user',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}
```

Step 2: Modify Urls.py 
Go to urls.py which is located in the AA_user folder. Add the code below:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
]
```

Step 3: Add Model
Go to models.py under the user folder. Define the model for each users.
```
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_senior=models.BooleanField(default=False)
    is_technical=models.BooleanField(default=False)

class Technical(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

class Senior(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
```

After defining the model, we need to migrate the database to create tables in MySQL.

```
python manage.py makemigrations
python manage.py migrate
```

You will see the tables have been created in your MySQL when the migration is successful.

<img src="..\Question 3\files\images\migration.png">

Step 4: Add forms.py
Create a file named forms.py in the user folder. Type the code below:
```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, Senior, Technical, User

class CustomerSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return customer
    
class SeniorSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_senior = True
        user.save()
        senior = Senior.objects.create(user=user)
        senior.save()
        return senior

class TechnicalSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_technical = True
        user.save()
        technical  = Technical.objects.create(user=user)
        technical.save()
        return technical 
```

Step 5: Add views
Then, add views to your app. Type the code in the views.py in the user folder.
```
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .models import Customer,Senior, Technical,User
from django.views.generic import CreateView
from .forms import CustomerSignUpForm,SeniorSignUpForm,TechnicalSignUpForm
from django.contrib import auth

def login_view(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.is_customer:
                return redirect('cust_index')
            elif user.is_technical:
                return redirect('tech_index')
            elif user.is_senior:
                return redirect('senior_index')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')
    
def index(request):
    return render(request,'index.html')

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        form.save()
        return redirect('cust_index')
    
class TechnicalSignUpView(CreateView):
    model = User
    form_class = TechnicalSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'technical'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        form.save()
        return redirect('tech_index')
    
class SeniorSignUpView(CreateView):
    model = User
    form_class = SeniorSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'senior'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        form.save()
        return redirect('senior_index')

def cust_index(request):
    return render(request, 'cust_index.html')

def tech_index(request):
    username = request.user.username
    return render(request, 'tech_index.html')

def senior_index(request):
    username = request.user.username
    return render(request, 'senior_index.html')
```

Step 6: Add html pages
In you user folder, create a `template` folder. In the `template` folder, create `user` folder. All the html file will be keep in this `user` folder.

Create index.html
```

{% block content %}
  <h2>Login</h2>
  <form method="POST" action="{% url 'login_view' %}">
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
  </form>

  <button><a href="{% url 'customer_signup' %}">Register as Customer</a></button><br><br>
  <button><a href="{% url 'senior_signup'%}">Register as Senior</a></button>
  <button><a href="{% url 'technical_signup'%}">Register as Technical</a></button>
{% endblock %}

```

Create signup.html
```
<html>
 <head>
    <title>
        More than one user
    </title>
</head>
<body>
    <form method="POST" accept-charset="utf-8">
        {% csrf_token %}
        {{form.as_p}}
        <input type="Submit" name="submit" value="Signup">
    </form>
</body>
</html>
```

Create cust_index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Customer Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js" integrity="sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Welcome to Customer Dashboard</h1>
        <br>
        <br>
        <button><a href="{% url 'login_view'%}">Logout</a></button>
    </div>
</body>
</html>
```

Create senior_index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Senior Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js" integrity="sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Welcome to Senior Management Dashboard</h1>
        <br>
        <br>
        <button><a href="{% url 'login_view'%}">Logout</a></button>
    </div>
</body>
</html>
```

Create tech_index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Technical Staff Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js" integrity="sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Welcome to Technical Staff Dashboard</h1>
        <br>
        <br>
        <button><a href="{% url 'login_view'%}">Logout</a></button>
    </div>
</body>
</html>
```

Step 7: Add urls
Go to the urls.py in the user folder. Include the url's of the pages that you have created just now.

```
from django.urls import path
from . import views
from .views import index, CustomerSignUpView, TechnicalSignUpView, SeniorSignUpView, cust_index, tech_index, senior_index

urlpatterns = [
    path('', index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('customer', CustomerSignUpView.as_view(), name='customer_signup'),
    path('senior', SeniorSignUpView.as_view(), name='senior_signup'),
    path('technical', TechnicalSignUpView.as_view(), name='technical_signup'),
    path('cust_index', cust_index, name='cust_index'),
    path('tech_index', tech_index, name='tech_index'),
    path('senior_index', senior_index, name='senior_index'),
]
```

Step 8: Run Django app
To run your system, type in this command in the Visual Studio Code terminal.

```
python manage.py runserver
```

Control+Click on the link.

<img src="..\Question 3\files\images\index.png.png">

Output:
Login page

<img src="..\Question 3\files\images\index.png.png" >

Sign up page (Customer, Senior Management, Technical Staff)

<img src="..\Question 3\files\images\signup.png.png" >

Customer index page after login

<img src="..\Question 3\files\images\cust_index.png">

Senior Management index page after login

<img src="..\Question 3\files\images\senior_index.png">

Technical Staff index page after login

<img src="..\Question 3\files\images\tech_index.png">

## Question 3 (b)
To ensure that the any changes made in one database are accurately reflected in the other, I use dual write method.

Step 1: Configure Settings.py
Modify you database connection as the code below:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_sales',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'mongodb': {
    'ENGINE': 'djongo',
    'ENFORCE_SCHEMA': False,
    'NAME': 'salesdb',
    'CLIENT': {
        'host': 'localhost:27017',
        'port': 27017,
    },
  },
}
```

Step 2: Define model
Define the model as the data structure in the json file.
```
from django.db import models

class Sale(models.Model):
    saleDate = models.DateTimeField()
    storeLocation = models.CharField(max_length=100)
    couponUsed = models.BooleanField()
    items = models.JSONField(default=list)
    customer = models.JSONField(default=dict)
    purchaseMethod = models.CharField(max_length=255)
```

Step 3: Migration
Perform migration to create necessary tables in MySQL.
```
python manage.py makemigrations
python manage.py migrate
```

Step 4: Create view
Go the views.py. This code will synchronize the operation of insert between the MongoDB and MySQL.
```
from django.shortcuts import render
from django.db import connections
from pymongo import MongoClient
import json

# Establish connections to MySQL and MongoDB
mysql_connection = connections['default']
mongodb_client = MongoClient('mongodb://localhost:27017/')

def insert(sales_data):
    try:

        mysql_cursor = mysql_connection.cursor()
        mysql_query = """
        INSERT INTO sync_sale(id, saleDate, storeLocation, couponUsed, purchaseMethod, customer, items) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        mysql_values = (
            sales_data['id'],sales_data['saleDate'],sales_data['storeLocation'],sales_data['couponUsed'],sales_data['purchaseMethod'],sales_data['customer'],
            sales_data['items']
        )

        mysql_cursor.execute(mysql_query,mysql_values)

        mongodb_db = mongodb_client['salesdb']
        mongodb_collection = mongodb_db['sales']
        mongodb_collection.insert_one(sales_data)

        print("Insert successful!")
    
    except Exception as e:
        print(f"Insert failed: {str(e)}")

def test_insert():

    customer_data = {
        "gender": 'F',
        "age": 12,
        "email": 'C2@gmail.com',
        "satisfaction": 3
    }

    items_data = {
    "item1": {
        "name": "Item 1",
        "price": 10.99
    },
    "item2": {
        "name": "Item 2",
        "price": 5.99
    }
    }

    sales_data = {
        "id": 111,
        "saleDate": '2017-12-03T18:39:48.253+00:00', 
        "storeLocation": 'Johor', 
        "couponUsed": '0', 
        "purchaseMethod": 'TnG', 
        "customer": json.dumps(customer_data),
        "items": json.dumps(items_data)
    }

    insert(sales_data)

test_insert()
```

Step 5: Run the project
Type in the command to see the output. When the insert operation is successful, it will show the message "Insert successful!" as below.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




