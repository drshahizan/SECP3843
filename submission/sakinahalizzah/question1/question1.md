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
As an IT consultant, I was responsible for guiding the technical team on how to implement a configuration that involved five servers for our latest project. For this endeavor, my team had to integrate the Django web framework with both MySQL and MongoDB databases and use a JSON dataset to create the required web pages. The five servers that we'll be leveraging for this project are:

Server 1: Web Server

To host and manage incoming HTTP requests for the Django application, usually using Nginx or Apache. 

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

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/be5be54f-9a52-42a2-b1f4-963ae7b7997f" />


The system architecture consists of the client tier, the part of the system that users interact with directly. Users send requests and receive responses through a web browser or a different client application through this tier. It's responsible for rendering the user interface and handling all user interactions, such as filling out forms and clicking links.

Second is the web tier, this is where all HTTP requests and responses are processed. It includes the Django web framework and various components that work in tandem to ensure seamless operation. As requests arrive from the client tier, the web tier directs them to the relevant views or controllers within the application tier. Additionally, it handles the task of generating templates and delivering dynamic HTML or other appropriate content in response.

Moving on to the application tier which is the core processing layer of the system. It's responsible for all the business logic, communicating with the web tier, databases, and datasets. This tier defines the Django models representing the database tables and contains all the necessary code to parse, validate, and process the JSON dataset. It also integrates with the database engines, MySQL and MongoDB, using Django's ORM to perform data storage, retrieval, and manipulation operations.

Lastly, the portal tier is the user-facing part of the system that provides all the functionality and data visualization. It relies on the application tier to retrieve data from the databases and dataset and transform it into a suitable format for presentation. The portal tier includes all the necessary components to make the user experience as smooth as possible, such as data visualization libraries, dashboard modules, and user interface templates. It uses Django's templating system or frontend frameworks to render dynamic web pages and display the requested data visually appealing and interactively.

In summary, these four tiers work together seamlessly to provide users a great experience. With the Django web framework, the JSON dataset, and the MySQL and MongoDB databases all working together, data storage, retrieval, and visualization are efficient and effective.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



