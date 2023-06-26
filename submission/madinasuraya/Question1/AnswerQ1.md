## Special Topic Data Engineering (SECP3843): Alternative Assessment ©️

#### Name: MADINA SURAYA BINTI ZHARIN
#### Matric No.: A20EC0203
#### Dataset: companies.json

### Question 1 (a)

Steps required to integrate multiple datasets with Django are as follows.

1. Install required softwares.
    - Xampp: To open localhost and access MySQL database.
    - MongoDB Compass: To store JSON format data. 
    - Django: Web development

2. Configure MongoDB Atlas and MongoDB Compass with connection string. 

3. Install djongo in terminal or command prompt to connect Django and MongoDB.
   
    ```
    pip install djongo
    ```

4. Tell Django the database server that will be used. Upon installing Django, you will see a file named settings.py. Here, we will define our databases. Example as follows:

    - MongoDB
      1. Create a database in mongodb.
      2. Configure the database with details about your mongodb such as defining the ‘ENGINE’ with djongo, ‘NAME’ as the database name created, and ‘CLIENT’ as the mongodb connection string.
         
         ```
         DATABASES = { 'default': {
            'ENGINE': 'djongo',
            'NAME': 'AA',
          CLIENT': {
                'host': 'mongodb+srv://user1:60XRzCr4mubxCPC5@cluster0.evngzba.mongodb.net/test',
            }}}
        ```
    - MySQL
        1. Create a database in MySQL.
        2. Configure the database with details about your MySQL database such as defining the ‘ENGINE’ with .mysql, ‘NAME’ as the database name created, and others as the   details of the localhost connectivity.

      ```
      DATABASES = {'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'aa',
              'HOST': 'localhost',
              'PORT': '3306',
              'USER': '',
              'PASSWORD': '',} }
      ```

5. Perform migration for MySQL.

```
 python manage.py makemigrations
```

6. Import JSON data into MongoDB.

7. Retrieve data from mongodb using python.

```
Client= pymongo.MongoClient(“mongodb+srv://user1:60XRzCr4mubxCPC5@cluster0.evngzba.mongodb.net/test”)
db = client[“AA”]
collection = db[“companies”]
Data = list(collection.find())
```
8. Make a model in models.py which represents the table and fields in MySQL database. Tables will be created according to the models and from here, we can insert or retrieve the data. 


### Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
