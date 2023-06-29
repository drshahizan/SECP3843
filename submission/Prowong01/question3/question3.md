<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Eddie Wong Chung Pheng
#### Matric No.: A20EC0031
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies" >Companies</a>

## Question 3 (a)
### Step 1: Set up Django Project & App
To set up Django project & app, I need to create and activate the virtual environment first

```
python -m venv env
env\Scripts\activate
```

Then, install the django package
```
pip install django
```

Create new Django project called question 3 and a new app called q3 through command prompt.
```
django-admin startproject question3
cd question3
python manage.py startapp q3
```

Command Prompt:
<img  src="./files/images/django.png"></img>

### Step 2: Install MySQL Python Driver & Configure Database Setting
Install the mysqlclient as this is a library that allows Django to connect and communicate with the MySQL database.
```
pip install mysqlclient
```
<img  src="./files/images/mysqlclient.png"></img>

Next, update the settings.py file in question3 project folder. I change the DATABASES dictionary to configure the MySQL database values.
<img  src="./files/images/setting.png"></img>


### Step 3: Configure models.py
I need to define the models for q3 app that represent the data that I want to store in the database.
<img  src="./files/images/model.png"></img>

## Question 3 (b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



