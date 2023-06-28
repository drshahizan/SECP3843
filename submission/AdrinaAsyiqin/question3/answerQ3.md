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

    ```python
    from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
    from django.db import models
    from django.utils import timezone


    class UserManager(BaseUserManager):

        def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
            if not email:
                raise ValueError('Users must have an email address')
            now = timezone.now()
            email = self.normalize_email(email)
            user = self.model(
                email=email,
                is_customer=is_customer,
                is_active=True,
                is_superuser=is_superuser,
                last_login=now,
                date_joined=now,
                **extra_fields
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_user(self, email=None, password=None, **extra_fields):
            return self._create_user(email, password, False, False, **extra_fields)

        def create_superuser(self, email, password, **extra_fields):
            user = self._create_user(email, password, True, True, **extra_fields)
            user.save(using=self._db)
            return user


    class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(max_length=254, unique=True)
        name = models.CharField(max_length=254, null=True, blank=True)
        is_customer = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        last_login = models.DateTimeField(null=True, blank=True)
        date_joined = models.DateTimeField(auto_now_add=True)

        USERNAME_FIELD = 'email'
        EMAIL_FIELD = 'email'
        REQUIRED_FIELDS = []

        objects = UserManager()

        def get_absolute_url(self):
            return "/users/%i/" % (self.pk)
        def get_email(self):
            return self.email

    ```
- In admin.py paste the following code
    ```py
        # Register your models here.
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

        from .models import User, user_type


        class UserAdmin(BaseUserAdmin):
            fieldsets = (
                (None, {'fields': ('email', 'password', 'name', 'last_login')}),
                ('Permissions', {'fields': (
                    'is_active',
                    'is_customer',
                    'is_technicalworker',
                    'groups',
                    'user_permissions',
                )}),
            )
            add_fieldsets = (
                (
                    None,
                    {
                        'classes': ('wide',),
                        'fields': ('email', 'password1', 'password2')
                    }
                ),
            )

            list_display = ('email', 'name', 'is_customer', 'last_login')
            list_filter = ('is_technicalworker', 'is_superuser', 'is_active', 'groups')
            search_fields = ('email',)
            ordering = ('email',)
            filter_horizontal = ('groups', 'user_permissions',)


        admin.site.register(User, UserAdmin)
        
    ```

- Next, register customuser app in customuser\apps.py
    ```py
    
        from django.apps import AppConfig


        class CustomuserConfig(AppConfig):
            name = 'customuser'
        
    ```

- Login a user in views.p
  
    ```py
    from django.shortcuts import render, redirect
    from django.contrib.auth import authenticate, login
    from customuser.models import user_type, User

    def signup(request):
        if (request.method == 'POST'):
            email = request.POST.get('email')
            password = request.POST.get('password')
            cs = request.POST.get('cutomer')
            tw = request.POST.get('technicalworker')
            sm = request.POST.get('senior')
            
            user = User.objects.create_user(
                email=email,
            )
            user.set_password(password)
            user.save()
            
            usert = None
            if st:
                usert = user_type(user=user,is_student=True)
            elif te:
                usert = user_type(user=user,is_teach=True)
            
            usert.save()
            #Successfully registered. Redirect to homepage
            return redirect('home')
        return render(request, 'register.html')
        
    def login(request):
        if (request.method == 'POST'):
            email = request.POST.get('email') #Get email value from form
            password = request.POST.get('password') #Get password value from form
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                type_obj = user_type.objects.get(user=user)
                if user.is_authenticated and type_obj.is_worker:
                    return redirect('cshome') #Go to customer home
                elif user.is_authenticated and type_obj.is_technicalworker:
                    return redirect('twhome') #Go to technical worker home
                elif user.is_authenticated and type_obj.is_senior:
                    return redirect('smhome') #Go to senior management home
            else:
                # Invalid email or password. Handle as you wish
                return redirect('home')

        return render(request, 'home.html')
    ```

