<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Chong Kai Zhe
#### Matric No.: A20EC0186
#### Dataset: Analytics

## Question 3 (a)
### Pre-Requisites
Make sure to start a new project using cmd
```python
django-admin startproject AAquestion3
python manage.py startapp AAquestion3app
```
![image](https://github.com/drshahizan/SECP3843/assets/120616074/a5785d3e-cc51-40c6-bd88-3673d9824dd5)

Then we create Database in phpMyAdmin
![image](https://github.com/drshahizan/SECP3843/assets/120616074/bf9e8282-2064-430f-91e7-98f6af349db3)

Then add our app to the installed apps definition and also MySQL database in `settings.py`
![image](https://github.com/drshahizan/SECP3843/assets/120616074/c97bc91f-37e6-48d4-9f13-990e90007a7c)
![image](https://github.com/drshahizan/SECP3843/assets/120616074/ff34254e-06f5-4868-ade5-ea6afc490482)

### Defining User Model

We will define our user model that includes username, name, password and also usertype in `models.py` file
![image](https://github.com/drshahizan/SECP3843/assets/120616074/7299be12-f2d5-4903-96dd-a6c91971516f)

Now we need to make migrations, so run the following code:

```python
python manage.py makemigrations
python manage.py migrate
```
![image](https://github.com/drshahizan/SECP3843/assets/120616074/2a57ccd6-c4b5-41bf-8f82-cfe31f99d24c)

### Creating User Registration, Login Views and Templates

Registration
![image](https://github.com/drshahizan/SECP3843/assets/120616074/342c721e-051d-41d3-9e9c-065bb8456e87)

Login
![image](https://github.com/drshahizan/SECP3843/assets/120616074/6804bd41-44a6-46b4-bd98-d4c351bdbcff)

Customers
![image](https://github.com/drshahizan/SECP3843/assets/120616074/8c0b6750-fbdc-4200-bc3f-a054f550fa97)

Managemnet
![image](https://github.com/drshahizan/SECP3843/assets/120616074/4af7e6bd-bb46-42e8-be2b-bcfbb0d47f78)

Worker
![image](https://github.com/drshahizan/SECP3843/assets/120616074/f556c28d-0fba-45d2-92e9-46f0afa77311)

### Configuring URLs

 We will defined in the `urls.py`. Therefore, we should configure it before running our application.

<br>
![image](https://github.com/drshahizan/SECP3843/assets/120616074/e4a95e16-da02-4051-b57e-4ffac3ecad1d)

## Question 3 (b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



