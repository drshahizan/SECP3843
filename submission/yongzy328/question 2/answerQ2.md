
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

Prerequisites:
✅Download MongoDB Shell
✅Download MongoDB Command Line Database Tools
✅Copy all the .exe file in the bin folder of the downloaded MongoDB Shell and MongoDB Command Line Database Tools and paste them in the bin folder of "MongoDB" folder which located under the "Program Files" folder. 
✅Add new environment path to MongoDB by following the steps below:
    - Open "Edit the system environment variables" control panel by typing env in the Window search bar.
    - Under the "Advanced" section, select "Environment Variables...".
    - Under the section of user variables, select "Path" and click "Edit".
    - Click "New" and paste the filepath to bin folder of MongoDB and add a "\" after it (example: "C:\Program Files\MongoDB\Server\6.0\bin\").
    - Finally click "OK" for 3 times for each window.


1. Open the Command Prompt of system by typing "CMD" in the Windows search bar and select "Command Prompt". 
2. Access the MongoDB through CMD by giving the command <code>mongod</code>. Then wait for the system to access MongoDB, the result is expected as below.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20103533.png" alt="access mongodb via cmd">

3. Import the JSON file using the function <code>mongoimport</code> with the JSON file's filepath, database name and collection name with the format <code>mongoimport "filepath" -d "database name" -c "collection name"</code>. 
In this case, I have saved the JSON file inside the folder Desktop/sem 6 notes/mso/ and created a database named "AA" along with a collection named "CityInspection", the code is shown as below.
<code>mongoimport "C:\Users\yong\This PC\Desktop\sem 6 notes\mso\city_inspections.json" -d AA -c CityInspection</code>
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104340.png" alt="upload json file to MongoDB">
The JSON file is successfully imported into MongoDB which can be viewed in MongoDB Compass.
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104937.png" alt="json file imported">

4. 
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104656.png" alt="access mongodb shell">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104711.png" alt="show all databases">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20104829.png" alt="use database AA">

## Question 2 (b)
<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20112357.png" alt="insertone()">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20112337.png" alt="view inserted data">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20113120.png" alt="find()">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20113354.png" alt="view find() at mongodb compass">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20114542.png" alt="updateone()">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20114609.png" alt="view updated date">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20115838.png" alt="updatemany()">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20115823.png" alt="view updatemany data">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20115905.png" alt="double check updatemany data">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20120101.png" alt="deleteone()">

<img src="https://github.com/drshahizan/SECP3843/blob/main/submission/yongzy328/question%202/files/images/Screenshot%202023-06-27%20120123.png" alt="view deleted date">



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



