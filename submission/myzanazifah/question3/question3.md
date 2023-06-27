<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Myza Nazifa Binti Nazry
#### Matric No.: A20EC0219
#### Dataset: Stories

## Question 3 (a)

1. Create a virtual environment and activate it.
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(1).png" /></div>
2.  Then, create a Django project. After creating a new Django project, then create a Django apps.
      
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(2).png" /></div>
4. Open the folder in Visual Studio Code and go to settings.py. Configure the database settings and also add the app in the code as shown in figures below:
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(3).png" /></div>
      
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(4).png" /></div>
5. Then, go to phpmyadmin and create a new database. I have named the database as 'storiesportal'.
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(5).png" /></div>
6.  Install two of these libraries to connect with MySQL database by using the commands below.
   
     ```
      pip install mysql-connector-python
      
      pip install mysqlclient
      ```
7.  Go to models.py and create the User Models. 
   
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(6).png" /></div>
8.  Run the following code to migrate the database and tables.
      
     ```
      python manage.py makemigrations
      
      python manage.py migrate
      ```
9.  The figure below shows the table that has been successfully migrated.
    
      <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(7).png" /></div>
10.  In settings.py, add the following command to ensure that Django is using the right User model.
     
     ```
      AUTH_USER_MODEL = 'AAapp.User'
      ```
11.  Then, we need to register the User Model. Go to admin.py and add the following code:    

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(8).png" /></div>
12.  In the Django application directory, create a new file named 'form.py' to create the registration and login form. Add the following code as shown below:

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(9).png" /></div>
13. Then, go to views.py and import necessary modules. Then, create a view for user registration, user login and logout. For the function customer_view, technical_worker_view and senior_management_view, ensure putting @login_required so that only authenticated users can access the page.

    <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(10).png" /></div>
    
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(11).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(12).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(13).png" /></div>
14. After that, configure the url path in url.py.

    <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(14).png" /></div>

15. Go to the Django application directory and go to the integrated terminal. Run the following code to create templates directory.

    ```
      mkdir templates
      ```
16. In the templates directory, create five new files which are 'customer.html', 'login.html', 'register.html', 'senior.html' and lastly is 'technical.html'.

    <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(21).png" /></div>
    
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(22).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(26).png" /></div>
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(24).png" /></div>     
     
     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/g3(25).png" /></div>
18. Once everything has been done, open a new terminal and run the command below.    

    ```
      python manage.py runserver
      ```

### Registration page

   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(15).png" /></div>


   Database after registering new users:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(16).png" /></div>

### Login page

   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(17).png" /></div>


   Customer view after logging in:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(18).png" /></div>

   Technical worker view after logging in:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(19).png" /></div>

   Senior management view after logging in:
   
   <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question3/files/images/q3(20).png" /></div>
     

## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



