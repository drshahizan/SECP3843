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
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




