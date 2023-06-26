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

Step 1. Connect to MongoDB server
-Open the command prompt and type `mongod`
![Screenshot 2023-06-26 102930](https://github.com/drshahizan/SECP3843/assets/92329710/54312172-12a9-484e-ba27-bfbe463f3f8a)

Step 2. Import the JSON file into MongoDB
- To import the JSON File into MongoDB, use `mongoimport` command.
`mongoimport "C:\Users\pc\Documents\dataset\03-movie\theaters.json" -d movie -c theaters --drop`

- The `mongoimport` is a command-line tool provided by MongoDB that allows user to import data from various file formats including JSON, CSV, and TSV into a MongoDB database.
- The `"C:\Users\pc\Documents\dataset\03-movie\theaters.json"` is the file path of where the JSON file that need to be imported is located.
- The `-d movie` defined as the specified database name which is movie database in MongoDB localhost.
- `-c theaters` defined as the specified collection in the database that is in the movie database.
- `--drop` is used to drop the target collection before the data is imported. It ensures that the existing collection is first deleted, and then the new data is imported.

Step 2. Launch the `mongosh` shell
- Launch the `mongosh` shell by opening your command prompt (CMD) and type `mongosh`. Make sure the MongoDB application has been installed and running locally.
![Screenshot 2023-06-26 105759 (2)](https://github.com/drshahizan/SECP3843/assets/92329710/13e69939-bed5-41b4-992b-dc88749d2988)

Step 3. 


## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



