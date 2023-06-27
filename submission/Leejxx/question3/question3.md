<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Jia Xian
#### Matric No.: A20EC0200
#### Dataset:

## Question 3 (a)
For this question, I will used the projecy(AA_Leejx) that created in Question 1a).
To create a user registration and login module using Django and MySQL for three types of users (customers, technical workers, and senior management), the steps are:

### 1. Database Setup for User Authentication (MySQL)
  a) In my case, i create a new app within the project(AA_Leejx) for User Authentication purpose:
  <img  src="./files/images/start1.JPG"></img>

  b) Then define the model for the new created app(user_accounts). From the question, we need to define the user_type field to the User model to distinguish between customer, technical worker, and senior management users. :
  <img  src="./files/images/model1.JPG"></img>

  c) Specify a custom user model for the Django project. For my case:
  
  <img  src="./files/images/model2.JPG"></img>

### 2. Database Migration
  a) Generate database migrations: Run the command `python manage.py makemigrations` to generate database migration files based on the changes made to the User model.
  
   <img  src="./files/images/manage1.JPG"></img>

  b) Apply database migrations: Run the command `python manage.py migrate` to apply the generated migrations and create the necessary tables in the MySQL database.
  
   <img  src="./files/images/maange2.JPG"></img>

  c) Result:

   <img  src="./files/images/manage3.JPG"></img>
  

### 3. User Registration
  a) Create a registration form: Create a Django form (UserRegistrationForm) that includes fields for username, password, email. 
     <img  src="./files/images/register1.JPG"></img>
     
  b) Create a registration view: Define a view function (register) that handles the registration logic. In this view, validate the form data, create a new User instance, save it to the database.
     <img  src="./files/images/register2.JPG"></img>
     
  c) Create a registration template: Create an HTML template (register.html) that displays the registration form and handles form submission.
     <img  src="./files/images/register3.JPG"></img>

### 4. User Login
  a) Create a login form: Create a Django form (UserLoginForm) that includes fields for username and password.
    <img  src="./files/images/login1.JPG"></img> 

  b) Create a login view: Define a view function (user_login) that handles the login logic. In this view, validate the form data, authenticate the user using Django's authenticate() function, and log in the user using login().
    <img  src="./files/images/login2.JPG"></img>

  c) Create a login template: Create an HTML template (login.html) that displays the login form and handles form submission.
    <img  src="./files/images/login3.JPG"></img>

### 5. User Dashboard
  a) Create dashboard templates: for me, I created three HTML templates (customer_dashboard.html, technicalWorker_dashboard.html, seniorManagement_dashboard.html) that represent the dashboards for each user type. 
     <img  src="./files/images/dashboard1.JPG"></img>

  b) Create a dashboard view: Define a view function (dashboard) that checks the authenticated user's user_type attribute and renders the appropriate dashboard template based on the user type. If the user is not recognized or not authenticated, redirect them to the login page.
    <img  src="./files/images/dashboard2.JPG"></img>

### 6. URL Configuration:
  a) Update URL patterns: Update the project's URL configuration (urls.py) to include URL patterns for user registration, login, and the dashboard view. Map the URLs to their respective views.
     <img  src="./files/images/url1.JPG"></img>

### User interfaces:
  a) Login:
     <img  src="./files/images/logini.JPG"></img>
     
  b) Register:
     <img  src="./files/images/registeri.JPG"></img>

  c) Customer's dashboard:
    <img  src="./files/images/dashboardc.JPG"></img>
    
  d) Technical Worker's dahboard:
     <img  src="./files/images/dashboardt.JPG"></img>

  e) Senior Management's dahboard:
     <img  src="./files/images/dashboards.JPG"></img>


## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



