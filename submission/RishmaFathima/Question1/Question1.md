<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Rishma Fathima Binti Basher
#### Matric No.: A20EC0137
#### Dataset: [Airbnb Listings Dataset](https://github.com/drshahizan/dataset/tree/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/05-airbnb)

## Question 1 (a)
   1. ``Set up the Django project with virtual environment``:
      </br>
        - The first step is to install django in my desktop. In order to install django, I use the command  ``pip install django`` in command prompt.
          
          <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.1.png">
          
        - Then, I created a new project b: Use the django-admin startproject command to create a new Django project from a folder I have created called ``AA_Question1``           by using the command called ``django-admin startproject AA_Question1``.
          
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.2.png">
           
        - After creating the project, I created the Django app by the command ``python manage.py startapp app``.
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/12219ef33b7e27340551d65a344b034a560bd2e4/submission/RishmaFathima/Question1/files/images/1.1.1.3.png">
           
        - Then, create a virtual environment for the project.
          
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/871e6e313e09d8f507b32aaf9d54173434080a29/submission/RishmaFathima/Question1/files/images/new%201.1.1.4.png">
          
  2. ``Define Django models in models.py``:
        - JSON file is downloaded from the Github.
        - Django models were created based on the attributes from the downloaded JSON file which contain the dataset of ``Airbnb Listing Dataset``.
        - From the app folder created, in the ``models.py`` file, the model of the prject would be defined.
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/c18d8db59264504dc5f34395291dfe90abb48c90/submission/RishmaFathima/Question1/files/images/1.1.2.png">
          
   
      

  3. ``Configure the settings of the project``:

        - Update the ``settings.py`` file in the project folder to define the database setting for Mysql and MongoDB
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/c18d8db59264504dc5f34395291dfe90abb48c90/submission/RishmaFathima/Question1/files/images/1.1.3.1.png">
        - Update the ``settings.py`` file to declare the created ``app``
           <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bda3ad57b1a66ccf70c740ca047c30a08ee4c1c7/submission/RishmaFathima/Question1/files/images/1.1.3.3.png">
        - Install django with the command ``pip install django`` to work as database connectors
           
        - Install mysqlclient with the command ``pip install mysqlclient`` to work as database connectors
          <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/c18d8db59264504dc5f34395291dfe90abb48c90/submission/RishmaFathima/Question1/files/images/1.1.3.2.png">
         
           
  4. ``Migration of database and load the JSON file``:

        - Add the command ``python manage.py makemigrations`` to migrate the database from the ``models.py``
        - Then add the command ``python manage.py migrate`` to make th emigrations work with Mysql and MongoDB
        - Finally to get the JSON data from the dataset and to save it into MogoDB server, I need to create a script in Django.
         
  5. ``Update and Testing Data``:

        - Update the MOngoDB and Mysql everytime there is changes in dataset
        - Finally, with testing and monitoring practices, I can ensure the reliability, performance, and stability of your Django application's integration with the               JSON dataset, MySQL, and MongoDB databases
        

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

