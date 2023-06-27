<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.
# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Luqman Ariff Bin Noor Azhar
#### Matric No.: A20EC0202
#### Dataset: 03 - Movies

## Question 3 (a)
Step 1: Design database schema
We will need lay the foundation of how the module will function later on. We would need four tables, user, customer, management, and technical. Customer, management, and technical will referenced to table user. Below are the overview of the tables along with the data types.
User

| Name         | Data Type |
|--------------|-----------|
| `user_id`    | int       |
| `name`       | string    |
| `email`      | string    |
| `password`   | string    |
| `created_at` | date      |
| `user_type`  | string    |

Customer
| Name     | Data Type |
|----------|-----------|
| `id`     | int       |
| `user_id`| int       |
| `phone`  | string    |
| `address`| string    |

Technical
| Name      | Data Type |
|-----------|-----------|
| `id`      | int       |
| `user_id` | int       |


Management
| Name        | Data Type |
|-------------|-----------|
| `id`        | int       |
| `user_id`   | int       |
| `department`| string    |

![Q3](file/image/q3_db.png)

Step 2: MySQL configuration
Head over to your Django project. We will need to install some packages in order for this step to work properly. Open the terminal and run the below commands to install the necessary packages.
```
pip install mysqlclient
pip install pymysql
```
Head over to the `settings.py` file. Navigate to the databases settings which we have created. We will change the configurations. It should look like this example below:

![Q3](file/image/q3_db1.png)

Step 3: Define Model
Now we will continue by defining the models of the recently created tables. Head over to your `models.py` file and define each model class. It should look like this example below:

![Q3](file/image/q3_model.png)

Step 4: Database Migration
Once we’re done with defining the models, we will need to migrate the database. Open up a terminal and run these two commands:
```
python manage.py makemigrations
python manage.py migrate
```
Step 5: User Registration
Head over to the `accounts` app directory, open the `views.py` file. Import the modules we will be using, as such:
```
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Customer, Technical, Management
```
Create the view function for registration. It should look like this:

![Q3](file/image/q3_view_regi.png)

Head over to the `forms.py` file and create the class for our form. It should look like this:

![Q3](file/image/q3_view_form.png)

Step 6: Login
Open the terminal and run the following command to install this package:
```
pip install django.contrib.auth
```
Open `views.py` file and create your login view, it should look like this:

![Q3](file/image/q3_login.png)

Open `urls.py` and insert both paths for login and register as such:

![Q3](file/image/q3_path.png)

## Question 3 (b)
Step 1: Master Database
Head over to your MySQL configuration file `my.cnf`. 

![Q3](file/image/q3b1.png)

Open the file and set the `server_id` = 1 as such:

![Q3](file/image/q3b2.png)

Enable binary logging by uncommenting the line:

![Q3](file/image/q3b3.png)

Specify the database to be replicated:

![Q3](file/image/q3b4.png)

Step 2: Slave Database

Set your `server_id`:

![Q3](file/image/q3b5.png)

Navigate to the `[mysqld]` section and insert these lines as seen below. You can set the parameters according to your preference.

![Q3](file/image/q3b6.png)

Step 3: Import Data

Open a command prompt and run the following command (change `admin` depending on your username):
```
mysql -u admin1 -p
```
Create the database, you can name it according to your preference
```
CREATE DATABASE aa;
```
Step 4: Replicate
Connect to MySQL shell on master instance:
```
mysql -u admin -p
```
Run the following command, note down the binary file and position as it will be needed later
```
SHOW MASTER STATUS;
```
Connect to the MySQL shell on slave instance:
```
mysql -u admin1 -p
```
Configure the replication details, your log file and position might be different from the one shown in the example below:
```
CHANGE MASTER TO
MASTER_HOST = 'localhost',
MASTER_USER = 'admin',
MASTER_PASSWORD = 'admin',
MASTER_LOG_FILE = `mysql-bin.000001',
MASTER_LOG_POS = 1234;
```
Start replication on slave:
```
START SLAVE;
```


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
