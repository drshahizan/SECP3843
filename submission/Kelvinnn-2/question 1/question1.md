<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kelvin Ee
#### Matric No.: A20EC0195
#### Dataset: City Inspection

## Question 1 (a)

### Solutions on implementing a configuration using five servers used in this project:

#### a) Web Server: This server will handle incoming HTTP requests and serve the Django web application. It will run the web server software (such as Apache or Nginx) and the necessary components for Django to operate.
#### b) Database Server 1 (MySQL): This server will host the MySQL database. It will handle storing and retrieving data from the MySQL database management system. Django will connect to this server to interact with the MySQL database.
#### c) Database Server 2 (MongoDB): This server will host the MongoDB database. It will handle storing and retrieving data from the MongoDB NoSQL database. Django will connect to this server to interact with the MongoDB database.
#### d) Load Balancer: If the web server has high traffic expect or want to distribute the load across multiple web servers, implement a load balancer to receive incoming requests and distribute them among the available web servers to ensure efficient handling of traffic.
#### e) Caching Server:  Introduce a caching server to improve performance and reduce database load. This server will store frequently accessed data in memory, allowing faster retrieval. For example, Redis or Memcached are popular choices for caching servers.

To integrate Django with the JSON dataset and ensure efficient data storage and retrieval from both MySQL and MongoDB databases, you can follow these comprehensive steps:

#### Django Installation: 
1. Begin by installing Django on all five servers. use the pip package manager to install Django by running the following command:
```pip install Django```

2. Set up Django project: Create a Django project on one of the servers. Use the following command to create a new Django project:
```django-admin startproject city_inspections```

3. Create Django app: Inside the Django project, create a new app that will handle the integration with the JSON dataset and databases. Use the following command to create a new app:
```python manage.py startapp city_inspections```

4. Install necessary packages by using the following command :
```pip install django mysqlclient pymongo``` and ```pip install djongo```

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


