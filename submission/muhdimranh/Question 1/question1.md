<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: MUHAMMAD IMRAN HAKIMI BIN MOHD SHUKRI
#### Matric No.:A20EC0213
#### Dataset:AIRBNB

## Question 1 (a)

To integrate Django with the JSON dataset and ensure efficient data storage and retrieval from both MySQL and MongoDB databases for Airbnb Booking Portal, there are numbers steps need to be followed:

### 1. **Install Django**
Start by installing Django by using the pip package manager to install Django. Use `python -m pip install Django`.

![Q1](files/images/q1_1.png)

### 2. **Set up Django project**
Create a new Django project using the `django-admin startproject` command. This will create a project directory with the necessary files and folders.

![Q1](files/images/q1_2.png)
![Q1](files/images/q1_3.png)

### 3. **Create Django app**
Inside the project directory, create a new Django app using the `python manage.py startapp` command. This will create an app directory with the required files for the app.

![Q1](files/images/q1_4.png)

### 4. **Configure the settings**
Open the settings.py file in the project directory and configure the database settings for both MySQL and MongoDB. Set the "DATABASES" dictionary to include the necessary configuration for MySQL and MongoDB databases. 

In this approach, I will be using the djongo library to connect to MongoDB. To add MongoDB and MySQL as database:

![Q1](files/images/q1_5.png)

a. Install djongo using `pip install djongo` and mysqlclient using `pip install mysqlclient`.

![Q1](files/images/q1_6.png)![Q1](files/images/q1_7.png)

b. Modify the "DATABASES" library as the following:

```
MongoDB: `DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'your-db-name',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
            }  
        }
}

MySQL: `DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'mydb',
		'USER': 'root',
		'PASSWORD': 'admin',
		'HOST':'localhost',
		'PORT':'3306',
	}
}
```

c. To use both, here is an example of how I implement it in my settings.py:

![Q1](files/images/q1_8.png)

### 5. **Define models**

In Django, models represent the structure of the data. Define models in the models.py file of the app to reflect the schema of the JSON dataset. Each model class should correspond to a table in the databases. Below is how can I write based on my dataset.

![Q1](files/images/q1_14.png)

### 6. **Migrate the database**
Run the `python manage.py makemigrations` command to create the necessary database migrations based on the defined models. Then, run the `python manage.py migrate` command to apply these migrations and create the corresponding tables in both MySQL and MongoDB.

Before applying migration, make sure in the settings.py, in INSTALLED_APPS, your application name is written.

![Q1](files/images/q1_12.png)

![Q1](files/images/q1_13.png)

Pictures below show how migration is made towards MySQL.

![Q1](files/images/q1_16.png)

![Q1](files/images/q1_15.png)

### 7. **Load data from JSON**
Write a script or a Django management command to read the JSON dataset (listingsAndReviews.json) and populate the tables in both databases. I will use the Django ORM to interact with the databases and insert the data.

### 8. **Querying and retrieving data**
Use Django's ORM to query and retrieve data from both databases. This can be done by writing queries and perform operations on the model to fetch the required data. For example, if i want to load anything from my dataset, I can use the retrieval query as below.

![Q1](files/images/q1_11.png)

### 9. **Update and synchronization**
If the JSON dataset is updated or new data is added, I will need to update the databases accordingly.

### 10. **Test and optimize**
Test the integration thoroughly to ensure that data is stored and retrieved correctly from both MySQL and MongoDB. Optimize the queries and database operations for better performance, considering factors such as indexes and query optimization techniques.

From all the steps above, there are some steps that I may skip in case I already have the airbnb datasets populated in my MongoDB database. In this case, I can skip loading data from JSON (step 7).



## Question 1 (b)

![Q1](files/images/q1_17.png)

### 1. User Interface (Application UI, Admin UI, Dashboard):

This is the interface through which users interact with the application. It sends HTTP/HTTPS requests to the web server.

### 2. Web Server (Django):

Acts as the central hub of the application. Handles incoming HTTP/HTTPS requests from the user interface. Contains the application layer, models layer, visualization module and JSON dataset.

### 3. Application Layer:

Includes forms, template and view function responsible for handling requests and generating responses. Communicates with the models layer and retrieves data for presentation.

### 4. Models Layer:

Represents the database layer of the application. Consists of two databases: MySQL DB and MongoDB. Stores and retrieves data using Django's ORM (Object-Relational Mapping). By including bidirectional arrows between the Models Layer and JSON Datasets components, I indicate that data synchronization can occur in both directions. This means that updates made in the models layer can be reflected in the JSON datasets, and vice versa. This ensures data synchronization.

### 5. JSON Datasets:

Contains the dataset the Airbnb dataset provided for analysis. These datasets serve as a source of data for the application.

### 6. Data Synchronization:

Involves the synchronization of data between the models layer (databases) and the JSON datasets. Ensures that the data remains consistent and up to date in both storage options.

### 7. Data Presentation:

Involves the generation of visualizations and the presentation of data to the user. This component includes the dashboard and visualization modules.



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



