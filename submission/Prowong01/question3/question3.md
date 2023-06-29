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


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



