<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Afif Hazmie Arsyad Bin Agus
#### Matric No.: A20EC0176
#### Dataset: Supply Store

## Question 1 (a)
### Step required to integrate the 5 servers
1. Setup the server
   - Install and configure the 5 servers.
     - Django Web Server
       - Using `pip install django` in the command prompt
         
          <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA1.jpg" style="width: 700px; height: 200px;">
       
     - MongoDB Database Server
       - Using the command `pip install pymongo`
         
         <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA3.jpg" style="width: 700px; height: 100px;">
         
     - MySQL Database Server
       - Using the command `pip install mysqlclient`
         
         <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA2.jpg" style="width: 550px; height: 150px;">
         
     - JSON Dataset Server
     - Integration Script Server
       
2. Install necessary software
   - On the Django web server, install Python, Django.
   - Install MongoDB on the MongoDB database server and configure it with appropriate authentication and security settings.
   - On the MySQL database server, install MySQL Server and configure it.
   - On the JSON dataset server, set up a file server to provide access to the JSON dataset.
     
3. Create Django project and app.
   - Open the terminal in visual studio code or command prompt and type
   - `django-admin startproject Store`
     
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA4.jpg" style="width: 600px; height: 60px;">
     
   - Create django app within the project with the command
   - `python manage.py startapp AA`
  
4. Define data models
   - Define models representing the JSON dataset and its fields in the Django app's `models.py` file, including the JSONField for storing JSON data.
     
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA5.jpg" style="width: 300px; height:250px;">
     
5. Generate and apply migration
   - Generate the database migration file using the `python manage.py makemigration` on the Django web server.
   - Apply the migration to generate the necessary table in the database server using the command below.
   - `python manage.py migrate`

   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA6.jpg" style="width: 300px; height:250px;">
   
6. Load JSON data into the database
   - Create a script in the Django web server to fetch the JSON data from the JSON dataset server and save it into MongoDB Database server.
   - Utilize appropriate library to make connection and perform data loading process
     
7. Configure database connection
   - In the Django web server, find the django setting file named `settings.py`.
   - Set up the database connection for both MongoDB and MySQL database by providing the credentials such as hostname and password.
     
8. Testing and Monitor
   - Run the Django web server to verify the database connection.
   - Test the data retrieval and manipulation
   - Deploy the Django application.

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


