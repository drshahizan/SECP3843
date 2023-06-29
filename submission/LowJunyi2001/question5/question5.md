<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Low Junyi
#### Matric No.: A20EC0071
#### Dataset: [Airbnb](https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb)

## Question 5 (a)
When dealing with large volumes of JSON data for dashboard visualization in a portal, there are several strategies we can employ to optimize performance. Data Preprocessing will be used in this scenario.

### Data Preprocessing:
- Filter and Aggregate: Analyze the requirements of your dashboard visualization and identify the specific data subsets or aggregations needed. Preprocess the JSON dataset to filter out irrelevant data and perform any necessary aggregations, reducing the overall dataset size.

- Data Compression: Consider compressing the JSON data to reduce its size. Techniques like gzip compression can significantly reduce network transfer time when retrieving the data from the server.

### Step 1:  Import Libraries
```python
import json
import pandas as pd
import pymongo
```

### Step 2:  Connect MongoDB
```python
# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client["AA"]
collection = db["db_airbnb"]

# Retrieve data from MongoDB
data = list(collection.find())
first_data = ""

if len(data) > 0:
    first_data = data[0]
    print(first_data)
else:
    print("No data found in the dataset.")
    
# Convert MongoDB data to JSON serializable format
json_data = json.loads(json.dumps(data, default=str))
```

### Step 3: Remove unnecessary fields
```python
# Remove fields from the first_data document
fields_to_remove = ['_id', 'listing_url', 'last_scraped', 'calendar_last_scraped', 'amenities', 'images', 'host', 'address', 'availability', 'review_scores', 'reviews']
for field in fields_to_remove:
    if field in first_data:
        del first_data[field]
```

### Step 4: Convert Decimal128 fields to float or string
```python
# Convert Decimal128 fields to float or string
decimal_fields = ['bathrooms', 'price', 'weekly_price', 'monthly_price', 'cleaning_fee', 'extra_people']
for field in decimal_fields:
    if field in first_data:
        first_data[field] = float(str(first_data[field]))
```

### Step 5: Preprocess text fields
```python
# Extract text fields
text_fields = ['name', 'summary', 'space', 'description', 'neighborhood']
text_data = {field: first_data[field] for field in text_fields if field in first_data}
```

### Step 6: Print result
```python
# Print the modified first_data document
print(first_data)

# Create a DataFrame from the modified data
df = pd.DataFrame([first_data])

# Save the DataFrame to a CSV file
df.to_csv('airbnb_data.csv', index=False)
```
Output:



![image](https://github.com/drshahizan/SECP3843/assets/120614501/7140a994-6eb2-43cb-8d11-d5c8d5087276)




## Question 5 (b)

### Dashboard
![image](https://github.com/drshahizan/SECP3843/assets/120614501/61ae1910-a60d-4ff8-a306-ee09105a03c6)


### Number of Listing by Property
![image](https://github.com/drshahizan/SECP3843/assets/120614501/17a39978-a6b7-48aa-8e31-203c7a319551)


### Number of Listing by Country
![image](https://github.com/drshahizan/SECP3843/assets/120614501/456eb1d1-a680-46ba-a3ac-02c20c15117c)


### Availability by Country
![image](https://github.com/drshahizan/SECP3843/assets/120614501/6e9a3236-3d26-47b9-8218-a879e6ac5b45)


### Availability by Property Type
![image](https://github.com/drshahizan/SECP3843/assets/120614501/b52aee07-dc11-459c-bd81-56dca3f5a1d9)


### Total Review by Town
![image](https://github.com/drshahizan/SECP3843/assets/120614501/b87b3adb-93c5-44ec-ab03-5d0ff4a0c5bc)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




