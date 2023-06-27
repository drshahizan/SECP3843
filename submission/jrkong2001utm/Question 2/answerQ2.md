<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kong Jia Rou
#### Matric No.: A20EC0198
#### Dataset: Supply store

## Question 2 (a)
### Setup environment
To import the database to MongoDB using the JSON file given, first we need to download the zip file below:
1. [MongoDB Shell Download](https://downloads.mongodb.com/compass/mongosh-1.10.1-win32-x64.zip)
2. [MongoDB Compass Download (GUI)](https://downloads.mongodb.com/compass/mongodb-compass-1.38.0-win32-x64.exe)
3. [MongoDB Database Tools](https://fastdl.mongodb.org/tools/db/mongodb-database-tools-windows-x86_64-100.7.2.zip)

After downloading the zip file, unzip them. 

Run the .exe of MongoDB Compass (GUI) which is located in the bin folder. 

Then, go to the bin folder of MongoDB Shell. Copy all the item in the bin folder.

Paste the item in the bin folder of MongoDB Compass (GUI).

Copy the folder path of the bin folder of MongoDB Compass (GUI).

Open the "Edit the system environment variables". 

Click the "Environment variables".

Choose the variable "Path" and click edit.

Click "New" and paste the folder path of the bin folder of MongoDB Compass (GUI) that we have copied earlier. Then, click "Ok".

Go to your Command Prompt. Type the command "mongod". You will see the output as follows:
<img src="..\Question 2\files\images\mongod.png">

# Import the database
Now, we can start to import the database using the JSON file given.

Run the code below to import the database:
```
mongoimport "C:\Users\User\OneDrive\Documents\Apowersoft\Desktop\WBL\STDE\sales.json" -d salesdb -c sales
```

The first part of the code is the file path where the json file located. The `-d` indicates the database name while the `-c` indicates the collection name. When the database has been successfully imported, it is expected to see the output as below:

<img src="..\Question 2\files\images\import.png">

To double-check on your database has been successfully imported or not, open your MongoDB Compass. You will see the data displayed in the database you have created just now.

<img src="..\Question 2\files\images\mongodb.png">

<br>

## Question 2 (b)
1.Create query

To perform the create operation, run the command below:
```
use salesdb;

db.sales.insertOne({
  "_id": ObjectId(),
  "saleDate": ISODate("2023-06-25T12:34:56Z"),
  "items": [
    {
      "name": "new item",
      "tags": ["tag1", "tag2"],
      "price": 10.99,
      "quantity": 3
    }
  ],
  "storeLocation": "New York",
  "customer": {
    "gender": "F",
    "age": 30,
    "email": "example@example.com",
    "satisfaction": 5
  },
  "couponUsed": false,
  "purchaseMethod": "In-store"
});
```

Output:
<img src="..\Question 2\files\images\create.png">

I will show the record created in the read query part later.
<br>
<br>

2.Read query

To perform the read operation to read the record created just now, run the command below:
```
db.sales.find({ "_id": ObjectId("649a953805e47cff7c6ec795") });
```

Output:
<img src="..\Question 2\files\images\read.png">

3.Update query

To perform the update operation, run the command below:

First query: updateOne()
This query will change the `storeLocation` of the record with id equals to `649a953805e47cff7c6ec795` to `Malaysia`.
```
use salesdb;

db.sales.updateOne(
  { "_id": ObjectId("649a953805e47cff7c6ec795") },
  { $set: { "storeLocation": "Malaysia" } }
);
```

Second query: updateMany()
This query will change all the `storeLocation` which is equals to `Denver` to `Malaysia`.
```
use salesdb;

db.sales.updateMany(
  { "storeLocation": "Denver" },
  { $set: { "storeLocation": "Malaysia" } }
);
```

Output

First query: updateOne()
<img src="..\Question 2\files\images\updateOne.png">

You can see the `storeLocation` is changed from New York to Malaysia.

<img src="..\Question 2\files\images\rupdateOne.png">

Second query: updateMany()

<img src="..\Question 2\files\images\updateMany.png">

You can see the `storeLocation` is changed from New York to Malaysia.

<img src="..\Question 2\files\images\rupdateMany.png">

4.Delete query

To perform the delete operation, run the command below:
```

```

Output:
<img src="..\Question 2\files\images\delete.png">

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