- Access the current logged in user by calling the default request.user. We can access the curently logged in user and check the user type by querying in user_type objects.
    ```py
    from customuser.models import user_type

    def shome(request):
        if request.user.is_authenticated and user_type.objects.get(user=request.user).is_customer:
            return render(request,'customer_home.html)
        elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_technicalworker:
            return redirect('twhome')
        elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_senior:
            return redirect('smhome')
        else:
            return redirect('login')
                        
    def twhome(request):
        if request.user.is_authenticated and user_type.objects.get(user=request.user).is_technicalworker:
            return render(request,'tech_home.html)
        elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_customer:
            return redirect('cshome')
        elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_senior:
            return redirect('smhome')
        else:
            return redirect('home')

    ```
    
### Step 2: Create database table
- Configure database in the settings.py
    ``` py
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
- This will create the required databases table for user registration
    ```py
        python manage.py makemigrations
        python manage.py migrate
    ```

### Step 3: Create Views
- define views for handling user registration and login 
- in views.py create function or classes that handle the registration and login logic
- use Django built-in authentication views and forms for handling user authentication

    ```py
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

    ```py
    # urls.py
    from django.urls import
    ```

### Step 6: Integrate with frontend
- Make appropriate HTTP request to Django endpoints for user registration and authentication. 
- Runserver and a login form should be created

    ![image](https://github.com/drshahizan/SECP3843/assets/96984290/7e8817a7-7938-4778-84f8-dee638b8134c)

 
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

### Example
- The following code demonstrates the basic concept of using triggers in MySQL to capture data changes and replicating to MongoDB. It is important to consider additional aspects such as error handling, data type conversions, handling updates, and deletions, conflict resolutions and monitoring the replication process.
- The code begins by specifying the connection details for both MySQL and MongoDB databases.
- A MySQL trigger is created using a SQL query. This trigger is set to execute after an insert operation on a specific MySQL table. In this example, the trigger captures the inserted data and inserts it into the MongoDB collection.
- The code enters a continuous loop to monitor the MySQL database for changes. It executes a query to fetch the rows that have been inserted since the last replication timestamp. The fetched rows are then transformed into MongoDB documents and inserted into the MongoDB collection.
- After each replication iteration, the last replication timestamp is updated to ensure that only new data is replicated in subsequent iterations.


    ```py
    import pymysql
    import pymongo
    from pymongo import MongoClient

    # MySQL Connection Configuration
    mysql_host = 'localhost'
    mysql_port = 3306
    mysql_user = 'root'
    mysql_password = ''
    mysql_database = 'db_sales'

    # MongoDB Connection Configuration
    mongo_host = 'localhost'
    mongo_port = 27017
    mongo_user = 'adrinaasyiqin'
    mongo_password = 'Adrina857600'
    mongo_database = 'salesdatabase'

    # Connect to MySQL and MongoDB
    mysql_connection = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_database)
    mongo_client = MongoClient(f"mongodb://adrinaasyiqin:Adrina857600@cluster0.yvk5zzq.mongodb.net:27017/salesdatabase")
    mongo_db = mongo_client[mongo_database]
    mongo_collection = mongo_db['salessample']

    # Create a trigger in MySQL to capture data changes
    mysql_cursor = mysql_connection.cursor()
    trigger_query = """
        CREATE TRIGGER mysql_to_mongo_trigger AFTER INSERT ON mysql_table
        FOR EACH ROW
        BEGIN
            INSERT INTO mongo_collection (field1, field2, field3)
            VALUES (NEW.field1, NEW.field2, NEW.field3);
        END;
    """
    mysql_cursor.execute(trigger_query)

    # Continuously monitor the MySQL database for changes and replicate them to MongoDB
    while True:
        mysql_cursor.execute("SELECT * FROM mysql_table WHERE created_at > last_replication_timestamp")
        rows = mysql_cursor.fetchall()
        for row in rows:
            document = {
                'field1': row[0],
                'field2': row[1],
                'field3': row[2]
            }
            mongo_collection.insert_one(document)
        
        # Update the last replication timestamp
        last_replication_timestamp = get_current_timestamp()

    # Close the connections
    mysql_cursor.close()
    mysql_connection.close()
    mongo_client.close()


    ```




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

