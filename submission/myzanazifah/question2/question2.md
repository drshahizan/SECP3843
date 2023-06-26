<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Myza Nazifa Binti Nazry
#### Matric No.: A20EC0219
#### Dataset: Stories

## Question 2 (a)

### Steps to Add Data from JSON File into MongoDB

1. Download the JSON file.
   - Go to Github repository which stores the dataset.
     
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/dw%20data(1).png" /></div>
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/dw%20data(2).png" /></div>
   - Next, click 'Raw' and it will display the overall dataset code. Then, download the file by clicking on Save As and save the code as JSON file.
          
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/dw%20datas(3).png" /></div>
   
2. Download and Install MongoDB
   - Go to the MongoDB official website (https://www.mongodb.com/try/download/community) and download the server.

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/dw%20mongodb.png" /></div>
   - After downloading and configuring the server, install the MongoDB server.

     
3. Connect to a MongoDB deployment
   - Open the MongoDB Compass and ensure that MongoDB is running and listening on the appropriate port. Run the code below in Command Prompt to check the listening port.
     ```python

      netstat -ano | findstr "LISTENING" | findstr "mongod"
      ```
   - Once we have confirmed it is listening to the appropriate port, we can connect to the MongoDB deployment as shown below.
     
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/q2%20mongodb(1).png" /></div>
      
   - After connecting, it should display like the picture below.
          
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/q2%20mongodb(2).png" /></div>

      
4. Create a new database.
   - For my database, I have named it as stories and the collection as col_stories. After naming both the database name and collection name, click on the create button.
     
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/q2%20mongodb(3).png" /></div>
      
   - After creating the database, it will display the newly created database as shown below:
     
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/q2%20mongodb(4).png" /></div>

      
5. Importing the JSON data
   - Click on Add Data and choose Import JSON file.
      
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/import(1).png" /></div>
      
   - Then, choose the correct JSON dataset and click on Import button.
      
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/import(2).png" /></div>
      
   - After the dataset has finished importing into MongoDB, check and verify the dataset. Verify if it is the correct dataset and if all the data has been successfully imported in the MongoDB database.
      
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question2/files/images/import(3).png" /></div>

      
## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



