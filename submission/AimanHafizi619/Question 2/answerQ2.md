
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
>Do to this location open command prompt or cmd and type in mongod. `Programs Files` > `MongoDB` > `Server` > `6.0` > `bin`.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image7.png)

**Step 3**

The MongoDB Shell is a command-line interface (CLI) tool provided by MongoDB that allows users to interact with MongoDB databases using a JavaScript-based scripting language. It provides a convenient way to perform various database operations, including querying, inserting, updating, and deleting data.

>Type in `mongosh` in a new command prompt in order to get access to MongoDB Shell.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image4.png)

**Step 4**
>Using MongoDB Shell, select database `analytics` by typing `use Analytics`.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image5.png)

**Step 5**
>Using MongoDB Shell, select selection `analyticsdataset`. The command db. should be followed by database name. For example: I will run db.ListingsAndReviews.

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image6.png)

**Step 6**
>Go to `Program Files` > `MongoDB` > `Tools` > `100` > `bin`. Using MongoDB Shell, type in the following code.

`mongoimport --uri mongodb+srv://admin:admin@projectcluster.7sndifd.mongodb.net/ --db analytics --collection analyticsdataset --file "C:\Users\ahmad\Desktop\Django\accounts.json".`

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image8.png)

**Step 7**
Final results should look like below

![Q2](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%202/files/images/Q2%20image9.png)

## Question 2 (b)

**Create Operation**

Create We will be using the db.comments.insertOne() method to insert a single document into the selected collection. This is an example of the method

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




