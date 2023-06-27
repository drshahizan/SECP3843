<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Rishma Fathima Binti Basher
#### Matric No.: A20EC0137
#### Dataset: [Airbnb Listings Dataset](https://github.com/drshahizan/dataset/tree/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/05-airbnb)

## Question 3 (a)
  1. Setting up the Django Project:
     - Install Django on my web server.
     - Create a new Django project using the django-admin startproject AA_Question3 command.
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.1.png">
          
     - Create a virtual environment for this project.
       
       ``` ruby
       python -m venv my_env
       my_env\Scripts\activate
       ```
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.2.png">
          
     - Install package Django with the code pip install Django
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.3.png">
          

  2. Creating a Django App:
     - Create a new Django app within your project using the python manage.py startapp q3 command.
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.4.png">
          


   3. Configuring the MySQL Database:
      - Install the MySQL database connector for Python using pip install mysqlclient.
        
         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.5.png">
          
      - In the project's settings.py file, configure the database settings to connect to the MySQL database with the details like database name, host, port, username,           and password.

         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.6.png">
          
 
   4. Designing the User Model:
      - Define a user model class that will represent the users of the system in the q3's models.py file which include fields like username, email, password, and              fields specific to each user type (customers, technical workers, senior management).
      - The user model should include fields like username, email, password, and additional fields specific to each user type (customers, technical workers, senior             management)

         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.7.png">
          
 
  5. Creating the Registration and Login Views:
     - Create view functions for user registration and login in the q3's views.py file.
     - The registration view will handle user sign-up, validate the input data, and create a new user instance in the database.
     - The login view will handle user authentication, verify credentials, and provide access to the system upon successful login.
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.8.png">
          
 
  6. Implementing the Registration and Login Templates:
     - Create HTML templates for user registration and login forms which will include input fields for the required user information, such as username, email, and              password and he login template will contain fields for username/email and password.
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.9.png">

       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.10.png">
          
 
   7. Mapping URLs to Views:
      - Defined URL patterns in the q3's urls.py file, mapping them to the registration and login views that is created earlier.
        
         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.11.png">
          
 
  8. Migrating the Database:
     - Run the database migrations using the python manage.py makemigrations and python manage.py migrate commands which create the necessary database tables based on          the user model defined earlier.

       ```ruby
       python manage.py makemigrations
       python manage.py migrate
       ```

  9. Testing and Deployment:
      - The user registration and login functionality tested locally to ensure everything works as expected using the command:
        
        ```ruby
        python manage.py runserver
        ```
## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


