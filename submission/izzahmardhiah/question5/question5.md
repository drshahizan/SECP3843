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

## Question 5 (a)
One of many ways to optimize the performance of our portal in dealing with large data especially when we would like to visualize dashboard is by <b>data aggregation.</b> 

Data aggregation is done on the server-side before sending it to the client for visualization. Use Django's query aggregation functions to calculate summaries, counts, averages, or other aggregated values based on our visualization requirements. This reduces the amount of data transferred and processed on the client-side.

Fortunately, using MongoDB Compass, we are able to perfom data aggregation easily! This is becuase MongoDB Compass offers a feature where we can build aggregation pipeline. Below, I will describe the step-by-step on how we can aggregate our data using a pipeline:-

1. Click on the "Aggregations" tab in MongoDB Compass.
<div align="center"><img src="files/images/optimize.PNG" height="350px" /></div>

2. In the Aggregations tab, we can construct the aggregation pipeline using various stages such as $match, $group, $project, $sort, etc. In this case, I created 2 stages and use $group and $sort operations.

3. First Stage: $group
- Use $group to group documents and perform aggregation operations.
- I group the documents based on 'result' column and calculate the count of documents in each group.

<div align="center"><img src="files/images/optimize2.PNG" height="350px" /></div>

- The code allows us to summarize the data by counting the occurrences of each distinct value in the "result" field. This provides a quick overview of the distribution of results in the dataset.
- Aggregating data using the $group stage allows the database to perform the aggregation operation on the server-side, which can be more efficient and scalable compared to fetching the entire dataset and performing the aggregation on the client-side.
  


## Question 5 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




