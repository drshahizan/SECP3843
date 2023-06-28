<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: AHMAD MUHAIMIN BIN AHMAD HAMABLI

#### Matric No.: A20EC0006

#### Dataset: Companies

## Question 5 (a)

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Question 5 (b)

### Building Chart Process

1. Login our MongoDB account and create new cluster inside the MongoDB Atlas.

2. Then connect the MongoDB atlas via MongoDB Compass

3. Create New Database and Collection and Upload the `companies.json` file inside the newly created collection.

<img src="../materials/Q5b_1.png">

4. Then, go to MongoDB Atlas go to `Charts` option, select our intended dataset and start creating our dashboard

<img src="../materials/Q5b_2.png">
<img src="../materials/Q5b_3.png">
 
### Category Distribution Explanation

<img src="../materials/Q5b_4.png">

I use the `company_code` variable as our Y-axis in this chart since it represents a specific type of sector. While preparing the chart, we also filter the `null and empty string` value. To count each sector in the 'company_code' attributes, we use `COUNT BY VALUE`.

### Top 15 Companies with Highest Number of Employees

<img src="../materials/Q5b_5.png">

In this Chart, I am using two fields from the json file. For X Axis is `name` attribute that represent name for each company in the json file and for Y Axis is `number_of_employees` attribute. We limit the X Axis by toggling `Limit Results` and set the counter to 15. For Y Axis I use `SUM` in the aggregate option to sum up the number of employees for each companies.

### Founded Year vs. Deadpooled Year

<img src="../materials/Q5b_6.png">

In this Heatmap, I am linking the two fields which are `founded_year` and `deadpooled_year`. For X Axis I use `deadpooled_year` while for Y Axis I use `founded_year` and the intensity is `id` set it to count. I use 20 Years interval for `each deadpooled_year` and `founded_year`.

### 



## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
