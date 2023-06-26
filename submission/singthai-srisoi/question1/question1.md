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
        name = models.CharField(max_length=255) # name of the user
        email = models.EmailField()             # email of the user
        movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)
        text = models.TextField()               # comment text
        date = models.DateTimeField()           # date of the comment

        def __str__(self):
            return self.text

    class Movie(models.Model):
        plot = models.TextField()               # plot of the movie
        genres = models.ManyToManyField('Genre')# array of genres of the movie
        runtime = models.IntegerField()         # runtime of the movie
        cast = models.ManyToManyField('Actor')  # array of actors in the members
        num_mflix_comments = models.IntegerField() # number of comments
        title = models.CharField(max_length=255)# title of the movie
        fullplot = models.TextField()           # description or plot summary of the movie
        countries = models.ManyToManyField('Country')   # array of countries where the movie was shot
        released = models.DateField()           # release date of the movie
        directors = models.ManyToManyField('Director')  # array of directors
        rated = models.CharField(max_length=255)# rating of the movie
        awards = models.JSONField()             # array of awards that the movie won
        lastupdated = models.CharField(max_length=255)  # date when the movie was last updated
        year = models.IntegerField()            # year when the movie was released
        imdb = models.JSONField()               # array of imdb information
        type = models.CharField(max_length=255) # type of the content
        tomatoes = models.JSONField()           # Information related to the movie's rating on Rotten Tomatoes.

        def __str__(self):
            return self.title

    class Theater(models.Model):
        theaterId = models.IntegerField()       # theater id
        address_street1 = models.CharField(max_length=255)  # street address
        address_city = models.CharField(max_length=255)     # city
        address_state = models.CharField(max_length=255)    # state
        address_zipcode = models.CharField(max_length=10)   # zipcode
        geo_type = models.CharField(max_length=255)         # type of the geo location
        geo_coordinates = models.JSONField()                # geo coordinates

        def __str__(self):
            return f"Theater {self.theaterId}"

    class User(models.Model):
        name = models.CharField(max_length=255) # name of the user
        email = models.EmailField()             # email of the user
        password = models.CharField(max_length=255) # password of the user

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

6. Implement Data Retrieval:
   - Utilize Django's ORM to retrieve data from both MySQL and MongoDB databases.
   ```python
   mysql_comments = Comment.objects.using('default').all()
   mysql_movies = Movie.objects.using('default').all()
   mysql_theaters = Theater.objects.using('default').all()
   mysql_users = User.objects.using('default').all()

   mongodb_comments = Comment.objects.using('mongodb').all()
   mongodb_movies = Movie.objects.using('mongodb').all()
   mongodb_theaters = Theater.objects.using('mongodb').all()
   mongodb_users = User.objects.using('mongodb').all()
   ```
   - Write queries or use Django's filter, aggregate, and related methods to fetch specific data based on requirements.
   
   ```python
   # Filter data based on requirements
   mysql_filtered_comments = Comment.objects.using('default').filter(movie__title='Some Movie')
   mongodb_filtered_movies = Movie.objects.using('mongodb').filter(year__gte=2000)

   # Aggregate data based on requirements
   mysql_aggregated_comments = Comment.objects.using('default').aggregate(models.Count('id'), models.Sum('num_mflix_comments'))
   mongodb_aggregated_movies = Movie.objects.using('mongodb').aggregate(models.Count('id'), models.Sum('num_mflix_comments'))
   ```
   - Transform the retrieved data into the desired format for further processing or rendering.
   ```python
   # Transform data into the desired format
   mysql_comments_list = list(mysql_comments.values())
   mysql_movies_list = list(mysql_movies.values())
   mysql_theaters_list = list(mysql_theaters.values())
   mysql_users_list = list(mysql_users.values())

   mongodb_comments_list = list(mongodb_comments.values())
   mongodb_movies_list = list(mongodb_movies.values())
   mongodb_theaters_list = list(mongodb_theaters.values())
   mongodb_users_list = list(mongodb_users.values())
   ```
   
   - You can also use Django's serializer classes to convert the retrieved data into JSON or other formats.
   
   ```python
   from django.core import serializers

   # Serialize data to JSON format
   mysql_comments_json = serializers.serialize('json', mysql_comments)
   mongodb_comments_json = serializers.serialize('json', mongodb_comments)
   ```

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


