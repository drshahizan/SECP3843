<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Madihah binti Che Zabri
#### Matric No.: A20EC0074
#### Dataset: <a href="https://github.com/drshahizan/dataset/blob/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/07-stories/stories.json">stories.json</a>

## Question 5 (a)

In order to optimize the performance of the portal when working with a lot of JSON data on the dashboard, we can do a few approach :

1. Data Pagination: Instead of loading all the JSON data at once, load it in smaller chunks. This way, the initial loading time will be faster, and the dashboard will be more responsive. You can show a limited number of JSON items on each page and provide navigation links to access other pages.

2. Data Aggregation: Pre-calculate and store summary data from the JSON dataset. This will help speed up the rendering process on the dashboard, as you won't need to perform complex calculations each time.

3. Indexing: Create indexes on the JSON data fields that are frequently used in queries or filters. This will improve the performance of data retrieval operations.

In the context of a JSON dataset, indexing involves identifying specific fields within the JSON data that are frequently used in queries or filters. These fields could be things like names, dates, or categories that you often search or sort by.

When you create an index on a field, the database system creates a separate data structure that maps the values in that field to the corresponding records or documents in the dataset. This index is typically stored in a more efficient and optimized format than the original JSON data.

When you perform a query or filter based on an indexed field, the database can quickly refer to the index to locate the relevant records or documents, rather than scanning through the entire dataset. This significantly speeds up the data retrieval process and improves the overall performance of the queries.

To create an index, you usually need to define it at the time of creating the database table or collection. The database system will then build the index based on the specified field(s). It's important to choose the fields for indexing carefully, considering the ones that are frequently used in your queries and have a significant impact on the performance.

Hence, this will optimize the data retrieval operations and the dashboard will be more responsive when dealing with large volumes of data.

4. Make sure the data type is correct and efficient when performing queries and analysis.
   In stories.json, submit_date and promote_date was in Unix timestamp. Thus, in Mongo Shell, run the queries:
```
   use Stories

    db.story.find().forEach(function(doc) {
      var timestamp = doc.submit_date;
      var date = new Date(timestamp * 1000);
      var formattedDate = date.toLocaleDateString();
      db.story.updateOne({ _id: doc._id }, { $set: { submit_date: formattedDate } });
    });

    db.story.find().forEach(function(doc) {
      var timestamp = doc.promote_date;
      var date = new Date(timestamp * 1000);
      var formattedDate = date.toLocaleDateString();
      db.story.updateOne({ _id: doc._id }, { $set: { promote_date: formattedDate } });
    });
  ```


## Question 5 (b)
For implementing data visualization in this project, I will use MongoDB Charts from MongoDB Atlas. From there, we will create 8 charts that will be included in Stories Dashboard.

Steps :

1. Login to [MongoDB Atlas](https://account.mongodb.com/account/login?signedOut=true)
2. At the three dynamic tab, click on the `Charts` tab.
3. After that, select either Start or Add Dashboard (if you already have dashboard) button.
4. Fill in the Title of the dashboard.
5. Select the Chart Builder..
6. Select collection of the dataset which is story.
7. Finally, we can start building the charts

#### Charts and Dashboard development

For this chart, I want to know which topic have the highest number of comments by dragging `comments` to the X-axis and `topic_name` to the Y-axis.
In this chart, I want to know the number stories submitted in each date. I put the `submit_date` in the X-axis and count the `title` in Y-axis.
This pie chart will show me the number of stories in each media. This is because I want to know which media has the most uploaded stories in it.
This scatter plot will show the relationship between `diggs` and `comments`. From this chart, we can conclude that highest diggs will probably have the highest comments.
This chart shows the total comments and diggs in each month so that I can know which month has the highest visit by the user.
For the last chart, I want to know the number of diggs based on each topic so that I can know which topic has the highest popularity.

Stories Dashboard:
<p align="center">
   <img src="../question5/files/images/StoriesDashboard.png">
</p>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





