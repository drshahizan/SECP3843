<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: ADAM WAFII BIN AZUAR

#### Matric No.: A20EC0003

#### Dataset: MFLIX DATASET

## Question 3 (a)

  1. Open command prompt to Setup the virtual environment

      <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/env%20setup.jpg">

      
  2. Type ```django-admin startproject mflix``` to create the Django Project. Create a new app called ```mflixportal``` inside the project

      <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/proje%20%26%20app.jpg">

      
  3. Inside the ```mflix``` project open ```settings.py``` file, configure the database MySQL according to my settings and the new app to ```INSTALLED_APPS```.

      <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/database.jpg">


      <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/installed%20appas.jpg">


  4. Next, define the user model for ```mflixportal``` inside ```mflixportal/models.py```. Additional fields will be added to Django Abstract Model to represent the user roles.


  <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/models.py.jpg">
  
      
  5. Next, Create views for user registration, login and dashboards purposes to handle the process inside ```mflixportal/views.py```.


  <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/view%201.jpg">


  <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/view%202.jpg">


  <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/view%203.jpg">


  <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/view%204.jpg">


  6. Create a registration form by creating a new python file ```forms.py``` inside ```mflixportal```.


  <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/formspy.jpg">


  7. Inside project's ```urls.py``` configure the URL route.

  <img src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/Jokeryde/question3/files/images/urls.jpg">


  8. Create HTML files for login, registration and dashboard

  login.html
  
  <img src="https://github.com/drshahizan/SECP3843/blob/72be4c95aa2a0465a72009898c0fbb82f2c28905/submission/Jokeryde/question3/files/images/login.jpg">

  register.html

  <img src="https://github.com/drshahizan/SECP3843/blob/72be4c95aa2a0465a72009898c0fbb82f2c28905/submission/Jokeryde/question3/files/images/register.jpg">


  9. Next, in order to apply changes made, type the following command below:

  <img src="https://github.com/drshahizan/SECP3843/blob/d80ed594214e2c1b457230f6a48af0cb5b1064f0/submission/Jokeryde/question3/files/images/makemig.jpg">


  <img src="https://github.com/drshahizan/SECP3843/blob/d80ed594214e2c1b457230f6a48af0cb5b1064f0/submission/Jokeryde/question3/files/images/migrate.jpg">


  10. Run the project by typing ```python manage.py runserver```

  <img src="https://github.com/drshahizan/SECP3843/blob/814e83ebd781e984a83b21a90855ec5bc64b1079/submission/Jokeryde/question3/files/images/runserver.jpg">

  
  <h2>Web Server</h2>

  Register Inside Web Server

  <img src="https://github.com/drshahizan/SECP3843/blob/a62afafd27e898b48c0a007e21b9a045242884f7/submission/Jokeryde/question3/files/images/register%20web.jpg">

  Login Inside Web Server

  <img src="https://github.com/drshahizan/SECP3843/blob/a62afafd27e898b48c0a007e21b9a045242884f7/submission/Jokeryde/question3/files/images/login%20web.jpg">
  

## Question 3 (b)

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
