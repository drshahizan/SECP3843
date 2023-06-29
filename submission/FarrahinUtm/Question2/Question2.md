![image](https://github.com/drshahizan/SECP3843/assets/121208097/9e9d377f-e061-420c-87de-266b1d920232)<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURFARRAHIN BINTI CHE ALIAS
#### Matric No.: A20EC0121
#### Dataset: Mflix

## Question 2 (a)
You have been given a JSON file that contains data that must be imported into a MongoDB database. The JSON file must follows the appropriate structure for MongoDB documents. Your task is to outline the step-by-step process to add the data from the JSON file into MongoDB. Provide a detailed explanation of each step involved in the process with screenshots, including any necessary commands. Ensure that your answer covers the preparation of the JSON file, starting the MongoDB server, accessing the MongoDB shell, selecting the target database, choosing the collection, and executing the import command.

**PREREQUISITES**

**Install each of the following:**

1.Install the community server for MongoDB.

2.Setup the MongoDB Shell

3.Make sure that you have python installed

**Retrieve and Download the dataset for Mflix;**

a.users.json

b.comments.json

c.theaters.json

d.movies.json

**Connect to MongoDB server** -Open the command prompt and type mongod
<img src="./image/mongod.png" style="width: 500px; height: 200px;">

**Import the JSON file into MongoDB**

To import the JSON File into MongoDB, use mongoimport command. 
```
mongoimport "C:\Users\Acer\Desktop\AA\theaters.json" -d Mflix -c theaters
mongoimport "C:\Users\Acer\Desktop\AA\users.json" -d Mflix -c users
mongoimport "C:\Users\Acer\Desktop\AA\comments.json" -d Mflix -c comments
mongoimport "C:\Users\Acer\Desktop\AA\movies.json" -d Mflix -c movies
```
<img src="./image/jsonimport.png" style="width: 500px; height: 200px;">
-The -d movie specifies the name of the database, which in MongoDB localhost is movie database.

-theatres is defined as the specified collection in the movie database using the -c option.

**Accessing the MongoDB Shell**

Next, inside the command type 'mongosh' to access the MongoDB Shell
<img src="./image/mongosh.png" style="width: 500px; height: 200px;">

This application allows users to inspect every database and collection from MongoDB Compass.
<img src="./image/mongodatabase.png" style="width: 500px; height: 200px;">
## Question 2 (b)

1.Use the mongod command at the command prompt to launch the MongoDB server.

2.To swap the database, type use mflix in the MongoDB Compass' MongoDB Shell terminal.
<img src="./image/mongosh.png" style="width: 500px; height: 200px;">



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/nurfarrahin-che-alias-26688827b/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


