
<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Yong Zhi Yan
#### Matric No.: A20EC0172
#### Dataset: City Inspections	

## Question 2 (a)
### Steps to Import JSON File into MongoDB Database Using Command Prompt (CMD)

Prerequisites: <br>
✅Download MongoDB Shell <br>
✅Download MongoDB Command Line Database Tools <br> 
✅Copy all the .exe file in the bin folder of the downloaded MongoDB Shell and MongoDB Command Line Database Tools and paste them in the bin folder of "MongoDB" folder which located under the "Program Files" folder. <br>
✅Add new environment path to MongoDB by following the steps below: <br>
    - Open "Edit the system environment variables" control panel by typing env in the Window search bar. <br>
    - Under the "Advanced" section, select "Environment Variables...". <br>
    - Under the section of user variables, select "Path" and click "Edit". <br> 
    - Click "New" and paste the filepath to bin folder of MongoDB and add a "\" after it (example: "C:\Program Files\MongoDB\Server\6.0\bin\"). <br>
    - Finally, click "OK" for each window. <br>
<br> 

1. Open the Command Prompt of system by typing "CMD" in the Windows search bar and select "Command Prompt". 
2. Access the MongoDB through CMD by giving the command <code>mongod</code>. Then wait for the system to access MongoDB, the result is expected as below.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20103533.png" alt="access mongodb via cmd">

3. Import the JSON file using the function <code>mongoimport</code> with the JSON file's filepath, database name and collection name with the format <code>mongoimport "filepath" -d "database name" -c "collection name"</code>. <br>
In this case, I have saved the JSON file inside the folder Desktop/sem 6 notes/mso/ and created a database named "AA" along with a collection named "CityInspection", the code is shown as below. <br>
<code>mongoimport "C:\Users\yong\This PC\Desktop\sem 6 notes\mso\city_inspections.json" -d AA -c CityInspection</code>
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104340.png" alt="upload json file to MongoDB">
The JSON file is successfully imported into MongoDB which can be viewed in MongoDB Compass.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104937.png" alt="json file imported">

4. Access the MongoDB Shell by giving the prompt <code>mongosh</code>.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104656.png" alt="access mongodb shell">

5. View all the available databases which stored in MongoDB via the command <code>show dbs</code>.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104711.png" alt="show all databases">

6. Since I am using the database named "AA", then I access it through the code <code>use AA</code>. 
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104829.png" alt="use database AA">

## Question 2 (b)
i. Create <br>
To insert a single document into the collection "CityInspection", use the query "db.collection.insertOne()" as shown as below.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20112357.png" alt="insertone()">
The inserted document can be viewed in MongoDB Compass.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20112337.png" alt="view inserted data">

ii. Read <br>
To find documents with the sector of "Mobile Food Vendor - 881" and result as "Closed", I use the query "db.collection.find()" to perform the searching. The results are shown as below.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20113120.png" alt="find()">
This find() operation can also be performed in the MongoDB Compass.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20113354.png" alt="view find() at mongodb compass">

iii. Update <br>
To update only one selected document, the operation "db.collection.updateOne()" is used. Here, I choose to update the zip code and street name of the business "TY Home".
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20114542.png" alt="updateone()">
The updated document can also be viewed in MongoDB Compass.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20114609.png" alt="view updated data">

To update many documents, the operation "db.collection.updateMany()" can be used. Here, I choose to update the business name to "Truck Service Inc" for all businesses which do not have a name and in the "Tow Truck Company - 124" sector. 
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20115838.png" alt="updatemany()">
The updated documents can be viewed in MongoDB Compass.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20115823.png" alt="view updatemany data">
Now, I double check whether all selected documents are updated or not. From here, I can tell that they are all updated, since there is no business under the "Tow Truck Company - 124" sector which does not has a name. 
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20115905.png" alt="double check updatemany data">

iv. Delete <br>
To perform delete operation to one specific document, I use the query "db.collection.deleteOne()". Here, I select the document with business name of "TY Home" to delete. 
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20120101.png" alt="deleteone()">
Now, I cannot find any document with business name "TY Home" since I had already successfully deleted it from the database. 
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20120123.png" alt="view deleted date">



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



