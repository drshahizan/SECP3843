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
<div align="center"><img src="images/optimize.PNG" height="350px" /></div>

2. In the Aggregations tab, we can construct the aggregation pipeline using various stages such as $match, $group, $project, $sort, etc. In this case, I created 2 stages and use $group and $sort operations.

3. First Stage: $group
- Use $group to group documents and perform aggregation operations.
- I group the documents based on 'result' column and calculate the count of documents in each group.

<div align="center"><img src="images/optimize2.PNG" height="350px" /></div>

4. Second Stage: $sort
- $sort stage is then used to sort the results based on the count in descending order.

<div align="center"><img src="images/optimize3.PNG" height="350px" /></div>

5. Click 'run'. This is the output
<div align="center"><img src="images/optimize4.PNG" height="350px" /></div>

**How it helps in optimize large data?**

- The code allows us to summarize the data by counting the occurrences of each distinct value in the "result" field. This provides a quick overview of the distribution of results in the dataset.
- Aggregating data using the $group stage allows the database to perform the aggregation operation on the server-side, which can be more efficient and scalable compared to fetching the entire dataset and performing the aggregation on the client-side.
  


## Question 5 (b)
<div align="center">
  <a href="https://app.powerbi.com/view?r=eyJrIjoiOWY2Y2VhYzctZTRmNC00ZDY2LThkYWYtZDI0YTRkMzAxNGEzIiwidCI6IjBlMGRiMmFkLWM0MTYtNDdjNy04OGVjLWNlYWM0ZWU3Njc2NyIsImMiOjEwfQ%3D%3D">
  <img src="images/dashboard.PNG" height="500px" />
  </a>
  [Click on the image to directly go to the dashboard]
</div>

### City Inspection Dashboard
The "City Inspection Dashboard" provides an overview of inspections carried out in different cities and sectors. It includes the following components:

#### <ins>Dashboard Cards</ins>
The dashboard features several cards that provide key metrics:

- Number of Cities: Displays the total number of cities involved in the inspections.
- Sectors Involved: Highlights the sectors that are included in the inspections.
- Inspections Carried Out: Shows the total count of inspections conducted.

#### <ins>Result of Inspection Percentage (Pie Chart)</ins>
The pie chart showcases the distribution of inspection results as a percentage. It offers insights into the outcome of the inspections.

#### <ins>Inspections by Month (Line Graph)</ins>
The line graph illustrates the number of inspections conducted over time, grouped by month. It enables the identification of inspection patterns and trends.

#### <ins>Sector Frequency (Heat Map)</ins>
The heat map represents the frequency of sectors involved in the inspections. It visually displays the sectors with higher or lower inspection frequencies.

#### <ins>Cities Involved (Map)</ins>
The map visualizes the cities that participated in the inspections. The bubble size corresponds to the frequency of inspections conducted in each city.



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




