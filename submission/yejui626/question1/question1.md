<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: GOO YE JUI
#### Matric No.: A20EC0191
#### Dataset: Stories Dataset

## Question 1 (a)
### Explanation of steps required to integrate Django with JSON, ensuring efficient data storage and retrieval from both MySQL and MongoDB databases.
These are the steps for implementing a configuration using the servers used in this project. It is to ensure seamless integration between the Django web framework, a JSON dataset provided in this project, and the MySQL and MongoDB databases.

### 1. Steps to setup Django server including the project and application folder.
First, we are using the Django web framework as the base for building the portal. Hence, we need to setup the Django server.

1. Locate to the project file and create a virtual environment.
```python
py -m venv env
env\Scripts\activate
```

2. Once you’ve created and activated your Python virtual environment, you can install Django into this dedicated development workspace using `pip install django`. <br>

3. After you’ve successfully installed Django, you’re ready to create the scaffolding for your new web application. With your virtual environment set up and activated and Django installed, you can now create a project using `django-admin startproject AA_Goo`

4. For this project, we need to create an app contain the functionality of providing users with a platform for viewing data and executing dashboard visualizations based on JSON-provided data. You can execute the startapp command through the manage.py file using `py manage.py startapp stories` to generates a default folder structure for a Django app.

### 2. Configuring Django database settings
   1. Open the Django project's `settings.py` file.
   2. Define the database settings for both MySQL and MongoDB.
   ``` python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'aa',
                'USER': 'root',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': 8000,
            },
            'mongodb': {
                'ENGINE': 'djongo',
                'ENFORCE_SCHEMA': False,
                'NAME': 'AA',
                'CLIENT': {
                    'host': 'localhost:27017',
                    'port': 27017,
                    'username': '',
                    'password': '',
                }
            }
        }
   ```
   3. Install database connectors ("mysqlclient" and "djongo" library) for MySQL and MongoDB using 
   ``` python
    pip install mysqlclient
    pip install djongo
   ```   
### 2. Configuring Django models
To allow seamless integration between Django and the databases, we need to define a Django models that represent the structure and fields of the JSON dataset.

   1. Open the stories app's `models.py` file.
   2. Define Django models that represent the structure and fields of the JSON dataset according to the data dictionary.
   ``` python
        from django.db import models


        class Container(models.Model):
            _DATABASE = "mongodb"
            name = models.CharField(max_length=255)
            short_name = models.CharField(max_length=255)


        class Topic(models.Model):
            _DATABASE = "mongodb"
            name = models.CharField(max_length=255)
            short_name = models.CharField(max_length=255)


        class User(models.Model):
            _DATABASE = "mongodb"
            name = models.CharField(max_length=255)
            registered = models.DateTimeField()
            fullname = models.CharField(max_length=255)
            icon = models.URLField()
            profileviews = models.IntegerField()


        class ShortURL(models.Model):
            _DATABASE = "mongodb"
            short_url = models.URLField()
            view_count = models.IntegerField()


        class Story(models.Model):
            _DATABASE = "mongodb"
            _id = models.CharField(max_length=255, unique=True)
            href = models.URLField()
            title = models.CharField(max_length=255)
            comments = models.IntegerField()
            container = models.ForeignKey(Container, on_delete=models.CASCADE)
            submit_date = models.DateTimeField()
            topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
            promote_date = models.DateTimeField()
            id = models.CharField(max_length=255)
            media = models.CharField(max_length=255)
            diggs = models.IntegerField()
            description = models.TextField()
            link = models.URLField()
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            status = models.CharField(max_length=255)
            shorturl = models.ManyToManyField(ShortURL)
   ```
### 3. Configuring Django Database Routing
To allow Django to support multiple databases, we require a database routing to specify which database to use for each model. Routing rules to route specific models to MySQL or MongoDB based on their requirements is set up under this file. For example, the models `[Container, Topic, User, ShortURL, Story]` that we have just created is routed to MongoDB.

```python
class DatabaseRouter:
    def db_for_read(self, model, **hints):
        return getattr(model, "_DATABASE", "default")

    def db_for_write(self, model, **hints):
        return getattr(model, "_DATABASE", "default")

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
        db_list = ('default')
        return obj1._state.db in db_list and obj2._state.db in db_list

    def allow_migrate(self, db, model):
        """
        All non-auth models end up in this pool.
        """
        return True  
```


## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


