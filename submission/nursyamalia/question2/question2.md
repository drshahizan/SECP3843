<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nur Syamalia Faiqah Binti Mohd Kamal
#### Matric No.: A20EC0118
#### Dataset : [Analytics Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 2 (a)
### Prerequisites
Install all the following below:
1. Install [MongoDB Community Server](https://www.mongodb.com/try/download/community)
2. Install [MongoDB Shell](https://www.mongodb.com/try/download/shell)
3. Edit paths in the system environment variables. Then, it will include the MongoDB and Mongosh folder directory

### Steps
1. Download the JSON file:
 - Download all datasets (accounts.json, customers.json and transactions. json in [Analytics Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics).
 - Check each JSON files metadata and values.

2. Start the MongoDB server / MongoDB Compass:
- Open your command-line interface and start the MongoDB server by running the following command:
     ```javascript
     mongod
     ```
  - Or, open and connect to localhost like below images
     <img  src="./files/images/connectMongodb.png"></img>

3. Access the MongoDB shell:
 - Open a new command-line interface window and access the MongoDB shell by running the following command:
     ```javascript
     mongo
     ```

4. Create database and Collection:
- In MongoDB Compass, right-click on '+' and create the database name = "analytics" and create the collections("accounts", "customers", "transactions").

5. Import JSON Files
 - Import the selected JSON file in the choose collection.
     <img  src="./files/images/importMongodb.png"></img>
- Check the documents after imported.
     <img  src="./files/images/importaccounts.png"></img>
     <img  src="./files/images/importcustomers.png"></img>
     <img  src="./files/images/importtransactions.png"></img>


## Question 2 (b)

<p>In the MongoDB Shell, all CRUD (Create, Read, Update and Delete} quesries operations will done here.</p>

i. Create - 1 query:
This query creates a new document in the specified collection with the provided fields and values.

```javascript
db.accounts.insertOne({
  account_id: NumberInt(123456),
  limit:  NumberInt(9000),
  products: ['Derivatives', 'InvestmentStock']
})
```


ii. Read - 1 query:
This query retrieves the first document from the collection that matches the specified field and value.

```javascript
db.accounts.findOne({account_id: NumberInt(123456)})
```

<img  src="./files/images/findinsert.png"></img>

iii. Update - 2 queries:
- This query updates a specific field in a document that matches the specified field and value.

```javascript
db.accounts.updateOne(
  { account_id: NumberInt(371138) }, 
  { $set: { limit: NumberInt(10000) } } 
)

```

<img  src="./files/images/updatequery1.png"></img>

- This query  updates by adding  value in array 'products' in a document that matches the specified field and value.

```javascript
db.accounts.updateOne(
  { account_id: NumberInt(12345) },
  { $push: { products: "Commodity" } }
)
```

<img  src="./files/images/updatequery.png"></img>

iv. Delete - 1 query:

This query deletes the first document from the collection that matches the specified field and value.
```javascript
db.accounts.deleteOne({ account_id: NumberInt(123456) })
```

<img  src="./files/images/deletequery.png"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



