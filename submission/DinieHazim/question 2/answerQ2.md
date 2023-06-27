<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Muhammad Dinie Hazim Bin Azali
#### Matric No.: A20EC0084
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 2 (a)

#### Install all required software:

1. MongDB Community Server
   - Simply go to this [link](https://www.mongodb.com/try/download/community) and click the download button.
     <p align="center">
        <img height="300px" src="./files/images/MongoDB%20Community.png"></img>
     </p>

2. MongoDB Command Line Database Tools
   - Go to this [link](https://www.mongodb.com/try/download/database-tools) and click download.
     <p align="center">
        <img height="300px" src="./files/images/MongoDB%20Command%20Line.png"></img>
     </p>

3. MongoDB Shell
   - Navigate to this [link](https://www.mongodb.com/try/download/shell) and click the download button.
     <p align="center">
        <img height="300px" src="./files/images/MongoDB%20Shell.png"></img>
     </p>

#### Prepare the JSON File
1. Ensure that JSON file follows the appropriate structure for MongoDB documents.
2. Download `stories.json` dataset.
3. Use python to modified the dataset.
   - `Data Preparation`: [Data Preparation.ipynb](https://github.com/drshahizan/SECP3843/blob/9b1709a25acd8278b73b3a6d17d1e2b2fa47f720/submission/DinieHazim/question%202/files/code/prepareJSON.ipynb)
   - `Modified Dataset`: [Modified_Stories.json](https://github.com/drshahizan/SECP3843/blob/6bf7dcc64f311177227022dc6dd865ea6c4d49bd/submission/DinieHazim/question%202/files/code/modified_stories.json)

#### Start MongoDB Server
1. Install and setup MongoDB Server.
2. Let all the requirement to default.
3. Then, open the zip file from MongoDB Shell and MongoDB Command Line Database Tools into this folder `C:\Program Files\MongoDB\Server\6.0\bin`.

   <img  src="./files/images/Shell%20zip.png"></img>
   <img  src="./files/images/Command%20Line%20exe.png"></img>
5. Open terminal or command prompt and direct to `C:\Program Files\MongoDB\Server\6.0\bin`
6. Start the MongoDB server by running the mongod command.
   <img  src="./files/images/mongod.png"></img>

#### Access MongoDB Shell
1. Open terminal or command prompt.
2. Run this following command `mongosh "mongodb+srv://cluster0.nd5oq2m.mongodb.net/" --apiVersion 1 --username DinieHazim`.
3. Enter password.
   <img  src="./files/images/mongosh.png"></img>

#### Import dataset
1. In order to import the dataset into MongoDB, use the mongoimport command.
   <img  src="./files/images/import.png"></img>

#### Check the data
1. Open MongoDB and will see all the data have been imported.
   <img  src="./files/images/verify.png"></img>

## Question 2 (b)

#### Create Query

1. There are two methods that we can use to create new documents into a MongoDB database.
   - `insertOne()`: Create a single object into the database.
   - `insertMany()`: Create an array of objects into the database.

2. I will be using `insertOne()`.
   ```
      db.Stories.insertOne({
         href: null
         title: "Dinie Hazim"
         comments: 1
         container: null
         submit_date: null
         topic: null
         promote_date: null
         id: "23042001"
         media: "news"
         diggs: 455
         description: "Dinie Hazim seorang lelaki"
         link: null
         user: null
         status: null
         shorturl: null
      });
   ```

3. It will create a new document in MongoDB.
   <img  src="./files/images/create.png"></img>

#### Read Query

1. There are two methods to read data from MongoDB database.
   - `find()`: Will find all documents that match the query provided.
   - `findOne()`: Will find the first document that matches the query.
  
2. I will be using `find()`.
   ```
      db.Stories.find({media: "videos"});
   ```

3. It will show all documents where the media is videos.
   <img  src="./files/images/read.png"></img>

#### Update Query

1. There are two methods to update documents in MongoDB.
   - `updateOne()`: Will update the first document that is found matching the provided query.
   - `updateMany()`: Will update all documents that match the provided query.

2. For `updateOne()`.
   ```
      db.Stories.updateOne(
         { title: "Dinie Hazim" },
         { $set: {comments: 51 } }
      );
   ```

3. Before `updateOne()`
   
   <img  src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/DinieHazim/question%202/files/images/updateOne%20before.png"></img>

5. After `updateOne()`
   
   <img  src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/DinieHazim/question%202/files/images/updateOne%20after.png"></img>

7. For `updateMany()`.
   ```
      db.Stories.updateMany(
        { comments: 0 },
        { $set: { comments: null } }
      );
   ```

8. Before `updateMany()`.
   
   <img  src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/DinieHazim/question%202/files/images/updateMany%20before.png"></img>

10. After `updateMany()`.
    
    <img  src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/DinieHazim/question%202/files/images/updateMany%20after.png"></img>


#### Delete Query

1. There are two methods to delete documents in MongoDB.
   - `deleteOne()`: Delete the first document that match the query.
   - `deleteMany()`: Delete all documents that match the query.

2. I will be using `deleteOne()`.
   ```
      db.Stories.deleteOne({ title: "Dinie Hazim"});
   ```

3. Before delete.
   <img  src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/DinieHazim/question%202/files/images/before%20delete.png"></img>

5. After delete
   <img  src="https://github.com/drshahizan/SECP3843/blob/7bc4e3f0bf153b15905ccc106dd24b67be842d3a/submission/DinieHazim/question%202/files/images/after%20delete.png"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
