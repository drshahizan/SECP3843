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

In the customer analysis, K-means clustering is applied to group customers based on their age. The goal is to identify distinct segments or clusters of customers with similar age characteristics. Here's how K-means clustering is applied in this analysis:

- Data Preparation

>The numerical feature used for clustering is "age".
The "age" values are extracted from the DataFrame and stored in the variable X.
The feature values are standardized using the StandardScaler to ensure that all features have the same scale.


- Determining the Optimal Number of Clusters

>The optimal number of clusters is determined using the elbow method. K-means clustering is performed for different values of k (number of clusters), and the inertia and silhouette score are calculated for each clustering result.
The inertia is the sum of squared distances between each data point and its centroid in a cluster. It measures the compactness of the clusters.
The silhouette score measures the quality of the clustering, indicating how well-separated the clusters are.
The elbow curve is plotted using the inertia values for different k values. The curve shows the trade-off between the number of clusters and the compactness of the clusters. The optimal number of clusters is typically identified at the "elbow" point, where the inertia improvement starts to diminish significantly.

- K-means Clustering

>Based on the optimal number of clusters determined from the elbow curve, K-means clustering is performed using the selected k value.
The K-means algorithm is applied to the standardized data (X_scaled), and it assigns each customer to one of the clusters.
The cluster labels are stored in the variable cluster_labels.

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

4. Based on the elbow curve, select the optimal number of clusters and perform K-means clustering

```python
# Set the optimal number of clusters
k = 3

# Perform K-means clustering
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)

# Assign cluster labels to the data
cluster_labels = kmeans.labels_
```

5. Analyze the clustering results

```python
# Add the cluster labels to the DataFrame
df['cluster'] = cluster_labels

# Group the data by cluster and calculate the average age for each cluster
cluster_averages = df.groupby('cluster')['age'].mean()

# Print the cluster averages
print(cluster_averages)
```

6. This will provide the average age for each cluster. Click [here](https://github.com/drshahizan/SECP3843/blob/main/submission/AimanHafizi619/Question%204/files/source-code/AnalyticsQ4.ipynb) to see the code

































## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/aiman-hafizi-63b0a8275/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





