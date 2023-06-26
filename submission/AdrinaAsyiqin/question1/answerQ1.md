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

## Question 1 (a)
### Step 1: Install and Configure Django
   
1. Install python from official Python Website (https://www.python.org/downloads/) and follow instructions for operating system. 

2. Download latest version of Python for windows by clicking on 'Download Python'

3. Run downloaded installer .exe file

4. Select option 'Add python PATH' and choose the 'Customize installation' option. In the customisation screen, ensure pip package and the 'add python to environment' variables option is selected
   <br>

### Step 2: Create Django Project Folder

1. Create a project folder and open it in Visual Studio Code

2. Run the following command. `myproject` can be renamed to desired name
 
```python
#start project
django-admin.py startproject myproject

#Move into project directory using the command 
cd myproject

#Open a new terminal and install virtual environment by running the below command. `myenv` can be replaced with desired name
virtualenv myenv

#Activate virtual environment by running command 
myenv\Scripts\activate
```

### Step 3: Run server

1. Go into project directory and run the command
```python
python manage.py runserver
```

2. Open the web browser and visit the link given

### Step 4: Install django
1. Ensure the virtual enironment is active

2. Run command . This will download the latest stable version of django
```python
pip install django
```

3. Verify installation by running python in the terminal. This will open a python shell and run
```
import django
```

### Step 5: Configure django settings
1. Open settings.py 

2. Configure DATABASES dictionary to configure both MySQL and MongoDB connections

3. Update INSTALLED_APPS list to include neccessary Django apps and django_pandas

### Step 6: Migrate database schema
1. Run `python manage.py migrate` command to create necessary models for the database

2. Check if migration ran successfully and table created in both databases

### Step 7: Import sales.json data into databases
1. Create a new python file named `import_json_data.py`

2. Open file and import modules using the following command
```python
from django.core.management.base import BaseCommand
from django.conf import settings
from yourapp.models import YourModel  # Replace "YourModel" with the appropriate model name for your JSON dataset
import json
```

3. Define class that inherits from BaseCommand
```python
class Command(BaseCommand):
    help = 'Imports JSON data into the MySQL and MongoDB databases'

    def handle(self, *args, **options):
        # Read the JSON file
        with open('path/to/your/json/sales.json', 'r') as f:
            json_data = json.load(f)

        # Import data into MySQL
        self.stdout.write('Importing data into MySQL...')
        for data in json_data:
            YourModel.objects.create(**data)
        self.stdout.write('Data import into MySQL completed.')

        # Import data into MongoDB
        self.stdout.write('Importing data into MongoDB...')
        for data in json_data:
            YourModel.objects.mongo_insert(data)
        self.stdout.write('Data import into MongoDB completed.')

```

4. Save the file and run management command
```python
python manage.py import_json_data
```

### Step 8: Implement dynamic web pages
1. create django views and templates to generate web pages based on the data stored in the databases

2. Write django queries to retrueve data from both MySQL and MongoDB databases

3. Use the retrieved data to render dynamic content in the templates

4. Test the web pages to ensure the integration is working as expected.


## Question 1 (b)

```
+----------------------+
|   User Interface     |
+----------------------+
       | HTTP Request
       |
       v
+----------------------+
|  Django Web Server   |
+----------------------+
       | Query
       |
       v
+----------------------+
|     MySQL Database   |
+----------------------+
       | Query
       |
       v
+----------------------+
|    MongoDB Database  |
+----------------------+
       | Result
       |
       v
+----------------------+
|  Django Web Server   |
+----------------------+
       | Response
       |
       v
+----------------------+
|   User Interface     |
+----------------------+

```
1. <b>User Interface</b>
   
The User Interface is responsible for the presentation layer of the system, allowing users to interact with the application. It is developed using web technologies such as HTML, CSS, and JavaScript, along with any relevant frontend frameworks or libraries. Users interact with the interface by inputting data, clicking buttons, or navigating through different pages. The User Interface communicates with the Django web server by sending HTTP requests, which trigger server-side processing and generate responses to be displayed back to the user.

2. <b>Django Web Server</b>
   
The Django Web Server, an advanced Python web framework, acts as the core component of the system. It manages the server-side logic and handles incoming HTTP requests from the User Interface. With its robust functionality, the web server processes these requests, executing necessary operations, and generating appropriate responses. It seamlessly integrates with the databases, enabling smooth data operations such as data retrieval and modification. Additionally, the Django Web Server takes charge of URL routing, request management, and template rendering, ensuring efficient handling of user interactions and dynamic content generation for the User Interface.

3. <b>MySQL Database</b>
   
The MySQL Database is a widely used relational database management system known for its reliability and scalability. It stores data in a structured manner, organized in tables with predefined schemas. In the context of our system, Django interacts with the MySQL Database through the Django ORM (Object-Relational Mapping). The Django ORM facilitates seamless communication between the web server and the database by mapping database tables to Django models. This abstraction layer allows developers to define models that represent the database tables and provides a convenient interface for performing queries and manipulating data. Through the Django ORM, the MySQL Database efficiently handles data storage and retrieval operations, ensuring the integrity and consistency of the system's data.

4. <b>MongoDB Database</b>
   
MongoDB is a versatile NoSQL document-oriented database that excels at handling unstructured or semi-structured data. It utilizes a JSON-like document format with dynamic schemas, offering flexibility in data representation and evolution. In our system, Django communicates with MongoDB through suitable database connectors or libraries. This integration enables Django to utilize MongoDB as an alternative database backend, empowering developers to define models and perform CRUD operations on the data. By leveraging MongoDB's scalability and flexibility, our system can effectively store and retrieve data, adapting to the changing requirements of the application.

### The Flow
1. User interacts with the User Interface and triggers an HTTP request.
2. The request is sent to the Django web server.
3. Django processes the request and performs necessary operations.
4. For data operations, Django interacts with both the MySQL and MongoDB databases.
5. Django queries the MySQL database using the Django ORM for relational data needs.
6. Django queries the MongoDB database using appropriate connectors or libraries for NoSQL data needs.
7. The databases process the queries and return the results to Django.
8. Django generates the appropriate response and sends it back to the User Interface.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

