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
   1. Set up the Django project:
        Install Django: Ensure that Django is installed on your system. You can use pip to install Django.
        Create a new Django project: Use the django-admin startproject command to create a new Django project.
        Set up the Django app: Create a new Django app within the project using the python manage.py startapp command.

  2. Define Django models:
        Analyze the JSON dataset to understand its structure and attributes.
        Create Django models: Define Django models that mirror the structure of the JSON data. Each attribute in the JSON should correspond to a field in the Django             model.
        Specify field types: Choose appropriate field types for each attribute in the Django models, considering the data types in the JSON dataset.

  3. Configure databases:

        Configure MySQL database:
            Install MySQL: Install MySQL on your system if it's not already installed.
            Create a MySQL database: Create a new MySQL database that will be used to store data from the JSON dataset.
            Configure Django to use MySQL: In the Django project's settings.py file, update the DATABASES dictionary to provide the necessary connection details for the             MySQL database.

  4. Configure MongoDB database:
            Install MongoDB: Install MongoDB on your system if it's not already installed.
            Create a MongoDB database: Create a new MongoDB database that will be used to store data from the JSON dataset.
            Configure Django to use MongoDB: Install the djongo package using pip and follow the package documentation to configure Django's settings file (settings.py)             to connect to the MongoDB database.

  5. Import JSON data:
        Download the JSON dataset and save it in a location accessible to your Django project.
        Create a Django management command: Implement a custom Django management command that reads the JSON dataset and imports the data into the MySQL and MongoDB             databases. The command should handle the mapping between the JSON data structure and the Django models.

  6. Store data in MySQL and MongoDB:
        Within the custom management command, parse the JSON dataset and use the Django ORM to create instances of the defined models.
        Save the instances in the MySQL database by calling the .save() method.
        Save the instances in the MongoDB database by using the Django ORM and the djongo package's features for MongoDB integration.

   7. Retrieve data from MySQL and MongoDB:
        In your Django views or API endpoints, define the logic to retrieve data from both the MySQL and MongoDB databases based on user requests.
        Use the Django ORM to query the MySQL database and retrieve the desired data.
        Use the djongo package's features to query the MongoDB database and retrieve the required data.

  8.  Optimize data storage and retrieval:
        Implement appropriate indexing and caching mechanisms in both the MySQL and MongoDB databases to optimize data retrieval.
        Monitor and profile the system's performance to identify any bottlenecks or areas for optimization.
        Consider using database-specific optimizations, such as denormalization or aggregations, to improve query performance.

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

