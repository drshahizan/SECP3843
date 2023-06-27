<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Terence Loorthanathan
#### Matric No.: A20EC0165
#### Dataset: [tweets.json](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets)

## Question 1 (a)
According to the case study, I was given five servers to be used in this project. Below i have listed my recommendation of how each one of the 5 servers should be configured and set up.

<br>

### Server 1: Django Web Framework

* Django should be set up here for the web application framework. (Simulation will be shown below)
* In this server database connections for both MySQL and MongoDB will be configured.
* Note : This server is required

### Server 2: MySQL Database Server

* MySQL should be installed here as the database for storing data.
* A new database can be created in MySQL to hold the relevant tables for storing data other than the JSON dataset [tweets](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets).
* Data Domain for this Database could be : User Informations 🧑
  * Storing User's Password
  * Storing User's Username


### Server 3: MongoDB Database Server

* MongoDB should be installed here as another database for storing data.
* A new database can be created in MongoDB to hold the relevant collections for storing the JSON dataset [tweets](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets).



### Server 4: Deployment Server

* This server should be set up to host and deploy the Django web application.
* A web server can be set up to handle incoming requests and route them to the Django application.
* Configure the server to run Django using a WSGI server (uWSGI).

### Server 5: Front-end Server

* this server can be configured as a front-end server (e.g., using Nginx, Apache) to handle incoming requests.
* Routing rules can be set up here to direct requests related to the portal to the Deployment Server (Server 4).
<br><br>

### Steps to integrate Django with MySQL and MongoDB
Below i will explain how to integrate Django with both MySQL and MongoDB. Keep in mind, i will be simulating a multi-server environment on my local machine to futher explain integration between all the components.
<br><br>

#### Server 1: Django Web Framework Integration
How will we simulate a Django Web Framwork server? By installing Django on my local machine. Then, Configuring the app's Django settings to establish connections with both MySQL and MongoDB databases. This will be done in the **settings.py** file.

1) Step 1 : Install Django

You can do this simply by running this command in your terminal. I would recommend to create a new folder for your application, opening it in **Visual Studio Code** and then running it in its built in Terminal.

```python
pip install django
```

Since i installed Django previously, I dont have to install it again. To check if Django is installed, you can run the code below.

```python
django-admin --version
```

Code & Output:

<img  src="./files/images/1_server1_1.jpg"></img>

2) Step 2 : Create the App

You can do this simply by using the **startproject** command shown below. Then, you have to use the **startapp** command to create the app. Note : Move into the directory after creating the project to make sure manage.py is readable.

Code & Output:

<img  src="./files/images/1_server1_2.jpg"></img>

3) Step 3 : Configure SQL

Before configuring, might be a good idea to set up the server first. [Click here](#Server 2: MySQL Database Server)

To connect Django with MySQL, update the **DATABASES** dictionary with the necessary MySQL settings. My SQL Database dictionary is shown below

<img  src="./files/image/../images/1_server1_3_configuring_sql.jpg"></img>

<br>
Keep in mind, you need to install **mysqlclient** to connect with your mySQL database server.
<br>

<img  src="./files/image/../images/1_server1_3_configuring_sql2.jpg"></img>












## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


