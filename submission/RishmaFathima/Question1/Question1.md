<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Rishma Fathima Binti Basher
#### Matric No.: A20EC0137
#### Dataset: [Airbnb Listings Dataset](https://github.com/drshahizan/dataset/tree/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/05-airbnb)

## Question 1 (a)
   1. Set up the Django project with virtual environment:
      </br>
        - The first step is to install django in my desktop. In order to install django, I use the command  ``pip install django`` in command prompt.
          
          <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.1.png">
          
        - Then, I created a new project b: Use the django-admin startproject command to create a new Django project from a folder I have created called ``AA_Question1``           by using the command called ``django-admin startproject AA_Question1``.
          
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.2.png">
           
        - After creating the project, I created the Django app by the command ``python manage.py startapp app``.
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.3.png">
           
        - Then, create a virtual environment for the project.
          
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/871e6e313e09d8f507b32aaf9d54173434080a29/submission/RishmaFathima/Question1/files/images/new%201.1.1.4.png">

  2. Set up MySql Database
        - First, need to install the MySQL database server on our system. The MySQL Community Server is downloaded from the official MySQL website                               ``(https://dev.mysql.com/downloads/)``.
        - Download Xampp. Once the XAMPP installer is downloaded, run the executable file to start the installation process. Follow the on-screen instructions to                proceed and finish the the process
        - Create a database called ``AA_Mysql``
          
  4. Set up MongoDB Database
        - Go to the MongoDB website ``(https://www.mongodb.com/try/download/community)`` and select the appropriate version of MongoDB for our operating system
        - Create a database called ``AA_Mongo``
          
  5. Define Django models in models.py:
        - JSON file is downloaded from the Github.
        - Django models were created based on the attributes from the downloaded JSON file which contain the dataset of ``Airbnb Listing Dataset``.
        - From the app folder created, in the ``models.py`` file, the model of the prject would be defined.
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/c18d8db59264504dc5f34395291dfe90abb48c90/submission/RishmaFathima/Question1/files/images/1.1.2.png">
          
   
      

  6. Configure the settings of the project:

        - Update the ``settings.py`` file in the project folder to define the database setting for Mysql and MongoDB
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/c18d8db59264504dc5f34395291dfe90abb48c90/submission/RishmaFathima/Question1/files/images/1.1.3.1.png">
        - Update the ``settings.py`` file to declare the created ``app``
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bda3ad57b1a66ccf70c740ca047c30a08ee4c1c7/submission/RishmaFathima/Question1/files/images/1.1.3.3.png">
        - Install django with the command ``pip install django`` to work as database connectors
        -  Install another package ``pip install pymongo`` for MongoDB
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/1713eba60cac85222b200ca02917e21d4d29ac00/submission/RishmaFathima/Question1/files/images/1.1.3.4.png">
           
        - Install mysqlclient with the command ``pip install mysqlclient`` to work as database connectors
          <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/c18d8db59264504dc5f34395291dfe90abb48c90/submission/RishmaFathima/Question1/files/images/1.1.3.2.png">
         
           
  7. Migration of database and load the JSON file:

        - Add the command ``python manage.py makemigrations`` to migrate the database from the ``models.py``
        - Then add the command ``python manage.py migrate`` to make th emigrations work with Mysql and MongoDB

          ```ruby
          python manage.py makemigrations
          python manage.py migrate
          ```
        - The Mysql output from the above command:

          <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/0992b610b05bfd19edb75c9e0c3d0cfb2dbb5431/submission/RishmaFathima/Question1/files/images/1.1.4.1.png">
          
        - TheMongoDB output:
          
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/0992b610b05bfd19edb75c9e0c3d0cfb2dbb5431/submission/RishmaFathima/Question1/files/images/1.1.4.2.png">
     
      
          
          
        - Finally python generate a script to read Django.
         
  8. Retrieve, Update and Testing Data:

        - To retrieve all data from the MongoDB ``AA_Mongo`` collection:
     
          ```ruby

            from app.models import AA_Mongo
            aa_Mongo = AA_Mongo.objects.all()

          ```
        - To retrieve all data from the MongoDB ``AA_Mysql`` collection:
          
          ```ruby

          from app.models import AA_Mysql
          aa_Mysql = AA_Mysql.objects.all()

          ```
           
        - Update the MOngoDB and Mysql everytime there is changes in dataset
        - Finally, with testing and monitoring practices, I can ensure the reliability, performance, and stability of your Django application's integration with the               JSON dataset, MySQL, and MongoDB databases
        

## Question 1 (b)

System Architecture Diagram 

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/7f5702fc9817206787792eb17ce2305d156b0284/submission/RishmaFathima/Question1/files/images/1.2.1.jpg">

Detailed explanations for each component:

1. Web Server (Django):
   <p align="justify">
    The web server component of the system design is implemented using the high-level Python web framework Django. Along with serving dynamic web pages, Django also       handles user authentication, session management, and the request-response cycle. It follows the Model-View-Controller (MVC) architectural design paradigm, which       promotes problem-solving by separating concerns and reusing code. Django uses an Object-Relational Mapping (ORM) layer to communicate with databases. This layer       provides a useful method for building database models and performing CRUD activities.
   </p>
 3. Dataset (JSON):
      <p align="justify">
      The dataset component consists of structured data that has been saved in the JSON format. A straightforward data communication format that is easy for both            humans and robots to read and write is JSON (JavaScript Object Notation). Because it encodes data as key-value pairs and enables layered structures, it can            store complex data. The dataset is useful for building up database tables, providing static data to a web application, and serving as a bridge data format for         data processing processes, among other things.
       </p>
 5. Databases:
    
    a. MySQL:
       <p align="justify">
       Open-source MySQL is a well-known relational database management system (RDBMS). Performance, dependability, and scalability are its three most famous                 qualities. One database choice used in the system architecture to store structured data is MySQL. Database activities can be readily controlled and seamlessly         integrated because Django's ORM supports MySQL.
        </p>
    b. MongoDB:
         <p align="justify">
         The flexible and document-oriented BSON (Binary JSON) format is used by MongoDB to store data. Due to its scalability and agility, it is appropriate for               managing huge amounts of unstructured or semi-structured data. The system architecture uses MongoDB as an extra database option to store data that doesn't             fit well in a relational structure or requires high scalability. Django connects to MongoDB via third-party libraries like Djongo or MongoEngine and provides          an ORM-like interface for interacting with the database.
      </p>
    <p align="justify">
Finally, the integration of the databases (MySQL and MongoDB), the JSON dataset, and the web server (Django) is made possible by the system design. In order to abstract the difficulties of interacting with databases, it makes use of Django's strong ORM capabilities, providing the web application with a dependable and efficient data access layer. Whether MySQL or MongoDB should be utilised depends on the precise specifications and characteristics of the data being stored, providing for flexibility and
  </p>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

