<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Amirah Raihanah binti Abdul Rahim
#### Matric No.: A20EC0182
#### Dataset: Tweets

## Question 2 (a)
### Step-by-step process to add the data from the JSON file into MongoDb
1. Prepare the JSON file to the correct format.
* Navigate to [Tweets Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets) to download the dataset.
* MongoDB has its specific document format for JSON files to be imported in the database. Therefore, it is crucial to check the documents structure before importing to the database. It is found out that the dataset file is not correctly formated. Hence, an additional step is needed to format the JSON data file.
* To prepare the data into correct JSON array, it needs to have bracket [ at beginning and end of the file. So the object is in [] and seperated with ','. I use Python to prepare the data and Google Colab as the code editor. Below I attached the link to Google Collab and the modified dataset.
   * Data preparation : [Data Preparation](https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question2/files/code/modifyjson.ipynb)<br>
      <img width="655" alt="image" src="./files/images/modifyjson.png">
   * Modified JSON file :[modifiedtweets.json](https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question2/files/modifiedtweets.json)<br>
2. Install the required software.
* MongoDB Community Server Download : [Link](https://www.mongodb.com/try/download/community)
* MongoDB Shell Download : [Link](https://www.mongodb.com/try/download/shell)
* MongoDB Command Line Database Tools Download : [Link](https://www.mongodb.com/try/download/database-tools)
3. Start the MongoDB server
* After downloading the software, copy the files and paste into `C:\Program Files\MongoDB\Server\6.0\bin`. It should look like this :
  <img width="655" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question2/files/images/downloadserver.png">
* Next, navigate to your local command prompt and go to Mongodb Server directory `C:\Program Files\MongoDB\Server\6.0\bin`.
  <img width="655" alt="image" src="./files/images/goserver.png">
* Then, type `mongosh` in command prompt as below : 
  <img width="655" alt="image" src="./files/images/mongosh.png">
* Change the database used by running this command `use tweets`. 
  <img width="655" alt="image" src="./files/images/tweets.png">
* Then, proceed to importing the JSON file by using this `mongoimport` command. In the command we specify the database : `tweets` and the collections : `tweetsdata` 
  <img width="655" alt="image" src="./files/images/import.png">
* Check in Mongodb Compass to ensure the file have been imported succesfully.
  <img width="655" alt="image" src="./files/images/impoert.png">
* tweets JSON dataset imported succesfully!
## Question 2 (b)
## Five MongoDB Queries

Go to command prompt and run the `mongosh` command to continue with querying MongoDB data.
<img width="655" alt="image" src="./files/images/mongosh.png">

### Create
 * To create or insert in MongoDB there are 2 methods which are 
	* `insertOne()` : This method insert a single object.
	* `insertMany()` : This method insert array of objects.
 * I will use the `insertOne()` method. Below is the command to use this method :
   <img width="655" alt="image" src="./files/images/insertop.png">
 * The data inserted succefully into the tweets database.
   <img width="655" alt="image" src="./files/images/endson.png">

### Read
 * To read data from MongoDB, I use the `find()` method.
 * I wanted to find this ` id : 22819398000 `from the database.
 * Below is the command to find the id and results :
   <img width="655" alt="image" src="./files/images/readop.png">
 * To ensure that the data exist, check in MongoDB Compass :
   <img width="655" alt="image" src="./files/images/read.png">
   
### Update
In MongoDB the are 2 methods to update your database which are<br>
	* `updateOne()` : This method update only one object.<br>
	* `updateMany()` : This method update array of objects.<br>
  I am going to demonstrate using both of the methods.

1. Update `id : 22819398000 ` and set `contributors = 2` using `updateOne()` method <br>
   i) In Mongosh, run the command below by specifying the id and what attributes you wish to      update :
 <img width="655" alt="image" src="./files/images/update2.png">
  ii) Before the update command :
 <img width="655" alt="image" src="./files/images/bfrupdate1.png">
  iii) After the update command :
 <img width="655" alt="image" src="./files/images/afterupdate1.png">
  iv) Succesfully updated the object! <br>
 
2. Update ` retweet_count: null ` and set `retweet_count: 0` using `updateMany()` method <br>
   i) In Mongosh, run the command below by specifying attributes you wish to      update :
 <img width="655" alt="image" src="./files/images/update1.png">
  ii) Before the update command :
 <img width="655" alt="image" src="./files/images/beforeupdate.png">
  iii) After the update command :
 <img width="655" alt="image" src="./files/images/afterupdate.png">
  iv) Succesfully updated the object!

### Delete
 * To delete data from MongoDB, I use the `deleteOne()` method.
 * I wanted to delete this ` id : 22819397800 `from the database.
 * Below is the command to delete the id and the result:
    <img width="655" alt="image" src="./files/images/deleteresult.png">
 * Before the delete command  :<br>
    <img width="655" alt="image" src="./files/images/beforedelete.png">
 * After the delete command  :<br>
    <img width="655" alt="image" src="./files/images/afterdelete.png">\
 * Succesfully deleted the object!

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



