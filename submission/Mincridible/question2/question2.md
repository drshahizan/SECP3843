<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: AHMAD MUHAIMIN BIN AHMAD HAMBALI

#### Matric No.: A20EC0006

#### Dataset: Companies

## Question 2 (a)

#### Prior Installation:

1. Install MongoDB Shell
2. Install MongoDB Database Tools
3. Make sure that you add those two path into system environment variable

#### Prepare the JSON file

1. Go to <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies">Companies Dataset</a> and download the json file

#### Start MongoDB Server

1. Run `mongod` in command prompt
<img src="../materials/Q2(a).png">

#### Access MongoDB Shell

1. Run the MongoDB Shell by executing the appropriate command: `mongosh`
<img src="../materials/Q2_2.png">

#### Setup Database

1. Open MongoDB Compass and create new Database named 'Companies' and Collection.
2. To switch to the intended database, execute the following command: `use Companies`

#### Import Dataset

1. Run this in command prompt ` mongoimport --uri mongodb+srv://mincridible:minzpro1@min.tan7fdn.mongodb.net/ --db Companies --collection CompaniesMeta --file "C:\Users\Hp\Downloads\companies.json" `

<img src="../materials/Q2_3.png">

2. Validate the imported dataset on MongoDB Compass

<img src="../materials/Q2_4.png">





#### 
## Question 2 (b)

### Start MongoDB Shell

1. Open your terminal or command prompt
2. Run `mongod` in the terminal

<img src="../materials/Q2_5.png">


### Create Operation

1. Run `mongosh "mongodb+srv://mincridible:minzpro1@min.tan7fdn.mongodb.net/"` to make connection to MongoDB Atlas
2. Select the intended database `use 
3. Run this query:
```python
  db.CompaniesMeta.insertOne({
  name: "Ahmad Muhaimin Bin Ahmad Hambali",
  age: 22,
  email: "ahmadmuhaimin135@gmail.com",
  matricNO: "A20EC0006"
})
```

4. Check the newly created ouput
<img src="../materials/Q2_6.png">

### Read Operation

1. Run `db.CompaniesMeta.find({}, { name: "Ahmad Muhaimin Bin Ahmad Hambali", email: "ahmadmuhaimin135@gmail.com" })` on command prompt or MongoDB Shell

2. Check the output
<img src="../materials/Q2_7.png">

### Update Operation

1. Run this to update one data

```python 
db.CompaniesMeta.updateOne(
  { name: "Ahmad Muhaimin Bin Ahmad Hambali" },
  { $set: { age: 23 } }
)
```
<img src="../materials/Q2_8.png">

2. Run this to update mulitple data

```python 
db.CompaniesMeta.updateMany(
  { age: { $gte: 20 } },
  { $inc: { age: 5 } }
)
```
<img src="../materials/Q2_9.png">

### Delete Operation

1. To delete one data we can use this:

```db.CompaniesMeta.deleteOne(
  { name: "Ahmad Muhaimin Bin Ahmad Hambali" }, {age: 28}
)
```
<img src="../materials/Q2_10.png">




## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
