<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nayli Nabihah Binti Jasni
#### Matric No.: A20EC0105
#### Dataset: Companies

## Question 1 (a)
This portal is going to implement the usage of Django, JSON, MySQL and MongoDB. To built the best portal in terms of seamless integration between these four things in five servers at most, there are many ways to do so. These are the ways that I choose to use as an IT consultant in this case.

First, since using Django web framework, we should install Django framework in all 5 servers to ensure that everything is uniformed and can work properly. 'pip' can be used to install Django project in the servers as it act as a package installer for Python specifically. All servers should have the same version of Django and make sure that the version is stable and compatible with the devices and operating system. The five servers are Web Server/Hosting for the portal after publishing it live, application server is used when doing the project locally, and two database server, one for each MySQL and MongoDB.

After installing it, build a Django project in one of four the servers that we had using the terminal (command prompt). Build the project in application server as it will act as a main server for this project

```python
!pip install django
```

```python
!django-admin startproject portal
```

After installing Django and building Django project in the application server, the settings of the Django project should be configured as it is where the database configurations is placed. When creating a Django Project, there is a file named as 'settings.py' where stores all the information on the database, in this case both databases that we used which are MySQL and MongoDB. In this file, the configurations of the databases including the database engine, database name, username, host, password and port. The configuration of MySQL and MongoDB might not be in the same exact look but they are similar too each other.For the JSON file provided, we need to make a Django model for the dataset in the JSON file. This model will be created in the application server just as the Django project is. All the columns in the JSON file should be declared as its own attribute in the table.

When the model is created, migration should be done in the Django project so that it can create compulsory tables in the database. These are the commands that should be used to perform the migration:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```

After tables were created in the database, now the JSON file can be inserted or loaded into the databases. This can be done by writing a Django command in the application server for reading and storing the JSON dataset in the created model. As the JSON file has already been stored in the model in  Django project, this is when the process of obtaining the data (in this case the JSON file imported) from the database into the Django project. Write Django views to get the data from the 2 database servers that stores the MySQL database and MongoDB database,  and the data should be obtained in JSON format. These are the steps that should be taken in all the other servers as every server should be set up the same way as the first server (application server) to avoid any issues since using more than one server. 

All the servers should be separated with different tasks and workload since it holds their significant use that are unique from each other. Application server will be used as the placed where the main project is done and data processing, Web server can be used as the platform for authentication for all users, the 2 Database servers (one for MySQL and the other one is for MongoDB) will be used to manage the data retrieval and storage purposes. 

## Question 1 (b)

![arch](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%201/files/images/archi.png)


#### User Interface

In Django, HTML templates and CSS stylesheets are used to create the user interface (UI). Templates enable the dynamic production of HTML pages by fusing Django template tags with HTML markup. Static files manage styling and interactivity, such as CSS and JavaScript. The logic to render templates and process data is contained in views. HTML form processing and form development are made easier by forms. By using template inheritance, a base template with elements used on multiple pages can be made. Static files are referred to in the template tag. In order to create a dynamic and interactive user interface, Django's UI development process entails structuring templates, creating static files, writing views for data processing, and using forms for form handling.


#### Web Server

This is where the deployment of the Django project built in Application Server were taken placed at. This server is used as a medium to deploy the portal to the user live on the internet. Thie web server will control the users requests and dispatch them to the responsible web pages responsively according to the requests.

#### Load Balancing Server

This server will be the one that controls the user traffic in the portal. As most of the time many other websites have problem which makes it crashed when too many users try to access the website. To prevent from this to happened, the usage of this server can be helpful.


#### Application Server

For this project, since application server is for the main place where the development is done, this server will be in the devices' localhost. This means that the Django Project is hosted in the devices' locally so that it will be easier to monitor the development of the portal especially when the development process is done by many individual. After all the functionalities and pages in the portal were finalized, only then will the portal be published live at the web server.  

#### Database Servers (MySQL and MongoDB)

The are 2 servers in the database servers, one for MySQL and the other one is for MongoDB. The reason why these databases are separated because they are not the same type as MongoDB is a NoSQL database management system while MySQL used SQL. This means that the command for each database is different from each other. So it will be easier and can prevent unreliable data and helps to increase the efficiency of the data retrieval. 

The storage item of these two databases is also different as it is better to put the JSON file into the MongoDB and use the MySQL database for other purposes. Data management for the portal is handled by the MySQL database server, which also communicates with the Django web framework for data operations.




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


