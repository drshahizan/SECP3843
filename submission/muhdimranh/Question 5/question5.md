<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: MUHAMMAD IMRAN HAKIMI BIN MOHD SHUKRI
#### Matric No.: A20EC0213
#### Dataset: Airbnb Dataset

## Question 5 (a)

To optimize the performance of the portal when dealing with large volumes of JSON data from the dataset during dashboard visualizations, I utilize MongoDB's aggregation pipeline and indexing features.
By leveraging MongoDB's aggregation framework and indexing, we can efficiently process and retrieve data from the JSON dataset, even when dealing with large volumes. This approach allows you to perform complex aggregations, filtering, sorting, and limiting operations, ensuring optimal performance during dashboard visualizations.

### 1. Import the necessary modules and connect to MongoDB database.

```
import pymongo

# Connect to MongoDB and retrieve data
client = pymongo.MongoClient("mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/")
db = client["airbnbportal"]
collection = db["ListingsAndReviews"]

```

### 2. Define an aggregation pipeline to aggregate and process the data.

```
# Define the aggregation pipeline
pipeline = [
    # Stage 1: Filter relevant documents
    {"$match": {"property_type": "Apartment"}},

    # Stage 2: Group and aggregate data
    {"$group": {
        "_id": "$room_type",
        "count": {"$sum": 1},
        "average_price": {"$avg": "$price"}
    }},

    # Stage 3: Sort the data
    {"$sort": {"count": -1}},

    # Stage 4: Limit the number of results
    {"$limit": 5}
]

# Execute the aggregation pipeline and retrieve the results
results = collection.aggregate(pipeline)

# Process the results and generate the data for visualization
x_data = []
y_data_count = []
y_data_price = []

for result in results:
    x_data.append(result["_id"])
    y_data_count.append(result["count"])
    y_data_price.append(result["average_price"])
```

![Q5](files/images/q5.10.png)


### 3. Implement indexing in the MongoDB database.

Indexing improves query performance by creating a data structure that allows for faster data retrieval.

```
# Create indexes for the dataset attributes
collection.create_index("property_type")
collection.create_index("room_type")
collection.create_index("price")

# Verify the indexes
indexes = collection.index_information()
print(indexes)
```



## Question 5 (b)


## [Dashboard - Click here to view interactive dashboard](https://muhdimranh.github.io/dashboard)

