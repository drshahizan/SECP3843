<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Jia Xian
#### Matric No.: A20EC0200
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales" >Supply Store Dataset</a>

## Question 5 (a)
  When dealing with large volumes of JSON data for dashboard visualizations, the performance of the portal can be adversely affected due to the time-consuming process of fetching and processing the data from the dataset.

### Solution : Caching
  Implement caching mechanisms to store pre-rendered visualizations or intermediate data results. This way, subsequent requests for the same data can be served from the cache, reducing processing time and improving overall performance.The objective is to optimize the performance by implementing a caching mechanism that stores the fetched data in memory, reducing the need for repetitive database queries and improving the response time for subsequent requests.

  #### Step 1: Implement Caching
    Use the Django caching framework to store and retrieve data from cache. The caching framework provides various cache backends such as in-memory cache, file-based cache, or database cache. In this example, we will use the in-memory cache backend.
   <img  src="./files/images/code1.JPG"></img>

  #### Step 2: Retrieve Data from Cache or Database
    Implement a function to retrieve data from cache. First, check if the data is available in the cache. If so, return the cached data. If not, retrieve the data from the database and store it in the cache for future use.<br>
  <img  src="./files/images/code2.JPG"></img>

  #### Step 3: Retrieve and Render Data in Dashboard
  In the view function for the dashboard, call the function to retrieve data from cache or database. Pass the retrieved data, along with other relevant information such as the total sales to the template for rendering.
   <img  src="./files/images/code3.JPG"></img>

### Screenshot:
  - Screenshot 1: Dashboard with data fetched from the database. <br>
   <img  src="./files/images/data1.JPG"></img>
   
  - Screenshot 2: Dashboard with data fetched from cache. <br>
    <img  src="./files/images/data2.JPG"></img>

### Conclusion
  By implementing a caching mechanism, the performance of the portal can be significantly improved when dealing with large volumes of JSON data during dashboard visualizations. Caching reduces the need for repetitive database queries, resulting in faster response times and an overall optimized user experience.





## Question 5 (b)
The dashboard is designed to provide comprehensive analysis and visualization of a JSON dataset. It offers various functionalities to explore and understand the data.

### Sales Analysis
 <img  src="./files/images/dashboard1.JPG"></img>
  The sales analysis section provides insights into customer demographics, sales channels, and satisfaction levels. It includes the following features:

  <b>-Gender Distribution</b>: A bar chart displaying the distribution of customers based on gender.<br>
  <img  src="./files/images/graph1.JPG"></img>
  
  <b>-Age Distribution</b>: A bar chart representing the distribution of customers across different age groups.<br>
  <img  src="./files/images/graph2.JPG"></img>
  
   <b>-Satisfaction Distribution</b>: A bar chart displaying the distribution of the customer's satisfaction leven (1-5)<br>
  <img  src="./files/images/graph3.JPG"></img>
  
  <b>-Satisfaction Level</b>: Average, minimum, and maximum satisfaction levels of customers.<br>
  <img  src="./files/images/graph5.JPG"></img>
  
  <b>-Sales Channel Distribution</b>: A bar chart showcasing the distribution of sales channels used by customers.<br>
  <img  src="./files/images/graph4.JPG"></img>

### Steps:
  #### 1. Data Loading
  The dashboard loads the JSON dataset using the MongoDB database. It retrieves the required data for analysis and processing.<br>
    <img  src="./files/images/load.JPG"></img>
    
  #### 2. Data Preprocessing
  The loaded data is processed to generate statistics and distributions for customer demographics, sales channels, and satisfaction levels. The processed data is then visualized using charts and displayed on the dashboard.<br>
     <img  src="./files/images/process.JPG"></img>

  #### 3. Visualization
  The dashboard utilizes various charts and graphs to present the analyzed data in a visually appealing manner<br>
      <img  src="./files/images/plot.JPG"></img><br>
      <img  src="./files/images/html.JPG"></img>

### Conclusion
  The dashboard provides an interactive and comprehensive analysis of the JSON dataset. It enables users to explore customer demographics, sales channels, and satisfaction levels through visualizations and statistics

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




