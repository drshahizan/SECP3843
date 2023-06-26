![Screenshot 2023-06-26 115123 (2)](https://github.com/drshahizan/SECP3843/assets/92329710/06e00bff-b256-4bfc-bf70-572ad28f3b56)<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
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
<h4>CRUD operations in MongoDB</h4>

Before start, make sure specify the database that want to be use. In order to do that, type `use movie` in command prompt which specify the command prompt to use movie database for further CRUD operations. Now can start the CRUD operations.

1. Create (1 query)
- use `db.theaters.insertOne()` to add a new data into JSON file in MongoDB.
- `theaters` in `db.theaters.insertOne()` define the collection of the database.
- `insertOne()` is the function to add new data into MongoDB.
![Screenshot 2023-06-26 113902 (2)](https://github.com/drshahizan/SECP3843/assets/92329710/1c90e65b-d819-4cf6-8ba8-d0ab66fca3a3)

2. Read (1 query)
- use `db.theaters.find()` to retrieve the detail information of the desired data from MongoDB database.
![Screenshot 2023-06-26 115123 (2)](https://github.com/drshahizan/SECP3843/assets/92329710/78d8bb0d-a0f6-44a0-8645-425c933ad8b9)
- As shown above, it specify the `theaterId` and return the details of the data based on the specified theaterId.

3. Update (2 queries)
i. updateOne() function.
- use `db.theaters.updateOne()` to update single data in MongoDB.
![Screenshot 2023-06-26 121656](https://github.com/drshahizan/SECP3843/assets/92329710/863354b0-5053-41fe-bf32-ad1a37639eb6)
- As shown above, it specify the theaterId that want to be updated and edit the information on `street1`, `city`, `state`, and `zipcode`.
- This is before it is updated:
![Screenshot 2023-06-26 121448](https://github.com/drshahizan/SECP3843/assets/92329710/23f34910-f190-41b5-9036-fb6d0e3a9107)
- This is after it is modified:
![Screenshot 2023-06-26 121733](https://github.com/drshahizan/SECP3843/assets/92329710/ab9010d3-120b-4395-86f6-d9b3feeab7c0)

ii. updateMany function.
- use `db.theaters.updateMany()` to update multiple data in MongoDB.
![Screenshot 2023-06-26 150325](https://github.com/drshahizan/SECP3843/assets/92329710/d63078f6-f128-4cfd-a176-23c5feec5f2a)
- As shown above, it specify the `location.address.city` equals to `Skudai` where the city is "Skudai" in the mongoDB database collection and edit the information on `location.address.street1` and `location.address.zipcode`.
- This is before it is updated:
![Screenshot 2023-06-26 122556](https://github.com/drshahizan/SECP3843/assets/92329710/c99260b9-ea2b-4062-bf3f-771413bb699c)
- This is after it is modified:
![Screenshot 2023-06-26 124118](https://github.com/drshahizan/SECP3843/assets/92329710/515f7395-3910-45fd-bbed-689409a6a874)

4. Delete (1 query)
- use `db.theaters.deleteOne()` to delete single data from MongoDB.
![Screenshot 2023-06-26 124948](https://github.com/drshahizan/SECP3843/assets/92329710/30ddd83e-5374-4515-91b0-a02c4595b549)
- As shown above, it specify the theaterId that want to be deleted.
- When view in MongoDB Compass, the data should be remove from the MongoDB database.
![Screenshot 2023-06-26 125007](https://github.com/drshahizan/SECP3843/assets/92329710/1c804747-88bd-46c4-8a21-6cf4021e50f6)



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



