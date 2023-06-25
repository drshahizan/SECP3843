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

1. Locate to your project file and create a virtual environment.
```python
py -m venv env
env\Scripts\activate
```

2. Once you’ve created and activated your Python virtual environment, you can install Django into this dedicated development workspace using `pip install django`. <br>

3. After you’ve successfully installed Django, you’re ready to create the scaffolding for your new web application. With your virtual environment set up and activated and Django installed, you can now create a project using `django-admin startproject AA_Goo`

4. For this project, we need to create an app contain the functionality of providing users with a platform for viewing data and executing dashboard visualizations based on JSON-provided data. You can execute the startapp command through the manage.py file using `py manage.py startapp stories` to generates a default folder structure for a Django app.

### 2. Configuring Django Settings
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


## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


