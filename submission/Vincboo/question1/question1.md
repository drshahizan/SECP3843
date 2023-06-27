![image](https://github.com/drshahizan/SECP3843/assets/120615951/45885157-677f-434a-98d1-b274d3f72876)<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Vincent Boo Ee Khai
#### Matric No.: A20EC0231
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 1 (a)
The following steps outline the process of setting up a configuration to seamlessly integrate Django with a JSON dataset, allowing for effective storage and retrieval of data from both MySQL and MongoDB databases. The primary components involved in this configuration are a web server, a MySQL database server, and a MongoDB database server.

### 1. Install Django
To install Django using `pip` on a terminal or command prompt, then execute the provided command:
```
pip install django
```
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/450f9692-82d7-4369-bfd9-839ad30ab0d5"></img>

### 2. Set up Django Server
1. Create a Virtual Environment
```
py -m venv myenv
```
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/487a673a-93b1-47cc-96ca-3586f83d06a7"></img>

2. Activate the virtual environment
After the virtual environment was created, activate it by running the code:
```
myenv\Scripts\activate
```
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/dd99ae8d-bd7b-4275-a612-ca84e6335554"></img>

3. Create new Django project with the following code
After it was activated, we proceed to create a project filewith the provided code:
```
django-admin startproject AA_stories
```

4. Create new App in the created project
Then, app is create in the same directory inside the project file.
```
py manage.py startapp stories
```

### 3. Install All Needed Package:
Given the requirement to integrate Django with both MySQL and MongoDB databases, it will be necessary to install multiple packages to facilitate this integration.
1. MySQL
```
pip install mysqlclient
```
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/3680612f-d051-47c8-8ffe-9b424f2269c9"></img>

2. MongoDB
```
pip install pymongo
```
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/5dc3e3f0-03e4-4978-a930-cdf3448a8ee3"></img>

3. Djongo
```
pip install djongo
```
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/7b590887-4f7e-4e08-bffc-1b5aa924d6c5"></img>

4. Python Library for timezone support:
```
pip install pytz
```
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/228e7502-4807-4298-8753-62a482cb0669"></img>

### 4. Confirgure Setting for Django Database
1. The code provided below needed to place in the `setting.py` of the project for define database:
```
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
        'NAME': 'AA',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
            'port': 27017,
            'username': '',
            'password': '',
        }
    }
}
```

2. Then, we create a `.py` file named 'dbrouter.py' to route the database.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/17f0087f-e949-4b02-97f8-9237f22afc31"></img>

3. Then, we will also need to define the file.
```
DATABASE_APPS_MAPPING = {
    'contenttypes': 'default',
    'auth': 'default',
    'admin': 'default',
    'sessions': 'default',
    'messages': 'default',
    'staticfiles': 'default',
    'user': 'default',
    'stories': 'mongodb',
}

DBROUTERS = ['AA_stories.dbrouter.DbRouter']
```


### 5. Migrate DAtabase
1. First of all we will need to tell Django to create the database tables that you defined in your application with using `py manage.py makemigrations'.

2. For MySQL
We uses `py manage.py migrate` to migrate it into MySQL.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/e50d3c22-5eb0-4caa-8dfb-f8674358f425"></img>

The result in MySQL:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/975dfc8e-e333-415c-891f-69dfa0fd0be5"></img>

3. For MongoDB
We uses `py manage.py migrate --database=mongodb` to migrate it into MongoDB.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/e50d3c22-5eb0-4caa-8dfb-f8674358f425"></img>

The result in MongoDB:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/92454593-9255-4e2c-a41b-7d191c0102f5"></img>

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


