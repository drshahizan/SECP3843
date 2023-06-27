<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Chloe Racquelmae Kennedy
#### Matric No.: A20EC0026
#### Dataset: City Inspections	

## Question 3 (a)
Continue with the project created in Question 1.

### 1. Create views
This is created for user authentication 
The code can be found here [views.py](./files/code/Portal/portalproject/portalapp/views.py)

### 2. Create templates
Create a new folder named templates in the app folder and paste all the html files used in this folder.

### 3. Create home.html
This is created as the index page of the system.
The code can be found here [home.html](./files/code/Portal/portalproject/portalapp/templates/home.html)

### 4. Create register.html
This is created to allow user to register.
The code can be found here [register.html](./files/code/Portal/portalproject/portalapp/templates/register.html)

### 5. Create login.html
This is created to allow user to enter the username and password for login.
The code can be found here [login.html](./files/code/Portal/portalproject/portalapp/templates/login.html)

### 6. Create profile.html
This is created to display the user profile when the user log in the system.
The code can be found here [profile.html](./files/code/Portal/portalproject/portalapp/templates/profile.html)

### 7. Create urls.py
Add all the urls of the html files in the templates folder.
```
from django.contrib import admin
from django.urls import path
from portalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
]
```

## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



