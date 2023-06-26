<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Muhammad Dinie Hazim Bin Azali
#### Matric No.: A20EC0084
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 1 (a)
#### 5 servers used in this project:

```1. Web Server```

```2. Django Application Server```

```3. MySQL Database Server```

```4. MongoDB Database Server```

```5. JSON Dataset Server```

Follow these steps to integrate Django with the JSON dataset and ensure efficient data storage and retrieval from both MySQL and MongDB databases:

#### Install Django:

1. Install and configure Django.
   - Ensure Python is installed on the server or download the latest version from the official [Python website](https://www.python.org/downloads/)
   - Open a terminal or command prompt.
   - Install Django using the command: `pip install Django`.
     ![image](https://github.com/drshahizan/SECP3843/blob/45c2d3cb9f768daea02df72426c9530b0ced805c/submission/DinieHazim/question%201/files/images/248708969-bf530713-0a4f-408f-a293-4969383b80c9.png)

2. Create Django project
   - Choose a directory for your Django project.
   - Navigate to the chosen directory in the terminal or command prompt.
   - Run the command: `django-admin startproject stories`.
     ![image](https://github.com/drshahizan/SECP3843/blob/d11ebdb1c7df59cb241c3b581b41e62201c9f55c/submission/DinieHazim/question%201/files/images/248711447-86eb15d2-6bdd-48d2-912a-f1316bcd0af8.png)

3. Create Django app
   - Create a new app inside the Django project created before.
   - The app will handle the integration of the dataset and databases.
   - Run the command: `python manage.py startapp storiesDataset`.
     ![image](https://github.com/drshahizan/SECP3843/blob/862e377bf91e814cf13f895dcb95971a067663aa/submission/DinieHazim/question%201/files/images/248779811-324bc2db-a63e-494e-8496-9d28afc3fcb9.png)

4. Install packages
   - Install two necessary packages by using the following command: `pip install django mysqlclient pymongo` and `pip install djongo`.
     ![image](https://github.com/drshahizan/SECP3843/blob/497402d5ed53342e70a0e8bdfb2b43c1f6e3e851/submission/DinieHazim/question%201/files/images/248794413-535309a3-a5af-4678-8a67-cf089a9b6326.png)

#### Configuring Django database settings:

1. Define the database settings for both MySQL and MongoDB.
   - Open `settings.py` file in project folder.
   - Define the database by using this code.
     ```python
          DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'stories',
             'USER': 'root',
             'PASSWORD': '',
             'HOST': 'localhost',
             'PORT': 3306,
         },
         'mongodb': {
             'ENGINE': 'djongo',
             'ENFORCE_SCHEMA': False,
             'NAME': 'Stories',
             'CLIENT': {
                 'host': 'mongodb+srv://DinieHazim:diniehazim@cluster0.nd5oq2m.mongodb.net/'
             }
         }
         }
     ```

#### Configuring Django models:

1. Models need to be defined because it represent the structure of the data.
2. Open models.py file and define model based on JSON dataset.
   ```python
      from django.db import models

      # Create your models here.
      class Story(models.Model):
          _id = models.CharField(max_length=255)
          href = models.URLField()
          title = models.CharField(max_length=255)
          comments = models.IntegerField()
          container_name = models.CharField(max_length=255)
          container_short_name = models.CharField(max_length=255)
          submit_date = models.DateTimeField()
          topic_name = models.CharField(max_length=255)
          topic_short_name = models.CharField(max_length=255)
          promote_date = models.DateTimeField()
          id = models.CharField(max_length=255)
          media = models.CharField(max_length=255)
          diggs = models.IntegerField()
          description = models.TextField()
          link = models.URLField()
          user_name = models.CharField(max_length=255)
          user_registered = models.DateTimeField()
          user_fullname = models.CharField(max_length=255)
          user_icon = models.URLField()
          user_profileviews = models.IntegerField()
          status = models.CharField(max_length=255)
          short_url = models.URLField()
          short_url_view_count = models.IntegerField()
      
          def __str__(self):
              return self.title
   ```

#### Migrate the database:

1. Open terminal or command prompt.
2. Run the `python manage.py makemigrations` and `python manage.py migrate`.
   ![image](https://github.com/drshahizan/SECP3843/assets/120595244/46baad24-37b1-4d0a-8989-04a6e02d8eb1)


#### Import JSON dataset:

1. Import the JSON dataset by using Django's ORM.
2. Create a python file `import_data.py` and insert this code.
   ```python
      import json
      from storiesDataset.models import Story

      # Load the JSON data from file
      with open('stories.json', 'r') as f:
          data = json.load(f)
      
      # Iterate over the JSON objects and create Story instances
      for item in data:
          story = Story(
              _id=item['_id'],
              href=item['href'],
              title=item['title'],
              comments=item['comments'],
              container_name=item['container']['name'],
              container_short_name=item['container']['short_name'],
              submit_date=item['submit_date'],
              topic_name=item['topic']['name'],
              topic_short_name=item['topic']['short_name'],
              promote_date=item['promote_date'],
              story_id=item['id'],
              media=item['media'],
              diggs=item['diggs'],
              description=item['description'],
              link=item['link'],
              user_name=item['user']['name'],
              user_registered=item['user']['registered'],
              user_fullname=item['user']['fullname'],
              user_icon=item['user']['icon'],
              user_profileviews=item['user']['profileviews'],
              status=item['status'],
              short_url=item['shorturl'][0]['short_url'],
              short_url_view_count=item['shorturl'][0]['view_count']
          )
          story.save()
   ```
   
3. Run `python manage.py import_data`

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
