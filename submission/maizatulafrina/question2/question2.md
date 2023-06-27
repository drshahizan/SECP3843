<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Maizatul Afrina Safiah Binti Saiful Azwan
#### Matric No.: A20EC0204
#### Dataset: City Inspections

## Question 2 (a)

To import JSON file to MongoDB database, several steps need to be done.

#### Step 1: Software Installation and Download

Required software to install and download:
 - MongoDB Community Server
    -  Go to https://www.mongodb.com/try/download/community and "Download".



   <img width="356" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/3eb261a3-e23d-4cc2-86f7-2ceb8d87b132"><img width="356" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/08429c72-1eaa-4929-bb0c-447dcb68b8b7">


- MongoDB Shell
    -  Go to https://www.mongodb.com/try/download/shell and "Download".

   <img width="321" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/b26193fd-2135-4aab-9dc6-3a610adcaad1">


- MongoDB Command Line Database Tools
    -  Go to https://www.mongodb.com/try/download/database-tools and "Download".

   <img width="359" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/54ab9247-ebb7-4aba-b01f-d1ba9a0e6407">

#### Step 2: Download and Prepare JSON dataset

- Download the JSON dataset by downloading the raw file

  <img width="700" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/8535e4b8-aa84-4767-83e1-4275288fb32c">

- Do data preparation **(if needed)** since the JSON dataset must be correctly formatted before import to the database.


#### Step 3: Run MongoDB Server

- Run MongoDB Community.
  
  <img width="387" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/68b61050-8d40-4f64-bdb7-18d8a8a06a13">

- Extract both MongoDB Command Line Database Tools and MongoDB Shell file and locate in `C:\Program Files\MongoDB\Server\6.0\bin`
  
  <img width="758" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/e2698aa9-deb5-4242-8d9a-7420b3cc5735">


  <img width="762" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/f2012450-b3b2-4523-9087-3bc765f24fb1">
   
 - Run `mongod` command to start MongoDB server

   <img width="586" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/3b3ece3b-5b77-4822-b1f9-cce59497f365">

#### Step 4: Access MongoDB Shell
 - Type this command `mongosh "mongodb+srv://clustersample01.timlof9.mongodb.net/" --apiVersion 1 --username maizatul`.

   <img width="582" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/5f78bd39-3e18-4ac8-b548-a43da17b07bd">
   
 - Select the target database and the collection

   <img width="586" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/43de9791-f162-445a-af12-57aace764fb9">

#### Step 5: Import Dataset
 - To import the dataset, run this command that contains uri, collection and the path of the dataset file.
   
   ```
   mongoimport --uri="mongodb+srv://maizatul:Afrina456@clustersample01.timlof9.mongodb.net/" --collection=city --file="D:\DATA ENGINEERING\STDE_AA\city_inspections.json"
   ```
   
   <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/0fdec767-7d8f-4acc-8600-b39c12d46594">

   
  - Result:

   
    <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/cd89804f-df14-4831-9948-cb27d7fe234b">

    

#### Step 6: Verify the Imported Dataset

  - To check whether the JSON dataset is successfully imported, run `db.city.find()` using MongoDB Shell.

    <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/6de91f67-4c46-4c31-bb53-3af6f8ddaac2">


## Question 2 (b)

These are the samples that demonstrate Create, Read, Update, Delete (CRUD) operations using MongoDB functions:

  - Create query
    - To insert documents into MongoDB database, use `insertOne()` function.

      <img width="949" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/093d8607-24d0-403a-9ce0-65f874a8eab8">
      
    - Use `db.city.find({ business_name:"ATLIXCO DELI GROCERY INC." })` to check whether the previous query is successfully executed or not.
      
      <img width="947" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/2498e442-c829-4f4d-8e19-bf7b3d1effc0">

      <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/c71eb80b-c594-4d5e-9e18-f8ae68188874">

  - Read query

    - Use `db.city.find({ result: "No Violation Issued" })` to read and find any query.

      <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/164f3a79-e61c-44bf-8ff3-69cace510d00">

  - Update Query

    - For update functions, there are 2 methods that can be done which are `updateOne()` and `updateMany()`.

      - f

  
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



