<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Hong Pei Geok
#### Matric No.: A20EC0044
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets" >Tweets</a>

## Question 5 (a)
There are several techniques that can be implemented to optimize the performance of the portal when dealing with large volumes of JSON data during dashboard visualizations. I will discuss about data preprocessing and data aggregation.

### Data Preprocessing

Data preprocessing needs to be performed for large amounts of JSON data in order to ensure that the data is in the most efficient and usable state for visualization. It may involve data cleaning, feature selection and data transformation.

#### Step 1: Load the JSON data
The JSON data is loaded for further analysis and preprocess. 
```
import json
import pandas as pd


with open('modified_tweets.json', encoding='utf-8') as file:
    data = json.load(file)
    
print(data[0])
```
Output: 

<img  src="./files/images/load.png"></img>


#### Step 2: Analyze the structure and content
Then, understand the JSON data structure to identify fields that are relevant for analysis and visualization.
```
df = pd.DataFrame(data)
df.info()
```
Output: 

<img  src="./files/images/info.png"></img>


#### Step 3: Select the feature
In my case, assume we will only use some columns like text, user, entities and source. The other fields will be removed. 
```
selected_columns = ['text', 'source', 'entities', 'user']
filtered_data = [{column: record[column] for column in selected_columns} for record in data]
```

Output:

<img  src="./files/images/drop.png"></img>

#### Step 4: Clean the data
Data cleaning is an important step in data processing. It may involve handling missing values, removing duplicate records and fixing inconsistency. In the code below, I am checking if the record contains null value.
```
df.isna().sum()
```
Output:

<img  src="./files/images/null.png"></img>
> It can be noted that the memory usage reduces from 3.1+ MB to 776.1+ KB.

**Why does data preprocessing help in optimizing large data?**
- Since large datasets often contain missing values, inconsistent formatting and duplicate records, data preprocessing can help to enhance the accuracy and reliability of the data. 
- It is normal that large datasets contain a vast number of features or variables which may be relevant to the analysis task and dashboard visualization. Feature selection can help to reduce the dimensionality of the dataset and improve performance. 


### Data Aggregation

We can use techniques like grouping and aggregation functions(sum, count and average) to optimize the performance when dealing with large datasets. 

#### Step 1: Open the MongoDB shell
We can access the MongoDB Shell by using MongoDB Compass or run the following command in command prompt to connect with MongoDB. I will using the MongoDB Shell through MongoDB Compass in this example.

Command Prompt:
<img  src="./files/images/shell.png"></img>

MongoDB Compass:
<img  src="./files/images/mongosh.png"></img>

#### Step 2: Switch to the database
Switch to the database where the collection contains the JSON data to be analyzed. 
```
use test
```
Output:

<img  src="./files/images/db.png"></img>

#### Step 3: Define the aggregation pipeline

Define the aggregation pipeline code. In the below example, there will be four stages.

`First Stage`: The first stage is $group and it is used to group the documents based on the user.screen_name field and calculate the sum of favorite_count for each group. 

`Second Stage`: The second stage is $sort and it is used to sort the documents based on the total_favorites field in descending order.

`Third Stage`: The third stage is $limit which limits the output to only the top 3 users with the highest total favorites.

`Four Stage`: The fourth stage is $project that will reshape the output document by excluding the _id field and including the user_screen_name and total_favorites fields.

```
var pipeline = [
  {
    $group: {
      _id: "$user.screen_name",
      total_favorites: { $sum: "$user.favourites_count" }
    }
  },
  {
    $sort: { total_favorites: -1 }
  },
  {
    $limit: 3
  },
  {
    $project: {
      _id: 0,
      user_screen_name: "$_id",
      total_favorites: 1
    }
  }
];
```

#### Step 4: Execute the aggregation pipeline

The following command will execute the aggregation pipeline to the collection with name tweets.
```
db.tweets.aggregate(pipeline);
```
Output:

<img  src="./files/images/pipeline.png"></img>

**Why does data aggregation help in optimizing large data?**
- Data Aggregation enables us to perform calculations, and analyses on a smaller set of summarized data. So, it results in faster processing times and improved performance when dealing with large datasets.
- Data Aggregation will help in reducing data volume by summarizing multiple records into a single representation. This condensed form reduces the overall data size since large datasets are difficult to process and analyze.


## Question 5 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




