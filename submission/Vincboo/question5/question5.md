<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Vincent Boo Ee Khai
#### Matric No.: A20EC0231
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)
## Question 5 (a)
It  is imortant to optimize the performance when dealing with large JSON data. There are quite a few ways of dealing it such as indexing and data caching.
### 1. Method 1:  Data Indexing 
Indexing can help to optimize the database management system by minimizes the need for excessive disk input/output operations and quickly locate the desired data based on the search criteria.

#### 1. Select the collection that you want to create index in MongoDB Compass.

<img src="https://github.com/drshahizan/SECP3843/assets/120615951/e8a3ec80-7c71-42b3-891d-b12982c269bb"/>

#### 2. Click on 'Index' at the navigation bar.

<img src="https://github.com/drshahizan/SECP3843/assets/120615951/758b5a7a-7d07-4051-8449-ab81e9610e42"/>

#### 3. Click on 'Create Index' button.

<img src="https://github.com/drshahizan/SECP3843/assets/120615951/08a0f8aa-bff6-4055-a6ae-20111308f314"/>

#### 4. Select the field that wanted to create index.

##### 1. Topic
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/20c1a61d-1969-40c0-b5ba-04ebebb9fd92"/>

2. Diggs
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/18be9333-c79f-4065-ab88-259455bff296"/>

3. User
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/181f42a5-dac3-44b6-9780-1bb4c395e0aa"/>

### 2. Method 2: Data Caching

#### 1. Install needed package `pip install cachetools`
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/08f81b8c-d342-4a31-bec2-d2048c15cd75"/>

#### 2. Set default connection in `setting.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'NAME': 'AA',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
            'port': 27017,
            'username': '',
            'password': '',
        }
    }
}
```
#### 3. Define function 
1. Define the for getting cache data
```
from django.core.cache import cache
from django.shortcuts import render

def get_data_from_cache_or_source():
    data = cache.get(cache_data)
```
2. To ensures that only None values are considered for fetching data from the database.
```
if data is None:
```
3. Define database and collection to get data from MongoDB
```
client = MongoClient('mongodb://localhost:27017')
db = client['AA']
collection = db['Stories']
```
4. Get data collection and retrieve data, then store in cache
```
data = list(collection.find())
cache.set(cache_data, data)
```

## Question 5 (b)
In this section, I am going to create my dashboard using the provide servidse on MongoDB Atlas
### 1. Login into [MongoDB Atlas](https://account.mongodb.com/account/login?nds=true) through any web browser
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/2f8bd64a-a420-493d-8791-97c1cc0a5fb0"/>

### 2. Select `Chart` in the navigation bar
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/2abffb6f-befa-4c77-9a40-8d9c167be5de"/>

### 3. Create New Dashboard and click on 'Add Chart'
Create dashboard\
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/ecece719-b236-4c84-84c5-0a8832479c32"></img>

Add Chart\
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/ff3edd76-3303-40a1-bc67-e0f7b951fa7f"/>

### 4. Select the collection that wanted to be use in the project.
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/458daa91-2e11-4cb5-9ac9-d2318e5c8f65"/>

### 5. We will need to drag the variable to where we want it to be(x-axis, y-axis)
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/14d2bf72-1e2e-4ed8-a8c6-8ce75e401442"/>

### Results:
#### 1. Media published by Top 10 Writters
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/f7f66aba-8e97-475a-95f3-24594ff89627"/>

#### 2. Comment by Media
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/701b1c48-6843-4c83-b1ba-d8a01c779c93"/>

#### 3. Comments by Topics
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/ab2dfe5a-7202-4b41-bb41-24bbefc180c9"/>

#### 4. Stories by Media
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/1f9980ad-f046-4ef9-9d78-9197c43c413d"/>

#### 5. Vote by Media
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/971a505f-3bcc-4cad-9b6e-42db19615564"/>

#### 6. Vote for Media in each Topic
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/5f25cc90-b0f2-4150-8b15-f5cecb114176"/>

#### 7. Dashboard
<img src="https://github.com/drshahizan/SECP3843/assets/120615951/880867f7-a519-49fc-ad20-8ead932dafac"/>





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




