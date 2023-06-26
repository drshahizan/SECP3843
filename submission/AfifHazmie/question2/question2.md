<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Afif Hazmie Arsyad Bin Agus
#### Matric No.: A20EC0176
#### Dataset: Supply Store

## Question 2 (a)
Requirement before following the steps:
- Install [MongoDB Shell](https://www.mongodb.com/try/download/shell)
- Install [MongoDB Community](https://www.mongodb.com/try/download/community)
- Install [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools)

### Steps:

1. Download and prepare the JSON data file [Supply Store](https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales) into device.
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA24.jpg" style="width: 800px; height: 350px;">
   
2. Open Command Prompt and type the command `mongod --version` to check the mongodb version and the type the command `mongod` to start mongodb server
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA21.jpg" style="width: 450px; height: 250px;">
---
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA22.jpg" style="width: 1000px; height: 600px;">
   
3. Type the command `mongosh` in command prompt to access to MongoDB shell
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA23.jpg" style="width: 700px; height: 250px;">
   
4. Select the target database and collection
   - type `use SupplyStore` in the command
   - type `db.Sales` to choose the collection

     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA25.jpg" style="width: 200px; height: 100px;">
     
5. Import json dataset file into mongoDB using mongo shell.
    - In the terminal with Mongo Shell active, type in the command
      - `mongoimport --uri mongodb+srv://afifhazmiearsyad:abc123456789@noctua.bw9bvzx.mongodb.net/ --db SupplyStore --collection Sales --file "C:\Users\User\Downloads\sales.json"`
    - Lets break the command into parts:
      - `--db` = database name
      - `--collection` = database collection name
      - `--file` = file path to the JSON dataset file
    - The Database and collection will be automatically created as we execute the command.
      
    <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA26.jpg" style="width:900px; height: 200px;">
      
6. Successfully import JSON dataset into mongoDB

   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA27.jpg" style="width:700px; height: 500px;">

## Question 2 (b)
Before start or make any queries on MongoDB, we first have to start the MongoDB server using the command `mongod`

### Steps:

1. Open MongoDB Compass. Find the MongoDB Compass terminal or in command prompt with Mongo Shell activated.
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/mongocompass.jpg">
   
2. In the terminal, execute the command `use` followed by database name. For example, I will execute the command `use SupplyStore`

3. Run CRUD Operations.
---
   ### Create query:
   - Run insertOne function in the terminal to insert new data into the collection.
     ```
     db.Sales.insertOne({
      saleDate: ISODate("2023-07-02T16:11:59.565Z"),
      items: [
        {
          name: "book stand",
          tags: ["office", "accessory"],
          price: 10.99,
          quantity: 4
        },
        {
          name: "stapler",
          tags: ["office", "stationery"],
          price: 7.99,
          quantity: 10
        }
      ],
      storeLocation: "Johor",
      customer: {
        gender: "M",
        age: 22,
        email: "afifhazmie2@gmail.com",
        satisfaction: 4,
        couponUsed: false,
        purchaseMethod: "In store"
      }}) 
   
   - the created data can be found inside the collecton by filtering using `{storeLocation: "Johor"}`

     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/createquery.jpg" style="width:500px; height: 400px;">
---
   ### View Query
   - Run the `find` in the Mongosh terminal
     
     ```
     db.Sales.find ( {storeLocation: "Johor" } )
     ```
   
   - the terminal will display the following data based on `find` field
     
     <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/viewquery.jpg" style="width:350px; height: 500px;">
     
 ### Update Query 1
 - Run the `updateOne` in the mongosh terminal with the field that I want to change
 - `updateOne` function is used to update a single document that first match field filter and then the `$set` is used to replace the current data with new data.
 - for example: I want to update the item 1 to bookshelf with price 19.99 and item 2 change the quantity to 15
   
  ```
   db.Sales.updateOne(
  { storeLocation: "Johor" },
  {
    $set: {
      "items.$[item1].name": "bookshelf",
      "items.$[item1].price": 19.99,
      "items.$[item2].quantity": 15
    }
  },
  {
    arrayFilters: [
      { "item1.name": "book stand" },
      { "item2.name": "stapler" }
    ]
  }
)
  ```
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/updateonequery.jpg" style="width:250px; height: 580px;">

 ### Update Query 2
 - Run the `updateMany` in the mongosh terminal with the field that I want to change
 - The `updateMany` function is used to update all the data that satisfied the filtered field.
 - For example in here I will add another data with the same store location "Johor" using the create query
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/NewData.jpg">
   
 - after that i will execute the below query which will filter data with `storeLocation="Johor"` to change it to `storeLocation = "Kuala Lumpur"`
   ```
   db.Sales.updateMany(
     { storeLocation: "Johor" },
     { $set: { storeLocation: "Kuala Lumpur" } }
   )
   ```
   
 - After update the location, when filter using the `storeLocation = "Johor"`, no data will appear as I already change the location.
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/jb.jpg" style="width:750px; height: 300px;">
   
 - The data will show if I filtered using `storeLocation = "Kuala Lumpur"`
   
   <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/kl.jpg" style="width:300px; height: 300px;">
   
### Delete Query 

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



