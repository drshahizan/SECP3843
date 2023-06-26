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

### Question 1 (a)

Steps required to integrate multiple datasets with Django are as follows.

1. Install required softwares.
    - Xampp: To open localhost and access MySQL database.
    - MongoDB Compass: To store JSON format data. 
    - Django: Web development

2. Configure MongoDB Atlas and MongoDB Compass with connection string. 

3. Install djongo in terminal or command prompt to connect Django and MongoDB.
   
    ```python
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
                'host': 'mongodb+srv://user1:______________.mongodb.net/test',
            }}}
        
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
    Client= pymongo.MongoClient(“mongodb+srv://user1:____________________.mongodb.net/test”)
    db = client[“AA”]
    collection = db[“companies”]
    Data = list(collection.find())
    ```
    
8. Make a model in models.py which represents the table and fields in MySQL database. Tables will be created according to the models and from here, we can insert or retrieve the data. 


### Question 1 (b)

<p align="center">
<img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/e0940131-906a-4617-a734-edb498634c2d">
</p>

**Data Source** <br>
Data that contains information about companies listed on Crunchbase website was collected in JSON format.

**Data processing** <br>
Data preprocessing including data cleansing and transformation will be done using Python libraries such as Pandas. The data then can be stored in MongoDB as data storage in JSON format. 
A subset of data processing components including feature extraction or sample selection as an early process performing machine learning. 
Machine learning algorithms used in ML:
- Model fitting: When a set of training data is allocated to a model, it can then be used to generate accurate predictions about new or untrained data.
- Execution:  Processed and trained data is forwarded for ML routines.
- Deployment:  Insights of ML process are deployed

**Web Application** <br>
Web framework such as Django used  for rapid development of secure and maintainable websites. It is also highly accessible with Python language for ML algorithms.
Data about user credentials are collected and retrieved in the MySQL database while data from MongoDB will be visualized as a dashboard.

**Data Visualization** <br>
Real-time analytics will be performed using preprocessed data in MongoDB. An instance dashboard will be created using MongoDB features which are MongoDB Charts.

**Data Storage** <br>
Preprocessed data is stored in MongoDB to be retrieved for data visualizations and data about users credential from Django will be stored in MySQL database.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

