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
Integrating the Django framework, JSON data, MySQL, and MongoDB can be achieved without explicitly using five servers. One way to do this is by running Django on a web server and using separate servers for MySQL and MongoDB databases. This method simplifies the integration and makes the system more efficient.

However, configuring five servers can improve performance and increase scalability. The five servers will serve the following functions:

1. Web Server: A web server such as Apache will host your Django application, handle HTTP requests, and create dynamic web pages.
2. MySQL Server: MySQL RDBMS that can handle structured data storage.
3. MongoDB Server: NoSQL database that can store and retrieves data using JSON-like documents.
4. Load Balancer Server: Distributes incoming traffic across multiple web servers.
5. Backup Server: Store backups of the application's data securely.

Considering the sales dataset size, we may only require some of the five servers when setting up a production environment. A load balancer server may not be necessary since we do not anticipate a lot of traffic.

### Steps required to integrate Django with the JSON dataset, MySQL, and MongoDB:

Step 1: Install Django and Required Packages

- Create a new directory called project, and navigate into it.
``` ruby
$ cd ~/desktop/
$ mkdir project
$ cd ~/desktop/project
```

- Create and activate a new virtual environment called .venv in the directory.
``` ruby
$ python3 -m venv .venv
$ source .venv/bin/activate
```
- To deactivate and leave a virtual environment, type deactivate.

- Install Django.
``` ruby
(.venv) $ python3 -m pip install django
```
- To ensure Django works correctly, create a new project called django_project and then type python manage.py runserver to start the local Django web server.
``` ruby
(.venv) $ django-admin startproject django_project .
(.venv) $ python manage.py runserver
```
In your web browser, navigate to http://127.0.0.1:8000/ and you should see the Django Welcome Page.

## Question 1 (b)
<img width="942" alt="Screenshot 2023-06-27 at 3 58 26 AM" src="https://github.com/yanakunn/SECP3843/assets/76076543/e8bbc259-afa4-42f6-af9e-8e57f4f27dde">

In this system architecture:
- Clients access the portal via web browsers. 
- The web server receives and handles HTTP requests, then passes them to the application server. 
- The Django web framework runs on the application server and communicates with the MySQL and MongoDB databases using its built-in Object-Relational Mapping system. Django models are used to define the structure and behaviors of corresponding database tables, which are Python classes. The Django ORM handles the translation between Python objects and database rows, allowing object-oriented syntax to be used for database operations. 
- A data loading script loads JSON data into the databases. 
- Visualization tools are utilized to create dashboard visualizations based on the retrieved data. The frontend integration then integrates these visualizations into the Django templates. 
- Users can interact with the dashboard, apply filters, and customize the displayed data.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


