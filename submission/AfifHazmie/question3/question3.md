<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Afif Hazmie Arsyad Bin Agus
#### Matric No.: A20EC0176
#### Dataset: Supply Store

## Question 3 (a)
1. Firstly, before creating the user login, registration and users view based on techinical workers, customers and senior management.
   - configure the database to insert and use MySQL database table
      <p align="center">
         <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/dbconfig.jpg">
      </p>
      
     
2. Create templates
   - Create new folder and named it `templates` within app folder which mine is `AA`
   - the templates will be used to create view of each of the page.
     <p align="center">
       <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/templatefolder.jpg">
     </p>
3. Model Define

   - define the model including the user type
   ```python
   
     class User(AbstractUser):
        is_customer = models.BooleanField(default=False)
        is_technical_worker = models.BooleanField(default=False)
        is_senior_management = models.BooleanField(default=False)
    
        groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    
        user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')
        
   ```
---

   - Migrate apply the model
     ```python
       python manage.py makemigrations
       python manage.py migrate
     ```

---
   - this model defined will create a new database table in the MySQL
   <p align="center">
       <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/dbtb.jpg">
   </p>
4. Create View
   - In Django, the `views.py` file is where we define the views for the web application. A view is a Python function or class that takes a web request and returns a web response. It contains the logic that processes the user's request, interacts with the database or other data sources, and renders the appropriate HTML templates to generate the response.

   #### Importing required libraries
    ```python
      from django.shortcuts import render, redirect
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib.auth import authenticate, login, logout
      from django.contrib.auth.forms import AuthenticationForm
      from .forms import RegistrationForm
      from django.contrib.auth.decorators import login_required
      from django.contrib import messages
    ```

   #### Define User Login view function
   
    ```python
      def user_login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
              username = form.cleaned_data.get('username')
              password = form.cleaned_data.get('password')
              user = authenticate(username=username, password=password)
              if user is not None:
                  login(request, user)
                  return redirect('dashboard')
      else:
          form = AuthenticationForm()
      return render(request, 'login.html', {'form': form})
    ```

    #### Define Register view function
    ```python
      def register(request):
      if request.method == 'POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Registration successful. You can now log in.')
              return redirect('login')
          else:
              # Form is not valid, display form errors
              for field, errors in form.errors.items():
                  for error in errors:
                      messages.error(request, f"{field}: {error}")
              # You can also add a general error message if needed
              messages.error(request, 'Error during registration. Please fix the errors below.')
      else:
          form = RegistrationForm()
  
      return render(request, 'register.html', {'form': form})
    ```

    #### Define seperate dashboard for each user type
   - `customer_dashboard`
   - `technical_worker_dashboard`
   - `senior_management_dashboard`
   
    ```python
      @login_required
      def dashboard(request):
          user = request.user
          if user.is_customer:
              return render(request, 'customer_dashboard.html')
          elif user.is_technical_worker:
              return render(request, 'technical_worker_dashboard.html')
          elif user.is_senior_management:
              return render(request, 'senior_management_dashboard.html')
          else:
              return redirect('profile')
      
      
      def redirect_dashboard(request):
          user = request.user
          if user.is_customer:
              return redirect('customer_dashboard')
          elif user.is_technical_worker:
              return redirect('technical_worker_dashboard')
          elif user.is_senior_management:
              return redirect('senior_management_dashboard')
          else:
              return redirect('profile')
    ```
    #### Define user logout view function
    ```python
      def user_logout(request):
      logout(request)
      return redirect('login')
    ```

5. Create `forms.py` file
   - To register a seperate user into the system, we must create forms that will receive the user type input
    ```python
      from django.contrib.auth.forms import UserCreationForm
      from django import forms
      from .models import User
      
      class RegistrationForm(UserCreationForm):
          ROLE_CHOICES = [
              ('customer', 'Customer'),
              ('technical_worker', 'Technical Worker'),
              ('senior_management', 'Senior Management'),
          ]
      
          role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
      
          class Meta:
              model = User
              fields = ('username', 'email', 'password1', 'password2', 'role')
      
          def save(self, commit=True):
              user = super().save(commit=False)
              role = self.cleaned_data.get('role')
      
              if role == 'customer':
                  user.is_customer = True
              elif role == 'technical_worker':
                  user.is_technical_worker = True
              elif role == 'senior_management':
                  user.is_senior_management = True
      
              if commit:
                  user.save()
              return user
      ```
    
6. Create routing in the `urls.py` file
   - In Django, the urls.py file is used to define the URL patterns for your web application. It maps the URLs requested by the user to the corresponding views that will handle those requests.
   ```python
      from django.contrib import admin
      from django.urls import path
      from AA.views import (
          register,
          user_login,
          dashboard,
          redirect_dashboard,
          user_logout,
      )
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', register, name='register'),
          path('register/', register, name='register'),
          path('login/', user_login, name='login'),
          path('dashboard/', dashboard, name='dashboard'),
          path('dashboard/', redirect_dashboard, name='dashboard'),
          path('logout/', user_logout, name='logout'),
      ]
   ```


