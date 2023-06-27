<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: ADAM WAFII BIN AZUAR

#### Matric No.: A20EC0003

#### Dataset: MFLIX DATASET

## Question 1 (a)

Server Used:
<ul>
	<li>Django Web Server</li>
	<li>MySQL Database Server</li>
	<li>JSON Dataset Server</li>
	<li>MongoDB Database Server</li>
	<li>Integration Script Server</li>
</ul>


1. Set up the virtual environment and activate the virtual environment
   
   ``` py -3 -m venv .venv ```
   
   ```.venv\scripts\activate ```

2. Install Django and the required packages

   ``` pip install Django ```
   
   ``` pip install djongo ```

   ``` pip install pytz ```

   ``` pip install mysqlclient ```

4. Create a Django Project & App

   ``` django-admin startproject Mflix ```
   
   ``` django-admin startapp Mflixx ```

6. Configure the Database and Django Settings. Update the databases setting to configure the MySQL and MongoDB connections.

```
     DATABASES = {
        'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'aa',
		'USER': 'root',
		'HOST':'localhost',
		'PORT':'3306',
	    },

        'mongodb': {
            'ENGINE': 'djongo',
            'NAME': 'mflix',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb+srv://jokeryde:adamkaya@jokeryde.cnn7sr4.mongodb.net/'
            }  
        }
      }
```

  6. Define Models inside the `models.py`. These models will represent as tables inside MongoDB and MySQL.
     ```
        from django.db import models
        class Movies(models.Model):
             _id = models.CharField(max_length=100)
             title = models.CharField(max_length=100)
             plot = models.TextField()
             genres = models.CharField(max_length=100)
             runtime = models.IntegerField()
             cast = models.CharField(max_length=100)
             num_mflix_comments = models.IntegerField()
             fullplot = models.TextField()
             countries = models.CharField(max_length=100)
             released = models.CharField(max_length=100)
             directors = models.CharField(max_length=100)
             rated = models.CharField(max_length=100)
             awards = models.JSONField()
             lastupdated = models.CharField(max_length=100)
             year = models.IntegerField()
             imdb = models.CharField(max_length=100)
             type = models.CharField(max_length=100)
             tomatoes = models.JSONField()
          
         class Comment(models.Model):
             _id = models.CharField(max_length=100)
             name = models.CharField(max_length=100)
             email = models.CharField(max_length=100)
             movie_id = models.CharField(max_length=100)
             text = models.TextField()
             date = models.CharField(max_length=100)
      
         class Users(models.Model):
             _id = models.CharField(max_length=100)
             name = models.CharField(max_length=100)
             email = models.CharField(max_length=100)
             password = models.CharField(max_length=100)
      
         class Theaters(models.Model):
             _id = models.CharField(max_length=100)
             theaterId = models.CharField(max_length=100)
             location = models.JSONField()
      ```

7. Next up, generate Django migrations and apply the migrations to both MySQL and MongoDB
   ``` python manage.py makemigrations ```

   ``` python manage.py migrate ```

8. Import the JSON datasets using Django's ORM to save the data to both databases. Create a python file called 'load_data.py' and write the codes as            following:
   ```
      import os
      import json
      from django.core.management.base import BaseCommand
      from Mflixx.models import Movies, Comment, Users, Theaters
      
      class Command(BaseCommand):
          help = 'Load data from JSON file to database'
      
          def handle(self, *args, **kwargs):
              print(os.getcwd())
              json_file = open('movies.json')
      
              with open(json_file.name) as f:
                  data = json.load(f)
      
              for i in data:
                  movie_data = {
                      '_id': i['_id'],
                      'title': i['title'],
                      'plot': i['plot'],
                      'genres': i['genres'],
                      'runtime': i['runtime'],
                      'cast': i['cast'],
                      'num_mflix_comments': i['num_mflix_comments'],
                      'fullplot': i['fullplot'],
                      'countries': i['countries'],
                      'released': i['released'],
                      'directors': i['directors'],
                      'rated': i['rated'],
                      'awards': i['awards'],
                      'lastupdated': i['lastupdated'],
                      'year': i['year'],
                      'imdb': i['imdb'],
                      'type': i['type'],
                      'tomatoes': i['tomatoes']
                  }
      
                  movie = Movies(**movie_data)
                  movie.save()
      
                  comment_data = {
                      '_id': i['_id'],
                      'name': i['name'],
                      'email': i['email'],
                      'movie_id': i['movie_id'],
                      'text': i['text'],
                      'date': i['date']
                  }
      
                  comment = Comment(**comment_data)
                  comment.save()
      
                  user_data = {
                      '_id': i['_id'],
                      'name': i['name'],
                      'email': i['email'],
                      'password': i['password']
                  }
      
                  user = Users(**user_data)
                  user.save()
      
                  theater_data = {
                      '_id': i['_id'],
                      'theaterId': i['theaterId'],
                      'location': i['location']
                  }
      
                  theater = Theaters(**theater_data)
                  theater.save()
      
              self.stdout.write(self.style.SUCCESS('Successfully loaded data from JSON file to database'))
   ```

   9. Run the following command to load the data into the database
      ```
         python manage.py load_data

      ```

   10. Next, by using the Django ORM to interact with the database, i can query the data from the database using Django models:
       ```
          from your_app.models import Movies
          movies = Movies.objects.all()      
          movie = Movies.objects.get(title='Spiderman')       
          genre = 'Action'
          movies = Movies.objects.filter(genres__contains=genre)       
          year = 2007
          movies = Movies.objects.filter(released__year=year)
          director = 'Sam Raimi'
          movies = Movies.objects.filter(directors__contains=director)
          min_rating = 8.0
          movies = Movies.objects.filter(imdb__rating__gte=min_rating)
          user_id = 1
          movies = Movies.objects.filter(comment__user_id=user_id)
          for movie in movies:
             print(movie.title)
            
          comments = movie.comment_set.all()  
          user = comment.user  
          theater = movie.theater  
      ```

## Question 1 (b)

 <img src="https://github.com/drshahizan/SECP3843/blob/ca87b2313a9579a7de089133b55c080755f239bc/submission/Jokeryde/question1/files/images/Question%201.jpg">

1. User Interface (UI):
The UI is the visual interface that allows users to interact with the application. It facilitates communication between users and the web server by sending HTTP/HTTPS requests.

2. Web Server (Django):
The web server acts as the central component of the application. It receives incoming HTTP/HTTPS requests from the UI and handles them. The web server consists of various layers, including the application layer, models layer, visualization module, and JSON dataset.

3. Application Layer:
The application layer comprises forms, templates, and view functions responsible for processing requests and generating responses. It interacts with the models layer to retrieve data and present it to the user.

4. Models Layer:
The models layer represents the database of the application. It consists of two databases, namely MySQL DB and MongoDB. Django's ORM is used to store and retrieve data from these databases. The bidirectional arrows indicate that data synchronization can occur between the models layer and JSON datasets, ensuring consistent and updated data.

5. JSON Datasets:
The JSON datasets contain the movies, comments, users and theaters dataset used for analysis in the application. These datasets serve as a source of data for the application's functionality.

6. Data Synchronization:
Data synchronization involves keeping the data consistent and up to date between the models layer (databases) and the JSON datasets. This ensures that any changes made in either storage option are reflected in the other.

7. Data Presentation:
Data presentation involves the generation of visualizations and the display of data to the user. This component includes the dashboard and visualization modules, which utilize the retrieved data to present meaningful insights to the user.
 


## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
