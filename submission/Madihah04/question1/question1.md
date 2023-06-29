<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Madihah binti Che Zabri
#### Matric No.: A20EC0074
#### Dataset: <a href="https://github.com/drshahizan/dataset/blob/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/07-stories/stories.json">stories.json</a>

## Question 1 (a)

As an IT consultant, I will provide instructions to the technical staff on implementing a configuration using these servers:
1. Apache: We will use Apache HTTP Server as the web server to host the Django application and serve web pages.
2. MySQL: We will use MySQL  as a relational database management system (RDBMS) to store and manage structured data.
3. MongoDB Compass: We will use MongoDB Compass as a NoSQL database. 
4. MongoDB Atlas: We will use MongoDB Atlas, which is a cloud-based service for MongoDB. It is included in our project as we can connect it with MongoDB Compass but on the cloud, therefore it is more flexible and the data is saved if anything happen.
5. Google Colab (that we will used in Question 4)
   
Steps:

1. Install XAMPP: Download and install XAMPP, which includes Apache, MySQL, and PHP. XAMPP provides an easy-to-install package that sets up a local development environment on your machine.

2. Start Apache and MySQL: Once XAMPP is installed, start the Apache and MySQL services. Apache will serve your Django application, while MySQL will be used as one of the databases.

3. Install MongoDB and MongoDB Compass: MongoDB is a NoSQL database that will be used alongside MySQL. Install MongoDB locally on your machine or use MongoDB Atlas, a cloud-based MongoDB service. Additionally, install MongoDB Compass, a graphical interface for managing MongoDB databases.

4. Install Django: Use pip to install Django on your machine. Open a command prompt and run the following command:
   ```pip install Django```

5. Create a new Django project: In your desired directory, create a new Django project using the following command:
   ```django-admin startproject portal```
   
6. Set up Django app: Change into the project directory by running:
   ```cd portal```

7. Then, create a new Django app that will handle the functionality related to the portal:
   ```python manage.py startapp dashboard```
   
8. Define models: In the models.py file within the "dashboard" app, define the data models that correspond to the JSON dataset. Map the JSON data structure to Django models, including the necessary fields, relationships, and data types.

9. Configure database settings: Open the settings.py file in the project directory and configure the database settings. Specify the MySQL database connection details, such as the host, port, database name, username, and password. Additionally, provide the connection details for MongoDB Atlas or your local MongoDB instance.

10. Create database tables: Django provides a command to create the necessary database tables based on the defined models. Run the following command to create the tables in the MySQL database:
    ```python manage.py migrate```
For MongoDB, the tables (or collections) will be created automatically when data is saved. Load JSON data: Write a script to read the JSON dataset and populate the corresponding Django models. You can create a management command in Django to automate this process. The script should parse the JSON file, create instances of the Django models, and save them to the appropriate databases (MySQL and MongoDB).

12. Define views and templates: In the views.py file of the "dashboard" app, define the necessary views to handle data retrieval and presentation. Each view should query the data from the respective databases (MySQL and MongoDB), process it if needed, and pass it to the templates for rendering.

12. Create templates: Design HTML templates that define the structure and layout of the web pages. Use Django's template language to incorporate dynamic data into the templates. Templates can access data retrieved from both the MySQL and MongoDB databases.

13. Implement data retrieval: In the views, query the MySQL and MongoDB databases to retrieve the required data based on user requests. Use Django's ORM (Object-Relational Mapping) to construct queries and retrieve data from the models.

14. Implement data storage: When data needs to be stored or updated, use the appropriate Django models and ORM to save the data to the respective databases (MySQL and MongoDB).

15. Enable JSON data handling: Django provides built-in support for JSON data handling. 

## Question 1 (b)

                                                         +------------------------+
                                                         |  Client (Web Browser)  |
                                                         +------------------------+
                                                                     |
                                                                     |
                                                                     v
                                                    +-----------------------------------+
                                                    |         Web Server Layer          |
                                                    +-----------------------------------+
                                                    |   Django Web Server (Django App)  |
                                                    |   +---------------------------+   |
                                                    |   |       Django Views        |   |
                                                    |   +---------------------------+   |
                                                    |   |       Django Models       |   |
                                                    |   +---------------------------+   |
                                                    +-----------------------------------+
                                                                     |
                                                                     |
                                                                     v
                                         +-----------------------+----------------------------+
                                         |                Data Storage Layer                  |
                                         +-----------------------+----------------------------+
                                         |        MySQL Database (Relational Database)        |
                                         |            +-------------------------+             |
                                         |            |   Django ORM (Object- |               |
                                         |            |   Relational Mapping)  |              |
                                         |            +-------------------------+             |
                                         |                                                    |
                                         |        MongoDB Database (NoSQL Document DB)        |
                                         |            +-------------------------+             |
                                         |            |    MongoDB Connector    |             |
                                         |            |                         |             |
                                         |            +-------------------------+             |
                                         +-----------------------+----------------------------+
                                                                     |
                                                                     |
                                                                     v
                                                          Integration Components
                                                                     |
                                                                     |
                                                                     v
                                                          +------------------+
                                                          |   stories.json   |
                                                          +------------------+





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


