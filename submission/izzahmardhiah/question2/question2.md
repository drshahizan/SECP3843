<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nur Izzah Mardhiah binti Rashidi
#### Matric No.: A20EC0116
#### Dataset: [City Inspections Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/08-city_inspections)

## Question 2 (a)
### Step-by-step process to add the data from the JSON file into MongoDB:
1. Download the JSON Dataset. Access the GitHub repository where the JSON dataset is hosted.
<div align="center"><img src="files/images/github.PNG" height="350px" /></div>
<div align="center"><img src="files/images/github2.PNG" height="350px" /></div>
Locate and download the JSON file containing the City Inspections data to our local machine.
Open the JSON file using any code editor. For me, I prefer Visual Studio Code. 
<div align="center"><img src="files/images/dataset.PNG" height="350px" /></div>

2. Start MongoDB Server. Ensure that MongoDB is installed on our machine. If you do not have it installed, you can download it [here](https://www.mongodb.com/try/download/community)
<div align="center"><img src="files/images/mongodb.PNG" height="350px" /></div>
After finished configure the setup, you can proceed to install.
<div align="center"><img src="files/images/mongodb2.PNG" height="350px" /></div>

3. Launch MongoDB Compass. Connect to the localhost. If there is no problem with the MongoDB Server previously, we will not have any problem to connect with localhost.
<div align="center"><img src="files/images/mongodb3.PNG" height="350px" /></div>

4. Create a database. I specify my database name to be "city_inspection". For collection, I named it "col_city_inspection".
<div align="center"><img src="files/images/mongodb4.PNG" height="350px" /></div>

The interface of newly empty database will be like this.
<div align="center"><img src="files/images/mongodb5.PNG" height="350px" /></div>

5. Import the JSON File. Within the collection view, locate the "Import Data" or "Import JSON" option. Select the JSON file we downloaded containing the City Inspections data.
<div align="center"><img src="files/images/mongodb6.PNG" height="350px" /></div>

6. Verify the Import. Once the import process completes, MongoDB Compass will provide a summary of the imported documents. Watch for the amount of documents imported. It should be the same as number of rows when we looked at the Visual Studio Code previously. We can change the view but I prefer to observe the dataset in tabular form. 
<div align="center"><img src="files/images/mongodb7.PNG" height="350px" /></div>

7. View the summary
We can observe the overview or summary of the dataset in Schema tab by simply importing schema.
<div align="center"><img src="files/images/summary.PNG" height="350px" /></div>



## Question 2 (b)
In MongoDB Compass, users are able to CRUD through GUI or Mongosh (MongoDB Shell). I prefer to use Mongosh terminal to execute the queries.


1. Create

I created a new document where the details are shown below in the query. I implemented the insertOne() method. "WowMurah Grocery Store" is a new business name.
Query:
<div align="center"><img src="files/images/create.PNG" height="350px" /></div>
Result:
To view the result, I use find() method by the business_name. "WowMurah Grocery Store" business name is just created, hence we can expect the result to be found and only one. 
<div align="center"><img src="files/images/create2.PNG" height="350px" /></div>


2. Read
I am curious and want to find some data that the result column is set to "Pass". Hence, I once again use the find() method. MongoDB list out several document results from the query.
Query:
<div align="center"><img src="files/images/read.PNG" height="350px" /></div>


3. Update
   
i. I want to change the result of document with id equals to "10021-2015-ENFO" to "Out of Business". First, I extract the data by its id using find() method, then I use the updateOne() to change a part of the document.
Query:
<div align="center"><img src="files/images/update.PNG" height="350px" /></div>
Result:
As can be seen in the result, the result attributes has updated to "Out of Business", from "No Violations Issued".
<div align="center"><img src="files/images/update2.PNG" height="350px" /></div>


ii. For the second update operation, I am curious about the Sector attributes. Hence, I started to look at the unique values of the attributes. 
<div align="center"><img src="files/images/update3.PNG" height="350px" /></div>
As you can see in the result of the query, there are two values that quite similar which are "Dealer In Products For The Disabled - 119" and "Dealer in Products for the Disabled - 119". Since they are different just from the capitalization of some letters, I assumed that this is a dirty data issue where they gives the same meaning but formatting error. Hence, I can update one of it to make them as one unique value.



Before that, I firstly count the amount of documents for both values. Clearly it is a formatting error since the second one has only one value. Therefore, after I have updated the one value to be formatted just like the other one, they are now considered as one unique value and the new count is 270.
<div align="center"><img src="files/images/update4.PNG" height="350px" /></div>

4. Delete
For delete, I want to delete by the document's id "10423-2015-CMPL" since it will be easier to see the result. I firstly looked for the existence of the id. Then, I delete the specific document using deleteOne() method. Then, to make sure that it is deleted, I searched for the document again and MongoDB did not return anything which indicates that the document is no longer exists.
<div align="center"><img src="files/images/delete.PNG" height="350px" /></div>





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



