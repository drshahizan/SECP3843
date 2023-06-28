<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Muhammad Dinie Hazim Bin Azali
#### Matric No.: A20EC0084
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 4
For the given case study, I will be using K-Means Clustering Model as a machine learning algorithms. I choose it because it is an unsupervised learning algorithm used for clustering or grouping data points based on their similarities. In my case, I can use the 'diggs' and 'comments' variables as features to cluster the stories based on the number of diggs and comments they received.

`Colab`: [Machine_Learning.ipynb]()

#### Install pymongo

1.1. Install the pymongo library into your colab.
   ```python
      !pip install pymongo
   ```

#### Set up the environment

1. Open Google Colab and create a new notebook.
2. Import the necessary libraries.
   ```python
      import pandas as pd
      import numpy as np
      from sklearn.cluster import KMeans
      from sklearn.preprocessing import StandardScaler
      from sklearn.metrics import silhouette_score
      import matplotlib.pyplot as plt
      from pymongo import MongoClient
   ```

#### Connect to MongoDB and retrieve data

1. Set up a connection to MongoDB database and retrieve the data.
   ```python
      # Set up MongoDB connection
      client = MongoClient('mongodb://your_mongodb_connection_string')
      db = client['your_database_name']
      collection = db['your_collection_name']
      
      # Retrieve data from MongoDB
      data = list(collection.find())
   ```

#### Prepare the data

1. Convert the MongoDB data into a pandas DataFrame.
   ```python
      df = pd.DataFrame(data)
      df
   ```

#### Cleaning the data

1. Identify if there are any null data in the dataset.
   ```python
      df.isna().sum()
   ```

2. If any, fill the null data with "NaN".
   ```python
      df["thumbnail"].fillna("NaN", inplace = True)
      df["inaccurate"].fillna("NaN", inplace = True)
      df["takedowndays"].fillna("NaN", inplace = True)
      df["takedownuri"].fillna("NaN", inplace = True)
   ```

3. Check again either there are any null data or not.
   ```python
      df.isna().sum()
   ```

#### K-Means Clustering Models

1. Extract columns 'diggs' and 'comments'.
   ```python
      X = df[['diggs', 'comments']]
      X
   ```

2. Run feature scaling to the feature. This is important because many machine learning algorithms, including K-Means clustering, are sensitive to the scale of the features. When the features are on different scales, it can lead to biased results, where the algorithm gives more importance to the features with larger values.
   ```python
      scaler = StandardScaler()
      scaled_df = scaler.fit_transform(X)
      scaled_df
   ```

3. Creates a KMeans object with 3 clusters.
   ```python
      kmeans = KMeans(n_clusters=3)
   ```

5. Fits the KMeans model to the scaled data.
   ```python
      kmeans.fit(scaled_df)
   ```

7. Retrieve the cluster labels and add as a new column.
   ```python
      labels = kmeans.labels_
      X['labels'] = labels
      X
   ```

9. Retrieves the coordinates of the cluster centroids.
    ```python
      centroids = kmeans.cluster_centers_
    ```

11. Plots a scatter plot of the diggs vs comments, with each point colored according to its cluster label.
    ```python
      plt.scatter(X['diggs'], X['comments'], c=X['labels'], cmap='viridis')
      plt.xlabel('Diggs')
      plt.ylabel('Comments')
      plt.title('K-means Clustering')
      plt.colorbar(label='Cluster')
      plt.show()
    ```

#### Find the optimal cluster

1. I will use silhouette model to find the optimal cluster for this dataset.
2. Define the range of clusters values.
   ```python
      k_values = range(2, 11)
   ```
   
4. Initialize variables to store the optimal values
   ```python
      best_k = None
      best_silhouette_score = -1
   ```

6. Iterate over each k value and calculate the average silhouette score
   ```python
      for k in k_values:
       kmeans = KMeans(n_clusters=k)
       labels = kmeans.fit_predict(X)
       silhouette_avg = silhouette_score(X, labels)
       
       if silhouette_avg > best_silhouette_score:
           best_k = k
           best_silhouette_score = silhouette_avg

       print("Optimal value of k:", best_k)
   ```

7. The optimal value of k determined using the silhouette method is 7. This suggests that the data can be best divided into 7 clusters based on the 'diggs' and 'comments' features.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
