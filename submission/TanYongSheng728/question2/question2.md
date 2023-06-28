<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Tan Yong Sheng
#### Matric No.: A20EC0157
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets">Tweets</a>

## Question 2 (a)
### Prerequisites
Before I import the json file into the database, I need to ensure that all the required software are installed to add <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets">Tweets</a> dataset into MongoDB. Below are the required software:
<li><strong><a href = "https://www.mongodb.com/try/download/community">MongoDB Community Server</a></strong>
<li><strong><a href = "https://www.mongodb.com/try/download/database-tools">MongoDB Database Tools</a></strong>
<li><strong><a href = "https://www.mongodb.com/try/download/shell">MongoDB Shell</a></strong>
<br>

#
### 1: JSON File Preparation
 - Firstly, download the file JSON file from <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets">Tweets</a> which contain 1 file only. <br>
 - Next the JSON file need to be verified to ensure the structure is correct. This step is perform by using google collab. <br>
  <p align="center">
    <img src="./files/images/tweets validation.png"></img>
  </p>

 - From the output we can see that this tweets.json file format is not exactly correct. Threrfore I need to perform file checking to find out the error in JSON file. <br>
 - After checking, it seems that the array is not enclosed with a square bracket "[ ]" and missing a comma "," between each object. Therefore the code below modified the JSON file into correct format.
  <p align="center">
    <img src="./files/images/fix tweets.png"></img>
  </p>

 - From the output, it shows that JSON file has been fixed. Means that the file is in correct format and ready to be imported to mongodb.
   <p align="center">
    <img src="./files/images/fix proof.png"></img>
  </p>

a. Google Collab for JSON preparation : <a href = "https://github.com/drshahizan/SECP3843/blob/main/submission/TanYongSheng728/question2/files/code/tweets_validation.ipynb">tweets_validation.ipynb</a>
<br>
b. Modified tweets.json : <a href = "https://github.com/drshahizan/SECP3843/blob/main/submission/TanYongSheng728/question2/files/code/modified_tweets.json">modified_tweets.json</a>

#
### 2: Start the MongoDB Server
 - Before we start the MongoDB server, we need to transfer all the .exe file from the mongodb shell and database tools into the server bin folder.
 
 The .exe file in MongoDB Shell:
<p align="center">
<img src="./files/images/exeshell.png"></img>
</p>
The .exe file in MongoDB Command Line Database Tools:
<p align="center">
<img src="./files/images/exetools.png"></img>
</p>

 - Open the command prompt and navigate to the MongoDB installation directory. (C:\Program Files\MongoDB\Server\6.0\bin)
```
cd C:\Program Files\MongoDB\Server\6.0\bin
```

 - Then start the MongoDB server by running the mongod command. 
```
mongod
```

Command Prompt: 
<p align="center">
<img src="./files/images/prompt.png"></img>
</p>

#
### 3: Access MongoDB Shell
 - Before we access the mongodb Shell, navigate to MongoDB Atlas and login to your account. 
 - In the database page click the "Connect" button at the cluster created.
<p align="center">
    <img src="./files/images/atlas.png"></img>
</p>

 - Select Shell
 <p align="center">
    <img src="./files/images/connect shell.png"></img>
</p>

 - Lastly select "I have MongoDB Shell installed" and copy the connection string.
 <p align="center">
    <img src="./files/images/shell string.png"></img>
</p>

 - Back to the Command Prompt, paste the string copied and run.
 ```
 mongosh "mongodb+srv://tyscluster.tyt40lp.mongodb.net/" --apiVersion 1 --username tys072801
 ```

 Command Prompt: 
 <p align="center">
    <img src="./files/images/shell prompt.png"></img>
</p>

#
### 4: Selecting a database
 - Now we can select a database using command follow by database name. Since this is the first time using, creating a new database is neccessary. This can be done using the code below.
 ```
 use tweet
 ```
 <p align="center">
    <img src="./files/images/use tweet.png"></img>
</p>

#
### 5: Choosing a collection
 - Next we need to choose a collection, MongoDB will create a new one if the collection provided does not exist. The collection I have chosen is "tweets"
 ```
 db.tweets
 ```
 <p align="center">
    <img src="./files/images/tweets.png"></img>
</p>

