<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Muhammad Naquib Bin Zakaria
#### Matric No.: A20BE0161
#### Dataset: 03 - Movie

## Question 2 (a)
<h4>Steps Adding JSON File into MongoDB</h4>

Before adding JSON file into MongoDB, there is some steps that need to be followed:
1. Install the MongoDB Community Server.
2. Install the MongoDB Shell.
3. Install MongoDB Database tools.
4. Lastly, add paths in system environment variables.
Can refer the tutorial <a href="https://www.youtube.com/watch?v=XZ4usENdH4s&list=PL_euSNU_eLbfmDxRw-Gx45ow5MtBAM3YS&index=7">here.</a>

Step 1. Download the dataset provided.
- Download the dataset that has been provided in github and put it in file repository.
![Screenshot 2023-06-26 142817](https://github.com/drshahizan/SECP3843/assets/92329710/bdd26807-f5ac-429a-9588-f2f0505eb604)

Step 2. Connect to MongoDB server
-Open the command prompt and type `mongod`
![Screenshot 2023-06-26 102930](https://github.com/drshahizan/SECP3843/assets/92329710/54312172-12a9-484e-ba27-bfbe463f3f8a)

Step 3. Import the JSON file into MongoDB
- To import the JSON File into MongoDB, use `mongoimport` command.
`mongoimport "C:\Users\pc\Documents\dataset\03-movie\theaters.json" -d movie -c theaters`
![Screenshot 2023-06-26 112034 (2)](https://github.com/drshahizan/SECP3843/assets/92329710/b08d3006-69fd-4ad5-8f12-b0a37596fbc9)

- The `mongoimport` is a command-line tool provided by MongoDB that allows user to import data from various file formats including JSON, CSV, and TSV into a MongoDB database.
- The `"C:\Users\pc\Documents\dataset\03-movie\theaters.json"` is the file path of where the JSON file that need to be imported is located.
- The `-d movie` defined as the specified database name which is movie database in MongoDB localhost.
- `-c theaters` defined as the specified collection in the database that is in the movie database.

Step 4. Launch the `mongosh` shell
- Launch the `mongosh` shell by opening your command prompt (CMD) and type `mongosh`. Make sure the MongoDB application has been installed and running locally.
![Screenshot 2023-06-26 105759 (2)](https://github.com/drshahizan/SECP3843/assets/92329710/13e69939-bed5-41b4-992b-dc88749d2988)

Step 5. View dataset in MongoDB
- From command prompt, type `show dbs` and the command prompt will show all databases that resides in MongoDB localhost.
![Screenshot 2023-06-26 112034 (3)](https://github.com/drshahizan/SECP3843/assets/92329710/1b9f2228-f886-4bdf-9075-0a0e3ff2ce2f)
- From MongoDB Compass, all the database and collection can be viewed in this application.
![Screenshot 2023-06-26 143635](https://github.com/drshahizan/SECP3843/assets/92329710/ec443a6a-f5c5-4c55-a1ed-4eb1a48b3279)

## Question 2 (b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



