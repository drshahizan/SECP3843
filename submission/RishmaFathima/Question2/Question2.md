<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Rishma Fathima Binti Basher
#### Matric No.: A20EC0137
#### Dataset: [Airbnb Listings Dataset](https://github.com/drshahizan/dataset/tree/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/05-airbnb)

## Question 2 (a)
1. Opened the dataset which was assigned to me in Github which was entitled ``Airbnb Listing Dataset``.

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.1.png">
2. Download the raw file and save it as ``listingAndReviews.json`` from the Github before working on it.


<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.2.png">
3. The file is opened through visual studio code to see if the data is available and ready to be used in MongoDB.


<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a90bbeb3cda83a1b6b9ba3097a2902cfe62dd494/submission/RishmaFathima/Question2/files/images/2.1.11.png">

4.  I navigated to MongoDB Compass on my device and opened it. I had to connect to deployment containing the collections I wish to import my dataset into. I left the connection string (URI) as default as ``mongodb://localhost:2017`` and connect to it.


<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.3.png">

5. After the connection is successful, I could view the MongoDB Compass User interface as below. Then, I clicked on the small ``+`` icon on database to add a database.

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.4.png">

6. Then, I created a new database with the database name as ``AA`` and Collection Name as ``Airbnb``.

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.5.png">

7. After the database is successfully created, I could see the collection and database created.

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.6.png">

8. Then, I could view the collection created with its details in MongoDB Compass.

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.7.png">

9. Then, to import the data, I clicked on the ``Import Data`` icon and it redirect to my file explorer for me to select the file which I wish to import. Then I selected the file which I downloaded from Github named ``listingAndReviews.json``
<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.8.png">

10. After the file is successfully imported, I could view a small notification at the bottom left indicating that the import is completed with 5555 documents imported.

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.9.png">

11. The output of imported document is shown below:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a45e09ab5dc208d5d0ae4d8774e37694bafbdadb/submission/RishmaFathima/Question2/files/images/2.1.10.png">
   
## Question 2 (b)


1. ``Create Query``
   </br>
 

   ```ruby 
      db.Airbnb.insertOne(
      {"listing_url":"https://www.airbnb.com/rooms/10006546",
      "name":"Rich Duplex", 
      "summary":"Super comfortable apartment", 
      "description":"located in the middle of city", 
      "neighbourhood_overview":"sea view and many beach side restaurants",
      "notes":"have a wonderful view with the foods", 
      "transit":"train and rental cars available",
      "access":"available to help guest",
      "interaction":"cot-10$", 
      "house_rules":"make home your comfort",
      "property_type":"apartment",
      "room_type":"duplex room",
      "bed_type":"double bed",
      "minimum_nights":"3",
      "maximum_nights":"40",
      "cancellation_policy":"moderate",
      "last_scraped":"2019-02-16T05:00:00.000+00:00",
      "calender_last_scraped":"2019-02-16T05:00.000+00:00",
      "first_review":"2016-01-03T05:00:00.000+00:00",
      "last_review":"2019-01-20T05:00:00.000+00:00",
      "accomodates":"7",
      "bedrooms":"3",
      "beds":"4"})
   ```
The following figure shows the code in the MongoDB shell terminal and the output from the terminal:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.3.png">

The following figure shows the output in the MongoDb Compass where a data is added when the Airbnb collection is filtered with a filter of ``{name:'Rich Duplex'}`` :

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.4.png">

2. ``Read Query 1``
    </br>


   ```ruby 
      db.Airbnb.find();
   ```

The following figure shows the code in the MongoDB shell terminal:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.5.png">

The following figure shows the output from the terminal of MongoDB shell:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.6.png">

 ``Read Query 2``
 </br>

   
   ```ruby 
      db.Airbnb.find().count();
   ```

The following figure shows the code in the MongoDB shell terminal and the output from the terminal: 

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.7.png">

 ``Read Query 3``
 </br>

   
   ```ruby 
    db.Airbnb.findOne({‘name’:’Rich Duplex’})
   ```

The following figure shows the code in the MongoDB shell terminal and the output from the terminal: 

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.8.png">

3. ``Update Query 1``
    </br>


   ```ruby 
     db.Airbnb.updateOne(
     {'name':'Rich Duplex'},
     {$set:{'name':'Rich Double Duplex'}
     })
   ```
   
The following figure shows the code in the MongoDB shell terminal and the output from the terminal:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.9.png">

The following figure shows the output in the MongoDb Compass where a data is added when the Airbnb collection is filtered with a filter of ``{name:'Rich Double Duplex'}`` :

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.10.png">

``Update Query 2``
    </br>


   ```ruby 
    db.Airbnb.findOneAndUpdate(
    {'name':'Rich Double Duplex'},
    {$set:{'beds':'5','bedrooms':'4'}},
    {returnNewDocument:true}
    )
   ```

The following figure shows the code in the MongoDB shell terminal and the output from the terminal:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.11.png">

The following figure shows the output in the MongoDb Compass where a data is added when the Airbnb collection is filtered with a filter of ``{name:'Rich Double Duplex'}`` :

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.12.png">

4. ``Delete Query``
    </br>


   ```ruby 
    db.Airbnb.deleteOne(
    {'name':'Rich Double Duplex'})
   ```
The following figure shows the code in the MongoDB shell terminal and the output from the terminal:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.13.png">

The following figure shows that there is no output in the MongoDb Compass when the Airbnb collection is filtered with a filter of ``{name:'Rich Double Duplex'}`` because the data is deleted:

<img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/447ca61d982b3267202ef5c42a6c443f23fa53f3/submission/RishmaFathima/Question2/files/images/2.2.14.png">







## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


