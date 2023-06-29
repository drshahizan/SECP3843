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

<h4>Step 1 - Import data</h4>

Import Accounts and Transaction data

```
import pandas as pd

df_acc = pd.read_json('accounts.json')

df_acc = pd.DataFrame(df_acc)

# View the DataFrame as a table
df_acc
```

```
import pandas as pd

df_trans = pd.read_json('transactions.json')

df_trans = pd.DataFrame(df_trans)

# View the DataFrame as a table
df_trans
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/1.png" />
</p>

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/5.png" />
</p>

<h4>Step 2 - Remove unwanted elements for value in the column</h4>

```
df_acc['_id'] = df_acc['_id'].str['$oid']
df_acc['account_id'] = df_acc['account_id'].str['$numberInt']
df_acc['limit'] = df_acc['limit'].str['$numberInt']
df_acc
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/3.png" />
</p>

```
df_acc['products'] = df_acc['products'].astype(str).str.replace('[', '').str.replace(']', '')
df_acc
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/4.png" />
</p>

```
df_trans['_id'] = df_trans['_id'].str['$oid']
df_trans['account_id'] = df_trans['account_id'].str['$numberInt']
df_trans['transaction_count'] = df_trans['transaction_count'].str['$numberInt']
df_trans['bucket_start_date'] = df_trans['bucket_start_date'].str['$date']
df_trans['bucket_end_date'] = df_trans['bucket_end_date'].str['$date']
df_trans
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/6.png" />
</p>

```
df_trans['bucket_start_date'] = df_trans['bucket_start_date'].str['$numberLong']
df_trans['bucket_end_date'] = df_trans['bucket_end_date'].str['$numberLong']
df_trans
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/7.png" />
</p>

<h4>Step 3 - Remove unwanted column</h4>

```
columns_to_remove = ['transactions']
df_trans = df_trans.drop(columns_to_remove, axis=1)
df_trans
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/8.png" />
</p>

<h4>Step 4 - Concat both Accounts and Transactions Table</h4>

```
df= pd.concat([df_acc, df_trans])
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/9.png" />
</p>

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

This graph shows that the account limit does not restrict the user to make transaction as we can see as the account limit increases, the transaction count increases too. 

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/page1.png" />
</p>
  
- Sum of transaction.price by products

The graph below shows that the product 'investmentStock'  has the highest transaction price compared to the others. The other products have almost the same amount of transaction price.

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question5/images/page2.png" />
</p>

- Count of product by transaction code

There are two types of transaction code which are sell and buy. Based on the bar chart below, the products that are sold is slightly higher that the products that are bought which is 50.02% higher than 49.98%.

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


