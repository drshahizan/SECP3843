<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Singthai Srisoi
#### Matric No.: A20EC0147
#### Dataset: Mflix Dataset

## Question 1 (a)

1. Set up the Django Project:
   - Install Django and create a new Django project using the command-line interface.
   ```bash
   pip install django
   django-admin startproject AA
   cd AA
   ```
   - Create a Django app within the project to handle the portal's functionality.
   ```bash
   python manage.py startapp AAapp
   ```

2. Define Django Models:
   - Analyze the JSON dataset structure and determine the relevant data fields to be stored in the databases.
   - Define Django models to represent the data structures of MySQL and MongoDB collections.
   
   ```python
    from django.db import models

    class Comment(models.Model):
        # Comment document fields
        name = models.CharField(max_length=255)  # Name of the commenter
        email = models.EmailField()  # Email address of the commenter
        movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)  # Unique identifier of the associated movie
        text = models.TextField()  # The actual comment text
        date = models.DateTimeField()  # Date and time of the comment

        def __str__(self):
            return self.text

    class Movie(models.Model):
        # Movie document fields
        plot = models.TextField()  # Brief description or summary of the movie
        genres = models.ArrayField(models.CharField(max_length=255))  # Array of genres associated with the movie
        runtime = models.IntegerField()  # Duration of the movie in minutes
        cast = models.ArrayField(models.CharField(max_length=255))  # Array of actors appearing in the movie
        num_mflix_comments = models.IntegerField()  # Number of comments/reviews for the movie
        title = models.CharField(max_length=255)  # Title of the movie
        fullplot = models.TextField()  # Detailed description or plot summary of the movie
        countries = models.ArrayField(models.CharField(max_length=255))  # Array of countries where the movie was produced
        released = models.DateField()  # Date of movie release
        directors = models.ArrayField(models.CharField(max_length=255))  # Array of directors of the movie
        rated = models.CharField(max_length=255)  # Rating of the movie (e.g., "UNRATED", "PG-13")
        awards = models.JSONField()  # Information about the awards won by the movie
        lastupdated = models.CharField(max_length=255)  # Date and time of the last update to the movie information
        year = models.IntegerField()  # Year of the movie release
        imdb = models.JSONField()  # IMDb-related information, including rating, votes, and ID
        type = models.CharField(max_length=255)  # Type of content (e.g., "movie", "series")
        tomatoes = models.JSONField()  # Information related to the movie's rating on Rotten Tomatoes

        def __str__(self):
            return self.title

    class Theater(models.Model):
        # Theater document fields
        theaterId = models.IntegerField()  # Identifier for the theater
        location = models.JSONField()  # Location information of the theater, including address and geographic coordinates

        def __str__(self):
            return f"Theater ID: {self.theaterId}"

    class User(models.Model):
        # User document fields
        name = models.CharField(max_length=255)  # Name of the user
        email = models.EmailField()  # Email address of the user
        password = models.CharField(max_length=255)  # Encrypted password of the user

        def __str__(self):
            return self.name
   ```

3. Configure Database Connections:
   - In the Django project's settings.py file, specify the necessary database settings for both MySQL and MongoDB.
   ```python
       DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mflix',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        },
        'mongodb': {
            'ENGINE': 'djongo',
            'NAME': 'mflix',
            'CLIENT': {
                'host': 'mongodb://localhost:27017/',
                'username': '',
                'password': '',
                'authSource': '',
                'authMechanism': '',
                'connectTimeoutMS': 5000,
                'serverSelectionTimeoutMS': 5000,
            }
        }
    }
   ```

4. Create Migration Files and Apply Migrations:
   - Generate migration files based on the Django models to create the corresponding database tables or collections.
   ```bash
   python manage.py makemigrations AAapp
   ```
   - Use Django's migration commands to apply the migrations and create the necessary database schema.
   ```bash
   python manage.py migrate app_name --database=default
   python manage.py migrate app_name --database=mongodb
   ```

5. Load JSON Data into Databases:
   - Read the JSON dataset files and parse their contents using Python's JSON library.
   ```python
   import json

   with open('comments.json') as f:
       comments_data = json.load(f)

   with open('movies.json') as f:
       movies_data = json.load(f)

   with open('theaters.json') as f:
       theaters_data = json.load(f)

   with open('users.json') as f:
       users_data = json.load(f)
   ```
   - Map the parsed JSON data to the Django models' fields and create model instances.
   ```python
   for comment_data in comments_data:
       movie_id = comment_data['movie_id']
       movie = Movie.objects.get(id=movie_id)
       Comment.objects.create(
           name=comment_data['name'],
           email=comment_data['email'],
           movie=movie,
           text=comment_data['text'],
           date=comment_data['date']
       )

   for movie_data in movies_data:
       Movie.objects.create(
           plot=movie_data['plot'],
           runtime=movie_data['runtime'],
           num_mflix_comments=movie_data['num_mflix_comments'],
           title=movie_data['title'],
           fullplot=movie_data['fullplot'],
           released=movie_data['released'],
           rated=movie_data['rated'],
           awards=movie_data['awards'],
           lastupdated=movie_data['lastupdated'],
           year=movie_data['year'],
           imdb=movie_data['imdb'],
           type=movie_data['type'],
           tomatoes=movie_data['tomatoes']
       )

   for theater_data in theaters_data:
       Theater.objects.create(
           theaterId=theater_data['theaterId'],
           address_street1=theater_data['address_street1'],
           address_city=theater_data['address_city'],
           address_state=theater_data['address_state'],
           address_zipcode=theater_data['address_zipcode'],
           geo_type=theater_data['geo_type'],
           geo_coordinates=theater_data['geo_coordinates']
       )

   for user_data in users_data:
       User.objects.create(
           name=user_data['name'],
           email=user_data['email'],
           password=user_data['password']
       )
   ```
