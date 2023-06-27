<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.


## Special Topic Data Engineering (SECP3843): Alternative Assessment ©️

#### Name: MADINA SURAYA BINTI ZHARIN
#### Matric No.: A20EC0203
#### Dataset: companies.json

### Question 3 (a)

1. Download Django in command prompt
   ```
   pip install django
   ```
   
2. In the desired file path, create new django project
   ```
   django-admin startproject djangoAA
   ```
   
3. Navigate path to the new created project
   ```
   cd AA
   ```
   
4. Startapp for the users. The folder directory is as follows.
   ```
   python manage.py startapp signup
   ```
  <p align="center">
      <img width="122" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/ed2447f0-a99d-4043-bb71-eeda4b2305ff">
  </p>

5. Open **settings.py** in **AA** folder and update the code.
   - Firstly, add the name of the startapp folder in **INSTALLED_APPS**.
      ```
      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'signup',
      ]
      ```
    - Next, configure the database connection to mysql.
      ```
      DATABASES = {'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
                'unix_socket': 'C:/xampp/mysql/mysql.sock',}}}
      ```
      
6. Apply migrations
     ```
     python manage.py makemigrations
     ```
     ```
     python manage.py migrate
     ```
     
7. Open localhost and create new database. I created my folder as 'aa'.
      <p align="center">
           <img width="162" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/af17e0cd-33c6-4216-9f79-50e4941f4f75">
      </p>

8. Open **models.py** in the **signup** folder and start making user authentication. To perform this, firstly, define django authentication models and import it. Then, define the class for each user needed. In here, there will be three users which are customers, technical workers, and senior management. This also means that each user type will have their own table in the database. Since we use some common fields such as **first_name, last_name, email, username, and password**, we dont have to specify it in the class as the django authentication model already include this.
   ```
   from django.contrib.auth.models import AbstractUser
   ```
   ```
   class Customer(AbstractUser):
       pass

   class TechnicalWorker(AbstractUser):
       pass
   
   class SeniorManagement(AbstractUser):
       pass
   ```

9. Perform migrations for database and tables using commands below:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
10. Create the views for user registration and login, create urls routing to the specific page and perform CRUD for each user using **request.POST** and **request.GET** method.
   <p align="center">
      <img width="389" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/45a21554-6f16-4e8d-aaea-12061a5a46ce">
       <br><br>
      <img width="228" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/34d325cc-a6e9-4758-a008-f5954a9f6113">
      <br><br>
       <img width="412" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/e6efb5fa-c714-4da8-8c9c-97cc2f00fa77">
   </p>
   
11. The tables and its field created in mysql database are as follows:
    <p align="center">
      <img width="157" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/44b21732-1880-44c7-87e6-58ff7886444a">
      <img width="515" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/a876d3d2-0c9d-46cf-be5d-bbf2bc90efdc">
   </p>
    
   
   

     
### Question 3 (b)

To maintain data consistency across both systems it is recommended to perform some data replication techniques dedicated to the specific database to facilitate real-time updates and seamless interaction between them. Here are the steps that can be used to overcome this challenges to maintain synchronization between MySQL and MongoDB.

Firstly, it is advisable to choose the best replication techniques. I would recommend using **master-slave replication**. This technique is also known as single-leader replication. The master (single leader) node works as the primary database, while the slave (one or more) will maintain copies of the master's data. To be specific, master nodes handle write queries while slave nodes handle read queries. Whenever, master node performs a write operation, it will be replicated across the system to maintain data consistency. Unless the sales database is offline and there are no other slaves, master will handle the operations temporarily. These replication techniques are often being used in relational databases such MySQL and NoSQL databases, MongoDB. One thing for sure, if the leader suddenly fails, the data is available to the followers.

Next, choose the replication technique for each database. MySQL and MongoDB will have different settings and replication techniques.

- MySQL
   1.  Set up virtual environment with root access
      
   2. Determine the master server and slave server IP address. <br>
      **Master server: 12.34.56.111** <br>
      **Slave server: 12.23.34.222**
  
   3. Setting up the master by finding the bind-address in the mysql config file and changing it from to the master server IP defined above.
      <p align="center">
         <img width="285" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/5198bb43-3c39-470b-8c86-fc30c83b9435">
      </p>

   4. Uncomment line below and restart mysql.
      
      ```
      server-id =
      log-bin =
      ```
      
      <p align='center'>
         <img width="368" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/25be0bee-b336-4975-b0b3-95c5acac7b0f">
      </p>

    5. Create a new user for slaves by granting replication to the slave server IP defined above.
         ```
         root@repl-master:~# mysql -uroot -p; 
         mysql> CREATE USER ‘slave’@’12.34.56.789‘ IDENTIFIED BY ‘SLAVE_PASSWORD‘; 
         mysql> GRANT REPLICATION SLAVE ON . TO ‘slave’@’12.34.56.222 ‘; 
         mysql> FLUSH PRIVILEGES; 
         mysql> FLUSH TABLES WITH READ LOCK;
         ```
     6. Move data from master to slave
         ```
         root@repl-master:~# mysqldump -u root -p –all-databases –master-data > data.sql
         ```

     7. Configure slave server by uncomment the second line shown below.
          <p align='center'>
            <img width="280" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/4b6371f8-fcc4-4627-867d-446a416e9dfa">
         </p>

     8. Start a slave by running its command.
        ```
        START SLAVE
        ```
        
- MongoDB
     1. Define master  host name and open mongo shell.
  
         **Master server: 12.34.56.111**
        
     2. Switch context to the local database.
        ```
        use local
        ```
     3. Get the collection and ensure that there are no documents in the collection.
         ```
         db.companies2.find()
         ```
     4. Insert documents into the master. Specify the host as the master host name and only, as the database name.
         ```
         db.companies2.insert( { host: <12.34.56.111> <,only: db_crunchbase> } );
         ```

Finally, monitor the replication using status page in tabular format with the following details:

   - **File**: Present binary log
   - **Position**: Binary log position
   - **Io run**: Slave IO Thread Running status
   - **Sql run**: SQL Thread Running status
   - **MongoDB run**: MongoDB Thread Running status
   - **ErrorNum**: Error number
   - **ErrorMeg**: Error message


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
