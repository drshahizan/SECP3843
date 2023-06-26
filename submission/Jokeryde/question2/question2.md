<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: ADAM WAFII BIN AZUAR

#### Matric No.: A20EC0003

#### Dataset: MFLIX DATASET

## Question 2 (a)

  1. Install the necessary requirement before starting the process:
     <ul>
       <li> Install MongoDB Community</li>
       <li> Install MongoDB Shell</li>
       <li> Install MongoDB Database Tools</li>
     </ul>

  2. Download JSON file from GitHub
     <ul>
       <li> movies.json</li>
       <li> comments.json</li>
       <li> users.json</li>
       <li> theaters.json</li>
     </ul>

  3. Set up path inside system enviroment
     <img src="https://github.com/drshahizan/SECP3843/blob/0ab73ca1ce9f455715b6856adb29aaf488f920c4/submission/Jokeryde/question2/files/images/image_2023-06-26_183600121.png" style="width: 800px; height: 350px;">
     
  4. And open command prompt and type 'mongod' to start the mongodb server
      <img src="https://github.com/drshahizan/SECP3843/blob/0ab73ca1ce9f455715b6856adb29aaf488f920c4/submission/Jokeryde/question2/files/images/mongod.jpg" style="width: 800px; height: 350px;">
      
  6. Next, inside the command type 'mongosh' to access the MongoDB Shell
     <img src="https://github.com/drshahizan/SECP3843/blob/0ab73ca1ce9f455715b6856adb29aaf488f920c4/submission/Jokeryde/question2/files/images/mongosh.jpg" style="width: 800px; height: 350px;">
     
  7. Select the target database by typing 'use mflix'
      
      
  8. Import JSON datatsets into MongoDB using Mongo Shell by typing inside the command ```mongoimport --uri mongodb+srv://jokeryde:adamkaya@jokeryde.cnn7sr4.mongodb.net/ --db mflix --collection mflixx --file "D:\STDE\movies.json"```

      <img src="https://github.com/drshahizan/SECP3843/blob/0ab73ca1ce9f455715b6856adb29aaf488f920c4/submission/Jokeryde/question2/files/images/movies.jpg" style="width: 800px; height: 350px;">
      
  9. Repeat the steps for comments.json, users.json and theaters.json

      <img src="https://github.com/drshahizan/SECP3843/blob/0520bb3bed079e157a1f5e2a857d1cf305cf112c/submission/Jokeryde/question2/files/images/other.jpg" style="width: 800px; height: 350px;">
      
  10. JSON file successfully imported into MongoDB

      <img src="https://github.com/drshahizan/SECP3843/blob/0520bb3bed079e157a1f5e2a857d1cf305cf112c/submission/Jokeryde/question2/files/images/mongo%20db.jpg" style="width: 800px; height: 350px;">

      
## Question 2 (b)

  1. Start MongoDB server by using ```mongod``` command inside the command prompt.
  2. Open MongoDB Shell terminal inside MongoDB Compass, type ```use mflix``` to switch the database.
     <img src="https://github.com/drshahizan/SECP3843/blob/2bfdac31d9e2d308440f320ba27d5f7030b08d5c/submission/Jokeryde/question2/files/images/switch.jpg" style="width: 800px; height: 350px;">
     
  3. Next, to create a new query, I'll be using the ```insertOne()``` method in MongoDB to insert a single record into my mflixx collection which represent as my movie collection.
     <img src="https://github.com/drshahizan/SECP3843/blob/2bfdac31d9e2d308440f320ba27d5f7030b08d5c/submission/Jokeryde/question2/files/images/insertdb.jpg" style="width: 800px; height: 350px;">

     <img src="https://github.com/drshahizan/SECP3843/blob/2bfdac31d9e2d308440f320ba27d5f7030b08d5c/submission/Jokeryde/question2/files/images/insert%20part%202.jpg" style="width: 800px; height: 350px;">
     

  4. The new record can be found in the database inside mflixx collection.
     <img src="https://github.com/drshahizan/SECP3843/blob/2bfdac31d9e2d308440f320ba27d5f7030b08d5c/submission/Jokeryde/question2/files/images/data%20insert.jpg" style="width: 800px; height: 350px;">

  5. Next for READ, I'll be using the ```find()``` method to read the record inside the mflixx collection. I filtered the record where the movie rated is "PG13".
     
     <img src="https://github.com/drshahizan/SECP3843/blob/2bfdac31d9e2d308440f320ba27d5f7030b08d5c/submission/Jokeryde/question2/files/images/find%20movie.jpg" style="width: 800px; height: 350px;">

  6. Next we have the UPDATE. So I'm going to update the year of the movie from "2020" to "2019" by using the ```updateOne()``` method.
     <img src="https://github.com/drshahizan/SECP3843/blob/2bfdac31d9e2d308440f320ba27d5f7030b08d5c/submission/Jokeryde/question2/files/images/updateone.jpg" style="width: 800px; height: 350px;">

  7. As for DELETE, I used the ```deleteOne()``` method to delete the records that are "PG13" rated.
     <img src="https://github.com/drshahizan/SECP3843/blob/2bfdac31d9e2d308440f320ba27d5f7030b08d5c/submission/Jokeryde/question2/files/images/delete.jpg" style="width: 800px; height: 350px;">

     

## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
