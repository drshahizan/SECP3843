<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Hong Pei Geok
#### Matric No.: A20EC0044
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets" >Tweets</a>

## Question 2 (a)


## Question 2 (b)
#### a) Create Query <br>
There are 2 methods to insert documents into a MongoDB database. <br>
```insertOne()```: This method inserts a single object into the database. <br>
```insertMany()```: This method inserts an array of objects into the database.

The following example shows the query using ```insertOne()```.
```
db.tweets.insertOne({
  text: "Alternative Assessment.",
  in_reply_to_status_id: null,
  retweet_count: 5,
  contributors: null,
  created_at: "2023-05-25 10:30:00",
  geo: null,
  source: "Twitter",
  coordinates: null,
  in_reply_to_screen_name: null,
  truncated: false,
  entities: { mentions: [], urls: [], hashtags: [] },
  retweeted: false,
  place: null,
  favorited: false,
  in_reply_to_user_id: null
});

```
MongoDB Shell:
<img  src="./files/images/insert.png"></img>
> The above query creates a new document in the tweets collection and includes values for some of the fields like text, retweet_count and created_at.

We can find the inserted document from the database.
<img  src="./files/images/insert1.png"></img>

#### b) Read Query
There are 2 methods to find and select data from a MongoDB collection. <br>
```find()```: The method will find all documents that match the query provided. <br>
```findOne()```: The method will find the first document matches the query provided.
The following example shows the query using ```find()```.
```
db.tweets.find({ source: "web" });
```

MongoDB Shell:
<img  src="./files/images/find2.png"></img>
>The above query retrieves all documents from the "tweets" collection where the "source" field matches the provided value ("web").

Result: 
<img  src="./files/images/find3.png"></img>

#### c) Update Query
There are 2 methods to update an existing document. <br>
```updateOne()```: The updateOne() method will update the first document that is found matching the provided query. <br>
```updateMany()```: The updateMany() method will update all documents that match the provided query.

##### updateOne
The following example shows the query using ```updateOne()```.

```
db.tweets.updateOne(
  { text: "Alternative Assessment."},
  { $set: { retweet_count: 10 } }
);
```
MongoDB Shell:
<img  src="./files/images/update1.png"></img>
> The above query updates a single document in the "tweets" collection that matches the provided "text" field by setting the value of the "retweet_count" field to 10 for the matching document.

Before updating the data:
<img  src="./files/images/update.png"></img>

After updating the data: 
<img  src="./files/images/update2.png"></img>

##### updateMany
The following example shows the query using ```updateMany()```.

```
db.tweets.updateMany(
  { retweet_count: null },
  { $set: { retweet_count: 0 } }
);
```
MongoDB Shell:
<img  src="./files/images/update5.png"></img>
> The above query updates all documents in the "tweets" collection where the "retweet_count" field is null to 0.

Before updating the data:
<img  src="./files/images/update4.png"></img>

After updating the data: 
<img  src="./files/images/update6.png"></img>

#### d) Delete Query
There are 2 methods to delete documents from a MongoDB database. <br>
```deleteOne()```: The deleteOne() method will delete the first document that matches the query provided. <br>
```deleteMany()```: The deleteMany() method will delete all documents that match the query provided.

The following example shows the query using ```deleteOne()```.

```
db.tweets.deleteOne({ text: "Alternative Assessment."});
```
MongoDB Shell:
<img  src="./files/images/delete1.png"></img>
> The above query deletes a single document from the "tweets" collection that matches the provided "text" field value.

Before deleting the data:
<img  src="./files/images/delete.png"></img>

After deleting the data: 
<img  src="./files/images/delete2.png"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



