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
       - Using the command
         ```python
         
         pip install pymongo
         
         ```
         
         <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA3.jpg" style="width: 700px; height: 100px;">
         
     - MySQL Database Server
       - Using the command
         ```python
         pip install mysqlclient
         ```
         
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
   - ```python
     django-admin startproject Store
     ```
     
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA4.jpg" style="width: 600px; height: 60px;">
     
   - Create django app within the project with the command
   - ```python
     python manage.py startapp AA
     ```
  
4. Define data models
   - Define models representing the JSON dataset and its fields in the Django app's `models.py` file, including the JSONField for storing JSON data.
     
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA5.jpg" style="width: 300px; height: 250px;">
     
5. Generate and apply migration
   - Generate the database migration file using the `python manage.py makemigration` on the Django web server.
   - Apply the migration to generate the necessary table in the database server using the command below.
   - `python manage.py migrate`

      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA6.jpg" style="width: 700px; height: 100px;">
   
6. Load JSON data into the database
   - Create a script in the Django web server to fetch the JSON data from the JSON dataset server and save it into MongoDB Database server.
   - Utilize appropriate library to make connection and perform data loading process
     
7. Configure database connection
   - In the Django web server, find the django setting file named `settings.py`.
   - Set up the database connection for both MongoDB and MySQL database by providing the credentials such as hostname and password.
   - For example, I have set up the connections for both MySQL and MongoDB 

      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/AA7.jpg" style="width: 650px; height: 300px;">
     
8. Testing and Monitor
   - Run the Django web server to verify the database connection.
   - Test the data retrieval and manipulation
   - Deploy the Django application.

## Question 1 (b)
### System Architecture
 - The system architecture diagram illustrates the seamless integration between Django, a web server framework, a JSON dataset, MySQL, and MongoDB databases.

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question1/files/images/SA.jpg" >

### Architecture Components
1. User interface
   - A user interface (UI) refers to the means by which a user interacts with a computer system, software application, or electronic device.
   - It encompasses all the elements and components that enable users to input commands, navigate through functionalities, and receive feedback from the system.
   - The purpose of a user interface is to facilitate effective communication and interaction between the user and the system.
   
3. Django Web Server
   - Handles HTTP requests, processes them, and generates dynamic web pages.
   - Utilizes Django's URL routing, request handling, session management, and template rendering capabilities.
   
4. Database Server
   - MySQL Database:
      - Stores and manages structured data, such as customer information.
      - Utilizes SQL queries for data retrieval and manipulation.
   - MongoDB Database:
      - Stores and manages the JSON dataset, which may have varying structures and nested data.
      - Follows a document-oriented model and uses MongoDB queries for data retrieval and manipulation.

5. Json Dataset
   - Contains structured data in JSON format, such as sales information, customer details, and product data.
     
6. Django App
   - Represents the Django application that integrates the JSON dataset, MySQL, and MongoDB.
   - Defines models to represent the JSON dataset and interact with the databases.
   - Utilizes Django's ORM for database operations and data retrieval.

7. Applications Layer
   - Views: Handles user requests, retrieves data from the databases, and passes it to the templates.
   - Templates: Render dynamically generated web pages using retrieved data.
     
8. Visualization
   - The Visualization Tool interacts with the MySQL and MongoDB databases to retrieve the required data for visualization purposes.
   - It executes queries against the databases to extract the relevant data and generates visual representations such as charts, graphs, or reports.
   - The resulting visualizations are then presented to the users through the web server, enabling them to gain insights and analyze the data.

At the center of the diagram is the Django web server, responsible for handling HTTP requests, processing, and generating dynamic web pages. The JSON dataset, represented by the Sales.json file, contains structured data such as sales information, customer details, and product data. To store and manage structured data, the architecture includes a MySQL database. MySQL follows a relational model and utilizes SQL queries for data retrieval and manipulation. On the other hand, the MongoDB database is used to store and manage the JSON dataset. MongoDB follows a document-oriented model and supports MongoDB queries for data operations.

The Django application, represented in the diagram as the Django App, acts as the bridge between the web server, the JSON dataset, and the databases. It defines models that represent the JSON dataset and facilitate interaction with the MySQL and MongoDB databases. Views and templates in Django handle user requests, retrieve data from the databases, and render dynamically generated web pages. Finally, visualization tools are used to produce insight and results 

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


