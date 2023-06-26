<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Adrina Asyiqin Binti Md Adha
#### Matric No.: A20EC0174
#### Dataset: sales.json

## Question 3 (a)
### Step 1: Define User Model
- in models.py define User model that extends Django's built in User model
- Add any additional model fields for user type : customer, technical worker, and senior management
  
### Step 2: Create database table
- Configure database in the settings.py
  ```
    # settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_sales',
            'HOST': 'localhost',
            'PORT': '3307',
            'USER': 'root',
            'PASSWORD': '',
        }
    }

  ```
- generate neessary tables based on the defined models by running migrations
- execute the following command
```
python manage.py makemigrations
python manage.py migrate
```
- This will create the required databases table for user registration

### Step 3: Create Views
- define views for handling user registration and login 
- in views.py create function or classes that handle the registration and login logic
- use Django built-in authentication views and forms for handling user authentication
```
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
```

### Step 4: Create template
- Create template for user registration and login forms
- place the template in app's template directory

### Step 5: Define URL patterns
- Configure URL pattern in the app's urls.py to map the views with appropriate URLs
- Define routes to user registration, login, logout
```
# urls.py

from django.urls import

```
### Step 6: Integrate with frontend
- Make appropriate HTTP request to Django endpoints for user registration and authentication. 

 
## Question 3 (b)
### Step 1: Database selection
Choose appropriate database replication method or tool that supports both MySQL and MongoDB databases. This could involve exploring options like native replication mechanisms provided by the database themselves or utilising third-party tools specifically designed for database synchronization

### Step 2: Configuration Setup
Configure the replication settings for both databases to establish the necessary connections and define the replicaiton behaviour. This typically involves configuring replication parameters such as replication source (MySQL) and replication target (MongoDB) settings.

### Step 3: Replication initialization
Initialise the replication process by ensuring that the target database (mongoDB) is empty or contains data consistent with the source database (MySQL). This step may require performing an initial data load from MySQL and MongoDB

### Step 4: Replication Monitoring
Set up monitoring mechanisms to track the replication process and ensure its smooth operation. This can involve monitoring tools or scripts that provide real-time status updates and alert in case of any issues or inconsistencies.

### Step 4: Testing and Verification
Thoroughly test and verify the replication setup to ensure data integrity and accuracy. Perform tests that simulate various scenarios and edge cases to validate the replication behavior.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

