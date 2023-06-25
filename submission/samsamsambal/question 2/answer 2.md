<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.
# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Luqman Ariff Bin Noor Azhar
#### Matric No.: A20EC0202
#### Dataset: 03 - Movies

## Question 2 (a)
Step 1: Prepare the JSON file

Download the Movies dataset. There should be four JSON files, comments, movies, theaters, and users. Download all four files and put them in a single folder.
![Q2](files/images/pic4.png)

Step 2: Command Prompt

Head over to the file where the MongoDB file is located. Navigate through the files until you see the `bin` file. Open a Command Prompt from there. <br>
![Q2](files/images/pic3.png)

Step 3: Import the JSON file

From the command prompt, execute `mongoimport --db mflix --collection movies --file "C:\Users\User\Desktop\Luqman's Work stuff\sem 6 shits\Dataset\movies.json"`. The data will be imported into your localhost and it will also automatically create both the database and the collection.

`mongoimport`: The MongoDB library we will be using to import the dataset. <br>

`--db`: The database name <br>

`--collection`: The collection name <br>

`--file`: The file path to the JSON file <br>

![Q2](files/images/pic1.png)
![Q2](files/images/pic2.png)
## Question 2 (b)
1. Create
We will be using the `db.comments.insertOne()` method to insert a single document into the selected collection. This is an example of the method
```
db.comments.insertOne({
  _id: ObjectId(),
  name: "John Doe",
  email: "johndoe@example.com",
  movie_id: ObjectId("5b7327724a68c3f7a7bcb1ae"),
  text: "This is a great movie!",
  date: ISODate("2023-06-25T12:00:00Z")
})
```

2. Read
To read a single document or multiple simply use `db.movies.find()` method. It will search through the whole document to find a document that fits the description. 
```
db.movies.find({ title: "Civilization" })
```

4. Update
To update a single document, we can use `db.users.updateOne()` method which will update only one. If we want to update multiple documents, we can use `db.movies.updateMany()` method to update multiple documents.
```
db.users.updateOne(
   { _id: ObjectId("59b99db4cfa9a34dcd7885b6") },
   { $set: { name: "Jane Doe" } }
)
```

```
db.movies.updateMany(
   { countries: "USA" },
   { $set: { countries: "Amerika" } }
)
```

6. Delete
To delete a single document we can use `db.users.deleteOne()` method.
```
db.users.deleteOne({ name: "Joffrey Baratheon" })
```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
