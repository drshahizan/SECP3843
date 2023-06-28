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
           Permission,
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

- Create new file name `register.py` to define user input

  ```
  from django import forms
  from .models import User
   
  class UserRegistrationForm(forms.ModelForm):
       password = forms.CharField(widget=forms.PasswordInput)
       user_type = forms.ChoiceField(choices=User.USER_TYPES)
   
       class Meta:
           model = User
           fields = ['username', 'password', 'email', 'first_name', 'last_name', 'user_type']
   
  class LoginForm(forms.Form):
       username = forms.CharField(label='username')
       password = forms.CharField(label='password', widget=forms.PasswordInput)
    ```

 - Create `views.py` file to define action for both Registration Form and Login Form as well as define the path to redirect to their respective dashboard page.

   ```
   from django.shortcuts import render
   from django.contrib.auth import authenticate, login
   from .register import UserRegistrationForm, LoginForm
   
   
   
   def user_register(request):
       if request.method == 'POST':
           form = UserRegistrationForm(request.POST)
           if form.is_valid():
               user = form.save(commit=False)
               user.set_password(form.cleaned_data['password'])
               user.save()
               return redirect('login')
       else:
           form = UserRegistrationForm()
       return render(request, 'user_register.html', {'register': form})
   
   
   def login_view(request):
       if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username, password=password)
   
           if user is not None:
               login(request, user)
               print(f"Logged in as {username}")
               print(f"User type: {user.user_type}")
               
               if user.user_type == 'customer':
                   print("Redirecting to customer dashboard")
                   return redirect('cust_dashboard')
               elif user.user_type == 'technical_worker':
                   print("Redirecting to technical worker dashboard")
                   return redirect('tech_dashboard')
               elif user.user_type == 'senior_management':
                   print("Redirecting to management dashboard")
                   return redirect('management_dashboard')
           else:
               messages.error(request, 'Invalid username or password.')
       
       return render(request, 'login.html')
   
   def customer_dashboard_view(request): return render(request, 'cust_dashboard.html')
   
   def technical_worker_dashboard_view(request): return render(request, 'tech_dashboard.html')
       
   def management_dashboard_view(request): return render(request, 'management_dashboard.html')
   
   ```
 - Create Registration Form `user_register.html`.

   ```
   <style>
    .form-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .form-row {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }

    .form-label {
        min-width: 100px;
        text-align: right;
        margin-right: 10px;
    }

    .form-input {
        min-width: 200px;
    }
   </style>
   
   <h1>Register</h1>
   <form method="POST" action="{% url 'login' %}" class="form-container">
       <div class="form-row">
           <label for="id_email" class="form-label">Email:</label>
           <input type="text" id="id_email" name="email" class="form-input">
       </div>
   
       <div class="form-row">
           <label for="id_username" class="form-label">Username:</label>
           <input type="text" id="id_username" name="username" class="form-input">
       </div>
   
       <div class="form-row">
           <label for="id_password" class="form-label">Password:</label>
           <input type="password" id="id_password" name="password" class="form-input">
       </div>
   
       <div class="form-row">
           <label for="id_role" class="form-label">Role:</label>
           <select id="id_role" name="role" class="form-input">
               <option value="customer">Customer</option>
               <option value="senior_management">Senior Management</option>
               <option value="technical_worker">Technical Worker</option>
           </select>
       </div>
   
       <div class="form-row">
           <input type="submit" value="Register">
       </div>
   </form>
   ```
   Result:

   <img width="707" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/6b2ae578-22f6-4caf-b418-b9b449aad2d5">

- Create Login Form `login.html`.

  ```
  <h1>Login</h1>
   <form style="align-content: center;" method="POST" action="{% url 'login' %}">
      
    
       <div>
          <label for="id_username">Username:</label>
          <input type="text" id="id_username" name="username">
       </div>
    
       <div>
          <label for="id_password">Password:</label>
          <input type="password" id="id_password" name="password">
       </div>
    
       <div>
          <input type="submit" value="Login">
       </div>
    
    </form>
  ```

  Result:

  <img width="607" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/d93b1367-ff03-4bc0-8a8e-10a7b275cc05">

