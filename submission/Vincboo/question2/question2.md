<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Vincent Boo Ee Khai
#### Matric No.: A20EC0231
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 2 (a)
### 1. Prerequisites
Download and install all related software.
1. [MongoDB Community Server](https://www.mongodb.com/try/download/community)
2. [MongoDB Shell](https://www.mongodb.com/try/download/shell)
3. [MongoDB Database Tool](https://www.mongodb.com/try/download/database-tools)

### 2. Edit paths in the system environment variables.
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/6e295d38-07d4-4edb-9f5f-8c19660b0f39"></img>

### 3. Install the dataset [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

### 4. Locate the file
Type in `cd C:\Program Files\MongoDB\Server\6.0\bin` into the command to locate the file.
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/a899f41c-a6ce-460d-b54c-6413ef93b435"></img>

### 5. Launch MongoDB Server
Open the Command Prompt and type `mongod`, then click enter for run.
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/390035d9-3fcc-4bd5-9dfc-2cd7e9b06586"></img>

### 6. Locate back to OS command prompt
Locate back to the OS section by enter `C:\Users\vince`, or else it will cause error such as "missing semicolon".

### 7. Import file into MongoDB
Import file by using the keyword `mongoimport`
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/f2974038-f894-4340-829e-15e2f087640b"></img>

### 8. Access MongoDB Shell
In the command prompt, enter `mongosh` in order to access MongoDB shell. 
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/f5eabe49-fa99-406f-b5e6-04da9365b4bb"></img>

### 9. Final result shown in MongoDB Compass
We can also view and check the imported dataset in MOngoDB Compass.
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/22bbb32a-1a7e-4657-9854-c463d39a6996"></img>

## Question 2 (b)
Enter `use AA` to chage from test to AA database.
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/195d9612-e1e6-42b0-a777-248bb8251579"></img>

### i. Create Query
Using the `.insertOne()` method to insert a single document, if the document being inserted does not have an explicitly defined _id field, MongoDB will automatically includes an _id field with a unique ObjectId value to identify the newly inserted document.
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/1de415af-d240-4a41-98bd-fa90f9f597c1"></img>

The by query using `.insertOne()` into the database. for my case is `db.Stories.updateOne()`.
```
db.Stories.insertOne({href: "http://digg.com/comedy/AA", title: "This_is_All_About_AA!", comments: 15, container: {name: "Offbeat",short_name: "offbeat"}, submit_date: 1268771801, topic: { name: "Comedy", short_name: "comedy" }, promote_date: 1268915964, id: "20230627", media: "news", diggs: 404, description: "AA was given on 25th June and the student were to submit it before 29th June.", link: "http://www.dailymail.co.uk/news/article-1258365/This_is_All_About_AAhtml", user: { name: "babychen", registered: 1141570067, fullname:"Babychen Mathew", icon: "http://digg.com/users/babychen/l.png", profileviews: 24749 }, status: "popular", shorturl: { short_url: "http://digg.com/d31Ln7s", view_count: 3682}});
```

The result after applied `.insertOne()` to create query in command prompt:
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/101872aa-e799-4785-89b7-41ad2a4dd1d8"></img>

Data successfully created into the database:
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/7e0b5afd-863a-44ce-93db-d63e502a5df2"></img>

### ii. View Query
By using `find()`, it will find the documents that related to the query provided.

In this case I will look for my result ased on "title: "This_is_All_About_AA!".
```db.Stories.find({ title: "This_is_All_About_AA!"})```

The result after applying the code:
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/f23f1694-321d-4ec3-a387-b2d22780c28d"></img>

### iii. Update Query
#### 1. Update Query 1
If wanted to update any data into the database, we can use `.updateOne()` which it will updates the first document that matches a specified filter.
`db.Stories.updateOne({title: "This_is_All_About_AA!"},{$set:{comments: 20}})`

The result after apllied the code:
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/5c85a6d0-94b3-40cd-9911-6a7dabaae66d"></img>

#### 2. Update Query 2
We try it again to word (string) instead of numbers (int).
`db.Stories.updateOne({title: "This_is_All_About_AA!"},{$set:{ media: 'test'}})`

The result:
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/5507c758-aff9-4162-b19b-b70cc27389cf"></img>

### iv. Delete Query
For delete query, we can use `deleteOne()` method to delete the first document that matches to the related query. 
`db.Stories.deleteOne({ title: "This_is_All_About_AA!"})`

The result in command prompt:
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/6c07b220-278a-405b-9ab5-5168c4e30546"></img>

The data successfully deleted from the database:
<img  src="https://github.com/drshahizan/SECP3843/assets/120615951/a2e241d0-9602-41d6-a432-874b6fc41364"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



