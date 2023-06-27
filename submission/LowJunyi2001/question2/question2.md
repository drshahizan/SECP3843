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
- MongoDB Community Server <br>
  Navigate to https://www.mongodb.com/try/download/community and click download button.
  <p align="center">
    <img height="300px" src="https://github.com/drshahizan/SECP3843/assets/120614501/adaec4b0-0a47-441b-8910-2c98f7a9d1b0"></img>
  </p>

- MongoDB Shell <br>
Navigate to https://www.mongodb.com/try/download/shell and click download button.
  <p align="center">
    <img height="300px" src="https://github.com/drshahizan/SECP3843/assets/120614501/f34b209a-8825-4c4c-994b-49beb588c0e8"></img>
  </p>
  
- MongoDB Command Line Database Tools <br>
Navigate to https://www.mongodb.com/try/download/database-tools and click download button.
  <p align="center">
    <img height="300px" src="https://github.com/drshahizan/SECP3843/assets/120614501/9031c90e-3582-445a-a2e3-b52b627a15f3"></img>
  </p>

### Step 1: Prepare the JSON File
Download the dataset from <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb" >listingsAndReviews</a>. It is important to ensure the JSON file follows the appropriate structure for MongoDB documents. It is found that the listingsAndReviews.json file is not formatted correctly as a JSON array. Therefore, python will be used to perform data preparation by adding brackets at the beginning and end of the file. Each individual tweet object should be enclosed within square brackets '[ ]' and separated by commas ','. <br>

```Data Preparation```: <a href="./files/code/Data_Preparation.ipynb">Data_Preparation.ipynb</a> <br>

### Step 2: Start the MongoDB Server
After download is completed, extract and copy all the .exe files from MongoDB Shell and  MongoDB Command Line Database Tools into the MongoDB bin folder[C:\Program Files\MongoDB\Server\6.0\bin].  

The .exe file in MongoDB Shell:

<img src="https://github.com/drshahizan/SECP3843/assets/120614501/b1018280-1188-4172-81a0-6ba0fc9f6f3a"></img>

The .exe file in MongoDB Command Line Database Tools:
<img src="https://github.com/drshahizan/SECP3843/assets/120614501/82b86e7a-8246-4927-9c6b-1c9de55f0615"></img>

Then, open the command prompt and navigate to the MongoDB installation directory.
```
cd C:\Program Files\MongoDB\Server\6.0\bin
```

Start the MongoDB server by running the mongod command. 
```
mongod
```
Command Prompt:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/56d70022-c686-48cd-b7d3-83984142d527"></img>


## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



