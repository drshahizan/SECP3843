<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Low Junyi
#### Matric No.: A20EC0071
#### Dataset: [Airbnb](https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb)

## Question 3 (a)
### Step 1: Set Environment 
a) Open Command Prompt:


  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/086f550c-8f6d-4e35-ae96-9ac80744621f"></img>


b) Redirect to the correct path with the following code.
```
cd C:\Users\user\Downloads\AA MSO\
```


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/ccaeb20d-0e9e-49c7-b63b-aed35a1213f3"></img>


c) Create a new Django project by using the code below and move to the project
```
django-admin startproject AA_Q3
```
```
cd AA_Q3
```


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/b8bd91ac-5379-42aa-aaad-9f486e56771a"></img>


d) Create and activate virtual environment in Python by using the following code.
```
py -m venv env
```
and
```
env\Scripts\activate
```


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/65874096-1bfb-4760-963c-2256c40a7a57"></img>


### Step 2: Install Django and mysqlclient
a) Install Django with the following code.
```
pip install Django
```


  <img  src="https://github.com/drshahizan/SECP3843/assets/120614501/cce64cae-7dfd-490a-901c-8a02177e2307"></img>


b) Install the mysqlclient in the command prompt using the code below.
```
pip install mysqlclient
```


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/50eb452e-609a-4067-b1d3-cee2162ff252"></img>


### Step 3: Create Django App
Create a new Django app within the project using the code below.
```
python manage.py startapp q3
```


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/97fb892f-a093-4e6a-80e3-09de5c6b25e8"></img>


### Step 4: Configure Database
a) Open setting.py to configure the database setting in order to connect with MySQL.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'q3',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost', 
        'PORT' : '3306',},
}
```


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/6dbfc7d5-d278-4b72-b6dc-7e48a4e50ec5"></img>



b) Make sure the INSTALLED_APPS already add the app name.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'q3'
]
```


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/aba5cc65-5dab-4a73-bd15-9ad171701381"></img>


### Step 5: Define Model
a) Define the user model class in the `models.py` according to the requirements of the three user types which are customers, technical workers, and senior management. The code as below.
```python
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

   class User(AbstractUser):
       is_customer = models.BooleanField(default=False)
       is_technical_worker = models.BooleanField(default=False)
       is_senior_management = models.BooleanField(default=False)
   
       groups = models.ManyToManyField(Group, blank=True, related_name='custome_user_set')
   
       user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custome_user_set')



    def __str__(self):
        return self.username
```



### Step 6: Create Views
a) Find `views.py` file in the app.


b)Create views for user login, registration and dashboard
```python
   from django.shortcuts import render, redirect
   from .forms import RegistrationForm
   from django.contrib.auth .forms import AuthenticationForm
   from django.contrib.auth import authenticate, login, logout
   from django.contrib.auth.decorators import login_required
   from .decorators import is_customer, is_technical_worker, is_senior_management
   from django.contrib.auth.decorators import user_passes_test
   
   # Create your views here.
   def user_login(request):
       if request.method == 'POST':
           form = AuthenticationForm(request, data=request.POST)
           if form.is_valid():
               username = form.cleaned_data.get['username']
               password = form.cleaned_data.get['password']
               user = authenticate(username=username, password=password)
               print('User: ', user)
               if user is not None:
                   login(request, user)
                   print('User logged in successfully')
                   return redirect('dashboard')
       else:
           form = AuthenticationForm()
       return render(request, 'login.html', {'form': form})
   
   def register(request):
       if request.method == 'POST':
           form = RegistrationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')
       else:
           form = RegistrationForm()
       return render(request, 'register.html', {'form': form})
   
   @login_required
   def profile(request):
       user = request.user
   
       return render(request, 'profile.html', {'user': user})
   
   @user_passes_test(is_customer)
   def customer_dashboard(request):
   
       return render(request, 'customer_dashboard.html')
   
   @user_passes_test(is_technical_worker)
   def technical_worker_dashboard(request):
   
       return render(request, 'technical_worker_dashboard.html')
   
   @user_passes_test(is_senior_management)
   def senior_management_dashboard(request):
   
       return render(request, 'senior_management_dashboard.html')
   
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
       
   def user_logout(request):
       logout(request)
       return redirect('login')
 ```


### Step 7: Create Registration Form
a) Create a new file named in `forms.py` in the app.
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
           fields = ['username', 'email', 'role', 'password1', 'password2']
   
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

