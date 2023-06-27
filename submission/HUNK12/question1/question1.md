<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Mikhel Adam Bin Muhammad Ezrin
#### Matric No.: A20EC0237
#### Dataset: [Tweets](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets)

## Question 1 (a)
There are several steps that are required to integrate Django with the JSON dataset, ensuring efficient data storage and retrieval from both MySQL and MongoDB databases to enable the creation of dynamic web pages. First of all, let' figure out how we can utilize and configure five(5) web servers for this project. Below are the configurations I would recommend to setup the servers:

1. `Web server`: This server will host the Django application and serve the web pages to users.
2. `MySQL server`: This server will host the MySQL database and store data that needs to be persisted.
3. `MongoDB server`: This server will host the MongoDB database and store data that needs to be persisted.
4. `Load balancer`: This server will distribute incoming traffic across the web servers to ensure high availability and scalability.
5. `Backup server`: This server will store backups of the data from the MySQL and MongoDB databases to ensure data integrity and recovery in case of a disaster.

**Next, we'll need to install Django. For this case study, we'll be installing Django on a local machine instead of a server. The steps for both are relatively the same. Below are the steps to install Django on a local machine:**
   - Install Django on the the local machine where the Django web framework will be deployed by running the command `pip install django` in the commmand prompt.
     ![image](https://github.com/drshahizan/SECP3843/blob/main/submission/HUNK12/question1/files/images/install%20django.png)
   - Create a new Django project using the `django-admin startproject <project name here>` command. 
     ![image](https://github.com/drshahizan/SECP3843/assets/3646429/251536ce-c663-4dcd-8c36-3943d19cf415)
   - Start an app for the project by typing `python manage.py startapp <app name>`. We'll simply name it `app`. This will create a new directory called `app` in the project folder
   - Open the project folder in an IDE. I will be using [Visual Studio Code](https://code.visualstudio.com/). Open the `manage.py` file located in the main project folder and add the `app` we just added as one of the installed apps.
    ![image](https://github.com/drshahizan/SECP3843/assets/3646429/1be8fdcb-70f4-4ecd-b91f-237eaa3daeb5)
   - Check if the system is able to run on a local server with the command `py manage.py runserver`
     ![image](https://github.com/drshahizan/SECP3843/assets/3646429/8e5ca02b-6dda-48f4-ac80-e9e1bd8588d2)

**Now let's setup the databases for this project. As mentioned, we'll be using MySQL and MongoDB as the databases to store our data**

### Setting up MySQL database
I'll be using [XAMPP](https://www.apachefriends.org/index.html) to setup the MySQL database server locally.

First, I'll startup the modules needed in XAMPP as seen in the figure below
![image](https://github.com/drshahizan/SECP3843/assets/3646429/bcf98adb-a02c-404c-8f7f-7a2b25eaebb7)

Then in the phpMyAdmin page, we'll add a new database called  `db_tweets`. That's all the setting up needed for MySQL for now
![image](https://github.com/drshahizan/SECP3843/assets/3646429/2344ad95-588d-4c19-8ec0-54aad6a2226d)

### Setting up MongoDB database
Install [MongoDB compass](https://www.mongodb.com/try/download/compass) 
<img src="https://github.com/drshahizan/SECP3843/assets/3646429/34fee783-a4aa-42af-a5b3-0bdb93c7e7a2" width="400">

In MongoDB Compass GUI, create a new database and collection.
![image](https://github.com/drshahizan/SECP3843/assets/3646429/90319dec-2898-4a61-80f9-ef23c6865b45)

**Both the databases are now setup**

IN PROGRESS

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


