<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURFARRAHIN BINTI CHE ALIAS
#### Matric No.: A20EC0121
#### Dataset: Mflix

## Question 2 (a)
You have been given a JSON file that contains data that must be imported into a MongoDB database. The JSON file must follows the appropriate structure for MongoDB documents. Your task is to outline the step-by-step process to add the data from the JSON file into MongoDB. Provide a detailed explanation of each step involved in the process with screenshots, including any necessary commands. Ensure that your answer covers the preparation of the JSON file, starting the MongoDB server, accessing the MongoDB shell, selecting the target database, choosing the collection, and executing the import command.

**PREREQUISITES**

**Install each of the following:**

1.Install the community server for MongoDB.

2.Setup the MongoDB Shell

3.Make sure that you have python installed

**Retrieve and Download the dataset for Mflix;**

a.users.json

b.comments.json

c.theaters.json

d.movies.json

**Connect to MongoDB server** -Open the command prompt and type mongod
![mongod](https://github.com/drshahizan/SECP3843/assets/121208097/60685a66-3f6f-4555-aadc-eb497c38fd4e)


**Import the JSON file into MongoDB**

To import the JSON File into MongoDB, use mongoimport command. 
```
mongoimport "C:\Users\Acer\Desktop\AA\theaters.json" -d Mflix -c theaters
mongoimport "C:\Users\Acer\Desktop\AA\users.json" -d Mflix -c users
mongoimport "C:\Users\Acer\Desktop\AA\comments.json" -d Mflix -c comments
mongoimport "C:\Users\Acer\Desktop\AA\movies.json" -d Mflix -c movies
```
![jsonimport](https://github.com/drshahizan/SECP3843/assets/121208097/b1919690-e88c-43dc-914b-def423d78397)

-The -d movie specifies the name of the database, which in MongoDB localhost is movie database.

-theatres is defined as the specified collection in the movie database using the -c option.

**Accessing the MongoDB Shell**

Next, inside the command type 'mongosh' to access the MongoDB Shell
![mongosh](https://github.com/drshahizan/SECP3843/assets/121208097/56a7de40-05ad-43b3-aa77-3618494c2458)


This application allows users to inspect every database and collection from MongoDB Compass.
![mongodatabase](https://github.com/drshahizan/SECP3843/assets/121208097/f96a3844-0833-4939-b504-839a855005b9)

## Question 2 (b)

1.Use the mongod command at the command prompt to launch the MongoDB server.

2.To swap the database, type use mflix in the MongoDB Compass' MongoDB Shell terminal.

![renamedb](https://github.com/drshahizan/SECP3843/assets/121208097/b75b473a-f235-43b6-9bdc-d4902925eeee)


3.Next:
- employ **db.theaters.theatres** in db.theaters using insertOne() to add new data to a JSON file in MongoDB.

- The database collection is defined by the **insertOne()** method.

- The function to add new data to MongoDB is **insertOne()**.

![create](https://github.com/drshahizan/SECP3843/assets/121208097/15c7f5a8-423b-4c6e-96dd-a70023d7ac18)


- To access the desired data's detail information from the MongoDB database, use **db.theaters.find()**.

  ![find](https://github.com/drshahizan/SECP3843/assets/121208097/b3e50c84-5c53-417f-a310-c82b2cf77280)

    
  - To change a single piece of data in MongoDB, use **db.theaters.updateOne()**.
    
    ![updateone](https://github.com/drshahizan/SECP3843/assets/121208097/3dc928eb-0313-4a0f-963c-cc2795f25c43)

    
- this is the data for id 1010 before update

   ![beforeupdate](https://github.com/drshahizan/SECP3843/assets/121208097/8500ff27-f493-49a9-af87-44c51415dd95)


    - this is the data for id 1010 after update
    
    ![afterupdate](https://github.com/drshahizan/SECP3843/assets/121208097/4b68eeaa-331f-481e-b2ca-f530123ddd23)



    - To change a many piece of data in MongoDB, use **db.theaters.updateMany()**.

 ![updatemany1](https://github.com/drshahizan/SECP3843/assets/121208097/51145969-8598-4821-a5a2-0a43976e61ba)

In the mongoDB database collection, it specifies the location.address.city = Permaisuri where the city is "Permaisuri" and edits the   information for location.address.street1 and location.address.zipcode as seen above.


Before it is updated, this

![afterupdate](https://github.com/drshahizan/SECP3843/assets/121208097/9ecba090-0c6b-461e-ab8b-d21ad367921d)


After it is updated, this

![updatemany](https://github.com/drshahizan/SECP3843/assets/121208097/13871127-ede9-4e8a-b46e-61c300156635)


- **Remove (1 inquiry)**
employ db.theaters.Delete one piece of data from MongoDB using **deleteOne()**

![Screenshot (276)](https://github.com/drshahizan/SECP3843/assets/121208097/956e01e9-10aa-4f1d-8bb0-cbed07add055)

before deletion:

![Screenshot (277)](https://github.com/drshahizan/SECP3843/assets/121208097/7c26b158-58cb-43e6-b85b-e68ab5dc30aa)

after deletion:

![Screenshot (278)](https://github.com/drshahizan/SECP3843/assets/121208097/220556b0-7f06-4ed8-a952-9e57ad1f94d9)






## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/nurfarrahin-che-alias-26688827b/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


