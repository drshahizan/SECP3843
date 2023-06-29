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

## Question 4
In this task, I implement the machine learning using the dataset, city_inspections.json through Jupyter. First, install the pymongo package to connect the MongoDB database with Jupyter using the code <code>pip install pymongo</code>.<br>
<img src="./files/images/Screenshot%202023-06-29%20130113.png" alt="install"><br>

#### 1. Import data from MongoDB
Import the dataset that stored in the database "AA", collection "city" from the MongoDB and store in a dataframe. <br>
<img src="./files/images/Screenshot%202023-06-29%20130129.png" alt="import"><br>

#### 2. Data preprocessing
View the database statistics by running the code <code>df.describe()</code><br>
<img src="./files/images/Screenshot%202023-06-29%20130143.png" alt="describe"><br>
View the dataframe information using the code <code>df.info()</code><br>
<img src="./files/images/Screenshot%202023-06-29%20130154.png" alt="info"><br>
Since I am focusing on performing a classification prediction towards the business name on its sector, hence I will process the column "business_name" and "sector".
Replace all empty row of the column "business_name" with nan value, and then remove all null rows from the column "business_name". <br>
<img src="./files/images/Screenshot%202023-06-29%20130215.png" alt="business null"><br>
Replace all empty row of the column "sector" with nan value, and then remove all null rows from the column "sector". <br>
<img src="./files/images/Screenshot%202023-06-29%20130226.png" alt="sector null"><br>
View the summary of each sector counts. <br>
<img src="./files/images/Screenshot%202023-06-29%20141951.png" alt="sector count"><br>
Since there is a lot of sector with counts less than 1000, hence I will be removing them as they would not be involved in the classification model. <br>
<img src="./files/images/Screenshot%202023-06-29%20142837.png" alt="filter df"><br>

#### 3. Classification using Decision Tree Classifier
I have applied a few classfication algorithms including the SVM model, Random Forest Classifier, Naive Bayes, and Decision Tree Classifier. All the algorithm mentioned do not give a high accuracy (60% - 70%), except that the Decision Tree Classifier shows the highest accuracy as 82.53%, hence it is accepted as the machine learning model for this dataset. <br>
<img src="./files/images/Screenshot%202023-06-29%20142035.png" alt="ml1"><br>
The model is also been tested with newly user input data, and show accurate results in prediction. <br>
<img src="./files/images/Screenshot%202023-06-29%20142043.png" alt="ml2"><br>





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




