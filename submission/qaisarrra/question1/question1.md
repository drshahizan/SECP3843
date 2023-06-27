<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Qaisara binti Rohzan
#### Matric No.: A20EC0133
#### Dataset: 04 - Companies

## Question 1 (a)
The answer to the question is divided into the following segments:
* [Requirements](#-requirements)
* [Integrating Django with JSON dataset](#️-integrating-django-with-json-dataset)

## Requirements

As an IT consultant, it is crucial for me to actively participate in overviewing the critical stages and concerns involved in developing a portal that seamlessly integrates various hardware and software applications. Implementing an amount of **5 servers** in this project is possible, whereby the servers are used as:

1. **Main Web Server**: Apache (Used by Django Web Framework)
2. **Database Server 1**: MySQL
3. **Database Server 2**: MongoDB
4. **Additional Application Server**:  Power BI Report Server
5. **Backup Server**

While implementing **5 servers** can be highly irresistible, there are several factors and questions that I must ask myself before deciding the final requirements needed to carry out this project:

* **Scalability**: Will the project's traffic or data volume significantly increase in the future? If the project has the potential for expansion, having numerous servers can provide scalability and properly share the workload.
> Answer: No, the project’s data volume will remain constant over the future. This is because the given project is based on a single dataset that contains 9,500 records of companies listed on Crunchbase. Having numerous servers will only lead to **wasting resources**. Unused servers consume hardware resources such as CPU, memory, storage, and electricity. This might result in inefficient resource utilisation and excessive maintenance and infrastructure costs.

* **Performance**: Consider the project's estimated load and performance requirements. Having numerous servers can aid in load distribution, assuring optimal performance and responsiveness. It enables the use of dedicated resources for specific activities like web hosting, database management, and redundancy.
> Answer: The database management activities can be considered as minimal as the project only revolves around the existing dataset. Moreover, this project would not require an on-premises Power BI Report Server that generates daily reports. Therefore, excess servers such as the Power BI Report and Backup Server may not be used properly, resulting in **inefficient resource allocation**. Valuable resources may have been diverted to other vital components or used to expand the existing infrastructure where it is most needed.

* **Cost and Resources**: Examine the project's budget and resources. Additional servers result in greater hardware, software licence, and maintenance costs. Determine whether the benefits of having many servers exceed the costs.
> Answer: Since the project can be considered as a low-scaled project, whereby all the software applications can be installed locally into our devices and are open-sourced (does not require any software licence). Additional servers can also lead to the **increase of maintenance and support requirements**. Excess servers necessitate additional maintenance, updates, troubleshootings, administrative and support tasks, which might distract resources and attention away from other project objectives.
  
* **Complexity and Management**: Consider the difficulty of managing and maintaining several servers. More servers necessitate more effort for configuration, monitoring, and troubleshooting. Determine whether the project team has the competence and resources to efficiently manage several servers.
> Answer: The project team does not have the competence and resources to efficiently manage several servers due to the lack of experience. The project's aim to seamlessly integrate the Django web framework, the JSON dataset, the MySQL and MongoDB database is straight-forward. Implementing additional and unnecessary servers will only **increase the project's complexity**. Managing and maintaining additional servers that are not actively used might add to the infrastructure's complexity. This complexity can lead to increased maintenance costs and possible sites of failure.

To mitigate these effects, it is best to re-evaluate the server architecture and make modifications based on project's portal real usage and requirements. After careful considerations, implementing the **3 Server Approach** for this project appears to be a viable option, with each server performing a specific purpose. This architecture promotes optimal task distribution and maintains a manageable infrastructure while ensuring seamless integration, efficient data storage, and retrieval.

<table>
  <tr>
    <th>No</th>
    <th>Server Purpose</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Main Web Server: Apache (Used by Django Web Framework)</td>
    <td>
      <ul>
        The main web server, which is powered by Apache, is critical in managing incoming HTTP requests and serving the Django web application. Apache, a popular web server, provides reliable performance and strong interoperability with the Django framework. The main web server efficiently handles web traffic by exploiting Apache's capabilities, providing the flawless delivery of dynamic web pages to consumers. It serves as the point of contact for user interactions, sending requests to the necessary components for processing and answer generation.
      </ul>  
     </td>
  </tr>
  <tr>
    <td>2</td>
    <td>Database Server 1: MySQL</td>
    <td>
      <ul>
        This server is dedicated to hosting the MySQL database and allows for the efficient storage and retrieval of structured data. MySQL, a dependable relational database management system, works effortlessly with Django, enabling for the effective storing and management of project-related data. MySQL assures the integrity and reliability of the stored data due to its proven track record and substantial community support. This server enables the project to reap the benefits of a relational database, guaranteeing effective data storage and retrieval for diverse application capabilities.
      </ul>  
     </td>
  </tr>
  <tr>
    <td>3</td>
    <td>Database Server 2: MongoDB</td>
    <td>
      <ul>
        The MongoDB database is hosted on the second database dedicated server. MongoDB, a versatile NoSQL database, excels at managing unstructured or semi-structured data like the JSON information provided. MongoDB is an excellent solution for applications demanding scalability and flexibility due to its ability to extend horizontally and accommodate massive amounts of data. The integration of MongoDB and Django allows for the effective storage and retrieval of JSON data within the project's portal. The query capabilities of MongoDB, as well as its document-oriented approach, allow for the effective management of various and growing data structures.
      </ul>  
     </td>
  </tr>
</table>


## Integrating Django with JSON dataset
This segment of Question 1. (a) is divided into several parts:
* [Prerequisites](#-prerequisites)
* [Setting Up A Django Project](#️-setting-up-a-django-project)

### Prerequisites
To carry out this segment of the question, it it crucial for to do the following:
1. Install [Python](https://www.python.org/downloads/)
2. Install [Visual Studio Code](https://code.visualstudio.com/download)
<br></br>

### Setting Up A Django Project

**Django Installation** 

1. Create a Django Project Folder. For this project I created a folder named **AA** on my **Desktop**, where it is easily accessible.
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question1/files/images/Create%20Project%20Folder.png">
</p>
     
<br>

2. Set up a virtual environment. In your current working directory, this command creates a new virtual environment called ``environment``. 
```bash
python -m venv environment
```
<br>

3. Activate the virtual environment. When the process is finished, you must additionally activate the virtual environment.
```bash
environment\Scripts\activate
```
<br>
   
4. Install Django.
```bash
pip install django
```
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question1/files/images/Django%20Installation.png">
</p>
<br>

5. Install necessary packages. Here we are installing  packages that allows integration between our Django App and MongoDB, those packages are **MySQL Client PyMongo** and **Djongo**. Djongo is a smarter approach to database querying. It maps python objects to MongoDB documents. 
```bash
pip install django mysqlclient pymongo
pip install djongo
```
Below are the output when running the commands:
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question1/files/images/Install%20Django%20MySQLClient%20PyMongo.png">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question1/files/images/Install%20Djongo.png">
</p>
<br></br>

**Create A Django Project** 

You can now create a project after setting up, activating your virtual environment and installing Django. To start a new Django project, open a new terminal in Visual Studio Code and run the following command. The project is named **Companies** in the code below, but it can be changed to any name you like.
```bash
python -m django startproject Companies
```
Navigate yourself to the project directory by inputing the command below:
```bash
cd Companies
```
<br></br>

**Create A Django Application** 

The  ``startapp `` command generates a default folder structure for a Django app. This tutorial uses **CompaniesApp** as the name for the app:
```bash
python manage.py startapp CompaniesApp
```
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question1/files/images/Create%20Django%20Project.png">
</p>
<br></br>

**Configure Database Connection** 

Set up the MySQL and MongoDB connections. Alter the code for the databases in the Django project's'settings.py' file as shown below.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_companies',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'AA',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'username': 'qaisara',
            'password': '8301',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}
```
<br></br>

**Create MySQL and MongoDB Models** 

In the **models.py** file, define the models that represent the data and correspond to the structure of the JSON dataset.
1. Defining  models for MySQL
```bash
from django.db import models

class Company(models.Model):
    _id = models.CharField(max_length=255, primary_key=True)
    acquisition = models.JSONField(null=True)
    acquisitions = models.JSONField(null=True)
    alias_list = models.JSONField(null=True)
    blog_feed_url = models.URLField(null=True)
    blog_url = models.URLField(null=True)
    category_code = models.CharField(max_length=255, null=True)
    competitions = models.JSONField(null=True)
    created_at = models.DateTimeField(null=True)
    crunchbase_url = models.URLField(null=True)
    deadpooled_day = models.IntegerField(null=True)
    deadpooled_month = models.IntegerField(null=True)
    deadpooled_url = models.URLField(null=True)
    deadpooled_year = models.IntegerField(null=True)
    description = models.TextField(null=True)
    email_address = models.EmailField(null=True)
    external_links = models.JSONField(null=True)
    founded_day = models.IntegerField(null=True)
    founded_month = models.IntegerField(null=True)
    founded_year = models.IntegerField(null=True)
    funding_rounds = models.JSONField(null=True)
    homepage_url = models.URLField(null=True)
    image = models.JSONField(null=True)
    investments = models.JSONField(null=True)
    ipo = models.JSONField(null=True)
    milestones = models.JSONField(null=True)
    name = models.CharField(max_length=255)
    number_of_employees = models.IntegerField(null=True)
    offices = models.JSONField(null=True)
    overview = models.TextField(null=True)
    partners = models.JSONField(null=True)
    permalink = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True)
    products = models.JSONField(null=True)
    providerships = models.JSONField(null=True)
    relationships = models.JSONField(null=True)
    screenshots = models.JSONField(null=True)
    tag_list = models.JSONField(null=True)
    total_money_raised = models.CharField(max_length=255, null=True)
    twitter_username = models.CharField(max_length=255, null=True)
    updated_at = models.DateTimeField(null=True)
    video_embeds = models.JSONField(null=True)

    def __str__(self):
        return self.name

class Users(models.Model):
    _id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
```

2. Defining  models for MongoDB
```bash
from djongo import models

class Company(models.Model):
    _id = models.CharField(max_length=255, primary_key=True)
    acquisition = models.JSONField(null=True)
    acquisitions = models.JSONField(null=True)
    alias_list = models.JSONField(null=True)
    blog_feed_url = models.URLField(null=True)
    blog_url = models.URLField(null=True)
    category_code = models.CharField(max_length=255, null=True)
    competitions = models.JSONField(null=True)
    created_at = models.DateTimeField(null=True)
    crunchbase_url = models.URLField(null=True)
    deadpooled_day = models.IntegerField(null=True)
    deadpooled_month = models.IntegerField(null=True)
    deadpooled_url = models.URLField(null=True)
    deadpooled_year = models.IntegerField(null=True)
    description = models.TextField(null=True)
    email_address = models.EmailField(null=True)
    external_links = models.JSONField(null=True)
    founded_day = models.IntegerField(null=True)
    founded_month = models.IntegerField(null=True)
    founded_year = models.IntegerField(null=True)
    funding_rounds = models.JSONField(null=True)
    homepage_url = models.URLField(null=True)
    image = models.JSONField(null=True)
    investments = models.JSONField(null=True)
    ipo = models.JSONField(null=True)
    milestones = models.JSONField(null=True)
    name = models.CharField(max_length=255)
    number_of_employees = models.IntegerField(null=True)
    offices = models.JSONField(null=True)
    overview = models.TextField(null=True)
    partners = models.JSONField(null=True)
    permalink = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True)
    products = models.JSONField(null=True)
    providerships = models.JSONField(null=True)
    relationships = models.JSONField(null=True)
    screenshots = models.JSONField(null=True)
    tag_list = models.JSONField(null=True)
    total_money_raised = models.CharField(max_length=255, null=True)
    twitter_username = models.CharField(max_length=255, null=True)
    updated_at = models.DateTimeField(null=True)
    video_embeds = models.JSONField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
```
<br></br>

**Perform Database Migration** 
```bash
 python manage.py makemigrations
 python manage.py migrate
```
<br></br>

## Question 1 (b)
The system architecture will consist of the following components:





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


