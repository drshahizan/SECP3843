<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.


## Special Topic Data Engineering (SECP3843): Alternative Assessment ©️

#### Name: MADINA SURAYA BINTI ZHARIN
#### Matric No.: A20EC0203
#### Dataset: companies.json

### Question 2 (a)
1. Download **MongoDB Command Line Database Tools** from MongoDB website. Choose ‘msi’ as its package.
<p align="center">
  <img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/861fe239-c18d-4739-b5ae-1fa1b773615c">
</p>

2. Open the downloaded installer and accept the license agreement. Continue until finish setting up.
   
3. In your MongoDB folder in program files, there should be two folders which are ‘server’ and ‘tools’. Since I already downloaded **MongoDB Server** before, this tool should be an add-on to the MongoDB folder. 
<p align="center">
  <img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/5e0abbe3-5e89-40df-9003-0e5d603ffb10">
</p>

4. Check if the folder ‘Server’ contains a **mongo.exe** file. If not, download MongoDB Shell as zip package.
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/19666183-79bb-4d9d-8361-2b1b68c0e750">
</p>

5. Unzip the folder, open the bin folder and there should be these two folders. Copy those and paste it in the ‘Server’ folder.
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/8c440801-08c2-4b43-b480-da5884087209">
</p>

6. Open command prompt for these two folders, ‘Server’ and ‘Tools’. Command for the server is to run the mongodb shell and tools to import file.
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/4902e274-e71b-4761-822a-c76017e27053">
</p>

7. Run mongodb shell using **mongosh** command in ‘Server’ command prompt. Here, I wanted to use a connection  that can connect to my MongoDB Atlas. Thus, I will specify the connection string to open the shell.

  ```
  mongosh “mongodb+srv://user1:____________a.mongodb.net/test”
  ```
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/be83fecb-9994-4981-b5e1-329ac6ba4022">
</p>

8. To add the database, run ‘use’ command, along with the database name, as follows. I named my database as ‘db_crunchbase’.

    ```
    use db_crunchbase
    ```
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/f6f549ca-e5bb-4b22-a54b-d0afa7c4540e">
</p>

9. Check if the database successfully created by running **show dbs**.
    ```
    show dbs
    ```
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/1dc9d505-5366-4b54-97bd-f9ad15af743b">
</p>

10. Next, go to another command prompt, which has ‘Tools’ as its directory to start importing the JSON file into the database. These are things needed in the command:
    - Command: mongoimport
    - URI:  connection string
    - Database name: db_crunchbase
    - Collection: companies (define name)
       File: JSON file path.

    ```
    mongoimport –uri “mongodb+srv://user1:________________.mongodb.net/test” - - db db_crunchbase - - collection companies - - file "C:\Users\dina_\Documents\companies.json"
    ```
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/296bda40-a024-4bfb-b736-c57713965e15">
</p>

11. Successful message will be shown below.
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/3e7bc6e4-70b7-49fa-8dda-293058c61210">
</p>

12. To see the JSON file data, in the shell, run **db.companies.find().pretty()** command. The **pretty()** command is used to make the JSON format more readable.

    ```
    db.companies.find().pretty()
    ```
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/5496d609-59f2-4f51-b148-999cfe73d5c8">
</p>

13. I can also check the database in my MongoDB Compass and Atlas.
<p align="center">
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/c5339acd-7018-4231-ac85-4c8b979bcedd"><br>
<img width="400" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/97c62a3d-1869-40bd-9c72-63d26e249e23">
</p>


### Question 2 (b)
1. Create
   ```
   db.companies.insertOne({
                    "email_address": "info@julieco.com",
                    "name": "Julie .co",
                    "founded_day": {
                          "$numberInt": "1"
                      },
                      "founded_month": {
                          "$numberInt": "3"
                      },
                      "founded_year": {
                          "$numberInt": "2015"
                      },
                    "number_of_employees": {
                          "$numberInt": "10"
                      },
                      "offices": [
                          {
                              "address1": "No 14 Jalan 15/2B,",
                              "address2": "Seksyen 15,",
                              "city": "Bandar Baru Bangi",
                              "country_code": "MY",
                              "description": null,
                              "latitude": null,
                              "longitude": null,
                              "state_code": null,
                              "zip_code": "43650"
                          }
                      ],
                    "overview": "<p>Julie .co provides consultation about pets.",
                    "permalink": "julie.co",
                    "phone_number": "+6012-3136850"
        })
   ```
<p align="center">
<img width="313" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/b5a693fa-ee3a-426a-9028-b09d0001337c">
</p>

2. Read
```
db.companies.find({ "founded_year": 2001}).limit(1)
```
<p align="center">
<img width="314" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/3a1e793c-6e82-4804-8ebe-e3734abac7f0">
</p>

3. Update
   -  updateOne()
   
      ```
      db.companies.updateOne({ "founded_day": 1}, {$set: {"founded_month":12}})
      ```
    <p align="center">
          <img width="485" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/1f0142aa-b401-4981-9deb-eec922f86746"><br>
    </p>
    
    ```
     db.companies.find({ "founded_day": 1}).limit(1)
     ```
     <p align="center">
     <img width="471" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/461d1d16-d050-40bf-96eb-af9d99986eb3">
     </p>

   - replaceOne()
     
      ```
      db.companies.replaceOne({ "name": "Julie .co" }, {"name":"Julie Corporation", "offices":[{"address1": "No 16 Jalan 15/2B,", "address2": "Seksyen 16"}]})
      ```
      
    <p align="center">
    <img width="474" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/794527d6-b29d-4798-99c2-5bc08a6d880a">
    </p>

      ```
      db.companies.find({"name":"Julie Corporation"})
      ```
      
      <p align="center">
      <img width="482" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/a63ac0d4-f8f0-4567-8d98-41b04dbc55a9">
      </p>


4. Delete

```
 db.companies.deleteOne({"name": "Julie Corporation"})
 ```
<p align="center">
<img width="453" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/f62bfec2-c3ea-4b60-aa75-ae6681fa910e">
</p>


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)








   
