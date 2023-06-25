<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: MUHAMMAD IMRAN HAKIMI BIN MOHD SHUKRI
#### Matric No.:A20EC0213
#### Dataset:AIRBNB

## Question 2 (a)

Step 1: Prepare the JSON file

Download the [Airbnb dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb). Ensure that the JSON file follows the appropriate structure for MongoDB documents. Each document should be enclosed within curly braces {} and separated by a newline.

![Q2](files/images/q2_7.png)

Step 2: Start the MongoDB server

Open command prompt and start the MongoDB server by running the the `mongod` command.

![Q2](files/images/q2_1.png)

Step 3: Access the MongoDB shell

Run the `mongosh` command to access the MongoDB shell.

![Q2](files/images/q2_2.png)

Step 4: Select the target database

In the MongoDB shell, switch to the desired database. The command `use` should be followed by database name. For example: I will run `use airbnbportal`.

![Q2](files/images/q2_3.png)

Step 5: Select the target collection

In the MongoDB shell, switch to the desired collection. The command `db.` should be followed by database name. For example: I will run `db.ListingsAndReviews`.

![Q2](files/images/q2_8.png)

Step 6: Start importing JSON file

From command prompt, execute `mongoimport --uri mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/ --db airbnbportal --collection ListingsAndReviews --file "C:\Users\imran\Documents\AA Special Topic\listingsAndReviews.json"`. 


Where,

`mongoimport --uri`: The library of MongoDB for importing dataset alongside with connection string.

`--db`: The database name in MongoDB.

`--collection`: The collection name for the database.

`--file`: The path to JSON file.

![Q2](files/images/q2_5.png)

![Q2](files/images/q2_6.png)

## Question 2 (b)

In order to execute CRUD operations for MongoDB,

### Step 1: Start the MongoDB server

Open command prompt and start the MongoDB server by running the the `mongod` command.

![Q2](files/images/q2_1.png)

### Step 2: Access the MongoDB shell

Run the `mongosh` command to access the MongoDB shell.

### Step 3: Select the target database

In the MongoDB shell, switch to the desired database. The command `use` should be followed by database name. For example: I will run `use airbnbportal`.

![Q2](files/images/q2_3.png)

### Step 4: Run CRUD operations.

From the command prompt or terminal,

#### For Create Operation:

Run the insertOne function. This will add a new data. Since the `_id` is not specified, MongoDB will create a random `ObjectId`.

```
db.ListingsAndReviews.insertOne({
"name": "1 Billion Dollar Mansion",
"summary": "Huge house made with 30,000 diamonds.",
"property_type": "Bungalow",
"room_type": "Entire home/apt",
"bedrooms": 15,
"bathrooms": 10,
"price": 20000})
```
![Q2](files/images/q2_11.png)

#### For Read Operation:

Run the find function. This will search for inquired column or attribute. In this example, I will be searching data with `name` : `"1 Billion Dollar Mansion"`

```
db.ListingsAndReviews.find({
"name": "1 Billion Dollar Mansion"})
```

![Q2](files/images/q2_10.png)


#### For Update Operation:

1. Run the updateOne function. This will search for inquired column or attribute, and update only one of the search results.

```
db.ListingsAndReviews.updateOne({
"name": "1 Billion Dollar Mansion" },
{ $set: { "price": 50000 } })
```

![Q2](files/images/q2_12.png)

![Q2](files/images/q2_14.png)

2. Run the updateMany function. This will search for inquired column or attribute, and update all of the search results.

```
db.ListingsAndReviews.updateMany({
"cancellation_policy": "moderate" },
{ $set: { "cancellation_policy": "normal" }})
```

![Q2](files/images/q2_15.png)

![Q2](files/images/q2_16.png)


#### For Delete Operation:

Run the deleteOne function. This will search for inquired column or attribute, and delete only one of the search results.

```
db.ListingsAndReviews.deleteOne({
"name": "1 Billion Dollar Mansion" })
```

![Q2](files/images/q2_17.png)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




