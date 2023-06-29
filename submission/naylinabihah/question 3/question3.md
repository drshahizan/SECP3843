<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nayli Nabihah Binti Jasni
#### Matric No.: A20EC0105
#### Dataset: Companies

## Question 3 (a)
#### Step 1: Define Django Model (For User)

Since in this part focuses in the authentication of users in Django project, a user model should be define in Django. In Django, there is a built-in framework specifically for authentication. By using this built-in framework, it helps to ease the processes of making models and some functionalities for user authentication management as it has already pre-built. The framework used in `django.contrib.auth.models'. Below is the code that shoul be written in models.py

![model](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/models.png)
 
#### Step 2: Create Registration Form for Users

This can be done by using the Django forms.  Since I had already used the built-in framework for authentication of users, the form will collect the information from the users such as username, email and password by default. As the form is submitted, Django will firstly validate the submitted data then, create a new user based on the user type that has been declared in models.py. Note that, all of these users information will be stored into MySQL database.

- Create forms.py under the folder 'app' in the Django project and add the code for registration form.

![forms](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/formspyreg.png)

- Update the views.py as we wanted to add the registration view.

  ![regview](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/viewspyreg.png)
  
- Create a folder named as 'template' under folder 'app' to grouped all the html files that being used in this Django project. Then create a html file for registration template.

![reghtml](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/reghtml.png)

#### Step 3: Implementation of User Authentication

Just as in Step 2, since I used the built-in Django authentication framework, it helps to ease the process of doing the authentications in the portal because it already include the controls for user login, logout, and session management. It also has done a pre-built views and backend authentication and authorization to handle the processes. All the authentications done by the users will be validated with MySQL database to get the credentials before access permission is granted for the users into the portal.

- Under the same file forms.py, add another class for login just as below:

![formslogin](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/formspylogin.png)

- Update the views.py as we wanted to add the login view.

  ![loginview](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/viewspylogin.png)
  
- Create a html file for login template.

![loginhtml](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/loginhtml.png)


#### Step 4: Manage the User Access

This can be done by managing the users according to the user type. Since in this project, there are going to be 3 users, there should be a restrictions set for each user type on the portal overall. This usually can be seen mostly on what are the limitation of each user type can do in the portal. By correctly identify the correct access permissions for each user type, it can ensure a better control on user access since not every user can change everything in the portal, some of the user can only view it and so on.


#### Step 5: Set the Configuration of Database in Django Project

Since using MySQL database to store the user authentication information, below are the settings that should be done in settings.py:

![db](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/db.png)
 
#### Step 6: Perform Database Migration in Django Project

By using the terminal in which the Django project is installed, use the below command lines:

```
python manage.py makemigrations
```
```
python manage.py migrate
```
The terminal should give response when these command was executed:

![migrate](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%203/files/images/makemigrate.png)


## Question 3 (b)

When it comes to working with different databases in one project, it may cause some issues with data replication and synchronization if it is not handled correctly. It can be handled using various ways, however, below are the steps I had taken to ensure the data synchronization between the two databases is correctly work. These steps were for database-specific replication technique.

#### Step 1: Install the REQUIRED Library


#### Step 
#### Step 
#### Step 
#### Step 
#### Step 

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


