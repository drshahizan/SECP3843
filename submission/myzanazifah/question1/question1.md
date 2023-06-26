<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Myza Nazifa Binti Nazry
#### Matric No.: A20EC0219
#### Dataset: Stories

## Question 1 (a)
As an IT consultant, I recommend implementing a set of servers for the project to ensure the development of an efficient portal. I propose utilizing a combination of four servers, including the following:
- First Server : Web Server and Django Application Server
- First Database Server : MySQL
- Second Database Server : MongoDB
- Reverse Proxy Server (that incorporates load balancing capabilities.)

Firstly, I would recommend integrating both web server and Django application server as one server. This method is a well-known method and is widely adopted and also an effective practice. The web server will handle the HTTP requests by receiving incoming HTTP requests, processing those requests and then deliver the corresponding web pages. On the other hand, the Django application server will be responsible for running the Django framework. Not only that but it will also manage the execution of Django applications, handle the URL routing and many more. By integrating the servers into one server, it will simplify the deployment process and also reduce the complexity of the server infrastructure. In addition, the team can achieve seamless integration while ensuring optimized data storage and retrieval. We can also eliminate using another server such as a file server by integrating these two servers as Django application server incorporates file handling capabilities within the application itself. So, Django application server can handle the storage and management of uploaded files.

For the database of the portal, I suggest using two database servers which are MySQL database and MongoDB database. This is because the portal requires storing not only the JSON data but also the user credentials such as username, email and password. The reason of using separate database to store JSON data and the user credentials is to achieve optimized performance. Both databases has its own data storage mechanisms and may be unsuitable for certain datas. Not only that but by separating the datas into different databases, it will also allow for better data organization. For the decision of which data should be stored in which database, it's important to consider the strengths of the databases. As MySQL is a relational database management while MongoDB is a NoSQL document database, I would suggest that the user credentials should be stored in the MySQL database as MySQL provides security features and is also commonly used for managing user credentials. On the other hand, the JSON data should be stored in MongoDB as MongoDB is a document-oriented database. MongoDB also has flexible schema and has high scalability. This makes it suitable for handling large volumes of JSON data and execute queries for dashboard visualizations.

Lastly, I would also recommend using reverse proxy server which incorporates load balancing capabilities as well. The reverse proxy server will act as an intermediary between the user and the backend servers. This includes receiving requests from users and forwarding the requests to the appropriate backend server. The load balancing functionality is useful for distributing incoming traffic across multiple backend servers. Hence, ensuring efficient resource utilization. This server is a strong option for portals and websites which receive many requests as this server will balance the load of many incoming requests and help reducing the bandwidth load.

### Steps to integrate Django with JSON dataset

1. Install and Set Up Django
   - Before installing Django, we need to install Python first by downloading the latest version of Python from the official website, https://www.python.org/downloads/windows/.
   - Once Python has been installed, create a virtual environment and activate it.

```python

python3 -m venv myenv

myenv\Scripts\activate

```
   - Next, we can install Django by running the following code:

```python

pip install django

```

   - Next, run the following code to verify installation
   
```python

python -m django --version

```
<br>

2. Create a Django project
   
   For this part, I would recommend using Visual Studio Code.

   - First, open new terminal in Visual Studio Code and use the following code to create a new Django project. In the code below, I named the project as AA but can be modified with other desired name.

```python

python -m django startproject AA

```
   - Next, run the code below to navigate to the project directory.
     
```python

cd AA

```
<br>

3. Create Django Apps
   - To create a new Django application, run the following code below. The AAapp is an example of the application name and can be modified to our own preference.
  
```python

python manage.py startapp AAapp

```
   -  After creating a new app, open the 'settings.py' file located in the AA project file and add the app to the 'INSTALLED_APPS' list. Below is an example of code:
          
```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AAapp',
]

```
<br>

4. Configure Database Settings
   - Go to the 'settings.py' file in the Django project and locate the code for databases.
   - Next, edit the code by defining the connection details for both MongoDB and MySQL databases such as username, password, host, port and engine.
<br>
5. Create Django Models
   - Go to the 'models.py' file and define the models which represents the data and match the structure of the JSON dataset.
   - After defining the models, run the following code to run migrations to create database tables.

```python

python manage.py makemigrations
python manage.py migrate

```
<br>

6. Load JSON data into MongoDB
   - Start the MongoDB server and ensure it is running.
   - Create a new database in MongoDB if it doesn't exist and load the JSON data.


   

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


