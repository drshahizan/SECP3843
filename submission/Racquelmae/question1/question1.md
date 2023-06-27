<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Chloe Racquelmae Kennedy
#### Matric No.: A20EC0026
#### Dataset: City Inspections	

## Question 1 (a)
### 1. Install Python & Django
- To utilize Django, a Python installation is required which can be obtained by downloading it from the [official website](https://www.python.org/downloads/).
- Open Command Prompt and type `pip install django` to install Django.
<img  src="./files/images/pip.jpg"></img>

### 2. Create & activate virtual environment
To create a virtual environment, run `python -m venv env` in your command prompt. Once the virtual environment is created, activate it by typing `env\Scripts\activate`.
<img  src="./files/images/env.jpg"></img>

### 3. Install package 
With the virtual environment activated, install the required package by running these 2 commands: `pip install djongo` and `pip install mysqlclient`.
<img  src="./files/images/package.jpg"></img>

### 4. Create project & app
Use `django-admin startproject portalproject` to create the Django project. Then, navigate to the project directory and create a new app by running `python manage.py startapp portalapp`.
<img  src="./files/images/project.jpg"></img>

### Configure the database
To use MongoDB and MYSQL as the database, modify the settings.py file in the project folder.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AA',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },

    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'AA',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://Chloe:Racq0711@atlascluster.uwqwdbv.mongodb.net/',
        }
    }
}
```

Create database tables `python manage.py makemigrations`
Once you have created the migration file, you can apply the migrations `python manage.py migrate`

## Question 1 (b)
<img  src="./files/images/architecture.jpeg"></img>

### User
Have access to the portal and contribute to the driving of flow as well as functionality of the application by performing tasks within the system.

### User Interface 
Presents the portal's visual interface to users which includes presentation of information, data entry forms, navigation and menu.

### Web Server (Django)
- Manages incoming user requests over the HTTP protocol and directs them to the relevant views for further handling.
- Performs data processing and transformation operations.
- Object-Relational Mapping (ORM) layer facilitate interactions with the databases.

### Dataset (JSON)
Ingested and processed by Django app for integration with the database.

### Databases
- MySQL: stores structured data such as users login and registration credentials.
- MongoDB: stores unstructured or semi-structured data such as the city_inspections.json dataset.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)