7. Create templates
   - In the `template` folder that have been created.
   - Add new file named `login.html`
     ```html
      {% extends 'base.html' %}
      {% block title %}Login{% endblock %} 
      
      {% block content %}
          <h2>Login</h2>
          <form method="post">
              {% csrf_token %}
              {{ form.as_p }}
              <button type="submit" class="btn btn-success">Login</button>
          </form>
      {% endblock %}
     ```
     
   - Add new file called `base.html`
     ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{% block title %} Django MySql User Authentification - Login and register{% endblock %}</title>
            {% load static %}
            <link rel="stylesheet" href="https://cdn.jsdeliver.net/npm/bootstrap@5.0.2/dist/css.bootstrap.min.css">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>
            <div class="container-fluid">
                <header>
                    <h1>
                        Django MySql User Authentification - Login, register and Logout
                    </h1>
                    <hr>
                </header>
                <main>
                    {% block content %}
                    {% endblock %}
                </main>
            </div>
        </body>
        </html>
     ```
     
   - Add new file named `register.html`
     ```html
        {% extends 'base.html' %}

        {% block content %}
            <h2>Sign Up</h2>
            <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="btn btn-success">Sign Up</button>
            </form>
        {% endblock %}
     ```
   - Lastly, add 3 new file for the following user type view with the same html code but different naming.
     - `customer_dashboard`
     - `technical_workers_dashboard`
     - `senior_management_dashboard`
       
     ```html
         {% extends 'base.html' %}

         {% block title %}Customer Dashboard{% endblock %} 
              
            {% block content %}
              
                <h2>Customer Dashboard</h2>
              
            {% endblock %}
     ```
       
 
8. In web views of the system.
   
   #### User table user type
   <p align="center">
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/usertype.jpg" width="500">
   </p>
   
---

   #### Register Page
   <p align="center">
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/register.jpg" width="450"">
  </p>
  
---

  #### Log in Page
  <p align="center">
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/login.jpg" style="width: 550px; height: 180px;">
  </p>
  
---

  #### Customer Page
  <p align="center">
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/customerd.jpg" width="550">
  </p>
  
---

  #### Technical Worker Page
  <p align="center">
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/technicald.jpg" width="550">
  </p>
  
---

  #### Senior Management Page
  <p align="center">
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question3/files/images/seniord.jpg" width="550">
  </p>

## Question 3 (b)
   - When addressing the challenge of data replication and synchronization between MySQL and MongoDB databases, the concept of master and slave servers can be relevant.
   - The master-slave replication model allows for data replication and synchronization between the master and slave databases, ensuring that changes made in the master database are propagated to the slave database.
   - This replication model is commonly used in scenarios where read scalability, high availability, and fault tolerance are required.
   - The specific steps for configuring master and slave servers may vary depending on the replication technique or tool chosen, as well as the specific configurations of the MySQL and MongoDB databases.
   - Master-slave replication enhances the reliability, scalability, and performance of database systems by providing redundancy, distributing the workload, and facilitating data backup and analytics. It is a widely adopted technique for achieving high availability and improving the overall efficiency of database operations.

---

#### To set up master-slave replication between a MySQL master server and a MySQL slave server, these are the following steps:
##### Step 1: Configure the master server
   - Open MySQL configuration on the Master server
   - Locate `[mysqld]` and add the following line:
   
   ```makefile
   server-id = 1
   log_bin = mysql-bin
   binlog_do_db = db_store
   ```
   > - `server-id` uniquely identifies the master server in the replication setup.
   > - `log_bin enables` binary logging to record changes made to the data
   > - `binlog_do_db` specifies the database(s) to be replicated.

##### Step 2: Create Replication User on the Master Server
   - Log in to the MySQL command-line interface on the master server.
   - Run the following SQL command to create a replication user
     
     ```python
      CREATE USER 'mafif'@'192.168.1.100' IDENTIFIED BY 'A@bc1234';
      GRANT REPLICATION SLAVE ON *.* TO 'mafif'@'192.168.1.100';
      FLUSH PRIVILEGES;
     ```
     
##### Step 3: Obtain the Master Binary Log Coordinates
   - Run the following line on master werver
     
   ```sql
   SHOW MASTER STATUS;
   ```

##### Step 4: Configure the Slave Server
   - Open the MySQL configuration file on the slave server.
   - Locate `[mysqld]` section and add the following lines:
     ```makefile
     server-id = 2
     replicate-do-db = db_store
     ```
     > - `server-id` uniquely identifies the slave server.
     > - `replicate-do-db` specifies the database(s) to be replicated from the master.

##### Step 5: Start Replication on the Slave Server
   - Log in to the MySQL command-line interface on the slave server.
   - Run the following SQL command to configure replication:
     ```makefile
     CHANGE MASTER TO MASTER_HOST='192.168.1.200', MASTER_USER='mafif', MASTER_PASSWORD='A@bc1234', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=0;
     ```
   - Start the replication process on slave server
     ```sql
     START SLAVE;
     ```
##### Step 6: Verify Replication Status
   - Run the following line on slave server
     ```sql
     SHOW SLAVE STATUS\G
     ```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



