<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Adrina Asyiqin Binti Md Adha
#### Matric No.: A20EC0174
#### Dataset: sales.json

## Question 2 (a)

### Requirements
- MongoDB Compass
- MongoDB Tools
- MongoDB Community
  
### Step 1: Prepare sales.json file 
1. `Use Validation Tool` : There are several online JSON validation tools available that can help you validate the format and structure of your JSON file. These tools can identify any syntax errors or formatting issues in your JSON file. For example: https://jsonlint.com/
2. `Check Data Types` : Verify that the data types of the values in the JSON file are appropriate for your MongoDB documents. For example, strings should be enclosed in double quotes, numbers should not be enclosed in quotes, and boolean values should be either true or false. The below shows the data type for json file.

| Data Type | Description                                        | Example             |
|-----------|----------------------------------------------------|---------------------|
| String    | A sequence of Unicode characters                   | "Hello, World!"     |
| Number    | Numeric value, can be integer or floating-point    | 42, 3.14            |
| Boolean   | Represents logical values, either true or false    | true, false         |
| Object    | Unordered collection of key-value pairs            | {"name": "John Doe"}|
| Array     | Ordered collection of values                       | ["apple", "banana"] |
| Null      | Represents the absence of a value                  | null                |

### Step 2: Start MongoDB server and upload sales.json file
1. Open MongoDB on your laptop 
   
2. Connect to a connection
   
![775b87814d848643d6659095730f5ae21acdc423](https://github.com/drshahizan/SECP3843/assets/96984290/7787ed1e-f131-4892-9fa1-e5724437f694)

3. Create a new database named `salesdatabase`
 
4. Create a new collection under salesdatabase named `salessample` 

![5e6a39d1ee4d01b029a6e5d8110dbce15e5178e4](https://github.com/drshahizan/SECP3843/assets/96984290/82ea7a74-64fa-4643-86ac-8ecd8b9b9462)

5. Click on 'Add Data' dropdown and choose Import JSON or . CSV file

![0daad43455d3666539873a89a1aa8e3e31baddfb](https://github.com/drshahizan/SECP3843/assets/96984290/b16f73ec-cde0-42b5-9fc4-78874f0906d9)

6. Choose sales.json from file explorer and click on `Import`.
7. The database will then appear in the mongodb database after all documents is imported.

![5f119ea6d353d75976418feac637716fcb405c8e](https://github.com/drshahizan/SECP3843/assets/96984290/1cb498ad-e28e-48ef-a53f-72fede3bae32)

![4a6211df17abc9ee7104328e404473fef59fdd2a](https://github.com/drshahizan/SECP3843/assets/96984290/b33324e7-f715-434a-a769-e15b33cd422d)


## Question 2 (b)
### Requirements
- MongoDB Compass
- MongoDB Tools
- MongoDB Community
  
### Step 1: Connect to MongoDB
1. Open command prompt where MongoDB is located. It is usually in the program files folder. For example mine is in 
```
C:\Program Files\MongoDB\Server\6.0\bin
```
2. Then create a connection string using the following command 
```
//connect to mongodb shell
mongod

//connect to mongodbcompass
mongosh "mongodb+srv://cluster0.yvk5zzq.mongodb.net/" --apiVersion 1 --username adrinaasyiqin
```
`cluster0.yvk5zzq.mongodb.net` : can be modified using your own connection

`adrinaasyiqin` : is the username of your MongoDB

The command prompt will then ask for the password.

![image](https://github.com/drshahizan/SECP3843/assets/96984290/aca4ca77-3f28-4fa0-84fe-1f302db55741)

![image](https://github.com/drshahizan/SECP3843/assets/96984290/5fb6f9c0-cb18-4572-81d0-76968c14591a)

3. Connect to a database by using the following command
```
use salesdatabase
```
`salesdatabase` : Can be modified using your own database name

![image](https://github.com/drshahizan/SECP3843/assets/96984290/ff1ef1f3-c400-4756-9794-93b78f6f86ca)


### Step 2: Create the queries
1. Create Query
```
db.salessample.insertOne({
  "_id": ObjectId(),
  "saleDate": { "$date": { "$numberLong": "1427144809506" } },
  "items": [
    {
      "name": "printer paper",
      "tags": ["office", "stationary"],
      "price": { "$numberDecimal": "40.01" },
      "quantity": { "$numberInt": "2" }
    }
  ],
  "storeLocation": "Denver",
  "customer": {
    "gender": "M",
    "age": { "$numberInt": "24" },
    "email": "abc@gmail.com",
    "satisfaction": { "$numberInt": "4" }
  },
  "couponUsed": false,
  "purchaseMethod": "Online"
})

```
![image](https://github.com/drshahizan/SECP3843/assets/96984290/3e05216d-b48b-4954-8f5a-47274c53fc7b)

2. Read Query
```
db.salessample.find({ "storeLocation": "Denver" })
```
![image](https://github.com/drshahizan/SECP3843/assets/96984290/7c14b81f-4c91-4723-9e07-1f050abb4d7c)

![image](https://github.com/drshahizan/SECP3843/assets/96984290/8bd5e995-ae5c-4bfb-89ce-f673ca554b05)


3. Update Query
 - Update One
 - Update Many
```
#update one
db.salessample.updateOne(
  { "_id": ObjectId("5bd761dcae323e45a93ccfe8") },
  { $set: { "storeLocation": "New York" } }
)
```
![image](https://github.com/drshahizan/SECP3843/assets/96984290/fd048863-fa38-40e9-a153-2e3d176b6bfa)

![image](https://github.com/drshahizan/SECP3843/assets/96984290/d0de0e7f-9d1c-417c-9d4f-eac2d0914841)

```
#update many
db.salessample.updateMany(
  { "customer.gender": "M" },
  { $set: { "storeLocation": "New York" } }
)
```
![image](https://github.com/drshahizan/SECP3843/assets/96984290/4634daba-bb73-47bb-a16f-a3f14024c901)

![image](https://github.com/drshahizan/SECP3843/assets/96984290/7fe0ae53-90cd-46f1-91d4-f36561404f18)

4. Delete Query
```
db.salessample.deleteOne({ "_id": ObjectId("5bd761dcae323e45a93ccfe8") })
```
![image](https://github.com/drshahizan/SECP3843/assets/96984290/4a39a065-d8d6-42dc-8c6c-870d04477de5)

![image](https://github.com/drshahizan/SECP3843/assets/96984290/004504fd-6d37-4053-bf10-db1a43ecbded)

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
