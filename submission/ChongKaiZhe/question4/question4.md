<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Chong Kai Zhe
#### Matric No.: A20EC0186
#### Dataset: Analytics

## Question 4 
In this analysis, K-means clustering is applied to identify to standardized data and minimize the varience within each customer cluster.

1. Install pymongo
  ```python
  !pip install pymongo
  ```

2. Import the libraries
 ```python
import pandas as pd
import numpy as np
import pymongo
```

3. Connect to MongoDB and retrive the data
 ```python
client = pymongo.MongoClient("mongodb+srv://kzchong:zhe010429@analytics.lqxybj3.mongodb.net/")
db = client["test"]
collection = db["Customers"]
data = list(collection.find())
```
4. Convert the data into pandas
 ```python
df = pd.DataFrame(data)
```

5. Extract information form the Dataframe and process the birthdate into age
```python
# Convert birthdate to datetime
df['birthdate'] = pd.to_datetime(df['birthdate'])

# Calculate age based on current date
current_date = pd.to_datetime('today').normalize()
df['age'] = (current_date - df['birthdate']).astype('<m8[Y]')

# Extract tier and details information
df['tier'] = df['tier_and_details'].apply(lambda x: x.get('tier') if isinstance(x, dict) else np.nan)
df['benefits'] = df['tier_and_details'].apply(lambda x: x.get('benefits') if isinstance(x, dict) else [])

# Drop unnecessary columns
df.drop(['_id', 'tier_and_details'], axis=1, inplace=True)
```

6. Group the data by age group and tier, and count the occurrences

```python
age_groups = pd.cut(df['age'], bins=[0, 18, 30, 40, 50, 60, np.inf])
age_group_labels = ['<18', '18-30', '31-40', '41-50', '51-60', '60+']

grouped_data = df.groupby([age_groups, 'tier']).size().unstack().reindex(columns=['Bronze', 'Silver', 'Gold', 'Platinum'])

grouped_data.columns = [f"{tier} ({age_group})" for tier, age_group in zip(grouped_data.columns, age_group_labels)]
```

```python
print(grouped_data)
```

**Step 3: Start Performing KMeans Clustering**
1.  Import the necessary libraries:  

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
```

2. Prepare the data for clustering

```python
numerical_features = ['age']

X = df[numerical_features].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

3. Determine the optimal number of clusters using the elbow method

# Perform K-means clustering for different values of k
```python
k_values = range(2, 10)
inertias = []
silhouette_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

import matplotlib.pyplot as plt

plt.plot(k_values, inertias, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve')
plt.show()
```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




