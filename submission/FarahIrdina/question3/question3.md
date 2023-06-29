<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: FARAH IRDINA BINTI AHMAD BAHARUDIN
#### Matric No.: A20EC0035
#### Dataset: AIRBNB LISTINGS DATASET

## Question 3 (a)

### Steps to create this module on Django web server by using MySql database server

#### 1. Define the user models

By using the same file 'models.py', add a new class. This class is about the information of the users. Since this project requires three types of users which are customers, technical workers and senior management, thus creating a custom user model is essential. 

```
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )

    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
```

#### 2. Configure authentication backend

Since we will be using a custom user model, thus we need to update the AUTH_USER_MODEL inside settings.py.

```
AUTH_USER_MODEL = 'Listings.User'
```

#### 3. Create login and register views

When we runserver, views help us to open the page that we have set. Views also handle the form submission, validations and user authentication processes.

```
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request=request, template_name="Listings/login.html")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="Listings/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if user.type == 'customer':
                    return render(request=request, template_name="Listings/customer.html")
                elif user.type == 'technical_worker':
                    return render(request=request, template_name="Listings/worker.html")
                elif user.type == 'senior_management':
                    return render(request=request, template_name="Listings/senior.html")
                else:
                    return render(request=request, template_name="Listings/home.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Listings/login.html", context={"login_form": form})
```

#### 4. Define url patterns

Open urls.py inside the project file, define both login and register views. 

```
from django.contrib import admin
from django.urls import path
from Listings import views

app_name = "Listings"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login")
    # Add more URL patterns as needed
]
```

#### 5. Create templates

Templates act as the interface that users will be accessing. Create forms inside both login.html and register.html files.

##### - login.html

```
{% block content %} {% load crispy_forms_tags %}

<!--Login-->
<div class="container py-5">
  <h1>Login</h1>
  <form method="POST">
    {% csrf_token %} {{ login_form|crispy }}
    <button class="btn btn-primary" type="submit">Login</button>
  </form>
  <p class="text-center">
    Don't have an account? <a href="/register">Create an account</a>.
  </p>
</div>

{% endblock %}
```

##### - register.html

```
{% block content %} {% load crispy_forms_tags %}

<!--Register-->
<div class="container py-5">
  <h1>Register</h1>
  <form method="POST">
    {% csrf_token %} {{ register_form|crispy }}
    <button class="btn btn-primary" type="submit">Register</button>
  </form>
  <p class="text-center">
    If you already have an account, <a href="/login">login</a> instead.
  </p>
</div>

{% endblock %}
```

#### 6. Create forms.py file

Create a forms.py file in Django app and define the custom registration form based on our user model. We can use ModelForm to simplify the form creation process.

```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    ]

    type = forms.ChoiceField(choices=USER_TYPE_CHOICES,
                             widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "type")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
```

#### 7. Perform databsae migrations

Lastly, we need to perform a database migration to update the database schema.

```
python manage.py makemigrations Listings
python manage.py migrate
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/three.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/three2.png)

### Result

#### - Register page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/register.png)

#### - Login page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/login.png)

#### - Customer page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/customer.png)

#### - Technical worker page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/worker.png)

#### - Senior management page

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/senior.png)

#### - MySQL Table User

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question3/files/images/mysql.png)


## Question 3 (b)

### 1. Use Trigger-based Replication Technique

This technique triggers to capture changes in the source database and apply them to the target database. Whenever the database detects changes in the source database, it will be triggered and insert the data to a table called listings_user_replicated. Open MySQL and go to SQL query and write the code below.

```
DELIMITER $$

CREATE TRIGGER replicate_listings_listings
AFTER INSERT ON listings_listings
FOR EACH ROW
BEGIN
    INSERT INTO listings_user_replicated (_id, listing_url, name, summary, space, description, neighborhood_overview, notes, transit, access, interaction, house_rules, property_type, room_type, bed_type, minimum_nights, maximum_nights, cancellation_policy, last_scraped, calendar_last_scraped, accommodates, bedrooms, beds, number_of_reviews, bathrooms, amenities, price, weekly_price, monthly_price, cleaning_fee, extra_people, guests_included, images, host, address, availability, review_scores, reviews)
    VALUES (NEW.id, NEW.listing_url, NEW.name, NEW.summary, NEW.space, NEW.description, NEW.neighborhood_overview, NEW.notes, NEW.transit, NEW.access, NEW.interaction, NEW.house_rules, NEW.property_type, NEW.room_type, NEW.bed_type, NEW.minimum_nights, NEW.maximum_nights, NEW.cancellation_policy, NEW.last_scraped, NEW.calendar_last_scraped, NEW.accommodates, NEW.bedrooms, NEW.beds, NEW.number_of_reviews, NEW.bathrooms, NEW.amenities, NEW.price, NEW.weekly_price, NEW.monthly_price, NEW.cleaning_fee, NEW.extra_people, NEW.guests_included, NEW.images, NEW.host, NEW.address, NEW.availability, NEW.review_scores, NEW.reviews);
