<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Hong Pei Geok
#### Matric No.: A20EC0044
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets" >Tweets</a>

## Question 3 (a)
There will be several steps to create the managing user module.
### Assumptions:
1. The project and application have been created.
2. The required packages have been installed. (django, mysqlclient)
3. The superuser has been created.
4. In this project, I assume customers will register through the website while technical workers and senior management will be registered by admin.

### Step 1: Configure Database
Open setting.py to configure the database setting in order to connect with MySQL.
<p align="center">
  <img  src="./files/images/mysql.png"></img>
</p>

### Step 2: Define Model
I have defined a custom user model that extends Django's built-in AbstractBaseUser or AbstractUser class to customize the user model fields according to the requirements of the three user types which are customers, technical workers, and senior management.
<p align="center">
  <img  src="./files/images/model.png"></img>
</p>

Afterward, specify the custom user model as the default authentication model by setting AUTH_USER_MODEL to the custom user model in the settings.py file.
```
AUTH_USER_MODEL = 'your_app_name.CustomUser'
```
In my case, I have the application name as authentication.

<p align="center">
  <img  src="./files/images/aut.png"></img>
</p>

### Step 3: Migrate Database
Run the following command to apply the migrations and create the necessary database tables.
```
python manage.py makemigrations
python manage.py migrate
```
Command Prompt:
<p align="center">
  <img  src="./files/images/migrate.png"></img>
</p>

Result:
<p align="center">
  <img  src="./files/images/migrateresult.png"></img>
</p>

### Step 4: Define Admin Site
This step is to enable the admin to register users through the http://127.0.0.1:8000/admin/. 
<p align="center">
  <img  src="./files/images/admin.png"></img>
</p>

### Step 5: Define User Registration and Login View
Define views in Django app's views.py file for user registration and login functionality to handle the registration and login forms, validate user input, and interact with the MySQL database.
First, import the required libraries.
```
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
```

Register
  <img  src="./files/images/registerview.png"></img>
  > It can be noted that the user who registered through the website will have the user type as customer.

Login

The user credentials will be verified and determine the type of user. For example, if the user is a customer, he will be redirected to the customer dashboard. Below shows the code to determine the user type. 
<p align="center">
  <img  src="./files/images/loginview.png"></img>
</p>

The following code will be the view that renders the template for each user type. 
<p align="center">
  <img  src="./files/images/redirectview.png"></img>
</p>


### Step 6: Create User Registration and Login Templates
The HTML templates for user registration and login forms will be created in Django app's templates folder to render the forms and handle form submissions.
- register.html
  <p align="center">
    <img  src="./files/images/registertemplate.png"></img>
  </p>
- login.html
  <p align="center">
    <img  src="./files/images/logintemplate.png"></img>
  </p>


### Step 7: Configure URL

Define URL patterns for the registration and login views.
<p align="center">
  <img  src="./files/images/url.png"></img>
</p>

The URL for the dashboard view after login is defined as below.
<p align="center">
  <img  src="./files/images/url2.png"></img>
</p>

### Output: User Interfaces
#### Register
- Customer <br>
  Customer will be registered through the website.
  <img  src="./files/images/customerregister.png"></img>
- Admin <br>
  Admin is able to register all users.
  <img  src="./files/images/adminsite.png"></img>
#### Login
  <img  src="./files/images/login.png"></img>
  
#### Customer Dashboard
<img  src="./files/images/customer.png"></img>

#### Technical Worker Dashboard
<img  src="./files/images/technical.png"></img>

#### Senior Management Dashboard
<img  src="./files/images/senior.png"></img>


## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



