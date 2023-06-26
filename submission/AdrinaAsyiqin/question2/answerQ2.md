# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Adrina Asyiqin Binti Md Adha
#### Matric No.: A20EC0174
#### Dataset: sales.json

## Question 2 (a)
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
3. Create a new database named `salesdatabase`
4. Create a new collection under salesdatabase named `salessample` 
5. Click on 'Add Data' dropdown and choose Import JSON or . CSV file
6. Choose sales.json from file explorer and click on `Import`.
7. The database will then appear in the mongodb database after all documents is imported.

## Question 2 (b)

### Step 1: Connect to MongoDB
1. Open command prompt where MongoDB is located. It is usually in the program files folder. For example mine is in 
```
C:\Program Files\MongoDB\Server\6.0\bin
```
2. Then create a connection string using the following command 
```
mongosh "mongodb+srv://cluster0.yvk5zzq.mongodb.net/" --apiVersion 1 --username adrinaasyiqin
```
`cluster0.yvk5zzq.mongodb.net` : can be modified using your own connection

`adrinaasyiqin` : is the username of your MongoDB

The command prompt will then ask for the password.

3. Connect to a database by using the following command
```
use salesdatabase
```
`salesdatabase` : Can be modified using your own database name

### Step 2: Create the queries
1. Create
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
2. Read
```
db.salessample.find({ "storeLocation": "Denver" })
```
3. Update
```
db.salessample.updateOne(
  { "_id": ObjectId("5bd761dcae323e45a93ccfe8") },
  { $set: { "storeLocation": "New York" } }
)
```
4. Delete
```
db.salessample.deleteOne({ "_id": ObjectId("5bd761dcae323e45a93ccfe8") })
```
