<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Sakinah Al'izzah Binti Mohd Asri
#### Matric No.: A20EC0142
#### Dataset: [Analytics](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 1 (a)
As an IT consultant, I was responsible for guiding the technical team on how to implement a configuration that involves five servers for our latest project. For this endeavor, my team had to integrate the Django web framework with both MySQL and MongoDB databases and use a JSON dataset to create the required web pages. The five servers that we'll be leveraging for this project are:

Server 1: Web Server
A web server is required to host and manage incoming HTTP requests for the Django application. For this project, nginx was chosen as it is highly scalable, efficient, and offers excellent support for load balancing, caching, and handling HTTP requests. 

Server 2: Django Application Server
To effectively use Django, a reliable application server is crucial. It provides infrastructure for seamless framework operation and easy logic management. With a Django server, developers can streamline development and improve app functionality.

Server 3: MySQL Database Server
MySQL is a great way to store relational data from the portal. It's a powerful database management system offers secure and efficient storage, optimal performance, and seamless integration with Django through the Django-MySQL package. 

Server 4: MongoDB Database Server
This project will be using MongoDB Compass or Atlass to manage JSON datasets. MongoDB's document-based approach is great for unstructured data and allows for scalability and advanced queries. For Django integration, we suggest using Django MongoDB Engine. MongoDB Compass or Atlass are flexible and reliable tools for managing JSON datasets.

Server 5: Load Balancer
It's important to have a good system for managing traffic to ensure the web server and database servers are balanced. This helps prevent overload and ensures users can access the website quickly. By monitoring traffic and making changes as needed, the system can be maintained and handles lots of traffic without problems. Also, improve performance and avoid downtime or data loss by using failover and redundancy measures.

### The steps to integrate Django with the JSON dataset.
**1. Create and activate a virtual environment**
       
  i. Create a virtual environment by navigating to the project file.
       
       python -m venv myenv //create a virtual environment
       myenv\Scripts\activate //activate the virtual environment

**2. Install and set up Django**

   i. Install Django with the pip package manager `pip install Django`.
   
   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/e9fc62ee-df72-4bed-8ac9-05b5eb829328" />

   ii. Start the Django project by executing the `django-admin startproject` command and navigate to the project directory.
   
   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/6683a49d-7ae0-46b6-bd7d-ee48ac0c5fa2" />
   
   Ensure that the project file has been generated.
   
   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/7ec8a872-45de-4a93-a010-ed7c9fecbf3e" />
    
   iii. Create a new Django app within the analytics directory, execute the command `python manage.py startapp financialAnalytics`.

   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/d523bb25-d9f3-4b97-903f-8452ee38584d" />

**3. Configure Django Settings**

   i. In order to establish connections to MySQL and MongoDB, it is necessary to gain access to the settings.py file located in the project directory and make modifications to the `DATABASES` setting.
   
   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/9f436ec6-1ff5-4623-96b9-6386b1a56fc8" />

   ii. Install both djongo and mysqlclient, simply use the pip command: `pip install djongo` for djongo and `pip install mysqlclient` for mysqlclient.

   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/5bbc6472-f34e-47bb-8f5d-11dcb56618b3" /> 

   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/92a6752e-8f2c-4a69-8c17-2554e66badba" />

**4. Define models**

To define your Django models, head to the models.py file found within your app directory. Use the JSON dataset and data structure to specify fields and relationships. Within this file, create three distinct model classes: accounts, transactions, and customers.

 <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/1c32b8bb-974a-4ccc-8e17-f338c54b8c49" />
 
**5. Run Migrations**

   i. To add an application to your project, open the settings.py file and include its name in the INSTALLED_APPS section.
   
   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/279e0d82-7e86-42f0-8fd3-67580a773226" />

   ii. To generate database migrations according to the specified models, execute the `python manage.py makemigrations` command. Subsequently, use the `python manage.py migrate` command to implement these migrations. 
   
   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/92922036-d6e2-4a97-af35-336ab10deefd" />
   <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/d04788ea-5681-43b5-bd87-642cb547821e" />

  The table create at MySQL after the migration is as pictured below.
  
  <img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/a3975966-4aab-4911-b08b-8cbaa13a3c80" />

**6. Load JSON Data into Databases**

**5. Perform Data Retrieval**

## Question 1 (b)

<img src="https://github.com/sakinahalizzah/SECP3843/assets/99240177/7d918d46-0aff-4e93-a0bf-d0bf57cfa040" />

Integrating a web server, dataset, and databases can be a complex process, but with the right system architecture in place, it can be seamless and efficient. The architecture that we recommend involves building the web server on the Django framework. Django is a popular Python-based framework for building web applications, and it provides developers with a range of useful tools and features for creating robust and scalable web applications.

In this architecture, the dataset is stored in JSON format. JSON is a lightweight data format that is commonly used for transmitting and storing structured data. By using JSON, developers can ensure that their data is easily accessible and can be transmitted quickly and efficiently.

To store and retrieve data, two databases are used: MySQL and MongoDB. MySQL is a popular relational database management system that is well-suited for structured data with predefined schemas. It is a reliable and robust database system that is widely used in enterprise applications. On the other hand, MongoDB is a NoSQL database that offers high scalability and flexibility for unstructured or semi-structured data. It is a popular choice for applications that require a high degree of flexibility and scalability.

To integrate Django with both databases, developers use Django's Object-Relational Mapping (ORM). The ORM provides an abstraction layer that simplifies database operations, allowing developers to interact with the databases using Python objects and methods. This abstraction simplifies the process of working with databases, making it easier for developers to write code that interacts with the databases.

The ORM also provides an abstraction layer between the application and the databases. This enables seamless data manipulation, ensuring that the application can interact with the databases in a seamless and efficient manner. By using the ORM, developers can ensure that their code is easily maintainable and scalable.

Overall, this system architecture provides a robust and scalable solution for integrating Django, JSON datasets, and both MySQL and MongoDB databases. It ensures efficient data storage and retrieval and allows for seamless integration between the web server and the databases. With this architecture in place, developers can build robust and scalable web applications that can handle a high volume of data and traffic.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



