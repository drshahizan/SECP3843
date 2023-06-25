<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: AHMAD AIMAN HAFIZI BIN MUHAMMAD
#### Matric No.: A20EC0177
#### Dataset: ANALYTICS DATASET

## Question 1 (a)

Setting up a Django project involves installing Python and Django, creating a virtual environment, creating a new Django project using the django-admin command, configuring the database in the settings.py file, and starting the development server using the python manage.py runserver command.

To integrate Django with the JSON dataset and ensure efficient data storage and retrieval from both MySQL and MongoDB databases for the Analytics Dataset, follow these steps.

1. *Install Django*: Install the Django using the pip package manager. Since I am using Windows, open the command prompt and type in `pip install django`.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image1.png)

2. *Create Django project*: Create a new Django project by typing `django-admin startproject Analytics` where Analytics is the name of this project. A new project directory will be create with all the necessary files and folders pre-install.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image2.png)

3. *Create Django app*: Change directory by typing 'cd Analytics` in command prompt. Inside the Analytics directory, create an app by typing `python manage.py startapp AnalyticsDataset` in the command prompt where AnalyticsDataset is the name of the app. A new app directory with the required files will be created.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image3.png)

4. *Locate Database*: Open the settings.py file in Analytics directory. Set the "DATABASES" dictionary to include the necessary configuration for MySQL and MongoDB databases. Locate the screenshot of database codes in the settings.py file.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image4.png)

Djongo is a Django database engine that allows you to use MongoDB as the backend database for your Django projects. It provides compatibility between Django's ORM (Object-Relational Mapping) and MongoDB's document-based data model.

With Djongo, you can define Django models that represent your data structure and relationships, and these models will be translated into corresponding MongoDB collections and documents. This allows you to leverage the powerful querying capabilities of MongoDB while still using Django's familiar ORM syntax and features.

5. *Install Djongo*: Install djongo extension by typing `pip install djongo`.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image5.png)

`mysqlclient` is a Python library that provides an interface for connecting to a MySQL database from a Python application. It is a MySQL connector for Python that allows the interaction with a MySQL database using Python code.

By using mysqlclient, it can establish a connection to a MySQL database server, authenticate with the necessary credentials, and perform CRUD (Create, Read, Update, Delete) operations on the database. It provides a convenient and efficient way to interact with MySQL databases from any Python applications.

6. *Install mysqlclient*: Install mysqlclient by typing `pip install mysqlclient` in the command prompt.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image6.png)

7. *Modify Databse*: In the settings.py file, update the "DATABASES" code as the screenshot below.
   
>The `default` database is for MySql. Create a new database in MySql database and name it 'analytics'.


>The `mongdb` database is for MongoDB. Create a new database cluster name `projectcluster` with both username and password as admin, for now. Name the database as `analytics`

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image7.png)

In the context of Django, a model represents the structure and behavior of a database table. It defines the fields and relationships of the data stored in the table. Models in Django are typically defined in the models.py file of an app.

8. *Create models*: Do to AnalyticsDataset app, locate the `models.py` file and update the models to match that of the AA dataset. Create three models: Accounts, Customers, and Transactions.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image8.png)

When you define or modify your Django models, such as adding new fields or altering existing ones, Django needs to keep track of these changes and apply them to the database. Database migrations provide a way to manage these changes and keep the database schema synchronized with the models.

Running `python manage.py makemigrations` examines the current state of your models and compares them to the existing database schema. It then generates a set of migration files that describe the required changes to be made to the database schema.

9. `Register Apps`: In the `setting.py` file, locate the INSTALLED_APPS method. Add a new app below the 'django.contrib.statisfiles' called `AnalyticsDataset` so that when the mogration proses is initiated, Django web server knows which app is being updated to the MySql and MongoDB databse.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image11.png)

9. `Migrate database`: Type in `python manage.py makemigrations` in the command prompt. Then, run the python manage.py migrate command to apply these migrations. My Sql and MongoDB database will be updated.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image9.png)

10. `Load JSON`: Write a script to read the three JSON datasets obtained from AA: accounts.json, accounts.json, and transactions.json. Update both MySql and MongoDB databases. Create a file called `load_dataset.py` in AnalyticsDataset app to retrieve the dataset later.

![Q1](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%201/files/images/Q1%20image10.png)

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



