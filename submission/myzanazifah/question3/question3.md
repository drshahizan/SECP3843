<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Myza Nazifa Binti Nazry
#### Matric No.: A20EC0219
#### Dataset: Stories

## Question 3 (a)

1. Create a virtual environment and activate it.
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(1).png" /></div>
2.  Then, create a Django project. After creating a new Django project, then create a Django apps.
      
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(2).png" /></div>
4. Open the folder in Visual Studio Code and go to settings.py. Configure the database settings and also add the app in the code as shown in figures below:
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(3).png" /></div>
      
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(4).png" /></div>
5. Then, go to phpmyadmin and create a new database. I have named the database as 'storiesportal'.
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(5).png" /></div>
6.  Install two of these libraries to connect with MySQL database by using the commands below.
   
     ```
      pip install mysql-connector-python
      
      pip install mysqlclient
      ```
7.  Go to models.py and create the User Models. 
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(6).png" /></div>
8.  Run the following code to migrate the database and tables.
      
     ```
      python manage.py makemigrations
      
      python manage.py migrate
      ```
9.  The figure below shows the table that has been successfully migrated.
    
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(7).png" /></div>
10.  In settings.py, add the following command to ensure that Django is using the right User model.
     
     ```
      AUTH_USER_MODEL = 'AAapp.User'
      ```
11.  Then, we need to register the User Model. Go to admin.py and add the following code:    

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(8).png" /></div>
12.  In the Django application directory, create a new file named 'form.py' to create the registration and login form. Add the following code as shown below:

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(9).png" /></div>
13. Then, go to views.py and import necessary modules. Then, create a view for user registration, user login and logout. For the function customer_view, technical_worker_view and senior_management_view, ensure putting @login_required so that only authenticated users can access the page.

    <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(10).png" /></div>
    
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(11).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(12).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(13).png" /></div>
14. After that, configure the url path in url.py.

    <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(14).png" /></div>

15. Go to the Django application directory and go to the integrated terminal. Run the following code to create templates directory.

    ```
      mkdir templates
      ```
16. In the templates directory, create five new files which are 'customer.html', 'login.html', 'register.html', 'senior.html' and lastly is 'technical.html'.

    <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(21).png" /></div>
    
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(22).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(26).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(24).png" /></div>     
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(25).png" /></div>
18. Once everything has been done, open a new terminal and run the command below.    

    ```
      python manage.py runserver
      ```

### Registration page

   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(15).png" /></div>


   Database after registering new users:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(16).png" /></div>

### Login page

   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(17).png" /></div>


   Customer view after logging in:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(18).png" /></div>

   Technical worker view after logging in:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(19).png" /></div>

   Senior management view after logging in:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(20).png" /></div>
     

## Question 3 (b)

To overcome the challenge of data replication and synchronization between MySQL and MongoDB databases, it is recommended to implement database-specific replication techniques. One approach is to utilize MySQL replication, which enables the automatic replication of data from MySQL to MongoDB. Additionally, triggers can be implemented to ensure data synchronization between the two databases, triggering actions based on specified events to keep the data consistent and up to date.

### Steps to Implement MySQL Replication

1. First, go to XAMPP go to my.ini file. Then, locate the [mysqld] section and add the following lines:

   ```
      server-id=1
      log-bin=mysql-bin
      binlog-format=row
      ```
2. Then, go to MongoDB Compass and create a new database. 

   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(27).png" /></div>
3. After that, set up a connection with MongoDB by installing MySQL Connector library and Pymongo library.

   ```
      pip install mysql-connector-python
      
      pip install pymongo
      ```
4. Then, open terminal in Visual Studio Code and create a new directory called replication and add a python file called 'replication.py' in the directory.

   ```
    mkdir replication
      ```
