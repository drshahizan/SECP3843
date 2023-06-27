<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: GOO YE JUI  
#### Matric No.: A20EC0191
#### Dataset: Stories Dataset

## Question 3 (a)
To create a user registration and login module in Django using a MySQL database, these are the steps that I have done:

### Step 1 : Set up Django with MySQL
Make sure that `mysqlclient` is installed with the settings define in the project folder's `settings.py` as below:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aa',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306,
    },
}
```

### Step 2 : Defining User Model
A `User` model that inherit the `AbstractBaseUser` class provided by Django. The `user_type` have been declared with 3 different values to differentiate between Customer, Technical Worker and Senior Management.
```python
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)  # Name field
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','user_type']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        app_label = 'user'
    
    def __str__(self):
        return self.email
```

Also, make sure thaat you have define `AUTH_USER_MODEL` as your `your_app_name.your_user_class_name`. In this case, mine is defined as below.<br>
![Alt text](./files/images/image-3.png)

### Step 3 : Implementating Registration View and Templates
Under this user registration, user will only be registered under user type `Customer`. For Technical Worker and Senior Management registration, it can only be implemented under the admin class.

#### Views and Forms 
In the user app's `views.py` declare the function below as the register function.
```python
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})
```
As we can see from the register view, we can see that the function used `NewUserForm` to request POST data. In the user app's `forms.py` declare the `NewUserForm` class that inherits `UserCreationForm`. Inside the class, there is a function that save the user data into the database that can be called in the register function.

```python
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email","name","password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.user_type = 'customer'
		if commit:
			user.save()
		return user
```

#### Templates
This is the template form that used to render the `NewUserForm`.
```python
                            <form method="POST">
                                {% csrf_token %}
								{% for field in register_form %}
                                <div class="form-group">
								  <label for="{{ field.id_for_label }}">{{ field.label }}</label>
								  <div class="mb-3">
									{{field|addclass:'form-control'}}
								  </div>
								  <span class="text-danger">{{ field.errors }}</span>
                                </div>
								{% endfor %}
                                <button type="submit" class="btn btn-primary btn-flat m-b-30 m-t-30">Register</button>
                                <div class="register-link m-t-15 text-center">
                                    <p>Already have account ? <a href={% url 'login' %}> Login Here</a></p>
                                </div>
                            </form>
```

#### Interface
![Alt text](./files/images/image-4.png)
![Alt text](./files/images/image-6.png)

### Step 4 : Implementating Login View and Templates

#### Views and Forms 
In the user app's `views.py` declare the function below as the user_login function.
```python
def user_login(request):
    form = LoginForm()  # Instantiate the LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Pass the POST data to the form
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'customer':
                	return redirect('customer')
                elif user.user_type == 'technical_worker':
                	return redirect('technical_worker')
                elif user.user_type == 'senior_management':
                	return redirect('senior_management')
                else:
                      return redirect('index')
            else:
                messages.error(request, "Unsuccessful Login. Invalid information.")
                return render(request, 'registration/login.html', {'form': form})
        else:
            messages.error(request, "Form validation failed")
    return render(request, 'registration/login.html', {'form': form})
```
As we can see from the register view, we can see that the function used `LoginForm` to request POST data. In the user app's `forms.py` declare the `LoginForm` class that inherits `forms.Form`.

```python
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
```

#### Templates
This is the template form that used to render the `LoginForm`.
```python
                            <form action="{% url 'login' %}" method="post">
                                <div class="form-group">
                                    <label>Email: </label>
                                    {{ form.email|addclass:'form-control'}}
                                </div>
                                <div class="form-group">
                                    <label>Password: </label>
                                    {{ form.password|addclass:'form-control'}}
                                </div>
                                {% csrf_token %}
                                <input type="hidden" name="next" value="{{ next }}" />
                                <button type="submit" class="btn btn-primary btn-flat m-b-30 m-t-30">Sign in</button>
                                <div class="register-link m-t-15 text-center">
                                    <p>Don't have account ? <a href={% url 'register' %}> Sign Up Here</a></p>
                                </div>
                            </form>
