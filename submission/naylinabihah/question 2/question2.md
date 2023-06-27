<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nayli Nabihah Binti Jasni
#### Matric No.: A20EC0105
#### Dataset: Companies

## Question 2 (a)
#### Step 1: Install MongoDB, MongoDB Shell and MongoDB Command Line Database Tools
This is the step in which the required software and MongoDB tools should be installed and set up in the devices locally. These required MongoDB components can be downloaded at the [community](https://www.mongodb.com/try/download/community), [shell](https://www.mongodb.com/try/download/shell) and [tools](https://www.mongodb.com/try/download/database-tools).

- MongoDB

<img src="https://github.com/drshahizan/SECP3843/assets/120543271/24cd1770-2b5f-49fc-ae2d-082c28e814ae" alt="image" height="450" width="330">


- MongoDB Shell

<img src="https://github.com/drshahizan/SECP3843/assets/120543271/5463bb7a-0be1-42d5-8b93-f1ef06a0e634" alt="image" height="450" width="330">

- MongoDB Command Line Database Tools
  
<img src="https://github.com/drshahizan/SECP3843/assets/120543271/9d395ad9-5f5a-4c24-9fe2-5c76a40f6030" alt="image" height="370" width="330">

After installing these 3 components in the 'Program Files' should have MongoDB folder, in the folder, there should be 2 other folder inside it which are 'Server' and 'Tools'

<img src="https://github.com/drshahizan/SECP3843/assets/120543271/b22b8437-8b6e-4350-8db0-9e7009e67db7" alt="image" height="370" width="630">

These are the things that should already been installed in the Server folder under 'bin' folder:


<img src="https://github.com/drshahizan/SECP3843/assets/120543271/1c4da0fb-9908-4e29-a729-b10e18527f62" alt="image" height="370" width="630">

These are the things that should already been installed in the Tools folder under 'bin' folder:

<img src="https://github.com/drshahizan/SECP3843/assets/120543271/1e4be7e4-2bf2-491d-99ec-884dac1b8271" alt="image" height="370" width="630">


#### Step 2: Set Up Database and Collection Configation in MongoDB Shell
- Open the command prompt that has the path in which the 'bin' folder in Server is located at. Then run this command below:
  
  ```
  mongosh
  ```
  
![mongosh](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/mongosh.png)

- Then, check for the existing database in the shell and choose in which database the JSON file will be stored at. I chose admin database. The commands used are listed out below:

 ```
  show dbs
 ```
![show_dbs](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/show_dbs.png)

 ```
  use admin
```

- After chose the database it will show this:

![choose_db](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/choose_db.png)

- Then, check for the existing collection. Can choose either inserting the JSON file in the existing collection or in new collection. In my case, there is no collection created in the admin database so i just leave it as it be. The command to check the colection is like below:

```
show collections
```

![collection](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/collection.png)

- That's all for setting up the database in MongoDB Shell.

#### Step 3: Use MongoDB Command Line Database Tools to Insert the JSON File into The Collection
- Open the command prompt that has the path in which the 'bin' folder in Tools is located at. Then run this command below just to check if the ```mongoimport``` can be run in the command prompt or not:

```
mongoimport --help
```

![help](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/help.png)


- Then, insert the JSON file by using this command:

```
mongoimport --db admin --collection company --file C:\Users\companies.json
```

![import](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/import_json_in_tools.png)

where, db is the name of the database selected, colection is the name of the collection (can be named as the existing collection or just name anything and it will create new collection in the database) and file is the path in which the cJson file is stored at locally in the device.

#### Step 4: Check in MongoDB Atlas to Confirm if the JSON File is Stored in The Selected Collection

- Open the MongoDB Atlas and navigate to the admin database and to the company collection. This is where the JSON file is stored.

![json](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/json_in_atlas.png)




## Question 2 (b)
All the queries can be done in MongoDB Shell. Below are the commands and the results for each query given:

##### i. Create – 1 query (insertOne)

```
test>db.company.insertOne({name":contozrss","permalink":"contozrss","crunchbase_url":"https://www.crunchbase.com/company/contozrss","homepage_url":"https://www.contozrss.com","twitter_url":"https://twitter.com/contozrss"});
```

![insert](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/insert.png)

##### ii. Read – 1 query (findOne)
Use this command to find the specific query. In this, I searched using the _id

```
test>db.company.findOne({_id:ObjectId("6499dacd3a2303517e6f366a")})
```

The result can be seen below:

![find](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/find.png)


##### iii. Update – 2 queries
##### a. updateOne
This query is used to update the value set for the specific column in the specific row.

```
test>db.company.updateOne({_id:ObjectId("6499dacd3a2303517e6f366a")}, {$set:{name:"Babino"}})
```

From this command, for the _id = "6499dacd3a2303517e6f366a", the name column is changed to 'Babino'.

![update1](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/update_one.png)

##### b. replaceOne
This query is used to update only the column set in the specific row and delete the one that is not specified in the replace command.

```
test>db.company.replaceOne({_id:ObjectId("6499dacd3a2303517e6f366a")}, {homepage_url:"https://www.babino.com"})
```

From this command, for the _id = "6499dacd3a2303517e6f366a", the homepage_url column is changed to 'https://www.babino.com' and all other attributes that were not specified were removed / set to be null.

![update2](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/update_2.png)


##### iv. Delete – 1 query

This how to delete the query.

```
test>db.company.deleteOne({_id:ObjectId("6499dacd3a2303517e6f366a")})
```

This is the result if try to find the deleted row/query:

![delete](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%202/files/images/delete.png)

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



