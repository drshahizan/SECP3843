<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Jia Xian  
#### Matric No.: A20EC0200
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales" >Supply Store Dataset</a>

## Question 2 (a)
### 1. Download dataset (JSON File)
Download the dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales" >Supply Store Dataset</a>

### 2. Start MongoDB server with command Prompt
Open Command Prompt and enter `mongod` to start the MongoDB server.
<img  src="./files/images/start.JPG"></img>

### 3. Import Dataset
In cmd enter `mongoimport "C:\Users\user\OneDrive\Desktop\special topic\AA\dataset\sales.json" -d AA -c Sales`.
The provided command mongoimport is used to import the JSON file sales.json into a MongoDB database named AA and the data will be stored in a collection called Sales.
<img  src="./files/images/import1.JPG"></img>

After the dataset is imported, you can find it at the MongoDB Compass:
<img  src="./files/images/import2.JPG"></img>

### 4. Accessing the MongoDB shell
Enter `mongosh` in the terminal to access the MongoDB shell
<img  src="./files/images/shell1.JPG"></img>

You can return the list of all databases running on MongoDB Server including default and user-defined databases with `show dbs`.
<img  src="./files/images/shell2.JPG"></img>

Then enter `use AA` to switch to the desired database where we want.
<img  src="./files/images/shell3.JPG"></img>

## Question 2 (b)
### i. Create - Insert a new document:
To create a new document, we can use the `insertOne()` method in MongoDB. Here's the example query that I used to insert a new document:
```
db.Sales.insertOne({
  "saleDate": new Date("2023-06-25T10:30:00.000Z"),
  "items": [
    {
      "name": "laptop",
      "tags": [
        "electronics",
        "computers"
      ],
      "price": 999.99,
      "quantity": 1
    },
    {
      "name": "headphones",
      "tags": [
        "electronics",
        "audio"
      ],
      "price": 79.99,
      "quantity": 2
    }
  ],
  "storeLocation": "San Francisco",
  "customer": {
    "gender": "M",
    "age": 35,
    "email": "john@example.com",
    "satisfaction": 4
  },
  "couponUsed": true,
  "purchaseMethod": "Online"
});

```
<img  src="./files/images/create1.JPG"></img>

You can found the created document in the mongoDB database:
<img  src="./files/images/create2.JPG"></img>

### ii.Read
The db.find() method in MongoDB is used to search for and retrieve documents from a collection based on specified query criteria.
In this case i want to return the document which _id equals "5bd761dcae323e45a93ccff3":

```
db.Sales.find({ "_id": ObjectId("5bd761dcae323e45a93ccff3") })
```
<img  src="./files/images/read1.JPG"></img>

You can find it by using the filter in Mongo DB too
<img  src="./files/images/read2.JPG"></img>




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



