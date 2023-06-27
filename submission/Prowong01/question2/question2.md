<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Eddie Wong Chung Pheng
#### Matric No.: A20EC0031
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies" >Companies</a>

## Question 2 (a)
### Prerequisites
Download and Install All Required Software including:
1. MongoDB Shell
2. MongoDB Command Line Database Tools
3. MongoDB Community Server

#### Step 1: Prepare the JSON File
Download the dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies" >Companies Dataset</a>
After download the dataset, I need to make sure that it follows the JSON syntax rules and can be import into MongoDB. I use the online tools (JSON Formatter) to validate the JSON file.
<img  src="./files/images/json_formatter.png"></img>

#### Step 2: Start the MongoDB Server
To start MongoDB server, run the mongod command in your terminal or command prompt. This will launch the MongoDB server and listen for connections on port 27017 by default. 
<img  src="./files/images/mongod.png"></img>
 
### Step 3. Import Dataset
In cmd enter `mongoimport "C:\Users\Asus\Desktop\AA Special Topic\companies.json" -d test -c companies`.
The command format is `mongoimport "dataset_location_path" -d name_of_database -c name_of_collection`
This command will import a JSON file named companies.json into a collection named companies in a database named test
<img  src="./files/images/mongoimport.png"></img>

View the collection at MongoDB Compass
<img  src="./files/images/data.png"></img>

### Step 3. Access MongoDB Shell
Enter `mongosh` in the terminal to access the MongoDB shell.
<img  src="./files/images/mongosh.png"></img>

## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



