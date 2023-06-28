<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: AHMAD AIMAN HAFIZI BIN MUHAMMAD
#### Matric No.: A20EC0177
#### Dataset: ANALYTICS DATASET

## Question 4

Based on the tables you provided in the JSON files, it seems like a structured data that involves numerical and categorical features. In this case, `Logistic Regression` may be the most suitable machine learning algorithm as it is primarily used for predicting continuous numeric values.

**Step 1: Open Google Colab**

- Open Google Colab. Create a file called `AnalyticsQ4`. Save a copy to `GitHub` using this path

- `drshahizan` > `SECP3843` > `submission` > `AimanHafizi619` > `Question 4` > `files` > `source-code`

**Step 2: Start Performing Data Cleaning**

1. Install pymongo

  ```python
  !pip install pymongo
  ```
2. Import the necessary libraries

```python
import pandas as pd
import numpy as np
import pymongo
```

3. Connect to MongoDB and retrieve the data

```python
# Connect to MongoDB and retrieve data
client = pymongo.MongoClient("mongodb+srv://admin:admin@projectcluster.7sndifd.mongodb.net/")
db = client["Analytics"]
collection = db["Customers"]
data = list(collection.find())

4. Convert the data into a pandas DataFrame

# Convert to dataframe
df = pd.DataFrame(data)
```

5. Extract the relevant information from the DataFrame and process the birthdate into age

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
# Define age groups
age_groups = pd.cut(df['age'], bins=[0, 18, 30, 40, 50, 60, np.inf])
age_group_labels = ['<18', '18-30', '31-40', '41-50', '51-60', '60+']

# Group by age group and tier, and count occurrences
grouped_data = df.groupby([age_groups, 'tier']).size().unstack().reindex(columns=['Bronze', 'Silver', 'Gold', 'Platinum'])

# Add age group labels to the columns
grouped_data.columns = [f"{tier} ({age_group})" for tier, age_group in zip(grouped_data.columns, age_group_labels)]
```

7. print(grouped_data)

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
# Select the numerical features for clustering
numerical_features = ['age']

# Extract the numerical features from the DataFrame
X = df[numerical_features].values

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

3. Determine the optimal number of clusters using the elbow method

```python
# Perform K-means clustering for different values of k
k_values = range(2, 10)
inertias = []
silhouette_scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plot the elbow curve
import matplotlib.pyplot as plt

plt.plot(k_values, inertias, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve')
plt.show()
```










































## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