- Create dashboard page for each users `cust_dashboard.html`, `tech_dashboard.html` and `management_dashboard.html`.

  **cust_dashboard.html**

  ```
  <!DOCTYPE html>
   <html>
   
   <head>
      <title>Dashboard</title>
      <style>
         .dash {
            font-size: 80px;
            text-align: center;
            margin-top: 200px;
         }
      </style>
   </head>
   
   <body>
      <div class="dash">
         Customer Dashboard
      </div>
   </body>
   
   </html>
  ```

  Result:

  <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/e1ab96f7-7dce-481e-8d2a-997351846924">
  
  **tech_dashboard.html**

  ```
  <!DOCTYPE html>
   <html>
   
   <head>
      <title>Dashboard</title>
      <style>
         .dash {
            font-size: 80px;
            text-align: center;
            margin-top: 200px;
         }
      </style>
   </head>
   
   <body>
      <div class="dash">
         Technical Worker Dashboard
      </div>
   </body>
   
   </html>
  ```

   Result:

  <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/edf15a6b-7064-4a8c-9679-3dbe5980cbef">

  
  **management_dashboard.html**

  ```
  <!DOCTYPE html>
   <html>
   
   <head>
      <title>Dashboard</title>
      <style>
         .dash {
            font-size: 80px;
            text-align: center;
            margin-top: 200px;
         }
      </style>
   </head>
   
   <body>
      <div class="dash">
         Management Dashboard
      </div>
   </body>
   
   </html>
  ```

  Result:

  <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/f56c424e-1160-4042-b538-90126d27a952">



## Question 3 (b)

The challenge of Data Replication and Synchronization arises between the MySQL and MongoDB databases when working with two different databases. There are few ways and steps to overcome this challenges including exploring database-specific replication techniques or leverage external tools that facilitate realtime
updates and seamless interaction between the databases.

   - Step 1: Identify the Replication Strategy
Determining the replication direction (MySQL to MongoDB, MongoDB to MySQL, or bidirectional) and establishing the synchronisation frequency are crucial for managing data replication and synchronisation between MySQL and MongoDB. This requires taking into account elements like data volume, system performance, and real-time needs. You may make sure that the data is consistent between the two systems by choosing which database drives the replication and specifying the synchronisation frequency. It is possible to achieve accurate replication and synchronisation, maintain data integrity, and enable seamless communication between the two databases by selecting the right direction and frequency.

### Step 2: Configure the database
The MySQL and MongoDB connection have been declared in setting.py. 


### Step 3: Set up connections to both MySQL and MongoDB databases
This step is done by importing necessary libraries like MongoClient to make connections with MySQL and MongoDB.
```
from django.db import connections
from pymongo import MongoClient

# Establish connections to MySQL and MongoDB
mysql_connection = connections['default']
mongodb_client = MongoClient('mongodb+srv://cluster0.cpy5tdw.mongodb.net', username='peiyu', password='1')
```

### Step 4: Define the dual_write function 
The dual_write function will implement the logic of synchronizing both databases during insert, update and delete. However, I will show the dual write operation for insertion in this example. 


### Step 5: Define view
In this step, create a view in the Django application that triggers the dual_write function to test it.

> The above code will pass a tweet document to dual_write function in order to test the insert operation. 


### Step 6: Test and validate the dual write process
Lastly, open the command prompt and execute ```py manage.py runserver```.

Output: 


> It can be noted that the “Dual write successful!” has been printed out and this indicated the success of insertion.

### Step 7: Check the data in MySQL and MongoDB
We can find the newly inserted data in both MySQL and MongoDB.
- MySQL
  
  
- MongoDB
  


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



