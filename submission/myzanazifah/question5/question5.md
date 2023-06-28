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

## Question 5 (a)
For the portal, I have suggested using MongoDB database to store the JSON dataset. With that, to optimize the performance of the portal when dealing with large volumes of JSON data from MongoDB database. There are a few ways to do so which are to use indexes and aggregations.

  ### Indexes
  
  Indexes is commonly used to find documents in a collection quickly. By implementing indexes, this will enable MongoDB to find documents that match a certain query quickly even though the dataset has a large volume of datas. Not only that but indexes can help improve the performance of queries which are used to create visualizations for dashboard as using indexes will reduce the amount of data that needs to be scan and read.

  #### Steps to Create Indexes in MongoDB

  1. Go to MongoDB Compass and navigate to the database which stores the dataset. In my case, the Stories dataset.
        
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(1).png" />
  2. Next, click on the Indexes tab. Based on the figure below, it is shown that there's an existing indexes which is _id.        

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(2).png" />
  3. Then, create a new index as shown below. Choose the column you want to become an index and for the index for submit_date, I chose the type to be descending.      

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(3).png" />
  4. From the figure below, I have created four new indexes which are submit_date, promote_date which both of the indexes I have set the types as descending. Other than that is comments and diggs which I have set the types as ascending.      

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(4).png" />
  
  ### Aggregations

  Aggregations can be used to perform complex queries in large volume of datasets. For example, it can be used to group data. As for making a dashboard, it will be very helpful as it can be used to create visualizations based on complex queries. Hence, it will improve the performance of queries.

  #### Steps to Create Aggregations in MongoDB

  1. Go to the Aggregations tab. Then, click on Add Stage button to create aggregations.     

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(5).png" />
  2. For the first stage in the pipeline, I use group and run the query below.     

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(6).png" />
  3. This is the sample output data for the first stage.     

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(7).png" />
  4. Then, for the second stage, I use sort for the total diggs where I sort it in descending order.     

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(8).png" />
  5. This is the sample output data for the second stage.     

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(9).png" />
  6. Lastly, run the pipeline and this is the output after running the pipeline.     

     <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question5/images/q5(10).png" />   
     
## Question 5 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




