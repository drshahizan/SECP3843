<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Low Junyi
#### Matric No.: A20EC0071
#### Dataset: [Airbnb](https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb)

## Table of Contents
- [Question 2 (a)](question-2-(a))
- [Question 2 (b)](question-2-(b))

## Question 2 (a)

### Prerequisites
Download and Install All Required Software.
- [MongoDB Community Server](https://www.mongodb.com/try/download/community)<br>

- [MongoDB Shell](https://www.mongodb.com/try/download/shell) <br>
  
- [MongoDB Command Line Database Tools](https://www.mongodb.com/try/download/database-tools) <br>



### Step 1: Prepare the JSON File
- Download the dataset <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb" >listingsAndReviews</a>.

### Step 2: Start the MongoDB Server
- Move all the .exe files from MongoDB Shell and  MongoDB Command Line Database Tools into the MongoDB bin folder[C:\Program Files\MongoDB\Server\6.0\bin].  

The .exe file in MongoDB Shell:

<img src="https://github.com/drshahizan/SECP3843/assets/120614501/b1018280-1188-4172-81a0-6ba0fc9f6f3a"></img>

The .exe file in MongoDB Command Line Database Tools:
<img src="https://github.com/drshahizan/SECP3843/assets/120614501/82b86e7a-8246-4927-9c6b-1c9de55f0615"></img>

- Open Command Prompt and paste the following code and run.
```
cd C:\Program Files\MongoDB\Server\6.0\bin
```

- Start the MongoDB server by running the mongod command. 
```
mongod
```
Command Prompt:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/56d70022-c686-48cd-b7d3-83984142d527"></img>


### Step 3: Import Dataset
In cmd enter 
```mongoimport "C:\Users\user\Downloads\listingsAndReviews.json" -d AA -c db_airbnb```
The provided command mongoimport is used to import the JSON file listingsAndReviews.json into a MongoDB database named AA and the data will be stored in a collection called db_airbnb.
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/4fdcd2b0-638f-49d3-bec8-0d6dd8b340ab"></img>

The similar dataset can be found in MongoDB Compass
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/5cf55382-90be-4420-b0b2-1322c6a17172"></img>

### Step 4: Access MongoDB Shell
Repen Command Prompt and paste the following code and run.
```cd C:\Program Files\MongoDB\Server\6.0\bin```

To access the MongoDB shell, insert
```mongosh``` 
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/8b475845-844a-465c-8170-f433e1adace4"></img>

The list of all databases running on MongoDB Server including default and user-defined databases can be seen with 
``` show dbs``` 
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/2c3f4fe0-4db9-4e20-97d5-45905df7b75c"></img>

Then enter the following code to switch to the desired database where we want.
```use AA``` 
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/995d0766-a1d3-4719-91f0-83da4afbf1e6"></img>

## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