6. Retrieve Data from Databases:

   - Retrieve all comments from the MySQL database:
   ```python
   all_comments = Comment.objects.all()
   for comment in all_comments:
       print(comment.text)
   ```

   - Retrieve comments associated with a specific movie from the MySQL database:
   ```python
   movie_id = 1  # Filter Movie id 1
   movie_comments = Comment.objects.filter(movie_id=movie_id)
   for comment in movie_comments:
       print(comment.text)
   ```

   - Retrieve all movies from the MongoDB database:
   ```python
   all_movies = Movie.objects.using('mongodb').all()
   for movie in all_movies:
       print(movie.title)
   ```

   - Retrieve movies released in a specific year from the MongoDB database:
   ```python
   year = 2022  # Filter year
   year_movies = Movie.objects.using('mongodb').filter(year=year)
   for movie in year_movies:
       print(movie.title)
   ```

   - Retrieve theaters from the MySQL database:
   ```python
   all_theaters = Theater.objects.all()
   for theater in all_theaters:
       print(theater.theaterId)
   ```

   - Retrieve users from the MySQL database:
   ```python
   all_users = User.objects.all()
   for user in all_users:
       print(user.name)
   ```


## Question 1 (b)
- **Client-Side**: Users access the portal through web browsers. They can communicate through the gateway by sending forms, pressing buttons, or making choices. Users can specify the parameters for data analysis by filling out a form, clicking a button to request a chart, or basing a decision on the data visualisation.

- **Django Web Server**: The Django web server offers the backend for the portal. It is implemented using the Django web framework, which provides a number of tools and frameworks for creating web applications. The web server receives and processes user requests. It controls routing, which entails deciding which view or function should respond to each request based on the URL. To ensure that only authenticated users can access particular parts of the website or carry out specific actions, the Django web server also manages authentication and permission. It interacts with databases to retrieve and save data as needed.

- **JSON Dataset**: The JSON dataset contains the data that is used for analysis and visualisation in the portal. It is typically saved in JSON file format, a compact and readable data interchange format. The Django web server reads the JSON dataset and processes it for analysis and visualisation. The JSON dataset provides the data that the Django web server needs, which it then transforms and presents in an understandable way.

- **MySQL Database**: Django connects to the MySQL database by using the appropriate database settings specified in the project's settings file ('settings.py'). The data schema of the MySQL database is specified by Django models. They describe the tables, fields, and connections in the database. The Django ORM (Object-Relational Mapping) offers a user interface for interacting with the MySQL database. It enables developers to create, retrieve, update, and delete data using Python code rather than writing direct SQL queries.

- **MongoDB Database**: Django can connect to MongoDB using third-party libraries like Djongo or MongoEngine, which provide integration with Django's ORM. Django models can be created for a MongoDB database just like they can for a MySQL database. The models define the data schema and correspond to MongoDB collections. Python code can be used by developers to carry out CRUD operations on the MongoDB database with the aid of third-party libraries and the Django ORM.

- **Django Models**: The Django models define the data structures for the MySQL and MongoDB databases as a python class. Each attribute in the models for the MySQL database maps to a column in a table, making them into tables for the database. In the MongoDB database, models are transformed into collections, where each instance of the model is transformed into a document in the collection. Django models specify the fields, relationships, and behaviours of the data. They also provide tools for data manipulation and query.

- **Data processing**: The fields listed in the Django models are mapped to the parsed JSON data from the dataset. The Django web server processes the data before saving it with the ORM in the proper database (MySQL or MongoDB). Executing data retrieval queries is guided by user requests or dashboard specifications. The Django ORM transforms these queries into database-specific queries (SQL or MongoDB queries), which then retrieve the necessary data.

- **Dashboard Visualisation**: Data that has been retrieved from the databases is processed and transformed for visualisation purposes. Charts can be made interactive and visually appealing by using libraries like Plotly or Highcharts. With the help of HTML templates and JavaScript code, the charts are displayed on the dashboard.



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


