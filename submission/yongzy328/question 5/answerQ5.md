<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Yong Zhi Yan
#### Matric No.: A20EC0172
#### Datatset: City Inspections	

## Question 5 (a)
To optimize the dataset, I choose to remove the unwanted or unrelated columns form the dataset to make it lighter and improve efficiency of the system. I had used Jupyter to code the optimization process.

#### 1. Import dataset
The dataset which stored in MongoDB under the database "AA" and collection "city" is loaded into a Python dataframe for further processes. <br>
<img src="./files/images/Screenshot%202023-06-29%20155117.png" alt="import"><br>

#### 2. Pre-process the dataset
Since all the columns are of data type "Object", I have changed the data type of the column "date" into datetime format, so that it will be easier for further analysis work. I also noticed that the "id" of each inspection record is quite lengthy but share common alphabetical identification such as "ENFO", "CMPL", "UNIT" and etc. Thus, I decided to split the "id" by the "-" within it and keep only the meaningful alphabetical path. <br>
<img src="./files/images/Screenshot%202023-06-29%20155131.png" alt="date id"><br>

#### 3. Drop unrelated or unwanted columns
The columns "_id", "id1", "id2", "address.number", "address.zip", "address.street", "certificate_number" do not play any significant role in data analysis and visualization, thus I decided to drop all of them in order to minimize the dataset's volume. <br>
<img src="./files/images/Screenshot%202023-06-29%20155141.png" alt="drop"><br>

#### 4. Export to CSV
The dataframe is exported to CSV file for the further analysis or visualization purposes. <br>
<img src="./files/images/Screenshot%202023-06-29%20155058.png" alt="csv"><br>

## Question 5 (b)
I have utilized Microsoft Power BI to create the dashboard for city_inspection dataset. First, open Microsoft Power BI and import the JSON file which contain the cleaned data into the Power BI. I have changed the format of column "date" form text to date, and for other columns, the format are remained as text. 

The first chart I plot is a line chart which shows the number of inspections against the months. The configurations are shown as below.<br>
<img src="./files/images/Screenshot%202023-06-29%20151055.png" alt="month"><br>
The second chart I plot is a bar chart which shows the top 10 sectors with most inspections. The configurations are shown as below.<br>
<img src="./files/images/Screenshot%202023-06-29%20151105.png" alt="sector"><br>
The third chart I plot is a horizontal stacked bar chart which shows the number of inspections against the sector along with the 5 most common results applicable. The configurations are shown as below.<br>
<img src="./files/images/Screenshot%202023-06-29%20151033.png" alt="result sector"><br>
The completed dashboard is shown as below. <br>
<img src="./files/images/Screenshot%202023-06-29%20150919.png" alt="dashbord"><br>





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




