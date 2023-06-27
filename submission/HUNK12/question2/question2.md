<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Mikhel Adam Bin Muhammad Ezrin
#### Matric No.: A20EC0237
#### Dataset: [Tweets](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets)

## Question 2 (a)
### Ensure JSON file follows the proper structure for importing into MongoDB
In this case, it does not because it is not contained within a square bracket `[]`. Each JSON document should be enclosed within curly braces `{}` and separated by commas `,`  which this dataset is. To add the square brackets to the JSON file, we can actually just simply modify the file and add the brackets using a text editor. However for this case, a Python script was created to read the JSON file, add the brackets, then save it into a new file. Below is the script to perform the previously mentioned actions
```
import json

# Read the JSON file
with open('tweets.json', 'r') as file:
    data = file.readlines()

# Add square brackets to the entire dataset
fixed_data = '[' + ','.join(data) + ']'

# Save the fixed dataset to a new JSON file
with open('fixed_tweets.json', 'w') as file:
    file.write(fixed_data)
```
### Install the following 
1. [MongoDB Community Server](https://www.mongodb.com/try/download/community-kubernetes-operator)
2. [MongoDB Shell](https://www.mongodb.com/try/download/shell)
3. [MongoDB Command Line Database Tools](https://www.mongodb.com/try/download/database-tools)

### Start the MongoDB Server
1. Open a command prompt in `C:\Program Files\MongoDB\Server\6.0\bin`. Then in the command prompt, type `mongod` to start start the server
   ![image](https://github.com/drshahizan/SECP3843/assets/3646429/b6974d26-7293-453d-ab88-6856cd3bffeb)
2. Access the MongoDB Shell by typing `mongosh`
3. Select the target database by typing `use STDE`
4. Now import the updated JSON file into MongoDB with the following command which contains our connection string, db and collection name as well as the path for the file
```
mongoimport --uri=mongodb+srv://mikhel:admin@cluster0.kwav8pt.mongodb.net/ --db=STDE --collection=tweets --file="C:\Users\HI THERE\Desktop\AA Special Topic DE\ST\tweets\fixed_tweets.json" --jsonArray
```
![image](https://github.com/drshahizan/SECP3843/assets/3646429/662d0e92-bdda-4b28-b584-a71666bad59f)

Now if we look in MongoDB Compass, we should be able to see the imported data.
![image](https://github.com/drshahizan/SECP3843/assets/3646429/f0c7d6e4-fff6-41f6-be30-e300ea2dae73)



## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



