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

## Question 3 (a)
  1. Setting up the Django Project:
     - Install Django on my web server.
     - Create a new Django project using the django-admin startproject AA_Question3 command.
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.1.png">
          
     - Create a virtual environment for this project.
       
       ``` ruby
       python -m venv my_env
       my_env\Scripts\activate
       ```
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.2.png">
          
     - Install package Django with the code pip install Django
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.3.png">
          

  2. Creating a Django App:
     - Create a new Django app within your project using the python manage.py startapp q3 command.
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.4.png">
          


   3. Configuring the MySQL Database:
      - Install the MySQL database connector for Python using pip install mysqlclient.
        
         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.5.png">
          
      - In the project's settings.py file, configure the database settings to connect to the MySQL database with the details like database name, host, port, username,           and password.

         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.6.png">
          
 
   4. Designing the User Model:
      - Define a user model class that will represent the users of the system in the q3's models.py file which include fields like username, email, password, and              fields specific to each user type (customers, technical workers, senior management).
      - The user model should include fields like username, email, password, and additional fields specific to each user type (customers, technical workers, senior             management)

         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.7.png">
          
 
  5. Creating the Registration and Login Views:
     - Create view functions for user registration and login in the q3's views.py file.
     - The registration view will handle user sign-up, validate the input data, and create a new user instance in the database.
     - The login view will handle user authentication, verify credentials, and provide access to the system upon successful login.
       
        <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.8.png">
          
 
  6. Implementing the Registration and Login Templates:
     - Create HTML templates for user registration and login forms which will include input fields for the required user information, such as username, email, and              password and he login template will contain fields for username/email and password.
       
          <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/3335e687c35ce6fac6dac1c3debb8a7d3ec81e50/submission/RishmaFathima/Question3/files/images/3.1.17.PNG">

         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/3335e687c35ce6fac6dac1c3debb8a7d3ec81e50/submission/RishmaFathima/Question3/files/images/3.1.16.PNG">
          
 
   7. Mapping URLs to Views:
      - Defined URL patterns in the q3's urls.py file, mapping them to the registration and login views that is created earlier.
        
         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/2f6313177e823c8cd516bd9e08d8e37d05123d50/submission/RishmaFathima/Question3/files/images/3.1.11.png">
          
 
  8. Migrating the Database:
     - Run the database migrations using the python manage.py makemigrations and python manage.py migrate commands which create the necessary database tables based on          the user model defined earlier.

       ```ruby
       python manage.py makemigrations
       python manage.py migrate
       ```

  9. Testing and Deployment:
      - The user registration and login functionality tested locally to ensure everything works as expected using the command:
        
        ```ruby
        python manage.py runserver
        ```
      - The output:
        
         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/3335e687c35ce6fac6dac1c3debb8a7d3ec81e50/submission/RishmaFathima/Question3/files/images/3.1.14.PNG">
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/3335e687c35ce6fac6dac1c3debb8a7d3ec81e50/submission/RishmaFathima/Question3/files/images/3.1.15.PNG">
## Question 3 (b)
  1. Determine the replication requirements by:
     - Determinining whether we need MySQL to MongoDB or MongoDB to MySQL) or both databases replicating to each  other and consider which database is the primary            source of data and which is the secondary.
     - Determine the level of consistency required between the databases.
     - Determine how often data is updated in our databases.
     - Identify the specific tables or collections that need to be replicated between the databases.
     - Determine if there are any dependencies between tables or collections that require maintaining data integrity during replication.

  2. Replication technique:
     - MySQL Replication:
       - Master-Slave replication
         -  In Master-Slave replication, there is one master database and one or more slave databases.
         -  The master database is the primary source of data, and any changes made to it are replicated to the slave database
         -  The slave databases are read-only copies of the master and can be used for various purposes like scaling read operations or providing backup options.
       - Master-Master Replication
         - Master-Master replication, also known as circular or bidirectional replication, allows multiple MySQL databases to act as both master and slave                        simultaneously
         - Each database in the replication setup can accept read and write operations and replicate changes to other databases.
          
     - MongoDB Replication
       - Replica sets are a feature offered by MongoDB. Multiple MongoDB instances, comprising a primary node and one or more secondary nodes, make up a replica set.           All write activities are received by the primary node, and the modifications are then automatically replicated to the secondary nodes.
       - The replication process in MongoDB is asynchronous.
         
  3. Set up replication for MySQL:
     - Enable binary logging in the MySQL configuration file (my.cnf or my.ini), ensure that binary logging is enabled. 
       ```ruby
       log_bin = /path/to/binary/log
       ```
     - Configure the master database: On the master database, create a replication user and grant the necessary privileges for replication.
     - Configure the slave database: On the slave database, configure the replication settings to connect to the master database.
     
       ```ruby
       server-id = unique_slave_id
       relay-log = /path/to/relay/log
       ```
     - Connect Slave to the Master
       ```ruby
       CHANGE MASTER TO MASTER_HOST = 'master_ip',
       MASTER_USER = 'root',
       MASTER_PASSWORD = '',
       MASTER_LOG_FILE = 'bin_log_file',
       MASTER_LOG_POS = bin_log_position;
       ```


  6. Set up replication for MongoDB:
     - Create a replica set by Initializing a MongoDB replica set by starting a MongoDB instance with the 
     - Add secondary nodes by Connecting to the primary node and add secondary nodes to the replica set. Each secondary node will replicate changes from the primary.

  7. Implement data synchronization logic by:
     - Determine the direction of synchronization: one-way (MySQL to MongoDB or MongoDB to MySQL) or bi-directional.
     - Decide on the synchronization frequency, such as real-time or scheduled intervals.
     - Establish connections to both the MySQL and MongoDB databases using drivers or connectors.
       ```ruby
       import mysql.connector
       from pymongo import MongoClient

        # Connect to MySQL
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="AA_STDE"
          )
          
          # Connect to MongoDB
          mongo_client = MongoClient("mongodb://localhost:27017/")
          mongo_db = mongo_client["AA_STDE"]
       ```
     - Fetch the data from the source database based on the synchronization approach
         ```ruby
         mysql_cursor = mysql_conn.cursor()
         mysql_cursor.execute("SELECT * FROM Airbnb")
         mysql_data = mysql_cursor.fetchall()
        ```
     - Apply the data changes to the MySQL or MongoDB based on the synchronization approach. For one-way synchronization, insert, update, or delete data accordingly.         For bi-directional synchronization, implement logic to determine the source and target databases for each change.
        ```ruby
         mongo_collection = mongo_db["AA"]
         mongo_collection.insert_many(mongo_documents)
        ```
  10. Test and monitor the replication and synchronization: Verify that the replication and synchronization processes are working as expected. 




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


