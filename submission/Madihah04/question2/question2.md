<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Madihah binti Che Zabri
#### Matric No.: A20EC0074
#### Dataset: <a href="https://github.com/drshahizan/dataset/blob/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/07-stories/stories.json">stories.json</a>

## Question 2 (a)
a.	You have been given a JSON file that contains data that must be imported into a MongoDB database. The JSON file must follows the appropriate structure for MongoDB documents. Your task is to outline the step-by-step process to add the data from the JSON file into MongoDB. Provide a detailed explanation of each step involved in the process with screenshots, including any necessary commands. Ensure that your answer covers the preparation of the JSON file, starting the MongoDB server, accessing the MongoDB shell, selecting the target database, choosing the collection, and executing the import command.
#### Prerequisites:

1. Install MongoDB Community Server (*required)
2. Install MongoDB Shell (*required)
3. Install MongoDB Database Tools (optional)
   
#### Download the JSON file

1. Go to <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories">stories.json</a> and download the json file

#### Start MongoDB Server

1. Run `mongod` in command prompt

#### Access MongoDB Shell

1. Run the MongoDB Shell by executing the appropriate command: `mongosh`

#### Setup Database

1. Open MongoDB Compass and create new DB named `Stories` under Collection `Story`.
2. To switch to the intended database, execute the following command: `use Stories`

#### Import Dataset

There are 2 ways to to import dataset.

#### 1. Using command prompt

1. Run this in command prompt `mongoimport --uri mongodb+srv://madihahzabri:admin@cluster0.xgsbper.mongodb.net/ --db Stories --collection story --file "C:\Users\Hp\Downloads\stories.json"`

#### 2. Using command MongoDB Compass
1. Open MongoDB Compass
2. Go to Database > Stories > story (Collection)
3. Click Add Data button
4. Choose Import JSON or CSV file
5. Choose stories.json from file exporer

<img src="../materials/Q2a.png">

## Question 2 (b)

### Start MongoDB Shell

1. Open your terminal or command prompt
2. Run `mongod` in the terminal

<img src="../materials/Q2b.png">


### Create Query

1. Run `mongosh "mongodb+srv://madihahzabri:admin@cluster0.xgsbper.mongodb.net/"` to make connection to MongoDB Atlas
2. Select the intended database `use 
3. Run this query to insert data:
```python
db.story.insertOne({
    "name": "Cakna Madani",
...   "href": "https://www.utusan.com.my/nasional",
...   "title": "Belia boleh tuntut RM200 eBeliaRahmah.",
...   "comments": 0,
...   "container": {
...     "short_name": "ekonomi"
...   },
...   "submit_date": 1654321123,
...   "topic": {
...     "name": "Ekonomi",
...     "short_name": "eco"
...   },
...   "promote_date": 1654321124,
...   "id": "123456",
...   "media": "image",
...   "diggs": 10,
...   "description": "BELIA dan pelajar institut pengajian tinggi boleh mula mendaftar untuk menerima kredit RM200 menerusi program eBeliaRahmah mulai Isnin ini",
...   "link": "https://www.utusan.com.my/nasional/2023/06/belia-boleh-tuntut-rm200-ebeliarahmah-isnin-ini/",
...   "user": {
...     "name": "HUSNI",
...     "registered": 1654321125,
...     "fullname": "MOHD. HUSNI MOHD. NOOR",
...     "icon": "https://www.utusan.com.my/nasional/avatar.jpg",
...     "profileviews": 100
...   },
...   "status": "active",
...   "shorturl": [
...     {
...       "short_url": "https://www.utusan.com.my/belia-boleh-tuntut-rm200-ebeliarahmah-isnin-ini",
...       "view_count": 5
...     }
...   ]
... })
```

4. Check the newly created ouput
<img src="../materials/Q2b(1).png">

### Read Query

1. Run this code on command prompt 
```python
db.story.findOne({ "_id": ObjectId("4ba267dc238d3ba3ca000001") })
```

3. Check the output
<img src="../materials/Q2b(2).png">

### Update Query

1. Run this to update data in one column

```python 
db.story.updateOne({ "_id": ObjectId("4ba267dc238d3ba3ca000001") }, { $set: { "comments": 200 } })
```
<img src="../materials/Q2b(3).png">

2. Run this to update data in mulitple column

```python 
db.story.updateOne({ "_id": ObjectId("4ba267dc238d3ba3ca000001") }, { $set: { "topic.name": "Berita Terkini Popular", "topic.short_name": "berita" } })
```
<img src="../materials/Q2b(4).png">

### Delete Query

1. To delete data:

```python
  db.story.deleteOne({ "_id": ObjectId("4ba267dc238d3ba3ca000001") })
```
<img src="../materials/Q2b(5).png">

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




