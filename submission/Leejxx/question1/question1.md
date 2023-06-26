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
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales" >Supply Store Dataset</a>

## Question 1 (a)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Question 1 (b)
<img  src="./files/images/System Architecture(AA).JPG"></img>

- ###  User
  - The User component represents the end-user or client who interacts with the web application.
  - Users access the application through a web browser and initiate requests by interacting with the user interface.

- ### Web Server
  - The Web Server component receives HTTP requests from users and forwards them to the appropriate URL within the Django application.
  - It handles the communication between the user's web browser and the application.
 
- ### Django Web Application
   In this project, Django will be as the framework for the web application.Django is a high-level web framework written in Python that follows 
   <b>MVT</b> architectural pattern, although it refers to the components as Models, Views, and Templates. It provides a comprehensive set of tools and libraries for building web applications efficiently and securely.
  - Model :
    - The Model component in Django defines the data structure and provides an interface to interact with the database.
    - It represents the logical structure of the data and includes fields and relationships between different entities.
    - In this case, the Model interacts with the MongoDB database to store and retrieve data represented in JSON format and also intracts with MySQL to manage the user registration and login.
  - Views :
    - The Views component contains the business logic of the application.
    - It processes the HTTP requests received from the Web Server, interacts with the Models and Databases, and prepares the appropriate response.
    - Views can perform actions such as retrieving data from the Models, modifying data, and rendering templates for the user interface.
  - Template
    - The Template component is responsible for rendering the user interface and generating dynamic web pages.
    - It defines the HTML structure and includes placeholders for dynamic content to be populated by Views.
    - Templates are rendered by Views and combined with data to produce the final output that is sent back to the user's browser.

- ### Database
  - MongoDB:
    - MongoDB is a NoSQL document database.
    - In this architecture, MongoDB is used as the database for storing data represented in JSON format.
    - The Model component interacts with the MongoDB database to perform CRUD operations (Create, Read, Update, Delete).
  - MySQL:
    - MySQL is a relational database management system.
    - The MySQL database is used specifically for user authentication in this architecture.
    - It stores user-related information, such as usernames, passwords, and other authentication details.
    - The user authentication functionality is handled separately from the main data storage in MongoDB.
- ### JSON Dataset (Supply Store Dataset)
   - The JSON dataset contains information about sales transactions, including items purchased, customer details, store location, coupon usage, and purchase method.
   - The dataset serves as the source of data for the portal's visualization and analysis features.
 
- ### Libraries user
   - Object-Relational Mapping (ORM):
       - Django's ORM is primarily designed to work with relational databases such as MySQL, PostgreSQL, and SQLite.
       - In this case, we use Django's ORM to interact with the MySQL database for user authentication.
       - Django's ORM provides an object-oriented interface to define models, query the database, and perform CRUD operations.
   - Djongo:
       - Djongo is a package that allows Django to integrate with MongoDB, a NoSQL database.
       - In this case, we use Djongo to interact with MongoDB for storing and retrieving JSON data.
       - Djongo translates Django's ORM queries and operations into MongoDB-specific queries, allowing us to utilize Django's ORM syntax and features with MongoDB.
     
  

    
 





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


