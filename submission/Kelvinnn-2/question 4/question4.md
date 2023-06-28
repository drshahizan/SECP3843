<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kelvin Ee
#### Matric No.: A20EC0195
#### Dataset: City Inspections

## Question 4 : Implementation of Machine Learning in Django
--------------------------------------------------------------------------------------
## <b>Predicting Business Sectors using Classification : Decision Trees and Random Forests </b>

In this task, I present a comparative study on the use of machine learning of classification with decision trees and random forests for predicting business sectors. The goal is to evaluate and compare the performance of these classification algorithms in accurately predicting the sector of a business based on its name. The study utilizes a dataset consisting of business names and corresponding sectors.

### 1: Install Required Modules

```
!pip install pymongo
!pip install pandas
```

### Step 2: Retrieving Data from MongoDB

The code begins by Import necessary libraries and modules. Then, Connect to MongoDB `client = pymongo.MongoClient("mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/")` and retrieve data from database `AA` collection `city_inspectionsDataset`. Then, Convert the data into a pandas DataFrame. Next, normalize the nested attributes in the DataFrame using json_normalize. Lastly, Check the data of first five row of table.

```
import pymongo
import pandas as pd
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np

# Connect to MongoDB and retrieve data
client = pymongo.MongoClient("mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/")
db = client["AA"]
collection = db["city_inspectionsDataset"]
data = list(collection.find())

# Convert to dataframe
df = pd.DataFrame(data)
# Convert nested attributes to separate columns using json_normalize
df = json_normalize(data)
df.head()
```

### Step 3: Data Pre-Processing 
Data preprocessing is a process of preparing the raw data and making it suitable for a machine learning model. It is the first and crucial step while creating a machine learning model.
First, I check for null values in the DataFrame. Then , I learn the data by generate descriptive statistics for the DataFrame. Next, I perform value counts on the "result" column. Lastly , I identify outliers in the "result" column and filter the DataFrame by remove outlier of results.

a. Check null values

```
# Check null values
df.isnull().sum()
```

b. Check description of the data in the DataFrame
```
df.describe()
```

c. Remove outlier of results
```
result_counts = df['result'].value_counts()
print(result_counts)
result_counts = df['result'].value_counts()
outliers = result_counts[result_counts < 500].index
df = df[~df['result'].isin(outliers)]
```

### Step 4: Define the machine learning function
a. Import necessary libraries and modules:
```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
```

b. Extract the business names and sector names from the data:
```python
business_names = []
sector_names = []

for shop in data:
    business_name = shop['business_name']
    sector_name = shop['sector']
    business_names.append(business_name)
    sector_names.append(sector_name)
```

c. Create an instance of CountVectorizer and fit the vectorizer on the business names and transform them into a bag-of-words representation
```python
vectorizer = CountVectorizer()
business_features = vectorizer.fit_transform(business_names)
```

d. Create an instance of the Decision Tree classifier and train the classifier on the business features and sector labels
```python
classifier = DecisionTreeClassifier()
classifier.fit(business_features, sector_names)
```

e. Prepare the new business name for prediction and transform the new business name using the fitted vectorizer. Run the code to make predictions on the new business name.
```python
new_business_name = ['KELVVIN CONSTRUCTION BUILDING']
new_business_name_vectors = vectorizer.transform(new_business_name)
predicted_sector = classifier.predict(new_business_name_vectors)
print('Predicted Sector:', predicted_sector)
```
f. Calculate the accuracy of the model (assuming model is referring to the Decision Tree classifier):
```python
accuracy = classifier.score(business_features, sector_names)
print('Accuracy:', accuracy)
```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





