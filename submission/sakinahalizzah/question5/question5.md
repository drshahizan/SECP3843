<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Sakinah Al'izzah Binti Mohd Asri
#### Matric No.: A20EC0142
#### Dataset: [Analytics](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 5 (a)

Optimizing portal performance is essential when working with a large amount of JSON data that requires display on a dashboard. To achieve this, consider the following approach as a recommendation:

### 1. Data Preprocessing and Aggregation

When creating a dashboard, it is critical to thoroughly analyze the requirements and identify the essential data that needs to be visualized. To achieve this, the JSON data must be preprocessed to extract and transform the relevant information needed for the dashboard. This can be done by aggregating the data to reduce its volume and complexity. Summarizing or grouping the data appropriately can avoid unnecessary details during visualization. For example, consider the aggregation of data in an accounts dataset using MongoDB. 

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/6af727be-64f2-4b0c-81f8-77ad4c3b4dd7" />

The output of group by limit and sort the count in descending order.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/45258a38-d311-4b26-b764-c80ae48730ac" />

Add field

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/abc9be0a-501e-4489-9ef3-e802e933e7f7" />

### 2. Data Indexing

For optimal performance in retrieving and filtering JSON data, it is highly recommended to establish indexes on the commonly used query fields. This process greatly decreases the time it takes to execute queries and improves the overall efficiency of the database. MongoDB, for instance, offers the Index function in MongoDB Compass, which is a user-friendly way to create indexes. By utilizing this feature, you can easily and conveniently create indexes that will enhance the performance of your MongoDB database.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/8d44b737-1785-4b79-86cf-8cf862b19e7b" />

## Question 5 (b)

I created the dashboard visualization using MongoDB Atlas. The graph was generated from an analytics dataset and provides useful insights about the data.

### Dashboard

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/961ee63b-46db-4919-bf33-a92b5a062843" />

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/09a064df-5032-4f83-9ec6-ff1cc8b40369" />

Graph Explanation

1. A visual representation of the distribution of accounts based on different products is shown through a pie chart. The count of accounts for each product category such as CurrencyService, Commodity, and InvestmentStock is displayed accordingly.

2. A histogram that exhibits the age distribution of our esteemed customers. This graphical representation is highly beneficial in providing insight into the demographic composition of our customer base. By analyzing this data, we can make informed decisions about our marketing strategies and tailor our products and services to better serve our valued customers.

3. A heatmap is a graphical representation that displays the number of limit products. It is a useful tool that allows users to quickly and easily analyze data and identify patterns or trends in the distribution of limit products. By providing a clear visual representation of the data, a heatmap can help users make informed decisions and take action based on the insights gained from the analysis.

4. A bar graph that displays the total number of transactions according to a specific code. This code serves to indicate whether the customer is making a purchase or selling a product or service. The graph provides a clear and concise overview of the transactional activity, allowing for easy analysis and interpretation of the data.

View the interactive graph:

https://charts.mongodb.com/charts-project-0-xxllg/public/dashboards/649d2c45-66f3-48ea-80e8-9a860b2955ad

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



