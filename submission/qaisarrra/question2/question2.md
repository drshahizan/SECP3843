<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Qaisara binti Rohzan
#### Matric No.: A20EC0133
#### Dataset: 04 - Companies

## Question 2 (a)
The answer to the question is divided into the following segments:
* [Prerequisites](#-prerequisites)
* [Preparation of JSON file](#️-preparation-of-json-file)
* [Starting MongoDB Server](#-starting-mongodb-server)
* [Import Dataset](#-import-dataset)
* [Accessing MongoDB Shell](#-accessing-mongodb-shell)
<br></br>

### Prerequisites
To carry out the tasks of this question, it it crucial for to do the following:
1. Install [MongoDB Community Server](https://www.mongodb.com/try/download/community)
2. Install [MongoDB Shell](https://www.mongodb.com/try/download/shell)
3. Install [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools)
4. Edit paths in the system environment variables. Include the MongoDB and Mongosh folder directory
<br></br>

### Preparation of JSON file
Ensure that you have downloaded the [Companies dataset](https://github.com/drshahizan/dataset/blob/main/mongodb/04-companies/companies.json) into your local device. Place it in a destination that is easily accessible.
<br></br>

### Starting MongoDB Server
Open command prompt by pressing on the Windows key + R **OR** type cmd or cmd.exe in the Run command box before pressing **Enter**. I start off by inputing the command below to take regard of the MongoDB version I have installed.
```bash
mongod --version
```
The next line of command processes data requests, maintains data access, and runs background management tasks. 
```bash
mongod 
```
Below shows the expected output of the commands:
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Start%20MongoDB%20Server.png">
</p>
<br>

### Import Dataset
To import the JSON dataset into MongoDB, ensure that you have already installed **MongoDB Database Tools**. In the Command Prompt Terminal, change the directory to the **bin** folder of **MongoDB - Tools**.
```bash
cd C:\Program Files\MongoDB\Tools\100\bin
```
The next line of command is used for listing computer files and directories. It is one of the fundamental instructions for navigating the file system.
```bash
dir
```
The following line of command allows me to import the dataset into MongoDB, where **-d** is the name of the database  and **-c** is the name of the collection. Do specify the correct path in which the dataset file is located. 
```bash
mongoimport "C:\Users\Qaisara Rohzan\Desktop\companies.json" -d AA -c Companies
```
Below shows the expected output of the commands:
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Import%20Dataset.png">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Dataset%20Successfully%20Uploaded.png">
</p>
<br></br>

### Accessing MongoDB Shell
Run the command from your server prompt to access the MongoDB shell. By default, the programme launches a shell linked to a locally installed MongoDB instance running on port 27017.
```bash
mongosh
```
The next command (after **test>**) allows me to see the existing databases in our MongoDB. As you can see, the **AA** database that stores the Companies dataset can be found if you input this line of command.
```bash
show cbs
```
Below shows the expected output of the command:
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Access%20MongoDB%20Shell.png">
</p>
<br></br>

## Question 2 (b)
For this question, I will have to create FIVE (5) MongoDB queries that demonstrate various **Create, Read, Update, and Delete (CRUD)** operations on the **Companies** database. The answer to the question is divided into the following segments:
* [Create - 1 Query](#-create-1-query)
* [Read - 1 Query](#️-read-1-query)
* [Update - 2 Queries](#-update-2-queries)
* [Delete - 1 Query](#-delete-1-query)
<br></br>

### Create
 For this segment, I have previously deleted the document at the **Delete** section and now I am recreating it using this method. You can also use the **sample document** from this [page](https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies). However, do not include the document ID as MongoDB will automatically generate it for you. I have also emptied certain arrays for future modification. To create a record using the MongoDB shell, I will use [db.collection.insertOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.insertOne/). The **insertOne()** method will allow me to create a document containing the following queries:
```bash
db.Companies.insertOne(
   {
      name: 'Mobiance', 
      permalink: 'mobiance', 
      crunchbase_url: 'http://www.crunchbase.com/company/mobiance',  
      homepage_url: 'http://www.mobiance.com', 
      blog_url: 'http://mobiance.wordpress.com/', 
      blog_feed_url: 'http://mobiance.wordpress.com/feed/', 
      twitter_username: null, 
      category_code: 'web', 
      number_of_employees: 5, 
      founded_year: 2004, 
      founded_month: 10, 
      founded_day: 1, 
      deadpooled_year: null, 
      deadpooled_month: null, 
      deadpooled_day: null, 
      deadpooled_url: null, 
      tag_list: null, 
      alias_list: null, 
      email_address: 'info@mobiance.com', 
      phone_number: '+91-80- 41264756', 
      description: null, 
      created_at: 'Tue Feb 12 17:31:58 UTC 2008',
      updated_at: 'Thu Dec 01 07:37:10 UTC 2011', 
      overview: '<p>Mobiance provides the technology to track cell phones whose owners have give them permission to be tracked for business or consumer applications</p>',       image:[], 
      products: [], 
      relationships: [], 
      competitions: [], 
      providerships: [], 
      total_money_raised: '$0', 
      funding_rounds: [], 
      investments: [], 
      acquisition: null, 
      acquisitions: [], 
      offices: [], 
      milestones: [], 
      ipo: null, 
      video_embeds: [], 
      screenshots: [], 
      external_links: [], 
      partners: []
   }
 )
```
Below shows the expected output of the command:
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Create%20from%20MongoDB%20Shell.png">
</p>
To view the document that we have created, simply search the query on MongoDB, the outcome should be as follows:

```bash
{"email_address": "info@mobiance.com"}
```
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Create%20from%20MongoDB.png">
</p>
<br></br>

### Read
Since the JSON dataset stores approximately **9500 rows** of records of **42 attributes**, it surely can be difficult to traverse through the list and find the specific line of record. To find a record using the MongoDB shell, I will have to utilize the [db.collection.find()](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/) that acts as a search bar. The **find()** method will return a document that matches the result of the query. For this example, the query that I am interested to find would be the email address of a company (info@mobiance.com).
```bash
 db.Companies.find({"email_address": "info@mobiance.com"})
```
Below shows the expected output snippet of the command:
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Read%20from%20MongoDB%20Shell.png">
</p>
To read/view the document, simply search the query on MongoDB and click 'Find'. The outcome should be as follows:

```bash
{"email_address": "info@mobiance.com"}
```
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Read%20from%20MongoDB.png">
</p>
<br></br>

### Update 
There are two alternative ways to update document(s) using MongoDB Shell.

**a. Update Single Document**

To update contents of a single document, I used [db.collection.updateOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/). To locate the record, I used the **{"email_address": "info@mobiance.com"}** query followed by setting the query that we would like to change. In the figures below, we can see that the **twitter_username** in the document is **null**, before setting it to **mobiance**.
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Before%20UpdateOne.png">
</p>

Execute this command in MongoDB Shell to set null valued twitter_username to **mobiance**
```bash
db.Companies.updateOne(
   {
      "email_address": "info@mobiance.com"
   },
   {
      $set: { twitter_username: "mobiance"}
   }
)
```
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/UpdateOne%20from%20MongoDB%20Shell.png">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/After%20UpdateOne.png">
</p>


**b. Update Many Documents**

To update contents of multiple documents, I used [db.collection.updateMany()](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateMany/). To locate the record, I used the **{"twitter_username": "", founded_year: 2004}** query followed by setting the query that we would like to change. In the figures below, we can see that the **twitter_username** in the document is **null**, before setting it to **temporary**. We can see that MongoDB returns 92 rows of records in which the column **twitter_username** are empty AND **founded_year** is **2004**.
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Before%20UpdateMany.png">
</p>

Execute this command in MongoDB Shell to set null valued twitter_username (with founded year 2004) to **temporary**
```bash
db.Companies.updateMany(
   {
      "twitter_username": "", 
      founded_year: 2004
   },
   {
      $set: { twitter_username: "temporary"}
   }
)
```
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/After%20UpdateMany.png">
</p>

### Delete
To delete a document record using the MongoDB Shell, I applied a similar approach to the **db.collection.find()** method but instead I used the [db.collection.deleteOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.deleteOne/) method. This methods will allow me to delete a document based on the related query, in this case using the email address of a company (info@mobiance.com).
```bash
 db.Companies.deleteOne({"email_address": "info@mobiance.com"})
```
Below shows the expected output of the command:
<p align="center">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Delete%20from%20MongoDB%20Shell.png">
   <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/blob/main/submission/qaisarrra/question2/files/images/Delete%20from%20MongoDB.png">
</p>

Because I deleted only one document from the database, MongoDB will return **9,499 rows** of records. When I try to find the document using the **({"email_address": "info@mobiance.com"})** query, MongoDB stops me since the document has already been removed and there are no matching query.
<br></br>


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