5. For the replication.py file, write the following code for data replication.
   - First, import necessary libraries.
     
      ```
      import mysql.connector
      from pymongo import MongoClient
      import logging
      ```
   - Then, configure the database

      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(28).png" /></div>
   - Then, make a function for replication.

     ```
      def replicate_to_mongodb(event, row):
       try:
           if event == 'INSERT':
               transformed_data = {
                   'id': row['id'],
                   'password': row['password'],
                   'last_login': row['last_login'],
                   'is_superuser': row['is_superuser'],
                   'username': row['username'],
                   'first_name': row['first_name'],
                   'last_name': row['last_name'],
                   'email': row['email'],
                   'is_staff': row['is_staff'],
                   'is_active': row['is_active'],
                   'date_joined': row['date_joined'],
                   'user_type': row['user_type'],
                   'address': row['address'],
                   'phone_number': row['phone_number'],
               }
               mongo_collection.insert_one(transformed_data)
               logging.info(f"Inserted data into MongoDB: {row}")
           elif event == 'UPDATE':
               filter_query = {'id': row['id']}  
               update_data = {
                   '$set': {
                       'password': row['password'],
                       'last_login': row['last_login'],
                       'is_superuser': row['is_superuser'],
                       'username': row['username'],
                       'first_name': row['first_name'],
                       'last_name': row['last_name'],
                       'email': row['email'],
                       'is_staff': row['is_staff'],
                       'is_active': row['is_active'],
                       'date_joined': row['date_joined'],
                       'user_type': row['user_type'],
                       'address': row['address'],
                       'phone_number': row['phone_number'],
                   }
               }
               mongo_collection.update_one(filter_query, update_data)
               logging.info(f"Updated data in MongoDB: {row}")
           elif event == 'DELETE':
               filter_query = {'id': row['id']}  
               mongo_collection.delete_one(filter_query)
               logging.info(f"Deleted data from MongoDB: {row}")
       except Exception as e:
           logging.error(f"Error during MongoDB replication: {e}")
   - After that, connect to MySQL database and make a replication loop for it to insert in MongoDB and then close the connection.

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(29).png" /></div>
     
6. Go to phpmyadmin and click on the storiesportal database. Then, go to SQL and run the command below to create triggers. This will enable data synchronization between two databases.

     ```
     DELIMITER //

      CREATE TRIGGER sync_insert_to_mongodb
      AFTER INSERT ON aaapp_user
      FOR EACH ROW
      BEGIN
          DECLARE new_row JSON;
          SET new_row = JSON_OBJECT(
              'id', NEW.id,
              'password', NEW.password,
              'last_login', NEW.last_login,
              'is_superuser', NEW.is_superuser,
              'username', NEW.username,
              'first_name', NEW.first_name,
              'last_name', NEW.last_name,
              'email', NEW.email,
              'is_staff', NEW.is_staff,
              'is_active', NEW.is_active,
              'date_joined', NEW.date_joined,
              'user_type', NEW.user_type,
              'address', NEW.address,
              'phone_number', NEW.phone_number
          );
          CALL replicate_to_mongodb('INSERT', new_row);
      END//
      
      CREATE TRIGGER sync_update_to_mongodb
      AFTER UPDATE ON aaapp_user
      FOR EACH ROW
      BEGIN
          DECLARE new_row JSON;
          SET new_row = JSON_OBJECT(
              'id', NEW.id,
              'password', NEW.password,
              'last_login', NEW.last_login,
              'is_superuser', NEW.is_superuser,
              'username', NEW.username,
              'first_name', NEW.first_name,
              'last_name', NEW.last_name,
              'email', NEW.email,
              'is_staff', NEW.is_staff,
              'is_active', NEW.is_active,
              'date_joined', NEW.date_joined,
              'user_type', NEW.user_type,
              'address', NEW.address,
              'phone_number', NEW.phone_number
          );
          CALL replicate_to_mongodb('UPDATE', new_row);
      END//
      
      CREATE TRIGGER sync_delete_to_mongodb
      AFTER DELETE ON aaapp_user
      FOR EACH ROW
      BEGIN
          DECLARE old_row JSON;
          SET old_row = JSON_OBJECT(
              'id', OLD.id,
              'password', OLD.password,
              'last_login', OLD.last_login,
              'is_superuser', OLD.is_superuser,
              'username', OLD.username,
              'first_name', OLD.first_name,
              'last_name', OLD.last_name,
              'email', OLD.email,
              'is_staff', OLD.is_staff,
              'is_active', OLD.is_active,
              'date_joined', OLD.date_joined,
              'user_type', OLD.user_type,
              'address', OLD.address,
              'phone_number', OLD.phone_number
          );
          CALL replicate_to_mongodb('DELETE', old_row);
      END//
      
      DELIMITER ;
     ```

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(30).png" /></div>

7. Go to SQL and run the command below to create events. This will trigger the execution of the trigger.
     ```
       -- Trigger for INSERT event
      CREATE EVENT sync_insert_event
      ON SCHEDULE EVERY 1 DAY
      STARTS CURRENT_TIMESTAMP
      DO
          INSERT INTO aaapp_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, user_type, address, phone_number)
          SELECT NEW.id, NEW.password, NEW.last_login, NEW.is_superuser, NEW.username, NEW.first_name, NEW.last_name, NEW.email, NEW.is_staff, NEW.is_active, NEW.date_joined, NEW.user_type, NEW.address, NEW.phone_number;

     -- Trigger for UPDATE event
      CREATE EVENT sync_update_event
      ON SCHEDULE EVERY 1 DAY
      STARTS CURRENT_TIMESTAMP
      DO
          UPDATE aaapp_user
          SET password = NEW.password, last_login = NEW.last_login, is_superuser = NEW.is_superuser, username = NEW.username,
              first_name = NEW.first_name, last_name = NEW.last_name, email = NEW.email, is_staff = NEW.is_staff,
              is_active = NEW.is_active, date_joined = NEW.date_joined, user_type = NEW.user_type, address = NEW.address,
              phone_number = NEW.phone_number
          WHERE id = NEW.id;

     -- Trigger for DELETE event
      CREATE EVENT sync_delete_event
      ON SCHEDULE EVERY 1 DAY
      STARTS CURRENT_TIMESTAMP
      DO
          DELETE FROM aaapp_user WHERE id = OLD.id;
     ```

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(33).png" /></div>
8. Then, run the code below to migrate the data from MySQL to MongoDB.
   ```
   python replication.py
   ```
9. Figures below shows that the data has successfully inserted in MongoDB.
    
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(31).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(32).png" /></div>

     
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



