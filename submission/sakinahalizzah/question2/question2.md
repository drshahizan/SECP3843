<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Sakinah Al'izzah Binti Mohd Asri
#### Matric No.: A20EC0142
#### Dataset: [Analytics](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 2 (a)

To import data from a JSON file into MongoDB, simply follow the step-by-step process detailed below:

1. To get started, first must **download** and **install** all the required software listed below:

   i. [MongoDB Community Server](https://www.mongodb.com/try/download/community-kubernetes-operator)
   
   ii. [MongoDB Shell](https://www.mongodb.com/try/download/shell)
   
   iii. [MongoDB Command Line Database Tools](https://www.mongodb.com/try/download/database-tools)

2. **Prepare the JSON file**
   
   Download the [Analytics dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics), it's important and ensure that the JSON file is formatted correctly for MongoDB documents. Represent each document as a JSON object within an array or newline-delimited format. Enclose each object within square brackets and separate them with commas.

3. **Start the MongoDB Server**
   
    Open the terminal or command prompt and run the command `mongod` to start the MongoDB server.
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/ac9bd905-ed02-402c-ba15-f5b71a91fef9" />

4. **Access the MongoDB Shell**
   
     To access the MongoDB shell, run the following command.
   
    ```
   mongosh "mongodb+srv://cluster0.cpy5tdw.mongodb.net/" --apiVersion 1 --username <username>
    ```

    <img src="https://github.com/drshahizan/SECP3843/assets/99240177/4a5d28de-52c7-4ccc-b30f-a3ca4134d950" />

5. **Select the Target Database**
   
   To select the desired database in the MongoDB shell, utilize this command:

    ```
    use db_analytics
    ```

   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/a51c5edf-b42b-44f4-8170-53818f00fd1b" />

6. **Choose the Collection**
    
   Specify the collection where you wish to import the JSON data. MongoDB will automatically generate the collection if it doesn't already exist. To select the collection, use the following command:
   ```
   db.accounts
   db.customers
   db.transactions
    ```
     <img src="https://github.com/drshahizan/SECP3843/assets/99240177/294814c4-fa20-40f1-bb35-086096f4c6df" />

7. **Execute the Import Command**
   
      To import data from a JSON file into a chosen collection, utilize the mongoimport command as follows.
      ```
      mongoimport --uri="<connection_string>" --collection=<collection_name> --file="<file_path>" --jsonArray
      ```
      where,
      `<connection_string>`: The MongoDB connection string
      
      `<collection_name>`: The collection name of imported JSON data
      
      `<file_path>`: JSON file path directory
      
      Replace with your data.
      ```
      mongoimport --uri="mongodb+srv://sakinahalizzah:Sakinah1234@clustersakinah.scfkjmg.mongodb.net/" --collection=accounts --file="C:\Users\User\OneDrive\Desktop\AA SECP3843\accounts.json" 
   
      mongoimport --uri="mongodb+srv://sakinahalizzah:Sakinah1234@clustersakinah.scfkjmg.mongodb.net/" --collection=customers --file="C:\Users\User\OneDrive\Desktop\AA SECP3843\customers.json" 
   
      mongoimport --uri="mongodb+srv://sakinahalizzah:Sakinah1234@clustersakinah.scfkjmg.mongodb.net/" --collection=transactions --file="C:\Users\User\OneDrive\Desktop\AA SECP3843\transactions.json" 
      ```
      <img src="https://github.com/drshahizan/SECP3843/assets/99240177/8a27b4a1-2ae1-4f62-af4a-4dc9e6637fe5" />
   
      Successfully import to MongoDB Compass
      
      <img src="https://github.com/drshahizan/SECP3843/assets/99240177/caa90567-bf62-4a81-9443-8db8ee49a8ce" />

      Successfully find the collection at command

      <img src="https://github.com/drshahizan/SECP3843/assets/99240177/63b65816-a74a-472b-a878-c4a2bd4b3570" />


## Question 2 (b)

Here are five MongoDB queries that showcase how to perform Create, Read, Update, and Delete (CRUD) operations on the documents stored in the database.

1. Create (Insert) Query: `insertOne()` function

```
db.customers.insertOne({
 "username": "sakinahalizzah",
 "name": "Sakinah Al Izzah",
 "address": "1 Jalan Tulip 10",
 "birthdate": {"$date": 54439275000},
 "email": "sakinahalizzah@gmail.com",
 "accounts": [
   470650,
   443178
 ],
});
```

   To create a new document in the customers collection in MongoDB Shell, simply run the query. The id for each new document will be automatically generated.
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/506ebb0e-9336-4c11-a061-5cc8e1664018" />

   The created document is found.
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/0fc47887-07c4-4c2b-8cfc-015e9a9ba294" />

2. Read (Find) Query:`find()` function

   ```
   db.customers.find({ accounts: 470650 });
   ```
   Once the query above is executed, the MongoDB Shell will gather all records from the "customers" collection that have a matching value ("470650") in the "accounts" field. 
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/dd01b32e-b5ef-42b0-86d9-7fcfa980959f" />
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/b7244344-2f1a-45ed-bf6f-a85ef22b80d8" />


3. Update Queries 1: `updateOne()` function to update a single document
   ```
   db.customers.updateOne(
     { username: "sakinahalizzah" },
     { $set: { address: "10 Tulip Street" } }
   );
   ```
   The above queries is executed at the MongoDB shell
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/c598e1b7-9cff-4221-9b49-5051b1cae70e" />

   Before update address:
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/78f3d4f4-0505-473c-a52a-6753687f3685" />

   After update address:
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/bd72562d-7b88-43ac-8f52-3980c7d16886" />

4. Update Queries 2: `updateMany()` function to update a multiple documen
    ```
      db.customers.updateMany(
        { accounts: 470650 },
        { $set: { email: "paul@gmail.com" } }
      );
      ```
   The above queries is executed at the MongoDB shell
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/5a2e7ca1-deb0-461d-8e73-b3ce5e0aa400" />

   Before update email for accounts: 470650:
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/a714ccdd-a5b0-4d01-b54b-2c72a617d1ff" />

   After update email for accounts: 470650:
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/e7a1b80e-f46b-4f74-8550-5535e4fa2fad" />

5. Delete Query: `deleteOne()` function
   ```
   db.customers.deleteOne({username:"sakinahalizzah"});
   ```
   The above queries are executed at the MongoDB shell and delete a single document that matches the specified condition.
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/97559f62-2543-44ac-b0fa-b20de38c3b30" />

   If the document is deleted, searching for the username will yield no results.
   <img src="https://github.com/drshahizan/SECP3843/assets/99240177/bbb02305-699c-4ac8-8624-db680a0ef725" />

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



