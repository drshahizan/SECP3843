<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: FARAH IRDINA BINTI AHMAD BAHARUDIN
#### Matric No.: A20EC0035
#### Dataset: AIRBNB LISTINGS DATASET

## Question 2 (a)

The JSON file that I have been received is about AirBnb Listing Reviews. To import this JSON file inside MongoDB database, there are a few steps that must be followed.

#### 1. Install MongoDB Command Line Database Tools

Firstly, click ![here](https://www.mongodb.com/try/download/bi-connector) to download MongoDB Command Line Database Tools. Click Download and install it.

#### 2. Install MongoDB Shell

Next, click ![here](https://www.mongodb.com/try/download/bi-connector) to download MongoDB Shell. Click Download and install it.

#### 3. Run mongosh

Then, open the directory file that has the mongosh.exe by using command prompt and type the code below. 

```
mongosh
```

![image](https://github.com/drshahizan/SECP3843/submission/FarahIrdina/question2/files/images/mongosh.png)

#### 4. Search for existing databases

Next, to search the existing databases inside your MongoDB, type the code below. 

```
show dbs
```

![image](https://github.com/drshahizan/SECP3843/submission/FarahIrdina/question2/files/images/dbs.png)

#### 5. Use any database

Next, use any database that you prefer based on the list of databases above. I will use 'admin' database to store the JSON data. Type the code below. 

```
use admin
```

![image](https://github.com/drshahizan/SECP3843/submission/FarahIrdina/question2/files/images/admin.png)

#### 6. Search for existing collections

Then, to search the existing collections inside your database, type the code below. 

```
show collections
```

![image](https://github.com/drshahizan/SECP3843/submission/FarahIrdina/question2/files/images/collections.png)

#### 7. Import JSON file into MongoDB

Lastly, you can import your JSON file into MongoDB. Type the code below. 

```
mongoimport --db admin --collection airbnb --file C:\Users\User\Downloads\listingsAndReviews.json
```

![image](https://github.com/drshahizan/SECP3843/submission/FarahIrdina/question2/files/images/mongoimport.png)

## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



