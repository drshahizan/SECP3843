<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.


## Special Topic Data Engineering (SECP3843): Alternative Assessment ©️

#### Name: MADINA SURAYA BINTI ZHARIN
#### Matric No.: A20EC0203
#### Dataset: companies.json

### Question 3 (a)

1. Download Django in command prompt
   ```
   pip install django
   ```
   
2. In the desired file path, create new django project
   ```
   django-admin startproject djangoAA
   ```
   
3. Navigate path to the new created project
   ```
   cd AA
   ```
   
4. Startapp for the users. The folder directory is as follows.
   ```
   python manage.py startapp signup
   ```
  <p align="center">
      <img width="122" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/ed2447f0-a99d-4043-bb71-eeda4b2305ff">
  </p>

5. Open **settings.py** in **AA** folder and update the code.
   - Firstly, add the name of the startapp folder in **INSTALLED_APPS**.
      ```
      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'signup',
      ]
      ```
    - Next, configure the database connection to mysql.
      ```
      DATABASES = {'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
                'unix_socket': 'C:/xampp/mysql/mysql.sock',}}}
      ```
      
6. Apply migrations
     ```
     python manage.py makemigrations
     ```
     ```
     python manage.py migrate
     ```
     
7. Open localhost and create new database. I created my folder as 'aa'.
      <p align="center">
           <img width="162" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/af17e0cd-33c6-4216-9f79-50e4941f4f75">
      </p>

8. Open **models.py** in the **signup** folder and start making user authentication. To perform this, firstly, define django authentication models and import it. Then, define the class for each user needed. In here, there will be three users which are customers, technical workers, and senior management. This also means that each user type will have their own table in the database. Since we use some common fields such as **first_name, last_name, email, username, and password**, we dont have to specify it in the class as the django authentication model already include this.
   ```
   from django.contrib.auth.models import AbstractUser
   ```
   ```
   class Customer(AbstractUser):
       pass

   class TechnicalWorker(AbstractUser):
       pass
   
   class SeniorManagement(AbstractUser):
       pass
   ```

9. Perform migrations for database and tables using commands below:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
10. Create the views for user registration and login, create urls routing to the specific page and perform CRUD for each user using **request.POST** and **request.GET** method.
   <p align="center">
      <img width="389" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/45a21554-6f16-4e8d-aaea-12061a5a46ce">
       <br><br>
      <img width="228" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/34d325cc-a6e9-4758-a008-f5954a9f6113">
      <br><br>
       <img width="412" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/e6efb5fa-c714-4da8-8c9c-97cc2f00fa77">
   </p>
   
11. The tables and its field created in mysql database are as follows:
    <p align="center">
      <img width="157" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/44b21732-1880-44c7-87e6-58ff7886444a">
      <img width="515" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/a876d3d2-0c9d-46cf-be5d-bbf2bc90efdc">
   </p>
    
   
   

     
### Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
