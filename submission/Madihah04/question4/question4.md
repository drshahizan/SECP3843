<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Madihah binti Che Zabri
#### Matric No.: A20EC0074
#### Dataset: <a href="https://github.com/drshahizan/dataset/blob/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/07-stories/stories.json">stories.json</a>

## Question 4 (a)
The machine learning that I will implement for my dataset is K-Means Clustering which is an unsupervised machine learning algorithm used to group a dataset into k clusters. For this project, I will be using Colab to do the code. The file is attached [here](https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/code/q4.ipynb).

#### Import Dataset

1. Open Google Colab and create a new notebook.
2. Install the pymongo.
   ```python
      !pip install pymongo
   ```
3. Import the necessary libraries.
   ```python
      # Import libraries
      import pandas as pd
      import numpy as np
      import seaborn as sns
      import matplotlib.pyplot as plt
      from pymongo import MongoClient
      from sklearn.cluster import KMeans
      from sklearn.preprocessing import StandardScaler
      from sklearn.metrics import silhouette_score, silhouette_samples
      import matplotlib.pyplot as plt  
      %matplotlib inline
   ```
4. Set up a connection to MongoDB database and retrieve the data.
   ```python
      # Set up MongoDB connection
      client = MongoClient('mongodb+srv://madihahzabri:admin@cluster0.xgsbper.mongodb.net/')
      # Access the database and collection
      db = client['Stories']
      collection = db['story']
      
      # Retrieve data from collection
      data = list(collection.find())

       # Convert data to a dataframe
       df = pd.DataFrame(data)
       df    
   ```

#### Data Preparation & Cleaning 

```
df.head()
```
```
df.info()
```
```
df.isna().sum()
```
Remove column that contain na value     

```
df["description"].fillna("NaN", inplace=True)
df["user.fullname"].fillna("NaN", inplace=True)
df["thumbnail.originalheight"].fillna("NaN", inplace=True)
df["thumbnail.originalwidth"].fillna("NaN", inplace=True)
df["thumbnail.src"].fillna("NaN", inplace=True)
df["thumbnail.height"].fillna("NaN", inplace=True)
df["thumbnail.width"].fillna("NaN", inplace=True)
df["thumbnail.contentType"].fillna("NaN", inplace=True)
```

#### Output:


#### K-Means Clustering

For this project, I decided to use columns "comments" and "diggs" as these columns represent the number of comments and diggs (votes) received by each story. Both columns are numeric and can be used for clustering. By using both features, we can group similar stories based on the engagement they received in terms of comments and diggs. As a result, it can help us to identify popular or controversial stories versus less popular ones.

```
 data = df[['comments', 'diggs']]
 data
```
```
# Perform feature scaling
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Perform k-means clustering
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(data_scaled)

# Get the cluster labels
labels = kmeans.labels_

# Add the cluster labels to the DataFrame
df['cluster'] = labels
```
```
# Visualize the clusters
plt.scatter(data['comments'], data['diggs'], c=labels)
plt.xlabel('Number of Comments')
plt.ylabel('Number of Diggs')
plt.title('K-means Clustering - Comments vs Diggs')
plt.show()
```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





