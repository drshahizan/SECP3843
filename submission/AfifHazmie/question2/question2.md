<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Afif Hazmie Arsyad Bin Agus
#### Matric No.: A20EC0176
#### Dataset: Supply Store

## Question 2 (a)
Requirement before following the steps:
- Install [MongoDB Shell](https://www.mongodb.com/try/download/shell)
- Install [MongoDB Community](https://www.mongodb.com/try/download/community)
- Install [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools)
  
1. Download and prepare the JSON data file [Supply Store](https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales) into device.
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA24.jpg" style="width: 800px; height: 350px;">
   
2. Open Command Prompt and type the command `mongod --version` to check the mongodb version and the type the command `mongod` to start mongodb server
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA21.jpg" style="width: 450px; height: 250px;">
---
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA22.jpg" style="width: 1000px; height: 600px;">
   
3. Type the command `mongosh` in command prompt to access to MongoDB shell
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA23.jpg" style="width: 700px; height: 250px;">
   
4. Select the target database and collection
   - type `use SupplyStore` in the command
   - type `db.Sales` to choose the collection

     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA25.jpg" style="width: 200px; height: 100px;">
     
5. Import json dataset file into mongoDB using mongo shell.
    - In the terminal with Mongo Shell active, type in the command `mongoimport --uri mongodb+srv://afifhazmiearsyad:abc123456789@noctua.bw9bvzx.mongodb.net/ --db SupplyStore --collection Sales --file "C:\Users\User\Downloads\sales.json"`
    - Lets break the command into parts:
      - `--db` = database name
      - `--collection` = database collection name
      - `--file` = file path to the JSON dataset file
    - The Database and collection will be automatically created as we execute the command.
      
    <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA26.jpg" style="width:900px; height: 200px;">
      
6. Successfully import JSON dataset into mongoDB

   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA27.jpg" style="width:700px; height: 500px;">

## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