END;
$$


DELIMITER ;
```

### 2. Implement Replication Process between MySQL and MongoDB

This technique triggers to capture changes in the source database and apply them to the target database. Whenever the database detects changes in the source database, it will be triggered and insert the data to a table called listings_user_replicated.

```
import mysql.connector
from pymongo import MongoClient
mysql_conn = mysql.connector.connect(host=localhost, user='root’, database=airbnb)
mysql_cursor = mysql_conn.cursor()

mongo_client = MongoClient("mongodb+srv://arasayooo:Irdin%407995335310@newcluster.rdxcnj3.mongodb.net/")
mongo_db = client["airbnb"]
mongo_collection = db["user"]

mysql_cursor = mysql_conn.cursor()
mysql_cursor.execute('SELECT * FROM airbnb)
changed_data = mysql_cursor.fetchall()

for item in changed_data::
    doc = {
        _id=item['_id'],
                listing_url=item['listing_url'],
                name=item['name'],
                summary=item['summary'],
                space=item['space'],
                description=item['description'],
                neighborhood_overview=item['neighborhood_overview'],
                notes=item['notes'],
                transit=item['transit'],
                access=item['access'],
                interaction=item['interaction'],
                house_rules=item['house_rules'],
                property_type=item['property_type'],
                room_type=item['room_type'],
                bed_type=item['bed_type'],
                minimum_nights=item['minimum_nights'],
                maximum_nights=item['maximum_nights'],
                cancellation_policy=item['cancellation_policy'],
                last_scraped=item['last_scraped'],
                calendar_last_scraped=item['calendar_last_scraped'],
                accommodates=item['accommodates'],
                bedrooms=item['bedrooms'],
                beds=item['beds'],
                number_of_reviews=item['number_of_reviews'],
                bathrooms=item['bathrooms'],
                amenities=item['amenities'],
                price=item['price'],
                weekly_price=item['weekly_price'],
                monthly_price=item['monthly_price'],
                cleaning_fee=item['cleaning_fee'],
                extra_people=item['extra_people'],
                guests_included=item['guests_included'],
                images=item['images'],
                host=item['host'],
                address=item['address'],
                availability=item['availability'],
                review_scores=item['review_scores'],
                reviews=item['reviews']    
}
    mongo_collection.insert_one(doc)

mysql_cursor.close()
mysql_conn.close()
mongo_client.close()
```

### 3. Implement Real-time Updates using Debezium

This allows to receive real-time notifications of changes happening in the database.

```
from debezium import connector

pipeline = [{'$match': {'operationType': {'$in': ['insert', 'update', 'replace', 'delete']}}}]
change_stream = mongo_collection.watch(pipeline=pipeline, full_document='updateLookup')

connector_config = {
    'name': 'mongodb-connector',
    'connector.class': 'io.debezium.connector.mongodb.MongoDbConnector',
    'tasks.max': '1',
    'mongodb.hosts': 'mongo_host:27017',
    'mongodb.name': 'mongodb_database',
    'database.hostname': 'mysql_host',
    'database.port': '3306',
    'database.user': 'mysql_user',
    'database.password': 'mysql_password',
    'database.dbname': 'mysql_database',
    'database.server.id': '1',
    'database.server.name': 'mysql_server',
    'collection.include.list': 'mongodb_database.mongodb_collection',
    'transforms': 'unwrap',
    'transforms.unwrap.type': 'io.debezium.transforms.ExtractNewRecordState',
    'transforms.unwrap.drop.tombstones': 'false'
}

connector = connector.Connector(connector_config)
connector.start()

for change in change_stream:
    operation_type = change['operationType']
    document_id = change['documentKey']['_id']
    document = change['fullDocument']

    if operation_type == 'insert' or operation_type == 'replace':
        pass
    elif operation_type == 'update':
        pass
    elif operation_type == 'delete':
        pass

change_stream.close()
connector.stop()
mongo_client.close()
mysql_cursor.close()
mysql_conn.close()
```




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



