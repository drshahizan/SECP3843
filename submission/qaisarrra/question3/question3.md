<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Qaisara binti Rohzan
#### Matric No.: A20EC0133
#### Dataset: 04 - Companies

## Question 3 (a)
This segment of Question 3. (a) is similar to Question 1. (a) and is divided into several parts:
* [Prerequisites](#-prerequisites)
* [Setting Up A Django Project](#️-setting-up-a-django-project)

### Prerequisites
To carry out this segment of the question, it it crucial for to do the following:
1. Install [Python](https://www.python.org/downloads/)
2. Install [Visual Studio Code](https://code.visualstudio.com/download)
<br></br>

### Setting Up A Django Project

**Django Installation** 

1. Create a Django Project Folder. For this project I created a folder named **AA** on my **Desktop**, where it is easily accessible.
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Create%20Project%20Folder.png">
</p>
     
<br>

2. Set up a virtual environment. In your current working directory, this command creates a new virtual environment called ``environment``. 
```bash
python -m venv environment
```
<br>

3. Activate the virtual environment. When the process is finished, you must additionally activate the virtual environment.
```bash
environment\Scripts\activate
```
<br>
   
4. Install Django.
```bash
pip install django
```
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Django%20Installation.png">
</p>
<br>

5. Install necessary packages. Here we are installing  packages that allows integration between our Django App and MongoDB, those packages are **MySQL Client PyMongo** and **Djongo**. Djongo is a smarter approach to database querying. It maps python objects to MongoDB documents. 
```bash
pip install django mysqlclient pymongo
pip install djongo
```
Below are the output when running the commands:
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Install%20Django%20MySQLClient%20PyMongo.png">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Install%20Djongo.png">
</p>
<br></br>

**Create A Django Project** 

You can now create a project after setting up, activating your virtual environment and installing Django. To start a new Django project, open a new terminal in Visual Studio Code and run the following command. The project is named **Companies** in the code below, but it can be changed to any name you like.
```bash
python -m django startproject Companies
```
Navigate yourself to the project directory by inputing the command below:
```bash
cd Companies
```

<br></br>

**Create A Django Application** 

The  ``startapp `` command generates a default folder structure for a Django app. This tutorial uses **CompaniesApp** as the name for the app:
```bash
python manage.py startapp CompaniesApp
```
<p align="center">
   <img width="800" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question3/files/images/Create%20Django%20Project.png">
</p>
<br></br>

**Configure Database Connection** 

Set up the MySQL and MongoDB connections. Alter the code for the databases in the Django project's'settings.py' file as shown below.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_companies',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'AA',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'username': 'qaisara',
            'password': '8301',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}
```
<br></br>


## Question 3 (b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



