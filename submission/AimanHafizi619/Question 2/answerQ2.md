
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: AHMAD AIMAN HAFIZI BIN MUHAMMAD
#### Matric No.: A20EC0177
#### Dataset: ANALYTICS DATASET

## Question 2 (a)
**Step 1**
>To import the three JSON files into MongoDB database, first download the [Analytics dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics).

accounts.json
![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image1.png)

customer.json
![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image2.png)

transactions.json
![Q3](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q3%20image3.png)

**Step 2**
>Go to this location open command prompt or cmd and type in mongod. `Programs Files` > `MongoDB` > `Server` > `6.0` > `bin`.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image7.png)

**Step 3**

The MongoDB Shell is a command-line interface (CLI) tool provided by MongoDB that allows users to interact with MongoDB databases using a JavaScript-based scripting language. It provides a convenient way to perform various database operations, including querying, inserting, updating, and deleting data.

>Type in `mongosh` in a new command prompt in order to get access to MongoDB Shell.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image4.png)

**Step 4**
>Using MongoDB Shell, select database `analytics` by typing `use Analytics`.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image10.png)

**Step 7**
>Go to `Program Files` > `MongoDB` > `Tools` > `100` > `bin`. Using MongoDB Shell, type in the following codes one after the other.

`mongoimport --uri mongodb+srv://admin:admin@projectcluster.7sndifd.mongodb.net/ --db analytics --collection Analytics --file "C:\Users\ahmad\Desktop\Analytics\accounts.json".`

`mongoimport --uri mongodb+srv://admin:admin@projectcluster.7sndifd.mongodb.net/ --db analytics --collection Analytics --file "C:\Users\ahmad\Desktop\Analytics\customers.json".`

`mongoimport --uri mongodb+srv://admin:admin@projectcluster.7sndifd.mongodb.net/ --db analytics --collection Analytics --file "C:\Users\ahmad\Desktop\Analytics\transactions.json".`

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image%2012.png)

**Step 8**
>Final results should look like below. All three collections named `Accounts`, `Customers`, and `Transactions` has been automatically filled with data from the JSON files.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image%2013.png)
![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image14.png)
![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image15.png)

## Question 2 (b)

Before applying the CRUD (Create, Read, Update, Delete) operations, do these steps first

**Step 1**: Start MongoDB server
>Clode the current command prompt

>Go to this location open command prompt or cmd and type in mongod. `Programs Files` > `MongoDB` > `Server` > `6.0` > `bin` again.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image17.png)

**Step 2**: Start MongoDB shell
>To run the mongosh command to access the MongoDB shell by type in `mongosh` in the command prompt

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image19.png)

**Step 3**: Select Database
>Type in `use Analytics` to access the `Analytics` database.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image20.png)

**Step 4**: Select Collection
>Type in `db.Accounts` to access the `Accounts` collection. The CRUD operation will take place in the Accounts collection.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image21.png)

**Step 5**: Create Operation
>Type in the code below to add a new row of data into the Accounts collections. There will be four attributes `_id`, `account_id`, `limit`, and `products`.

>MongoDB will create a random ObjectId if left unspecified.

```
db.Accounts.insertOne({
... "account_id":101010,
... "limit":2500,
... "products":["InvestmentStock"]})
```

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image22.png)

**Step 6**: Read Operation
>Type in the code below to find a particular row of data from Accounts collections.

```
db.Accounts.find({
... "account_id":101010})
```

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image23.png)

**Step 7**: Update Operation (1)
>Type in the code below to search for a particular record using the `account_id`

>Then select an attribute to change

>Only one record will be change that has the mentioned `account_id`

>Redo step 6 to see the old and new values of `limit`

```
db.Accounts.updateOne(
... {"account_id":101010},
... {$set:{"limit":5200}})
```

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image24.png)

**Step 8**: Update Operation (2)
>This code is to update all records that has the mentioned `limit`

>Type in the code

>Then select attribute `limit` to change

>Only one record will be change that has the mentioned `limit`

>Redo step 6 to see the old and new values of `limit`

```
db.Accounts.updateMany(
... {"limit":5200},
... {$set:{"limit":10400}})
```

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image25.png)

**Step 9**: Delete Operation
>Type in the code below to delete one record from the Accounts collection

>Search by `account_id`

>Redo step 6 and search for previous `account_id`. As demonstrated, the `account_id` doesn't exist anymore

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image26.png)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




