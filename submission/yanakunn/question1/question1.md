<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURARISSA DAYANA BINTI MOHD SUKRI
#### Matric No.: A20EC0120
#### Dataset: SALES

## Question 1 (a)
Integrating the Django framework, JSON data, MySQL, and MongoDB can be achieved by running Django on a web server and using separate servers for MySQL and MongoDB databases. Depending on the project's specific needs, it may require additional servers for specialized purposes such as load balancing, caching, or scaling. The five servers in this project have the following functions:

1. Web Server: A web server such as Apache will host your Django application, handle HTTP requests, and create dynamic web pages.
2. MySQL Server: MySQL RDBMS that can handle structured data storage.
3. MongoDB Server: NoSQL database that can store and retrieves data using JSON-like documents.
4. Django Application Server: This server will run the Django application and connect to MySQL and MongoDB. It will process requests and generate responses.
5. Development/Testing Server: A separate server for development or testing.

### Steps required to integrate Django with the JSON dataset, MySQL, and MongoDB:

Step 1: Install Django and setup Django project

1. Create and activate a new virtual environment called .venv in the project directory.
``` ruby
$ python3 -m venv .venv
$ source .venv/bin/activate
```
2. Install Django, then create a new project called project and start the local Django web server.
``` ruby
(.venv) $ python3 -m pip install django
(.venv) $ django-admin startproject project .
(.venv) $ python manage.py runserver
```
In your web browser, navigate to http://127.0.0.1:8000/ and see the Django Welcome Page.

3. Configure the project settings to connect to the MySQL and MongoDB databases. Modify your Django project directory's `settings.py` file and provide the necessary database connection details for MySQL and MongoDB.

Step 2:


## Question 1 (b)
<img width="1000" alt="Screenshot 2023-06-28 at 12 11 32 PM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/de697f28-c2e8-4809-95d7-c4be00f5f974">

The system architecture seamlessly integrates Django with MySQL and MongoDB databases to create a dashboard visualization and data viewing platform. It consists of several tiers and components:

<table>
  <tr>
    <th>Tiers</th>
    <th>Components Description</th>
  </tr>
  <tr>
    <td>Client Tier</td>
    <td>Web Browser</td>
  </tr>
  <tr>
    <td>Web Server Tier</td>
    <td>Hosts the Django application and handles incoming client HTTP requests.</td>
  </tr>
  <tr>
    <td>Application Tier</td>
    <td>
      <ol>
        <li>Django Web Framework: Main framework for handling business logic, requests, and responses.</li>
        <li>MySQL Database: Hosts the relational database for storing data of users to the Django application.</li>
        <li>MongoDB Database: Stores the JSON sales data.</li>
        <li>JSON Data: Sales dataset in JSON file.</li>
        <li>Data Preparation: Prepare the JSON data to follow the MongoDB documents structure.</li>
      </ol>
    </td>
  </tr>
  <tr>
    <td>Dashboard Tier</td>
    <td>
      <ol>
        <li>
          Dashboard: Visual representations of the data into the application's front end.
        </li>
        <li>
          User Interaction: Enables users to interact with the dashboard.
        </li>
    </td>
  </tr>
</table>

In this system architecture:
- Clients send HTTP requests to the web server.
- The web server uses a Web Server Gateway Interface to communicate with the application server.
- The application server receives requests and forwards them to the Django web framework.
- Python code to prepare and load JSON data into the databases. 
- The Django web framework runs on the application server and communicates with the MySQL and MongoDB databases using its built-in Object-Relational Mapping system. Django models are used to define the structure and behaviors of corresponding database tables, which are Python classes. The Django ORM handles the translation between Python objects and database rows, allowing object-oriented syntax to be used for database operations.
- Visualization tools are utilized to create dashboard visualizations based on the retrieved data. The frontend integration then integrates these visualizations into the Django templates. 
- Users can interact with the dashboard that allows them to filter and select data.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