```
#### Define the URLs
From the login view, user with different user_type is redirected to different urls, hence the urls is defined as below:
```python
urlpatterns = [
    path('', index, name='index'),
    path('customer/', customer, name='customer'),
    path('technical_worker/', technical_worker, name='technical_worker'),
    path('senior_management/', senior_management, name='senior_management'),
]
```

#### Interface
Login Page: <br>
![Alt text](./files/images/image-5.png)

Senior Management Redirection: <br>
![Alt text](./files/images/image-7.png)

Customer Redirection: <br>
![Alt text](./files/images/image-8.png)

Technical Worker Redirection: <br>
![Alt text](./files/images/image-9.png)

### Step 5 : Admin View (Registration)
To add manage the User class in Django Administration, a `CustomUserAdmin` class need to be declared inside `admin.py`
```python
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'user_type', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'user_type')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('name', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'user_type', 'is_staff', 'is_superuser'),
        }),
    )
admin.site.register(User, CustomUserAdmin)
```

#### Admin User Registration 

![Alt text](./files/images/image-10.png)

![Alt text](./files/images/image-11.png)

## Question 3 (b)
To ensure that changes made in one database are accurately reflected in another, I have explored a database-specific replication techniques using a third-party integration tool **Apache Kafka**. The reason that I picked Apache Kafka is because it is a free and open-source project and it suits well to perform real-time replication. 

### Step 1 : Install and configuring Apache Kafka
1. First, we need to download ![Apache Kafka](https://kafka.apache.org/downloads). Make sure that you have downloaded the correct latest version that suits your OS. Also, download the binary version of it. <br>
![Alt text](./files/images/download.png)

2.  Extract the file and move the extracted folder to the directory where you wish to keep the files. In this case, I have extracted it to `C:` and renamed it to `kafka`, making the folder path as `C:\kafka`. Copy the folder path for further use.

3. Under `C:\kafka\config`, modify the `zookeeper.properties` file and change the `dataDir` to `C:\kafka\zookeeper-data`.
![Alt text](configuration1.png)

4. Under the same folder, modify the `server.properties` file. Scroll down to log.dirs and paste the path. To the path add /kafka-logs. This completes the configuration of zookeeper and kafka server.
![Alt text](configuration2.png)

### Step 2 : Running Apache Kafka (Do Not Close)
1. Now open command prompt and change the directory to the kafka folder `C:\kafka`. First start zookeeper using the command given below:
```python
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```
![Alt text](./files/images/image.png)

2. Then, open another command prompt and change the directory to the kafka folder `C:\kafka`. Run kafka server using the command:
```python
`.\bin\windows\kafka-server-start.bat .\config\server.properties`
```
![Alt text](./files/images/image-1.png) <br>
Now kafka is running and ready to stream data.

### Step 3 : Set up Kafka Topic
1. Create a Kafka topic for data replication
A topic is a category or feed name to which messages are published. The command to create a topic is `kafka-topics.bat --create --topic <event_name> --bootstrap-server localhost:9092 --partitions <partition_number> --replication-factor <replication_factor>`. In this case, I have created a Kafka event named `story-events` that will have 5 partitions. Make sure to cd to `C:\kafka\bin\windows`
```python
kafka-topics.bat --create --topic story-events --bootstrap-server localhost:9092 --partitions 5 --replication-factor 1
```
![Alt text](./files/images/topics.png)

### Step 4 : Set up Kafka producer
1. Install `confluent-kafka-python` package in your project to interact with Kafka in Python using `pip install confluent-kafka`.

2. Create the producer script file `send_to_kafka.py` under the folder path `management/commands` in your application folder.

```python
from django.core.management.base import BaseCommand
from django.conf import settings
from confluent_kafka import Producer, KafkaError
import json
from user.models import Story

