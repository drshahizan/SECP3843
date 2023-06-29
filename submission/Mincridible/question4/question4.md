<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: AHMAD MUHAIMIN BIN AHMAD HAMBALI

#### Matric No.: A20EC0006

#### Dataset: Companies

## Question 4 

### Random Forest algorithm for machine learning

 #### Steps

1. Install necesasry packages: `!pip install pymongo`

2. Connect with MongoDB 

 ```python
 from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://mincridible:minzpro1@min.tan7fdn.mongodb.net/')
db = client['Companies']
collection = db['CompaniesMeta']
```

3. Retrieve data and turn it into DataFrame

```python
import pandas as pd

data = list(collection.find())

# Convert the data into a DataFrame
df = pd.DataFrame(data)
```

<img src="../materials/Q4_1.png">


4. Examine the dataset's details.

```python # Display the first few records of the DataFrame
print(df.head())

# Get information about the dataset, including column names, data types, and non-null values
print(df.info())

# Compute summary statistics for numerical columns
print(df.describe())

# Check for missing values in each column
print(df.isnull().sum())

```

<img src="../materials/Q4_2.png">

<img src="../materials/Q4_3.png">

<img src="../materials/Q4_4.png">

5. Preparing the data

```python

import numpy as np

# Splitting acquisitions Data
df['price_amount'] = df['acquisition'].apply(lambda x: x['price_amount'] if pd.notnull(x) else np.nan)
df['acquired_year'] = df['acquisition'].apply(lambda x: x['acquired_year'] if pd.notnull(x) else np.nan)

# Drop the original "acquisition" column
df.drop('acquisition', axis=1, inplace=True)

# Drop columns with a high percentage of missing values
df.drop(columns=['matricNO', 'email','age','ipo','blog_feed_url','twitter_username'], inplace=True)

# Impute missing values with mean
# Impute missing values with mean
df['founded_year'].fillna(df['founded_year'].mean(), inplace=True)
df['founded_month'].fillna(df['founded_month'].mean(), inplace=True)
df['founded_day'].fillna(df['founded_day'].mean(), inplace=True)
df['deadpooled_year'].fillna(df['deadpooled_year'].mean(), inplace=True)
df['deadpooled_month'].fillna(df['deadpooled_month'].mean(), inplace=True)
df['deadpooled_day'].fillna(df['deadpooled_day'].mean(), inplace=True)
df['price_amount'].fillna(df['price_amount'].mean(), inplace=True)
df['acquired_year'].fillna(df['acquired_year'].mean(), inplace=True)

# Drop rows with missing values if they are a small portion of the dataset
df.dropna(axis=0, inplace=True)
```

### Machince learning Code:

```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

features = [
    'founded_year',
    'number_of_employees',
    'price_amount',
]

target = 'category_code'

X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

gb_model = GradientBoostingClassifier(n_estimators=100, max_depth=3, random_state=42)

gb_model.fit(X_train, y_train)

y_pred = gb_model.predict(X_test)

# Evaluate the performance of the model
print(classification_report(y_test, y_pred))
```

<img src="../materials/Q4_5.png">


#### Visualization of the result:

```python

import matplotlib.pyplot as plt
plt.figure(figsize=(16, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.show()
```

<img src="../materials/Q4_6.png">



## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
