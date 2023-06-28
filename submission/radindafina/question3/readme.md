<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: RADIN DAFINA BINTI RADIN ZULKAR NAIN
#### Matric No.: A20EC0135
#### Dataset: [Supply Store](https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales)

## Question 3 (a)
### Prerequisite
  - ``pip install mysqlclient``
  - supplystore Database

### Set up

1. Connect to database. 
   
 ```python
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'supplystore',
      'USER' : 'root',
      'PASSWORD' : '',
      'HOST' : 'localhost',
      'PORT' : '3306',
  },
}
```

models.py 

 ```python
from django.contrib.auth.models import AbstractUser, Group, Permission
class CustomUser(AbstractUser):
    customer = models.BooleanField(default=False)
    technical_worker = models.BooleanField(default=False)
    senior_management = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')

```

views.py - index
```python
def index_view(request):
    # Add your logic here
    return render(request, 'index.html')
```

views.py - login
```python
def login_view(request):
    if request.method == 'POST':
        # Retrieve the username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'password':
            # If the login is successful, you can redirect to a success page
            return redirect('/success/')
        else:
            # If the login fails, you can render the login page again with an error message
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

    # If the request method is GET, render the login page
    return render(request, 'login.html')
```
views.py - register
```python
def register_view(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            role = request.POST.get('role')
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                error_message = "Username already exists. Please choose a different username."
                return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')
```

index.html
```python
<body>
    <div class="container">
        <h1>Welcome to Supply Store</h1>
        <p>Your one-stop shop for all your supply needs.</p>
        <div class="button-container">
            <a href="/login">Login</a>
            <a href="/register">Register</a>
        </div>
    </div>
</body>
```

  <div align="center"><img src="files/images/index.png" height="500px" /></div>
  
login.html
```python
<body>
    <div class="container">
        <h2>User Login</h2>
        <form action="/login" method="post">
            {% csrf_token %}
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <button type="submit">Login</button>
            </div>
        </form>
    </div>
</body>
```

  <div align="center"><img src="files/images/login.png" height="500px" /></div>
  
register.html
```python
<body>
    <div class="container">
        <h2>User Registration</h2>
        <form action="/register" method="post">
            {% csrf_token %}
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="role">Role:</label>
                <select id="role" name="role" required>
                    <option value="">Select Role</option>
                    <option value="customer">Customer</option>
                    <option value="technical_worker">Technical Worker</option>
                    <option value="senior_management">Senior Management</option>
                </select>
            </div>
            <div class="form-group">
                <button type="submit">Register</button>
            </div>
        </form>
    </div>
</body>
```
  <div align="center"><img src="files/images/register.png" height="500px" /></div>

## Question 3 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