[![Q5](files/images/q5.3.png)](https://muhdimranh.github.io/dashboard)

Above is the completed dashboard, like Tableau, MongoDB allows real-time dashboard filtering. In the above picture, the filter is on the right side of the dashboard and we can customize to whatever filter we intend to use.


In order to create a visualization dashboard, I chose MongoDB Atlas charts. I began by uploading my JSON Airbnb dataset into the MongoDB database (using mongoimport as in Question 2).  

MongoDB charts provide a drag-and-drop visualization creator, just like Tableau and PowerBI. It is very easy to use and it utilizes the JSON dataset that has been uploaded into the database.

Once JSON dataset has been uploaded, we can proceed with:

### 1. Go to MongoDB website.

Open the [MongoDB website](https://account.mongodb.com/account/login?_ga=2.62663724.188383531.1687805900-413483686.1685199079).

### 2. Click on `Charts` from the project dashboard.

![Q5](files/images/q5.4.png)


### 3. Click `Add Dashbord` if it is not already created.

![Q5](files/images/q5.5.png)


### 4. Inside the dashboard, click on Add Chart to begin visualization.

![Q5](files/images/q5.6.png)


### 5. Choose your dataset.

![Q5](files/images/q5.7.png)


### 6. Begin drag-and-drop attributes fields into chart requirement field.


![Q5](files/images/q5.8.png)

---

### Charts and Dashboard Development.



![Q5](files/images/chart1.png)

Above chart shows average monthly room price for each property type. But before visualization can be made, we need to ensure the price currency is standard and does not follow that particular country's currency. This is to ensure accurate data visualization. In order to do that, we can standardize the currency to be in USD. For that, we will utilize the query field the chart designer.

As we can see, cottage properties have the highest monthly price out of all property types.

![Q5](files/images/q5.9.png)

Query:

```
[
  {
    "$addFields": {
      "converted_monthlyprice": {
        "$switch": {
          "branches": [
            {
              "case": { "$eq": [ "$address.country", "Brazil" ] },
              "then": { "$multiply": [ "$monthly_price", 0.21 ] }  // Convert BRL to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Spain" ] },
              "then": { "$multiply": [ "$monthly_price", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Canada" ] },
              "then": { "$multiply": [ "$monthly_price", 0.76 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Portugal" ] },
              "then": { "$multiply": [ "$monthly_price", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "China" ] },
              "then": { "$multiply": [ "$monthly_price", 0.14 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Turkey" ] },
              "then": { "$multiply": [ "$monthly_price", 0.039 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Hong Kong" ] },
              "then": { "$multiply": [ "$monthly_price", 0.13 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Australia" ] },
              "then": { "$multiply": [ "$monthly_price", 0.67 ] }  // Convert CAD to USD using exchange rate
            }
          ],
          "default": "$monthly_price"  // Keep the original price for other countries
        }
      }
    }
  }
]
```

![Q5](files/images/chart7.png)


Line chart above shows the number of reviews for listings over the years. It peaked in 2018 but dropped drastically in 2019. `According to The Wall Street Journal, Airbnb reportedly lost USD322 million and went unprofitable for the first 9 months of 2019`.


![Q5](files/images/chart3.png)

The Geo Choropleth chart above describes the average room price per night accross different countries. This will give accurate representation on how different countries' Airbnb listings prices differ from each other. Similarly, the price per night must be converted to be in USD.

The chart suggests that United States Airbnb listings charge the most money per night at USD185.77 while Turkey is the cheapest at only USD14.36 per night.


<img src="files/images/usa.airbnb.png" align="left">
<img src="files/images/turkiye.airbnb.png" align="right">

From above search queries in Airbnb website, there are not as many choices for cheap rooms in the USA aside from campsites.

Query:

```
[
  {
    "$addFields": {
      "converted_price": {
        "$switch": {
          "branches": [
            {
              "case": { "$eq": [ "$address.country", "Brazil" ] },
              "then": { "$multiply": [ "$price", 0.21 ] }  // Convert BRL to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Spain" ] },
              "then": { "$multiply": [ "$price", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Canada" ] },
              "then": { "$multiply": [ "$price", 0.76 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Portugal" ] },
              "then": { "$multiply": [ "$price", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "China" ] },
              "then": { "$multiply": [ "$price", 0.14 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Turkey" ] },
              "then": { "$multiply": [ "$price", 0.039 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Hong Kong" ] },
              "then": { "$multiply": [ "$price", 0.13 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Australia" ] },
              "then": { "$multiply": [ "$price", 0.67 ] }  // Convert CAD to USD using exchange rate
            }
          ],
          "default": "$price"  // Keep the original price for other countries
        }
      }
    }
  }
]
```

![Q5](files/images/chart4.png)

Line chart above describes price changes over the years across different countries.

![Q5](files/images/chart5.png)

Scatter plot above visualizes the relationship between room cleanliness rating and cleaning fee. The result shows that higher cleaning fee tends to have higher cleanliness rating.

Query:

```
[
  {
    "$match": {
      "review_scores.review_scores_cleanliness": { "$ne": null }
    }
  },
  {
    "$addFields": {
      "converted_cleaning_fee": {
        "$switch": {
          "branches": [
            {
              "case": { "$eq": [ "$address.country", "Brazil" ] },
              "then": { "$multiply": [ "$cleaning_fee", 0.21 ] }  // Convert BRL to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Spain" ] },
              "then": { "$multiply": [ "$cleaning_fee", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Canada" ] },
              "then": { "$multiply": [ "$cleaning_fee", 0.76 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Portugal" ] },
              "then": { "$multiply": [ "$cleaning_fee", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "China" ] },
              "then": { "$multiply": [ "$cleaning_fee", 0.14 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Turkey" ] },
              "then": { "$multiply": [ "$cleaning_fee", 0.039 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Hong Kong" ] },
              "then": { "$multiply": [ "$cleaning_fee", 0.13 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Australia" ] },
              "then": { "$multiply": [ "$cleaning_fee", 0.67 ] }  // Convert CAD to USD using exchange rate
            }
          ],
          "default": "$cleaning_fee" // Keep the original cleaning fee for other countries
        }
      },
      "converted_price": {
        "$switch": {
          "branches": [
            {
              "case": { "$eq": [ "$address.country", "Brazil" ] },
              "then": { "$multiply": [ "$price", 0.21 ] }  // Convert BRL to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Spain" ] },
              "then": { "$multiply": [ "$price", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Canada" ] },
              "then": { "$multiply": [ "$price", 0.76 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Portugal" ] },
              "then": { "$multiply": [ "$price", 1.09 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "China" ] },
              "then": { "$multiply": [ "$price", 0.14 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Turkey" ] },
              "then": { "$multiply": [ "$price", 0.039 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Hong Kong" ] },
              "then": { "$multiply": [ "$price", 0.13 ] }  // Convert CAD to USD using exchange rate
            },
            {
              "case": { "$eq": [ "$address.country", "Australia" ] },
              "then": { "$multiply": [ "$price", 0.67 ] }  // Convert CAD to USD using exchange rate
            }
          ],
          "default": "$price" // Keep the original price for other countries
        }
      }
    }
  }
]
```


![Q5](files/images/chart6.png)

Heatmap chart above shows the number of reviews given on each day of the week over the years.

![Q5](files/images/chart8.png)

Donut chart above shows the distribution of property type in listings. It suggests that apartment has the most listings.

![Q5](files/images/chart9.png)

Scatter plot above describes the relationship between review ratings and number of reviews for listings. The higher the number of reviews tends to result in higher review ratings.







## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





