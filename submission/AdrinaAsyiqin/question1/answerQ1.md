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

3. Verify installation by running python in the terminal. This will open a python shell 

4. run 
```
import django
```

5. check django version

### Step 5: Configure django settings
1. Open settings.py 

2. Configure DATABASES dictionary to configure both MySQL and MongoDB connections

3. Update INSTALLED_APPS list to include neccessary Django apps and django_pandas

### Step 6: Migrate database schema
1. Run `pyhton manage.py migrate` command to create necessary models for the database

2. Check if migration ran successfully and table created in both databases

### step 7: Import sales.json data into databases
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

4. Save the file

5. Run management command
```python
python manage.py import_json_data
```

### Step 7: Implement dynamic web pages
1. create django views and templates to generate web pages based on the data stored in the databases

2. Write django queries to retrueve data from both MySQL and MongoDB databases

3. Use the retrieved data to render dynamic content in the templates

4. Test the web pages to ensure the integration is working as expected.


## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