### Step 8: Configure URL route
a) Open `urls.py` file and insert the code.
```python
   from django.contrib import admin
   from django.urls import path
   from storyportal.views import user_login, register, customer_dashboard, technical_worker_dashboard, senior_management_dashboard, redirect_dashboard, user_logout
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', register, name='register'),
       path('register/', register, name='register'),
       path('login/', user_login, name='login'),
       path('dashboard/', redirect_dashboard, name='dashboard'),
       path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
       path('technical_worker_dashboard/', technical_worker_dashboard, name='technical_worker_dashboard'),
       path('senior_management_dashboard/', senior_management_dashboard, name='senior_management_dashboard'),
       path('logout/', user_logout, name='logout'),
   ]
   ```


### Step 9: Create both HTML file

a) `login.html`
```
<!DOCTYPE html>

<html>

<body>

{% extends 'base.html' %} {% block content %}
<h2>Login</h2>
<form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button type="submit">Login</button>
</form>
{% endblock %}

</body>

</html>
```


b) `register.html`
```
<!DOCTYPE html>

<html>

<body>

{% extends 'base.html' %} {% block content %}
<h2>Register</h2>
<form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button type="submit">Register</button>
</form>
<br>
<text>Already have an account? <a href="{% url 'login' %}">Login</a></text>
{% endblock content %}

</body>

</html>
```



### Step 10: Migrate Database
a) Run the code below in the cmd.
```
python manage.py makemigrations
```
```
python manage.py migrate
```


### Step 11: Execute
```
python manage.py runserver
```


### Register
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/08dcd5b2-e3a2-43cf-889b-0c819d3d319b"></img>



### Login
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/fe86fb84-4585-4a50-a4b2-9125a278ef2f"></img>



### Dashboard Customer
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/fee6387d-4989-4ddd-9fe6-88fad42c3034"></img>



### Dashboard Technical Worker
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/47474316-eec0-434b-a560-c5305428b766"></img>



### Dashboard Senior Management
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/d5dfbab8-719b-4dbd-ae66-0eff84b76185"></img>



## Question 3 (b)
To ensure data synchronization between MySQL and MongoDB databases. We need to make sure:
- MySQL follows a relational data model
- MongoDB follows a document-based data model


In certain cases, the Dual Writes replication strategy is appropriate since it allows for real-time data synchronisation and assures data consistency between two separate databases, such as MySQL and MongoDB. The Dual Writes technique may be explored for the following reasons:

- Heterogeneous Database Support: Dual Writes is particularly useful when working with heterogeneous databases, meaning databases that have different underlying architectures or data models. In this case, MySQL and MongoDB have fundamental differences in how they store and represent data. The Dual Writes approach enables seamless integration and synchronization between these databases without requiring significant modifications to the existing database structure.


- Flexibility and Independence: Dual Writes allows you to maintain the independence of each database system. You can continue using MySQL and MongoDB for their respective strengths and features, leveraging their specific capabilities and ecosystems. The approach does not impose any strict coupling or dependencies between the databases, providing flexibility in choosing the appropriate technology for different use cases.


- Real-time Data Synchronization: With Dual Writes, changes made in one database are propagated and replicated to the other database in near real-time. This ensures that data remains consistent and up-to-date across both systems, enabling applications to access the most recent information from either database. Real-time synchronization is crucial for scenarios where immediate data consistency is required, such as financial systems, inventory management, or collaborative applications.
  

- Conflict Resolution: The Dual Writes approach includes mechanisms for handling conflicts that may arise when changes are made simultaneously in both databases. Conflicts can occur due to differences in data models, constraints, or business logic between the databases. By implementing appropriate conflict resolution strategies, such as timestamp-based conflict detection or application-specific rules, you can resolve conflicts and maintain data consistency across databases.


- Scalability and Performance: Dual Writes allows you to distribute the load and improve performance by leveraging the strengths of each database system. For example, you can utilize MySQL for transactional operations and complex querying while using MongoDB for fast read-heavy operations or document-based storage. By carefully designing the replication process and considering the specific workload patterns, you can achieve better scalability and performance characteristics for your application.


It is important to note that the Dual Writes technique necessitates careful design, development, and maintenance to ensure optimal synchronisation, conflict resolution, and performance optimisation. There may also be certain trade-offs to consider, such as additional complexity and potential overhead associated with managing numerous databases. As a result, before using the Dual Writes approach or any replication strategy, you must first assess your specific requirements, existing infrastructure, and development resources. Here are the steps involved in implementing the Dual Writes strategy:


### Step 1: Set up the MySQL and MongoDB connections
- Configure  the MySQL database connection using Django's database configuration in `settings.py` file.
- Configure connection to the MongoDB database using the pymongo library.


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/d77341a9-fd76-41ba-9659-8fbd990f5bf5"></img>


### Step 2: Define the Django model
-  In the Django application's models.py file, define the room_details model.

<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/03f24b60-c171-4d50-8beb-8a37ff5a80f4"></img>

### Step 3: Dual Writes Approach
- For this step, there will be Insert, Update and Delete.


### Step 4: Testing and Validation






## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