#
### 6: Import Dataset into MongoDB
 - To import the dataset we need to open a new command prompt and run the code below with own connection string, collection and file.
 ```
 mongoimport --uri="mongodb+srv://tys072801:alextys072801AB@tyscluster.tyt40lp.mongodb.net/" --collection=tweets --file="C:\Users\Acer\OneDrive - hsdjnxye\Documents\SEM 6\SECP3843-01 SPECIAL TOPIC IN DATA ENGINEERING\modified_tweets.json" --jsonArray
 ```

<p align="center">
    <img src="./files/images/import mongo 1.png"></img>
    <img src="./files/images/import mongo 2.png"></img>
</p>

 - After complete importing, we can check the MongoDB Compass to validate the import result.

 <p align="center">
    <img src="./files/images/mongo proof.png"></img>
</p>


## Question 2 (b)
### Create a Query
There are two type of create in MongoDB which is 
 - insertOne() = insert single document to the collection
 - insertMany() = insert multiple document to the collection

 In this case I am going to use <strong>insertOne()</strong> to demonstrate the process of adding one document into mongodb.

 ```
 db.tweets.insertOne({
  text: "Tan Yong Sheng AA",
  in_reply_to_status_id: null,
  retweet_count: 3,
  contributors: null,
  created_at: "2023-06-27 10:30:00",
  geo: null,
  source: "Twitter",
  coordinates: null,
  in_reply_to_screen_name: null,
  truncated: false,
  entities: { mentions: [], urls: [], hashtags: [] },
  retweeted: false,
  place: null,
  favorited: false,
  in_reply_to_user_id: null
});
```
MongoDB Shell:
<p align="center">
    <img src="./files/images/insert proof.png"></img>
</p>

MongoDB Compass:
<p align="center">
    <img src="./files/images/insert mongo.png"></img>
</p>

#
### Read Query
There are two type of read in MongoDB which is 
 - find() = retrieve multiple document that matches the condition from the collection.
 - findOne() = retrieve first document that matches the condition from the collection

 In this case I am going to use <strong>findOne()</strong> to demonstrate the process of reading one document in mongodb where the text is "Tinha que abrir a El Divino Club aqui. muahhahaha".
```
 db.tweets.findOne({
  text = "Tinha que abrir a El Divino Club aqui. muahhahaha"
})
```
MongoDB Shell:
<p align="center">
    <img src="./files/images/find proof.png"></img>
</p>

MongoDB Compass:
<p align="center">
    <img src="./files/images/find mongo.png"></img>
</p>

#
### Update a Query
There are two type of update in MongoDB which is 
 - updateOne() = update single document that matches condition into the collection
 - updateMany() = update multiple document that matches condition into the collection

 In this case I am going to use <strong>updateOne()</strong> to demonstrate the process of updating one document into mongodb. 

 ```
 db.tweets.updateOne(
  { text: "Tan Yong Sheng AA" },
  { $set: { source: "Web" } }
)
```
MongoDB Shell:
<p align="center">
    <img src="./files/images/update proof.png"></img>
</p>

MongoDB Compass:
<p align="center">
    <img src="./files/images/update mongo.png"></img>
</p>

#
Now I am going to use <strong>updateMany()</strong> to demonstrate the process of updating multiple document into mongodb by changing the contributor from <strong>"null" to 0</strong>

```
db.tweets.updateMany(
  { contributors: null },
  { $set: { contributors: 0 } }
)
```
MongoDB Shell:
<p align="center">
    <img src="./files/images/updatemany proof.png"></img>
</p>
Successfully updated all the data in mongodb.<br><br>

MongoDB Compass:
<p align="center">
    <img src="./files/images/updatemany mongo.png"></img>
</p>
Could not find contributor with null value.

#
### Delete Query
There are two type of delete in MongoDB which is 
 - deleteOne() = delete single document that matches the condition in the collection
 - deleteMany() = delete multiple document that matches the condition in the collection

 In this case I am going to use <strong>deleteOne()</strong> to demonstrate the process of deleting one document in mongodb.

 ```
 db.tweets.deleteOne({ 
    text: "Tan Yong Sheng AA" 
})
```
MongoDB Shell:
<p align="center">
    <img src="./files/images/delete proof.png"></img>
</p>

MongoDB Compass:
<p align="center">
    <img src="./files/images/delete mongo.png"></img>
</p>
The document created at the beginning now is being deleted and cannot be found.<br><br>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



