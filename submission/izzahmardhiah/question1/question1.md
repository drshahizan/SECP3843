<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nur Izzah Mardhiah binti Rashidi
#### Matric No.: A20EC0116
#### Dataset: [City Inspections Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/08-city_inspections)

## Question 1 (a)
For the platform I am proposing to build, it is feasible to use three servers to achieve our goals.
- Server 1: Web Server + Django Application Server
- Server 2: MySQL database
- Server 3: MongoDB Atlas or Compass

Firstly, we can combine the roles of the web server and Django application server into a single server, which is a common and efficient practice. This approach will enable us to handle incoming HTTP requests, serve the Django application, and manage the application logic seamlessly. By integrating the web server and Django framework on one server, we can ensure seamless integration and efficient data storage and retrieval. I suggest managing file storage within the existing servers without the need for an additional dedicated server. Django provides options for handling file uploads and storage directly within the application server. By configuring the Django application server to manage file storage, we can avoid the complexity and overhead of setting up a separate file server.

Secondly, I suggest dedicating a separate server for hosting the MySQL database. This dedicated server will securely store user login and registration credentials. By having a separate MySQL server, we can optimize it specifically for handling database operations efficiently. With proper configuration, indexing, and query optimization, we can ensure reliable and fast data storage and retrieval.

Thirdly, I propose leveraging cloud-based services such as MongoDB Atlas or Compass for storing the JSON dataset. These services provide highly scalable and managed databases, eliminating the need for separate server infrastructure. By utilizing a cloud-based solution, we can leverage the scalability and flexibility offered by the service provider, enabling efficient storage and retrieval of the JSON dataset. Configuring the appropriate connection settings will allow the Django application server to seamlessly communicate with the MongoDB Atlas or Compass service.

### Steps required to integrate Django with the JSON dataset, ensuring efficient data storage and retrieval from both MySQL and MongoDB databases:- 
1. Configure Django for MySQL and MongoDB

Edit the settings.py file in our Django project.Then, define the connection details for both the MySQL and MongoDB databases, including host, port, username, and password.

2. Define Django models

In the models.py file of our Django application, define models that represent the data structures in the JSON dataset. Create fields in the models that correspond to the JSON data, ensuring the appropriate data types are used.

3. Generate database tables

Run Django's migration commands to create the necessary tables in both the MySQL and MongoDB databases. This step will ensure that the database schemas align with the defined Django models.

4. Implement data storage and retrieval for MySQL


5. Implement data storage and retrieval for MongoDB


## Question 1 (b)
<img height="200px" src="materials/system_architecture.png" />





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


