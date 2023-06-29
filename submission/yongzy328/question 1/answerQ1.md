<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Yong Zhi Yan
#### Matric No.: A20EC0172
#### Datatset: City Inspections	

## Question 1 (a)
The 5 servers of this project are implemented as below:
<table>
  <thead>
    <th>Server</th>
    <th>Functionality</th>
  </thead>
  <tbody>
    <tr>
      <td>Web server</td>
      <td>Used to handle the network routings (including the incoming requests and outgoing responses) between the user's browser and the Django framework through HTTP protocols. Examples of web server services are Apache HTTP Server, Nginx, and Microsoft IIS.</td>
    </tr>
    <tr>
      <td>Database Server 1 (MySQL)</td>
      <td>Used to host the MySQL database for the system. It is crucial in handling the client's request from the application and executing the database operations such as inserting, querying, updating and deleting through the SQL queries. Django application will connect to this database using the package <code>mysqlclient</code>.</td>
    </tr>
    <tr>
      <td>Database Server 2 (MongoDB)</td>
      <td>Used to host the MongoDB database for the system. It is significant in handling high volume of unstructured data of the Django application through the processes of storing and retrieving. The package <code>djongo</code> is applied to manage the connection between Django framework and MongoDB database.</td>
    </tr>
    <tr>
      <td>File Server</td>
      <td>Used as a file storage system that responsible for managing all the files which will be accessed by the users through the application or system over the network. Example of file servers are Server Message Block (SMB) and Network File System (NFS) which enable the files to be accessed remotely by the client.</td>
    </tr>
    <tr>
      <td>Load Balancer</td>
      <td>Used to evenly distribute the incoming and outgoing network traffic accross the available servers in order to optimize the overall performance, increase realibility and prevent overload of the Django application. </td>
    </tr>
  </tbody>
</table>

### Steps to Integrate Django with JSON dataset
#### 1. Set up a new Django application
Using the Command Prompt (CMD), change the directory to the created project folder's location (the AA folder in this case) and then set up a virtual environment for it by running the command <code>py -m venv env</code>. Then run the virtual environment by using the command <code>env\Scripts\activate</code>. <br>
<img src="./files/images/Screenshot%202023-06-27%20153108.png" alt="activate virtual environment"><br>
Install the neccessary packages using the code <code>pip install django mysqlclient pymongo</code>. Django is necessary for the implementation of Django framework, mtsqlclient is needed to connect MySQL database to Django framework, whereas pymongo is used to connect MongoDB database to the Django framework.<br>
<img src="./files/images/Screenshot%202023-06-27%20153218.png" alt="install django mysqlclient pymongo"><br>
Install the djongo package using the code <code>pip install djongo</code> to translate the SQL queries into MongoDB queries. <br>
<img src="./files/images/Screenshot%202023-06-27%20153237.png" alt="install djongo"><br>
Create a new project named "CityAA" using the command <code>django-admin startproject CityAA</code>. <br>
<img src="./files/images/Screenshot%202023-06-27%20153149.png" alt="django start project"><br>
Create a new Django application named "CityAAdata" in the directory of the CityAA project using the command <code>python manage.py startapp CityAAdata</code>. <br>
<img src="./files/images/Screenshot%202023-06-27%20153205.png" alt="startapp"><br>

#### 2. Set up the setting of the application
In the settings.py file, update information of the newly created application in the installed_apps as shown as below. <br>
<img src="./files/images/Screenshot%202023-06-27%20164105.png" alt="setting.py"><br>
Update the database credential information in the database setting as shown as below. <br>
<img src="./files/images/Screenshot%202023-06-28%20015242.png" alt="database setting"><br>

#### 3. Create model of the application
The model of application is set according to the data types of the dataset provided as shown below. <br>
<img src="./files/images/Screenshot%202023-06-28%20153939.png" alt="model"><br>

#### 4. Migrate to database
All the data of the application will be migrated to the database in order to store them efficiently. The command <code>python manage.py makemigrations</code> is run to intialize the migration process. <br>
<img src="./files/images/Screenshot%202023-06-28%20015411.png" alt="make migrations"><br>
After that, the data are migrated to the database using the command <code>python manage.py migrate</code><br>
<img src="./files/images/Screenshot%202023-06-28%20015441.png" alt="migrate"><br>
All the data is successfuly migrated to the database as shown as the sceenshot below.<br>
<img src="./files/images/Screenshot%202023-06-28%20015852.png" alt="mysql after migration"><br>

#### 5. Load JSON file into database
In order to load JSON file into the Django model and database, a script named "loaddata.py" is written and saved in the same directory as the manage.py file. <br>
<img src="./files/images/Screenshot%202023-06-28%20153924.png" alt="loaddata.py"><br>
The command <code>python manage.py loaddata city_inspections.json</code> is run to load the data into the database. Note that within the command above, "city_inspections.json" is the JSON file which I am loading, it can be replaced by any other desired json file. <br>
<img src="./files/images/Screenshot%202023-06-28%20162050.png" alt="loaddata json"><br>
The loaded JSON data can be viewed in the database. <br>
<img src="./files/images/Screenshot%202023-06-28%20162035.png" alt="load data success"><br>


## Question 1 (b)
<img src="./files/images/use%20case%20diagram%20(current%20system)%20-%20Page%203.png" alt="system architecture"><br>

The diagram above shows the system architecture of the application. The structure of this system can be viewed from a few perspectives, which are the end-users, front-end architecture and back-end architecture. 

#### End-user
The end-users of this system include the customers, technical workers and senior management team. The users are able to register and login into the system in order to access the information stored in the system, and also make modifications towards the data, such as inserting new data, updating existing data, or deleting unwanted data. 

#### Front-end architecture
The front-end of the system consisits of the user interfaces where the users can access to the system. The user interfaces link the users together with the back-end of the system, the Django application, using HTML web pages, where users can view and make changes to the application through HTML forms. 

#### Back-end archituecture
The back-end of the system is the core of the Django application, which consists of the application itself in the structure of Model-View-Template (MVT), MySQL database, MongoDB database and the JSON dataset. 

1. Django framework: <br>
<li>Model: The component where the data structure of the application is defined. Connect to databases via the database connector such as <code>mysqlclient</code> and <code>djongo</code>. </li>
<li>View: The place where data is proceesed and retireved from the databases. Acts as the intermediate connection between the model and template. </li>
<li>Template: Consists of HTML-based structure which is integrated along with the render of Django to generate a dynamic content to the user. </li>

2. MySQL database <br>
Used to store data and manage user credential information securely. Connected to the Django framework using the package <code>mysqlclient</code>.

3. MongoDB database <br>
Used to handle (store and manipulation) the unstructured or semi-structured data of the application. The JSON file is stored in this database. Connected to the application using <code>djongo</code>.

4. JSON file <br>
Consists of the dataset which stored in JSON format. 




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



