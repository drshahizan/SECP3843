<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Cai Xuan
#### Matric No.: A20EC0062
#### Dataset: Analytics Dataset

## Question 2 (a)

<h4>Step 1 - Install MongoDB Shell and MongoDB database tools</h4>

Download the MongoDB Shell and MongoDB database tools:

[MongoDB Shell](https://downloads.mongodb.com/compass/mongosh-1.10.1-win32-x64.zip)

[MongoDB Database Tools](https://fastdl.mongodb.org/tools/db/mongodb-database-tools-windows-x86_64-100.7.2.zip)


<h4>Step 2 - MongoDB Shell and Database Tools Setup</h4>

Copy the all the files from the bin file in MongoDB Shell and MongoDB Database Tools that you downloaded to the bin file of MongoDB in your PC. All the files will be shown in the bin file of MongoDB like the image below.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/bin.png" />
</p>

Open the 'Edit Environment Variables For You Account' by searching it in your window search bar. Add a new path of by copying the bin file of MongoDB to the environment variables and click 'OK'. The MongoDB Shell and Database Tools are setup.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/env.png" />
</p>

<h4>Step 3 - Import Data</h4>

To import the data, write the command ```mongoimport "C:\Users\User\Downloads\AA_SpecialTopic\accounts.json" -d AnalyticsDataset -c Accounts``` in your command prompt. ```-d AnalyticsDataset``` means your database name and ```-c Accounts``` is your collection name.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/import%20data.png" />
</p>


<h4>Imported Data</h4>

- Accounts JSON imported

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/acc.png" />
</p>

- Customers JSON imported

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/cust.png" />
</p>

-Transactions JSON imported

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/trans.png" />
</p>

## Question 2 (b)

Make sure to connect to your database by typing the command ```use AnalyticsDataset```

1) Create query

Create a new account_id  = 371140, limit = 10000 and products = "Derivatives".

```
db.Accounts.insertOne({
  account_id: 371140,
  limit: 10000,
  products: [
    "Derivatives",
  ]
})
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/create.png" />
</p>

Result:

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/create_result.png" />
</p>

2) Read query

Read the data where the username is equal to "fmiller" in the Customers table.

```db.Customers.find({username:"fmiller"})```

Result:

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/read.png" />
</p>

3a) Update query

Update the limit number to 8000 which the account_id is equal to 371138.

```
db.Accounts.updateOne(
   { account_id: 371138 },  
   { $set: { limit: 8000 } }  
)
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/update1.png" />
</p>

Result:

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/update1_result1.png" />
</p>

b) Update query 

Update the transaction_count to 86 which the account_id is equal to 443178.

```
db.Transactions.updateOne(
   { account_id: 443178 },  
   { $set: { transaction_count: 86 } }
)
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/update2.png" />
</p>

Result:

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/update2_result2.png" />
</p>

4) Delete query

Delete the data from Accounts table where the account_id is 371138.
```db.Accounts.deleteOne({ account_id: 371138})```

<p align="center">
  <img height="200px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/delete.png" />
</p>

Result:

The result shows null after the data is deleted from the Accounts table.

<p align="center">
  <img height="200px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question2/files/images/delete_result.png" />
</p>









## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


