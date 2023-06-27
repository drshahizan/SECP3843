<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Vincent Boo Ee Khai
#### Matric No.: A20EC0231
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 3 (a)
### 1. Setup Environment
1. Create a and activate the Virtual Environment:
```
py -m venv myenv
myenv\Scripts\activate
```

2.Install all the needed package:
```
python pip install django
pip install mysql-connector-python
```

3. Create new Django project with the following code:
```
django-admin startproject q3
py manage.py startapp app
```

### 2. Configure Database
1. Create a new database in MySQL
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/51284dba-093a-426e-a396-9b50a10243c9"></img>

2. Configure the database setting in `setting.py` to connect with MySQL.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'q3',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Define Model 
Created a model in Django by extending the AbstractUser class. This customization allows to tailor the user model fields for three user types: customers, technical workers, and senior management.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/cacec9c3-b84c-47ba-a2be-a534e3f4cbe4"></img>

Then, set the model as default authentication model in `setting.py` as the following code:
```
AUTH_USER_MODEL = 'app.User'
```

### 4. Migrate Database
Migrate and create the databse table with these code:
```
python manage.py makemigrations 

python manage.py migrate
```
The output from terminal:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/fa0ff521-58ed-4785-8b97-4fab57c3d737"></img>

The result in MySQl:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/85c9aa43-d8c2-4d95-968a-732e56a1b599"></img>

### 5. Create Forms for User
Create a new file named 'form.py' in the app that are newly created.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/2fb1e2e7-60ec-4ed0-8012-563fb556aac3"></img>

### 6. Define Views that Handle the User Registration and Login.
These views will be responsible for managing the registration and login forms, validating user input, and interacting with the MySQL database. To begin, necessary libraries is needed to be import.
```
from app.form import UserRegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
```
We will need to write these following code to define Login for user:
```
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
                return redirect('customer_dashboard')
            elif user.user_type == 'technical_worker':
                print("Redirecting to technical worker dashboard")
                return redirect('technical_worker_dashboard')
            elif user.user_type == 'senior_management':
                print("Redirecting to management dashboard")
                return redirect('management_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')
```
Then, define register user
```
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})
```
Lastly, locate each user type to view to the related the template.
```
def customer_dashboard_view(request):
    return render(request, 'customer_dashboard.html')

def technical_worker_dashboard_view(request):
    return render(request, 'technical_worker_dashboard.html')

def management_dashboard_view(request):
    return render(request, 'management_dashboard.html')
```

### 7. Create Template for Create User Registration and Login
1. Login:
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/b22cccfd-5346-4978-9265-dc54f5284716"></img>

2. Register
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/5d1564f0-98ed-4e89-ae6e-a20667e96d62"></img>

### 8. Configure the URL
1. URL path for login and user registration.
```
from django.contrib import admin
from django.urls import path, include
from app.views import user_registration, login_view, customer_dashboard_view, technical_worker_dashboard_view, management_dashboard_view

urlpatterns = [
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', user_registration, name='user_registration'),
]
```

2. URL path for dashboard view for each user type
```
path('customer_dashboard/', customer_dashboard_view, name='customer_dashboard'),
path('technical_worker_dashboard/', technical_worker_dashboard_view, name='technical_worker_dashboard'),
path('management_dashboard/', management_dashboard_view, name='management_dashboard'),
```

### User Interface
1. Login
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/af501f19-f79a-4169-9b96-d269f7d623cb"/>

2. Register
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/c4551943-55e4-4665-a516-19b1c4b2b25e"></img>

#### Dashboard
1. Customer 
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/00a01dd0-a4a2-49a4-8403-46460d70e8f6"></img>

2. Technical Worker
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/ce4098cd-5872-46f4-a3a1-c31a10eaa6cb"></img>

3. Management
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/cbb73235-1106-4aa8-8242-50b0b95782c2"></img>

## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



