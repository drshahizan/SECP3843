<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NUR IRDINA ALIAH BINTI ABDUL WAHAB
#### Matric No.:A20EC0115
#### Dataset:AIRBNB

## Question 5 (a)
a.How can the performance of the portal be optimized when dealing with large volumes of JSON 
data from the dataset, especially during dashboard visualizations? Please provide an illustrative 
solution with code and screenshots. 

create connection animport necessary module
  ```
import pymongo

# Connect to MongoDB and retrieve data
client = pymongo.MongoClient("mongodb+srv://irdinaaliah2:Freekindome_00@cluster0.o4fadwf.mongodb.net/")
db = client["dashboard"]
collection = db["dashboard"]

```
create aggregation pipeline
```
# Define the aggregation pipeline
pipeline = [
    # Stage 1: Filter relevant documents
    {"$match": {"property_type": "House"}},

    # Stage 2: Group and aggregate data
    {"$group": {
        "_id": "$room_type",
        "count": {"$sum": 1},
        "average_price": {"$avg": "$price"}
    }},

    # Stage 3: Sort the data
    {"$sort": {"count": -1}},

    # Stage 4: Limit the number of results
    {"$limit": 6}
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

## Question 5 (b)
Create a dashboard utilizing a JSON dataset, and provide a comprehensive description of its 
functionalities. You may include relevant code snippets and screenshots that illustrate the 
solution implemented. 

<img src="https://github.com/drshahizan/SECP3843/blob/be9cdf7d0ce95b9430f35093fc1f6d47bf9abca9/submission/IrdinaAliah/question5/images/DASHBOARD.jpg" style="width: 700px; height: 200px;">




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





