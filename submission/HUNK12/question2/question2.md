<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Mikhel Adam Bin Muhammad Ezrin
#### Matric No.: A20EC0237
#### Dataset: [Tweets](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets)

## Question 2 (a)
### Ensure JSON file follows the proper structure for importing into MongoDB
In this case, it does not because it is not contained within a square bracket `[]`. Each JSON document should be enclosed within curly braces `{}` and separated by commas `,`  which this dataset is. To add the square brackets to the JSON file, we can actually just simply modify the file and add the brackets using a text editor. However for this case, a Python script was created to read the JSON file, add the brackets, then save it into a new file. Below is the script to perform the previously mentioned actions
```
import json

# Read the JSON file
with open('tweets.json', 'r') as file:
    data = file.readlines()

# Add square brackets to the entire dataset
fixed_data = '[' + ','.join(data) + ']'

# Save the fixed dataset to a new JSON file
with open('fixed_tweets.json', 'w') as file:
    file.write(fixed_data)
```
### Install the following 
1. [MongoDB Community Server](https://www.mongodb.com/try/download/community-kubernetes-operator)
2. [MongoDB Shell](https://www.mongodb.com/try/download/shell)
3. [MongoDB Command Line Database Tools](https://www.mongodb.com/try/download/database-tools)

### Start the MongoDB Server
1. Open a command prompt in `C:\Program Files\MongoDB\Server\6.0\bin`. Then in the command prompt, type `mongod` to start start the server
   ![image](https://github.com/drshahizan/SECP3843/assets/3646429/b6974d26-7293-453d-ab88-6856cd3bffeb)
2. Access the MongoDB Shell by typing `mongosh`
3. Select the target database by typing `use STDE`
4. Now import the updated JSON file into MongoDB with the following command which contains our connection string, db and collection name as well as the path for the file
```
mongoimport --uri=mongodb+srv://mikhel:admin@cluster0.kwav8pt.mongodb.net/ --db=STDE --collection=tweets --file="C:\Users\HI THERE\Desktop\AA Special Topic DE\ST\tweets\fixed_tweets.json" --jsonArray
```
![image](https://github.com/drshahizan/SECP3843/assets/3646429/662d0e92-bdda-4b28-b584-a71666bad59f)

Now if we look in MongoDB Compass, we should be able to see the imported data.

![image](https://github.com/drshahizan/SECP3843/assets/3646429/994d5741-3593-4c5c-89a9-b5262d8d95e1)




## Question 2 (b)
### CRUD Operations

**1. Create**

 Let's insert a new entry into the database by using the command `insertOne()`. Below is how this method can be used to insert a single entry into the database via CLI
```
db.tweets.insertOne({
  text: "This is just a demonstration to show how the inserOne() method works",
  in_reply_to_status_id: null,
  retweet_count: 69,
  contributors: null,
  created_at: "2023-06-27 15:04:00",
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
![image](https://github.com/drshahizan/SECP3843/assets/3646429/4dab4038-b999-4121-aeb6-3d6c683eb0a5)

As we can see below, the entry has successfully been inserted
![image](https://github.com/drshahizan/SECP3843/assets/3646429/66f54390-227c-41e5-ab48-8d97fab93cab)

**2. Read**

Let's use the MongoDB Shell to find and read an entry in the database. We can do so by using the `find()` method. Below we can see how to use it to search for an entry with the ObjectId: `5c8eccb0caa187d17ca6240d` 
```
db.tweets.find({ _id: ObjectId("5c8eccb0caa187d17ca6240d") });
```
We can see below it successfully found the entry
![image](https://github.com/drshahizan/SECP3843/assets/3646429/6fbf86d4-7694-4016-b5b6-f7e25888dae9)


**3. Update**

Now, let's demonstrate two methods/queries to update an entry in the database.

First I will demonstrate the use of the `updateOne()` method which is used to update the first entry found that matches the query. Below, we can see how it's used to update the `text` field of an entry
```
db.tweets.updateOne(
  { text: "This is just a demonstration to show how the inserOne() method works"},
  { $set: { text: "This text has been updated" } }
);
```
As we can see, after running this query, the text has been updated

![image](https://github.com/drshahizan/SECP3843/assets/3646429/7217ee8c-fb00-4eb2-8cdb-14f9cca165a5)

Next, I'll demonstrate the `updateMany()` method which is used to update **all** the entries matching the query. Below we can see how it's used to update entries with the `place` field from null to "Earth"
```
db.tweets.updateMany(
  { place: null },
  { $set: { place: "Earth" } }
);
```
As we can see, the `place` field that had the value null, now has the value "Earth"

![image](https://github.com/drshahizan/SECP3843/assets/3646429/20467820-6b5d-48db-ab87-a5d4fc6a8fd6)![image](https://github.com/drshahizan/SECP3843/assets/3646429/785ad666-828c-405c-9d02-b3eb02f639d8)

**4. Delete**

Finally, I will demonstrate how to delete an entry using the `deleteOne()` method which deletes the first entry that matches the query. Below we can see how it’s used to delete the entry we had previously created.
```
db.tweets.deleteOne({ text: "This text has been updated"});
```
After running the command, we can see the entry can no longer be found in the database.

![image](https://github.com/drshahizan/SECP3843/assets/3646429/0531f4b5-224c-442f-9f37-33f33c2b400b)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



