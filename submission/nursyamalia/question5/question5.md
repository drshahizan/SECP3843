<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nur Syamalia Faiqah Binti Mohd Kamal
#### Matric No.: A20EC0118
#### Dataset : [Analytics Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 5 (a)
<p>One of the many ways to optimize the performance when dealing with large volumes of JSON data from the dataset, especially during dashboard visualizations is aggregation. In MongoDB, we can do aggregation which is grouping multiple documents together. We can also filter and sort documents to analyze changes.</p>

<p>In addition, there are many stages in the aggregation pipeline we can use such as $match, $group, $sort and $project. However, for this alternative assessment, I will only be using two stages which are $group and $sort.</p>

### Steps

Open MongoDb Compass on your laptop. Connect with the connection strings and open the desired database and collection. I will do demonstration for **accounts**. Then, click on the **Aggregations**.

  <img  src="./files/images/agg.png"></img>

In the first stage, I will be using $group which can group multiple documents based on the requirements. Select ‘+’ to add a new stage and choose $group. Then, write below code which I group based on account_id and total products which are the total products based in the products array.

  <img  src="./files/images/group.png"></img>

In the second stage, I will sort the data based on the decreasing total products by using $sort.

  <img  src="./files/images/sort.png"></img>

Lastly, click **Run** to establish the aggregation pipeline. This aggregation pipeline output can simplify the data, make process more faster and optimizing of the performance when dealing with large volumes of JSON data from the dataset.

  <img  src="./files/images/run.png"></img>

## Question 5 (b)
In answering this question, I will be creating a dashboard for `customer.json` using MongoDB Atlas Charts. I choose this tool because it is fast, easy to use and powerful in creating dashboard for JSON file especially for beginner. Creating a dashboard is important in helping visualizing the JSON dataset in meaningful way, interactive interaction, monitor key metrics and track the performance of your data over time.

### Prerequisite
- Create an account in MongoDB Atlas in https://www.mongodb.com/cloud/atlas/register.
- Create a project and also setup the databases and collections.

### Steps
1. Sign in into MongoDB Atlas and select **Charts**.
   
  <img  src="./files/images/chart.jpg"></img>

3. If this is your first time using MongoDB Atlas Charts, it will display below page. Click **Start**.
   
  <img  src="./files/images/start.jpg"></img>
  
- Then, it will lead to the below page. You can choose either Chart Builder or Sample Dashboard. In my case, I just choose Chart Builder as I already have data I want to use.

  <img  src="./files/images/choose.jpg"></img>

3. Select data source. I will be using `customer.json` for this question.
 
  <img  src="./files/images/data.jpg"></img>

4. Build charts and dashboard. In MongoDB Atlas Charts, it will create a few charts suggestions. You can choose or build any charts you can customized by **FIELDS** (the attributes in `customer.json`), **CHART TYPE** (any types of chart lists - bar chart, line chart, etc.) and below it for **Encode** (Choose the X and Y axis values), **Filter** (create any filtering based on conditions) and **Customize** (customize colour, rename labelling, etc.).

  <img  src="./files/images/ch1.jpg"></img>
  
  - Firstly, I will apply the first suggestion in the Charts which is Total Customer that involved in this dataset. After writting the title, click on the **Save and close**. It will directly redirect to dashboard page where I can adjust the sizes of the created charts and adjust its position.

  <img  src="./files/images/ch2.jpg"></img>

  - Create a new chart by clicking on the **Add Chart**. Then, I will create a new chart title named Sum of Account which is the customers overall total account associated.

  <img  src="./files/images/ch3.jpg"></img>

  - Create a new chart title named Range Number of Account of Total Customer and Total Address which is the customers with their address associated with certain amount of account range.

  <img  src="./files/images/ch4.jpg"></img>

  - Lastly, create a new chart title named Total Customer per Year which is the total customer have/create account in certain range of years. Then, I adjust the postion and size of the dashboard.

  <img  src="./files/images/ch5.jpg"></img>


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




