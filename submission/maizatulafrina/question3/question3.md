<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Maizatul Afrina Safiah Binti Saiful Azwan
#### Matric No.: A20EC0204
#### Dataset: City Inspections

## Question 3 (a)

**1. Django Installation**
   - Open Command Prompt and run `pip install Django` command.
     
     <img width="761" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/de153eb9-991a-4ff8-90c5-274078679718">

   - Then, run `django-admin startproject inspection` command to create Django project.
     
     <img width="436" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/0fd1bd51-bc43-45ff-9b77-310da84583e6">

   - Next step, in order to create a django app inside the folder, run `python manage.py startapp inspectionApp`. This is where we can define all the models for MySQL and MongoDB.

     <img width="465" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/3aa6d421-d49d-4332-813d-bb60aff4f53e">

   - The other packages that need to be installed are mysqlclient and djongo. To install mysqlclient, run `pip install django mysqlclient pymongo` command.
     
     <img width="415" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/aaddfea3-909f-4de1-b7a3-ca1570a8bf53">

   - For djongo, run `pip install djongo` command.

     <img width="415" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/ca408d19-7517-4282-b26b-86746daaff01">

**2. Define Connection Details for MySQL and MongoDB**
   -  In `settings.py` file, define the connection details for both MySQL and MongoDB database which include database name, username, password, host and others.
     
      <img width="499" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/de4a6b80-cecb-4912-8f8c-0b3aece9f262">
      
      Ensure the settings for Installed Apps is correct.

      <img width="615" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/fbc54a40-c0b7-4fc5-8e99-acebd7a0757d">


**3. Define Models**

-  In `models.py` file, define the models according to its data structure and data types.

      ```python
      from django.db import models
      from django.contrib.auth.models import AbstractUser, Group, Permission
      
      class User(AbstractUser):
          USER_TYPE_CHOICES = (
              ('customer', 'Customer'),
              ('technical_worker', 'Technical Worker'),
              ('senior_management', 'Senior Management'),
          )
          
          user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
      
          groups = models.ManyToManyField(
           Group,
           verbose_name='groups',
           related_name='customUser_set',
           blank=True,
           
          )
   
          user_permissions = models.ManyToManyField(
           'Permission,
            verbose_name='user permissions',
            related_name='customUser_set',
            blank=True,
          )

          def _str_(self):
               return self.username 
    

**4. Migrate the Models**

- To do migration, run `python manage.py makemigrations` command and `python manage.py migrate` command. 

    <img width="626" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/373af744-c84a-4df6-914b-c53d6ca621f8">

    Result:

    <img width="814" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/0884fd8b-e96a-40cd-826c-ae3f0f4f6005">

**5. Create User Registration and Login Views**



## Question 3 (b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



