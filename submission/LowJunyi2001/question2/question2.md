<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Low Junyi
#### Matric No.: A20EC0071
#### Dataset: [Airbnb](https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb)

## Table of Contents
- [Question 2 (a)](question-2-(a))
- [Question 2 (b)](question-2-(b))

## Question 2 (a)

### Prerequisites
Download and Install All Required Software.
- [MongoDB Community Server](https://www.mongodb.com/try/download/community)<br>

- [MongoDB Shell](https://www.mongodb.com/try/download/shell) <br>
  
- [MongoDB Command Line Database Tools](https://www.mongodb.com/try/download/database-tools) <br>



### Step 1: Prepare the JSON File
- Download the dataset <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb" >listingsAndReviews</a>.

### Step 2: Start the MongoDB Server
- Move all the .exe files from MongoDB Shell and  MongoDB Command Line Database Tools into the MongoDB bin folder[C:\Program Files\MongoDB\Server\6.0\bin].  

The .exe file in MongoDB Shell:

<img src="https://github.com/drshahizan/SECP3843/assets/120614501/b1018280-1188-4172-81a0-6ba0fc9f6f3a"></img>

The .exe file in MongoDB Command Line Database Tools:
<img src="https://github.com/drshahizan/SECP3843/assets/120614501/82b86e7a-8246-4927-9c6b-1c9de55f0615"></img>

- Open Command Prompt and paste the following code and run.
```
cd C:\Program Files\MongoDB\Server\6.0\bin
```

- Start the MongoDB server by running the mongod command. 
```
mongod
```
Command Prompt:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/56d70022-c686-48cd-b7d3-83984142d527"></img>


### Step 3: Import Dataset
- The provided command mongoimport is used to import the JSON file listingsAndReviews.json into a MongoDB database named AA and the data will be stored in a collection called db_airbnb.
```
mongoimport "C:\Users\user\Downloads\listingsAndReviews.json" -d AA -c db_airbnb
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/4fdcd2b0-638f-49d3-bec8-0d6dd8b340ab"></img>

- The similar dataset can be found in MongoDB Compass
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/5cf55382-90be-4420-b0b2-1322c6a17172"></img>

### Step 4: Access MongoDB Shell
- Repen Command Prompt and paste the following code and run.
```
cd C:\Program Files\MongoDB\Server\6.0\bin
```

- To access the MongoDB shell, insert
```
mongosh
``` 
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/8b475845-844a-465c-8170-f433e1adace4"></img>

- The list of all databases running on MongoDB Server including default and user-defined databases can be seen with 
```
show dbs
``` 
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/2c3f4fe0-4db9-4e20-97d5-45905df7b75c"></img>

- Then enter the following code to switch to the desired database where we want.
```
use AA
``` 
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/995d0766-a1d3-4719-91f0-83da4afbf1e6"></img>

## Question 2 (b)
### i. Create 
Use the `insertOne()` method in MongoDB to create a new document. Here's the example query:
```
db.db_airbnb.insertOne( {"listing_url":"https://www.airbnb.com/rooms/10075934","name":"Duplex", "summary":"Modern and convenient room ", "description":"clean and fully furnish, 2 minutes walking distance to train station", "neighbourhood_overview":"lots of skyrise buildings", "notes":"have an enjoyable shopping experience living here", "transit":"train and bicycle rental", "access":"available to help guest", "interaction":"cot-10$", "house_rules":"make home your comfort", "property_type":"duplex", "room_type":"duplex room", "bed_type":"double bed", "minimum_nights":"1", "maximum_nights":"10", "cancellation_policy":"flexible", "last_scraped":"2019-03-11T05:00:00.000+00:00", "calender_last_scraped":"2019-03-11T05:00.000+00:00", "first_review":"2012-01-03T05:00:00.000+00:00", "last_review":"2020-01-20T05:00:00.000+00:00", "accomodates":"4", "bedrooms":"2", "beds":"2"})
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/e1b7c84c-46de-4ea5-9467-fbd2e5e9eb2d"></img>

Created document in the mongoDB database:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/c8a11ae3-71c2-4204-8738-98ddad84b80a"></img>

### ii.Read
Use db.find() method in MongoDB to find retrieve document
For example search for the listing_url "https://www.airbnb.com/rooms/10267144":

```
db.db_airbnb.find({'listing_url' : 'https://www.airbnb.com/rooms/10267144'})
```
Command Prompt:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/b9f4f1f6-d1a8-4c7d-a13d-3300be058dc7"></img>

Mongo DB:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/e309d39b-396f-4d52-9f50-cc3382ddd928"></img>

### iii. Update
#### a) updateOne()
Use `updateOne()` method in MongoDB to update a single document 
The update is for name value "IPANEMA LUXURY PENTHOUSE with MAID" and set it to "HAWAII PENTHOUSE".
```
db.db_airbnb.updateOne(
  { 'name': 'IPANEMA LUXURY PENTHOUSE with MAID' }, // Specify the filter criteria to match the document
  { $set: { 'name': 'HAWAII PENTHOUSE' }  // Update the name field
})

Command Prompt:
```
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/8955f15d-0413-4eb0-a587-3b30970e4dd0"></img>

MongoDB before update:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/342573e1-f4b6-493e-9fcb-731f2d8eeb67"></img>

MongoDB after update:
<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/ee8b2b26-7451-4420-bef0-07812c50aca1"></img>
Name is changed from `IPANEMA LUXURY PENTHOUSE with MAID` to `HAWAII PENTHOUSE`

#### b) updateMany()




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



