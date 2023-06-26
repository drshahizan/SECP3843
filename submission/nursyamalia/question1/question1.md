<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nur Syamalia Faiqah Binti Mohd Kamal
#### Matric No.: A20EC0118
#### Dataset : [Analytics Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 1 (a)
### Prerequisites
Install the following below:
- [Python](https://www.python.org/downloads/)

### Steps
Step 1: Install Django and required dependencies:
 - Make sure you have Python installed on your system.
 - Open command prompt.
 - Install Django using pip: `pip install django`.
 - Install the Django MySQL package: `pip install mysqlclient`.
 - Install the Django MongoDB package: `pip install djongo`.
 - Install any other necessary dependencies based on your specific project requirements.

Optional: Set up the virtual environment:
- A virtual environment is a self-contained environment that allows you to install packages without changing the overall Python installation on your machine. Run the following command in your terminal to establish a virtual environment:
  ```javascript
       python -m venv myenv
  
      // activate virtual environment
      myenv\Scripts\activate
  ```

Step 2: Set up the Django project:
 - Create a new Django project using the command: `django-admin startproject analytics`.
 - Navigate into the project directory: `cd analytics`.
<img  src="./files/images/setup.png"></img>

Step 3: Set up the Django app:
- Create a new Django project using the command: `django-admin startapp analytics`.
  
Step 4: Configure the database in project settings:
 - Open the `settings.py` file located in the project 'analytics' directory.
 - Set the `DATABASES` configuration to include both MySQL and MongoDB settings. Here's an example:

 <img  src="./files/images/db.png"></img>

Step 5: Define Django models:
 - Open the `models.py` file in the 'accounts' directory.
 - Define your models according to the JSON dataset's structure. Use Django's model fields to map the JSON data fields to the database fields.
 - Repeat this steps for 'customers' and 'transaction'.

 <img  src="./files/images/ac.png"></img>
 <img  src="./files/images/cs.png"></img>
 <img  src="./files/images/tr.png"></img>

Step 6: Migrate the models:
 - Apply the initial migrations for both MySQL and MongoDB databases using the command: `python manage.py migrate`.
 - Django will create the necessary tables and collections in the databases based on your model definitions.

Step 7: Load the JSON dataset into databases:
 - Write a script or use Django's management command to load the JSON dataset into the MySQL and MongoDB databases.
 - In the script or management command, parse the JSON dataset, create Django model instances, and save them to the respective databases.

   ```javascript
     mysql_accounts = accounts.objects.using('default').all()
     mysql_customers = customers.objects.using('default').all()
     mysql_transactions = transactions.objects.using('default').all()

     mongodb_accounts = accounts.objects.using('mongodb').all()
     mongodb_customers = customers.objects.using('mongodb').all()
     mongodb_transactions = transactions.objects.using('mongodb').all()
     ```

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


