<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: FARAH IRDINA BINTI AHMAD BAHARUDIN
#### Matric No.: A20EC0035
#### Dataset: AIRBNB LISTINGS DATASET

## Question 2 (a)

### Steps to import JSON file into MongoDB

The JSON file that I have been received is about AirBnb Listing Reviews. To import this JSON file inside MongoDB database, there are a few steps that must be followed.

#### 1. Install MongoDB Command Line Database Tools

Firstly, click [here](https://www.mongodb.com/try/download/bi-connector) to download MongoDB Command Line Database Tools. Click Download and install it.

#### 2. Install MongoDB Shell

Next, click [here](https://www.mongodb.com/try/download/bi-connector) to download MongoDB Shell. Click Download and install it.

#### 3. Run mongosh

Then, open the directory file that has the mongosh.exe by using command prompt and type the code below. 

```
mongosh
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/mongosh.png)

#### 4. Search for existing databases

Next, to search the existing databases inside your MongoDB, type the code below. 

```
show dbs
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/dbs.png)

#### 5. Use any database

Next, use any database that you prefer based on the list of databases above. I will use 'admin' database to store the JSON data. Type the code below. 

```
use admin
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/admin.png)

#### 6. Search for existing collections

Then, to search the existing collections inside your database, type the code below. 

```
show collections
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/collections.png)

#### 7. Import JSON file into MongoDB

Lastly, you can import your JSON file into MongoDB. Type the code below. 

```
mongoimport --db admin --collection airbnb --file C:\Users\User\Downloads\listingsAndReviews.json
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/mongoimport.png)

### Output

Finally, the JSON file will be stored in MongoDB.

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/output.png)

## Question 2 (b)

There are five queries that will be performed which are Create, Read, two queries of Update, and Delete (CRUD) on the documents stored in the MongoDB database. All the queries have different types of functions.

#### 1. Connect to MongoDB

Before performing any operations, you need to connect to the MongoDB database. Open the directory file of mongosh.exe and insert the MongoDB's connection string. 

```
mongodb://localhost:27017
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/localhost.png)

#### 2. Use any database

Next, use the database that you have stored the data. I will use 'admin' database since it is the database that I used to store the airbnb data. Type the code below. 

```
use admin
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/admin.png)

#### 3. Perform operations

##### - Create

Create allows user to insert data into the database. Type the code below to insert one.

```
db.airbnb.insertOne({
  "_id": "1234567",
  "listing_url": "https://www.airbnb.com/rooms/1234567",
  "name": "Beautiful Beachfront Villa with Stunning Views",
  "summary": "Escape to paradise and enjoy breathtaking ocean views from this luxurious beachfront villa. Perfect for a relaxing vacation!",
  "space": "Experience the ultimate beachfront living in this spacious villa. With 3 bedrooms and 2 bathrooms, it can accommodate up to 8 guests comfortably. The villa features a fully equipped kitchen, a stylish living room, and a private balcony overlooking the ocean. You'll have direct access to the beach, where you can swim, sunbathe, or take a leisurely walk along the shore.",
  "description": "Escape to paradise and enjoy breathtaking ocean views from this luxurious beachfront villa. Perfect for a relaxing vacation!\n\nExperience the ultimate beachfront living in this spacious villa. With 3 bedrooms and 2 bathrooms, it can accommodate up to 8 guests comfortably. The villa features a fully equipped kitchen, a stylish living room, and a private balcony overlooking the ocean. You'll have direct access to the beach, where you can swim, sunbathe, or take a leisurely walk along the shore.",
  "neighborhood_overview": "The villa is located in a peaceful beachfront community, offering tranquility and privacy. It's just a short drive away from local attractions, restaurants, and shops. You can also explore nearby hiking trails and enjoy various water activities such as snorkeling and kayaking.",
  "notes": "Please note that a security deposit of $500 is required upon check-in. This will be refunded upon checkout, subject to any damages or additional charges.",
  "transit": "A rental car is recommended for getting around the area. Parking is available on-site for guests. Public transportation options are also accessible nearby.",
  "access": "Guests will have full access to the villa and all its amenities. The community facilities, including a swimming pool, fitness center, and tennis courts, are also available for guests to use.",
  "interaction": "Our team is available 24/7 to assist you with any questions or concerns. We strive to provide a seamless and enjoyable experience for our guests.",
  "house_rules": "1. No smoking allowed inside the villa.\n2. Pets are not permitted.\n3. Please respect the quiet hours between 10 PM and 8 AM.\n4. Keep the villa clean and tidy.\n5. Report any damages or issues to the host immediately.\n6. Enjoy your stay and have a wonderful vacation!",
  "property_type": "Villa",
  "room_type": "Entire home/apt",
  "bed_type": "Real Bed",
  "minimum_nights": "5",
  "maximum_nights": "30",
  "cancellation_policy": "strict",
  "last_scraped": {
    "$date": {
      "$numberLong": "1654300800000"
    }
  },
  "calendar_last_scraped": {
    "$date": {
      "$numberLong": "1654300800000"
    }
  },
  "first_review": {
    "$date": {
      "$numberLong": "1654286400000"
    }
  },
  "last_review": {
    "$date": {
      "$numberLong": "1654286400000"
    }
  },
  "accommodates": {
    "$numberInt": "8"
  },
  "bedrooms": {
    "$numberInt": "3"
  },
  "bathrooms": {
    "$numberInt": "2"
  },
  "beds": {
    "$numberInt": "4"
  }
})
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/insert.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/insert2.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/insert3.png)

##### - Read

Read allows user to find the data from the database. Type the code below to find one.

```
db.airbnb.find({_id:"1234567"})
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/read.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/insert3.png)

##### - Update #1

The first update allows user to update the data from the database. Type the code below to update one.

```
db.airbnb.updateOne({_id:"1234567"}, {$set: {"name": "Beautiful gingerbread house"}})
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/update.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/update2.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/update5.png)

##### - Update #2

The second update allows user to replace all column in a data from the database. Type the code below to replace one.

```
db.airbnb.replaceOne({_id:"1234567"}, {_id: "1234567", instock: [{name: "Beautiful house"}]})
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/update3.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/update4.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/update6.png)

##### - Delete

Delete allows user to delete data from the database. Type the code below to delete one.

```
db.airbnb.deleteOne({_id:"1234567"})
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/delete.png)
![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question2/files/images/delete2.png)

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



