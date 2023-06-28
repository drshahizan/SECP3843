<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Afif Hazmie Arsyad Bin Agus
#### Matric No.: A20EC0176
#### Dataset: Supply Store

## Question 5 (a)
  - When dealing with large volumes of JSON data for dashboard visualizations, optimizing the performance of the portal is crucial.
  - There are many type of ways and some of them are:
    1. Data Preprocessing and Aggregation
    2. Data Indexing
    3. Caching
    4. Pagination and Lazy Loading

## Question 5 (b)
  - The tool that I used to create dashboard using the JSON dataset given is `MongoDB Charts`.
  - `MongoDB Charts` are MongoDB tool that help user to create or produce visualizations such as dashboard or single chart based user data stored in MongoDB.
    
#### To utilize JSON dataset using MongoDB, we have to insert/import the data into MongoDB
- Import json dataset file into mongoDB with Mongo Shell.
- In the terminal with Mongo Shell active, type in the command
  - `mongoimport --uri mongodb+srv://afifhazmiearsyad:abc123456789@noctua.bw9bvzx.mongodb.net/ --db SupplyStore --collection Sales --file "C:\Users\User\Downloads\sales.json"`
  - `--db` = database name
  - `--collection` = database collection name
  - `--file` = file path to the JSON dataset file
<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question2/files/images/AA27.jpg" width="700">
</p>

#### Create Dashboard
- Open [MongoDB Atlas](https://www.mongodb.com/atlas/database) and log in into account.
- In the top navigation bar, there is a button link named charts, click on it to access Mongo Charts
<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/mongochart.jpg" width="300">
</p>

- After clicking on the charts, a collections of created dashboard will appear on the page. In this picture I already created a dashboard named SupplyStore for this project.
  
<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/createdashboard.jpg" width="800">
</p>

---

#### The Creating of `Dashboard` Using MongoDB charts
- Click on `add chart` to add new chart into the dashboard
  
##### Create Bar Chart
- Drag the column `age` and choose aggregate count to `x - axis`.
- Drag the column `couponUsed` and choose short by value into `y - axis`
- Column `gender` to `series` as image below:
  
<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/Coupons.jpg" width="200">
</p>

- Filter:

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/filter1.jpg" width="200">
</p>

- This will create a `bar chart` according to the data input.

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/vbarchart.jpg" width="600">
</p>

##### Create Bar Chart
- Drag the columns into `x - axis` and `y - axis` and Filters.

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/heatmap.jpg" width="200">
</p>

- Filter:

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/filter2.jpg" width="200">
</p>

- This will create a `Heatmap` according to the data input.

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/vheatmap.jpg" width="600">
</p>

##### Create Donut chart
- Drag the columns into `x - axis` and `y - axis` and Filters.

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/donut.jpg" width="200">
</p>

- Filter:

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/filter3.jpg" width="200">
</p>

- This will create a `Donut Chart` according to the data input.

<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/vdonut.jpg" width="400">
</p>

##### Create the other two charts chart to complete the dashboard.
 - `group column`
 - `colored column` 


<p align="center">
  <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question5/files/images/vdashboard.jpg" width="900">
</p>

> First chart `Bar Chart`.
> Coupon used by customer according to their age
> it is safe to say that most of the customer in this dataset does not used coupons when buying items

> Second chart `Headtmap`.
> Customer Age and their Satisfaction
> The heatmap shows that custoer within the age group 40 - 50 are very satisfied with thier purchase.

> Third chart `Donut Chart`.
> Percentage Customer Based on Locations.
> The highest Customer count is in `Denver` while the lowest customer count is from store in `San Diego`

> Forth chart `Group Column Chart`.
> Relation Between Store Location & Customer Satisfaction
> Overall, we can see that Satisfaction count is increasing with the satisfaction level except for location `Denver` which the satisfaction 1 is more than satisfaction 2

> Fifth chart `Coloured Column Chart`.
> Total Items Bought by Tags and Customer Age
> Based on the graph, the most bought item are `office` items while the lowest possible record items bought would be `electronic` item.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




