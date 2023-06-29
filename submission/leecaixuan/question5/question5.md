<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Cai Xuan
#### Matric No.: A20EC0062
#### Dataset: Analytics Dataset

## Question 5 (a)

## Question 5 (b)

## Creating dashboard using Power BI

<h4>Step 1 - Import data</h4>

Import all the Analytics JSON files into Power BI.
  
<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/getdata.png" />
</p>

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/choose%20import.png" />
</p>

Result:

- Accounts Table

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/transaction%20acc.png" />
</p>

- Transactions Table

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/transaction%20table.png" />
</p>

<h4>Step 2 - Merge table</h4>

Merge the accounts and transactions table based on the same account_id. Select inner join for merging both tables.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/merge.png" />
</p>

Choose the columns you want to show in the merged tables.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/choose%20column.png" />
</p>

<h4>Step 3 - Remove errors and null value</h4>

To remove null values of each column, select 'remove errors', the null value will be removed.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/remove%20errors.png" />
</p>

Rename the column of the table.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/rename%20column.png" />
</p>

<h4>Step 4 - Create graphs</h4>

- Count of limit by transaction count

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/page1.png" />
</p>
  
- Sum of transaction.price by products

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/page2.png" />
</p>

- Count of product by transaction code

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/page3.png" />
</p>

- Sum of transaction amount and total by products

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/page4.png" />
</p>

<h4>Step 5 - Dashboard</h4>

Drag all the graphs created before in the canvas in Power BI. Add slicer to filter the graph results by products.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/addedslicer.png" />
</p>

Dashboard result:

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/dashboard.png" />
</p>

When the products is chosen from the slicer, all the graphs will interact and display the result based on the products.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/filter%20by%20products.png" />
</p>



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


