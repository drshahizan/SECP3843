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
### Instructions To Integrate Django with Json Dataset with MySQL and MongoDB Databases
### Step 1: Install and Configure Django
   
- Install python from official Python Website (https://www.python.org/downloads/) and follow instructions for operating system. 

- Download latest version of Python for windows by clicking on 'Download Python'

- Run downloaded installer .exe file

- Select option 'Add python PATH' and choose the 'Customize installation' option. In the customisation screen, ensure pip package and the 'add python to environment' variables option is selected
   
- Open command prompt and execute each of the following 
    ```s
    pip install django
    pip install pymongo
    pip install mysqlclient
    ```
    ![WhatsApp Image 2023-06-27 at 15 41 48](https://github.com/drshahizan/SECP3843/assets/96984290/f8fcea37-f079-4cc3-9d6f-0728c09e8a4e)

    ![WhatsApp Image 2023-06-27 at 15 42 21](https://github.com/drshahizan/SECP3843/assets/96984290/fd84853c-1477-4711-b7de-e42f661f9c94)

    ![WhatsApp Image 2023-06-27 at 15 42 58](https://github.com/drshahizan/SECP3843/assets/96984290/cea83ec3-0977-4671-8f77-1a8a05b424fd)

### Step 2: Create Django Project Folder

- Create a project folder and open it in Visual Studio Code

- Run the following command. `myproject` can be renamed to desired name
 
    ```python
    #start project
    django-admin.py startproject store

    #Move into project directory using the command 
    cd store

    #startapp
    python manage.py startapp STDE

    #Open a new terminal and install virtual environment by running the below command. `myenv` can be replaced with desired name
    virtualenv myenv

    #Activate virtual environment by running command 
    myenv\Scripts\activate
    ```

    ![WhatsApp Image 2023-06-27 at 15 53 11](https://github.com/drshahizan/SECP3843/assets/96984290/0e175134-f986-4f96-aec0-bcb3a5ddb31f)


### Step 3: Run Server

- Go into project directory and run the command
    ```python
    python manage.py runserver
    ```

- Open the web browser and visit the link given
   
    ![image](https://github.com/drshahizan/SECP3843/assets/96984290/92a6f40c-1769-4b1b-8aa0-494ab73b1562)


### Step 4: Configure Django Settings
- Open settings.py 

- Configure DATABASES dictionary to configure both MySQL and MongoDB connections
   
- Update INSTALLED_APPS list to include neccessary Django apps and django_pandas
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'store',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3307',
        },
        'mongodb': {
            'ENGINE': 'djongo',
            'NAME': 'store',
            'CLIENT': {
                'host': 'cluster0.yvk5zzq.mongodb.net',
                'username': 'adrinaasyiqin',
                'password': 'Adrina857600',
                
            }
        }
    }
    ```

    ![image](https://github.com/drshahizan/SECP3843/assets/96984290/cf239ac3-6587-4dfe-adc1-546dcabc15b6)

### Step 5: Migrate Database Schema
- Run `python manage.py migrate` command to create necessary models for the database

- Check if migration ran successfully and table created in both databases

### Step 6: Import sales.json Into Databases
- Create a new python file named `import_json_data.py`

- Open file and import modules using the following command
    ```python
    from django.core.management.base import BaseCommand
    from django.conf import settings
    from yourapp.models import YourModel  # Replace "YourModel" with the appropriate model name for your JSON dataset
    import json
    ```

- Define class that inherits from BaseCommand
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

- Save the file and run management command
    ```s
    python manage.py import_json_data
    ```

### Step 7: Implement Dynamic Web Pages
- create django views and templates to generate web pages based on the data stored in the databases

- Write django queries to retrueve data from both MySQL and MongoDB databases

- Use the retrieved data to render dynamic content in the templates

- Test the web pages to ensure the integration is working as expected.


## Question 1 (b)
### System Architecture

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
   
    The User Interface, developed using web technologies like HTML, CSS, and JavaScript, allows users to interact with the application visually. It communicates with the Django web server through HTTP requests and receives responses for display to the user.

2. <b>Django Web Server</b>
   
    The Django Web Server is the core component of the system, built on the Python web framework. It handles server-side logic, processes HTTP requests from the User Interface, integrates with databases, and manages URL routing, request handling, and template rendering.

3. <b>MySQL Database</b>   
    
    Django interacts with MySQL through the Django ORM (Object-Relational Mapping). The ORM maps database tables to Django models, simplifying data communication between the web server and the database. It enables efficient data storage, retrieval, and manipulation operations while maintaining data integrity and consistency.

4. <b>MongoDB Database</b>
   
    Django integrates with MongoDB using appropriate connectors or libraries. This integration allows Django to utilize MongoDB as an alternative database backend, enabling developers to define models and perform CRUD operations. By leveraging MongoDB's scalability and flexibility, our system efficiently stores and retrieves data, adapting to evolving application needs.

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