class Command(BaseCommand):
    help = 'Send data from Story model to Kafka topic'

    def handle(self, *args, **options):
        KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'  # Update with your Kafka bootstrap servers

        # Kafka Producer configuration
        producer_config = {
            'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'client.id': 'mysql_to_mongodb_producer',  # Update with a unique client ID
        }

        # Create Kafka producer instance
        producer = Producer(producer_config)

        # Fetch data from the Story model
        stories = Story.objects.all()

        # Loop over the stories and send them to Kafka
        for story in stories:
            # Prepare the data to be sent to Kafka
            data = {
                'id': story.id,
                'href': story.href,
                'title': story.title,
                'comments': story.comments,
                'container': story.container,
                'submit_date': story.submit_date.isoformat(),
                'topic': story.topic,
                'promote_date': story.promote_date.isoformat(),
                'idJSON': story.idJSON,
                'media': story.media,
                'diggs': story.diggs,
                'description': story.description,
                'link': story.link,
                'user': story.user,
                'status': story.status,
                'shorturl': story.shorturl,
            }

            # Convert the data to JSON string
            json_data = json.dumps(data)

            # Send the JSON data to the Kafka topic using the producer
            producer.produce(topic="story-events", value=json_data)

            # Poll the producer to trigger delivery reports
            producer.poll(0)

        # Flush the producer to ensure all messages are sent
        producer.flush()

        producer.close()
```
3. Run the producer script using the command `python manage.py send_to_kafka`. <br>
![Alt text](./files/images/image-2.png)
All the data in MySQL stories table is sent to the Kafka topic.


### Step 5 : Set up Kafka consumer
1. Create the consumer script file `consume_and_save_to_mongodb.py` under the folder path `management/commands` in your application folder. Replace `AA` with your database name, `stories_story` with your collection name, `mongodb://localhost:27017` with your connection string.

```python
from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
from pymongo import MongoClient
from django.forms.models import model_to_dict
from stories.models import Story
import json

class Command(BaseCommand):
    help = 'Consume data from Kafka and save it to MongoDB'

    def handle(self, *args, **options):
        # Connect to Kafka
        consumer = KafkaConsumer(
            'story-events',
            bootstrap_servers=['localhost:9092'],
            group_id=None,
            auto_offset_reset='earliest',
        )

        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['AA']

        # Consume messages from Kafka and save to MongoDB
        for message in consumer:
            data = message.value.decode('utf-8')  # Decode the bytes to a string
            data_dict = json.loads(data)  # Parse the JSON string to a dictionary
            # Exclude the ModelState field
            data_dict.pop('_state', None)

            # Get the document id
            document_id = data_dict.get('id')

            # Check if a document with the same id already exists in the collection
            existing_story = db.stories_story.find_one({'id': document_id})
            existing_story_1 = db.stories_story_1.find_one({'id': document_id})
            if not existing_story:
                data_dict['replica'] = None
            elif not existing_story_1:
                data_dict['replica'] = 1
            else:
                data_dict['replica'] = 2

            story = Story(**data_dict)  # Create a Story object using the dictionary
            story_dict = model_to_dict(story)  # Convert the Story object to a dictionary

            # Get the replica information
            replica = data_dict.get('replica')

            # Determine the collection name based on the replica information
            if replica:
                collection_name = f'stories_story_{replica}'
            else:
                collection_name = 'stories_story'

            collection = db[collection_name]
            collection.insert_one(story_dict)

        # Close connections
        consumer.close()
        client.close()
```
3. Run the consumer script using the command `python manage.py consume_and_save_to_mongodb`. <br>
![Alt text](./files/images/consumer.png)<br>

#### First Replica
![Alt text](./files/images/consumer1.png)<br>

#### Second Replica
![Alt text](./files/images/consumer3.png)

#### Third Replica
![Alt text](./files/images/consumer4.png)


![Alt text](./files/images/consumer2.png)<br>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



