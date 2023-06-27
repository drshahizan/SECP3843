<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Amirah Raihanah binti Abdul Rahim
#### Matric No.: A20EC0182
#### Dataset: Tweets

## Question 1 (a)
To implement a configuration using five servers in this project, below are the breakdowns of each server :
1. `Web Server`<br>
 The web server that will be used is Apache and the purpose of this server is to handle HTTP requests from clients and send back HTTP response. This server will handle static files such as JavaScript, HTML, CSS or any media files like images. 
2.  `MySQL Database Server`<br>
 This server is responsible to host the MYSQL database. The installation and configuration of MYSQL will be done in this server. All operations such as storing and retrieving data from MYSQL will interact with this server.
3.  `MongoDB Server`<br>
   Since the project require MongoDB database, a dedicated server is use to host MongoDB database. The installation and configuration of MongoDB will be done in this server. All operations such as storing and retrieving data from MongoDB will interact with this server.
4.  `Django Server`<br>
   The main purpose of this server is to execute the python-based Django web application framework. This server will handle the logic of our web application that includes interacting with database and processing requests.
5.  `Load Balancer`<br>
    Load balancer server is important to maintain and handle the traffic between multiple instances of web server and Django server. This server would distribute traffic between the other servers, which can improve performance and availability.

<br>
Next, here are the steps required to integrate Django with the JSON dataset that are stored in both  MYSQL and MongoDB database.
<br>
<br>
Figure below show the flow of Django with the JSON dataset integration : 
<img width="655" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question1/files/images/integration-flow.png">

### 1. Install Django
Begin with installing Django and other packages required such as pymongo. There are many ways of doing so and one of it is by installing packages using pip. <br>
For example : 
```
pip install Django
pip install pymongo
pip install mysqlclient
pip install djongo
```
### 2. Setup Project in Django
Next, create a project in Django. Open a terminal and navigate to the directory you want to store the project. Then, run the followwing command and your project file will be created :
```
django-admin startproject tweetsAA
```
<br>

Then, create an app in the project file and the directory should be in manage.py. Run the following command :
```
python manage.py startapp tweetsdataAA
```
Lastly, in settings.py register the app created above.
<br>
Before moving on to the next step, we need to configure our databases server.
- MySQL database server
  - i) Firstly, open your XAMPP controller
  - ii) Click start on both Apache and phpmyadmin
  <br> <img width="655" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question1/files/images/integration-flow.png">
  - iii) Click on Admin on phpmyadmin
  - iv) You will be redirected to the page and create a new database as below :
   <br> <img width="655" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question1/files/images/integration-flow.png">

- MongoDB database server
  - i) Open MongodbCompass.
  - ii) Connect to the database.
 <br>  <img width="655" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question1/files/images/integration-flow.png">
  - iii) Create a new database and insert your database name with its collection name.
 <br> <img width="655" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question1/files/images/integration-flow.png">
  - iv) Click on create database.
  
### 3. Define data model in Django
Moving on, in the Django app created, navigate to models.py. This is where you define your models based on the JSON data you are using. Below is the example on defining tweets JSON data model in django.
```
from django.db import models

    class Tweets(models.Model):
        _id = models.CharField(max_length=255)
        text = models.TextField()
        in_reply_to_status_id = models.CharField(max_length=255, null=True)
        retweet_count = models.IntegerField(null=True)
        contributors = models.CharField(max_length=255, null=True)
        created_at = models.DateTimeField()
        geo = models.CharField(max_length=255, null=True)
        source = models.CharField(max_length=255)
        coordinates = models.CharField(max_length=255, null=True)
        truncated = models.BooleanField()
        entities = models.JSONField()
        retweeted = models.BooleanField()
        place = models.CharField(max_length=255, null=True)
        user = models.JSONField()
        favorited = models.BooleanField()
        in_reply_to_user_id = models.CharField(max_length=255, null=True)
        id = models.CharField(max_length=255, unique=True)
        in_reply_to_screen_name = models.CharField(max_length=255, null=True)
      

```
### 4. Configure Django database connections
Next, configure your database connection to connect both MySQL and MongoDB. This is where we use our installed packages which are pymongo, djongo and mysqlclient. In your Django project file, navigate to settings.py and change the configuration as follows:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<MySQL_dbname>',
        'USER': '<MySQL_username>',
        'PASSWORD': '<MySQL_password>',
        'HOST': '<MySQL_host>',
        'PORT': '<MySQL_port>',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'tweetsAA',
        'CLIENT': {
            'host': '<mongodb_host>'',
            'username': '<mongodb_user>'',
            'password': '<mongodb_password>,
            'authMechanism': '<mongodb_authmechanism',
            'authSource': '<mongodb_authsource>',
        },
    },
}
      

```

### 5. Run Django database migration
- mySQL<br>
In  Django, to manage database schema changes we need to use migration. Firstly create an initial migrations that will analyze the models created above and create migration files using the command below :
```
python manage.py makemigrations
```
Next, apply the migration to create tables in mySQL database.
```
python manage.py migrate
```
- MongoDB<br>
To apply migration to your MongoDB run the following command :
```
python manage.py migrate --database=mongodb
```
### 6. Import data into both databases
After succesfully migrate to both databases, now we will import our JSON data using Django management command to create instances of our model with Python Script. 
```
import json
from django.core.management.base import BaseCommand
from tweetsdataAA.models import Tweets

class Command(BaseCommand):
    help = 'Parse JSON dataset and create instances of Tweets model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to JSON dataset file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        
        with open(json_file) as file:
            data = json.load(file)
        
        tweets = []
        
        for item in data:
            tweet = Tweets(
                _id=item['_id'],
                text=item['text'],
                in_reply_to_status_id=item['in_reply_to_status_id'],
                retweet_count=item['retweet_count'],
                contributors=item['contributors'],
                created_at=item['created_at'],
                geo=item['geo'],
                source=item['source'],
                coordinates=item['coordinates'],
                truncated=item['truncated'],
                entities=item['entities'],
                retweeted=item['retweeted'],
                place=item['place'],
                user=item['user'],
                favorited=item['favorited'],
                in_reply_to_user_id=item['in_reply_to_user_id'],
                id=item['id'],
                in_reply_to_screen_name=item['in_reply_to_screen_name']
            )
            tweets.append(tweet)

        Tweets.objects.bulk_create(tweets)

        self.stdout.write(self.style.SUCCESS('Successfully created instances of Tweets model.'))

```
Next, run it using the command below :
```
python manage.py parse_json_dataset AA/tweets.json

```
### 7. Define query methods
Then, write your query to retrive or manipulate from both databases. For instance, I want to retrieve all data from both databases using the query below :
```
from tweetsdataAA.models import Tweets, TweetsMongo

# Retrieve tweets from MySQL database
def get_tweets_from_mysql():
    return Tweets.objects.all()

# Retrieve tweets from MongoDB database
def get_tweets_from_mongodb():
    return TweetsMongo.objects.all()

# Retrieve tweets from both databases
def get_all_tweets():
    mysql_tweets = get_tweets_from_mysql()
    mongodb_tweets = get_tweets_from_mongodb()
    all_tweets = list(mysql_tweets) + list(mongodb_tweets)
    return all_tweets

```
### 8. Implement database router
Next, implementing database router is important if you want to to distribute queries to different databases based on specific logic. The database router ensure  handling of the database operations in your Django application because you can specify which database you want to use for different operations.
### 9. Test and debug
Final step, to ensure a succesful integration you may test and debug your Django application by creating test cases and analyze the result. If there are no problems encountered, then you have succesfully integrate your Django application with JSON data using mySQL and MongoDB databases.

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


