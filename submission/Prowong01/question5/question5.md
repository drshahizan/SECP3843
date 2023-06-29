<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Eddie Wong Chung Pheng
#### Matric No.: A20EC0031
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies" >Companies</a>

## Question 5 (a)
Use caching techniques to save and access pre-processed data. This reduces redundant computations and database queries, improving performance. Common caching options include Redis or Django's built-in caching framework.

Steps to implement cache when handling large volumes of JSON data from the dataset are shown below.

### Step 1:  Install all required packages
```
pip install cachetools
```

### Step 2: Import the necessary classes and functions from cachetools
```
from cachetools import cached, TTLCache
```

### Step 3: Define cache instance
```
result_by_sector_cache = TTLCache(maxsize=1, ttl=3600)  # Cache for inspections_by_sector
inspections_by_month_cache = TTLCache(maxsize=1, ttl=3600)  # Cache for inspections_by_month
```

### Step 4: Apply cache decorator to function
```
@cached(result_by_sector_cache)
def inspections_by_sector(request):
    
@cached(inspections_by_month_cache)
def inspections_by_month(request):
```

### Step 5: Verify cache to check if cached data is available
```
    cached_data = cache.get('inspections_by_sector')
    if cached_data:
        print("Using cached data")
        result_by_sector = cached_data
    else:
        print("Generating new data")
```

## Question 5 (b)
### Step 1: Login to MongoDB Atlas and Load the dataset
Go to this <a href="https://charts.mongodb.com/"> link </a> to start create dashboard and select the dataset.

<img  src="./images/data.png"></img>

### Step 2: Go to MongoDB Chart develop dashboard
Create a dashboard in MongoDB Charts and add charts using your JSON data. You can use different chart types to visualize your data, such as bar charts, line charts, maps, etc. You can also apply filters and aggregations to your data

### Dashboard
<img  src="./images/dashboard.png"></img>

### Bar Chart
This bar chart shows the employee size and funding raised amount for various companies and startups in the dataset. This allows to see the relationship and comparison of employee size and funding raised amount for different companies and startups.
<img  src="./images/1.png"></img>

### Line Chart
This line chart shows the stock symbol and IPO valuation amount over the year for various companies and startups in the dataset. This chart allows to see the trends and patterns of stock symbol and IPO valuation amount over the year for different companies and startups.
<img  src="./images/3.png"></img>

### Donut Chart
This donut chart shows the top 10 most popular category codes by company count in the dataset. A donut chart is a circular chart that shows the proportion of each category within the total. The larger the slice, the higher the company count. This chart allows to see the popularity and ranking of different category codes by company count.
<img  src="./images/2.png"></img>

### Heatmap
This heatmap shows the frequency of founded year and deadpooled year for various companies and startups in the dataset. A heatmap is a graphical representation of data where the values are encoded by colors. The darker the color, the higher the frequency. This heatmap allows to see the distribution and concentration of founded year and deadpooled year for different companies and startups. 
<img  src="./images/5.png"></img>

### Line Chart
This chart shows the category and acquisition price amount for companies and startups over the year. The columns show the total price for each category and the lines show the percentage of each category. This report helps to see the changes and differences of category and price over the year.
<img  src="./images/4.png"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




