<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Myza Nazifa Binti Nazry
#### Matric No.: A20EC0219
#### Dataset: Stories

## Question 4 (a)
The machine learning that I will implement for my dataset is K-Means Clustering which is an unsupervised machine learning algorithm used to group a dataset into k clusters. For this project, I will be using Colab to do the code. The file is attached [here](https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/code/q4.ipynb).

1. Import Database
   - Install pymongo by running the code below:

     ```
       !pip install pymongo
     ```
   - Then, import the necessary libraries for data-cleaning.

      ```
       import pymongo
       import pandas as pd
       import numpy as np
      ```
   - Next, by using pymongo, connect to the MongoDB database and retrieve the data from the database.

      ```
      # Connect to MongoDB server
      client = pymongo.MongoClient("mongodb+srv://mnazifa:myza0701@cluster0.k5mjpna.mongodb.net/test")
           
      # Access the database and collection
      db = client["stories"]
      collection = db["col_stories"]
           
      # Retrieve data from the collection
      data = list(collection.find())
           
      # Convert data to a dataframe
      df = pd.DataFrame(data)
      df
      ```
   
      <div align="center"><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(1).png" />
<br>
2. Data Cleaning 

   - To identify the number of columns and rows in the dataset, run the command as follows:
     
     ```
       df.shape
      ```  

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(2).png" />

     Based on the figure above, it is shown that the dataset has 9842 rows and 20 columns overall.
   - Next, we need to identify if there are any null data in the dataset. To identify the null data, run the code below:

     ```
      df.isna().sum()
      ```  

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(3).png" />

     Based on the figure above, it is shown that the columns 'thumbnail', 'inaccurate' ,'takedowndays' and 'takedownuri' have null datas.
   - To ensure there are no null data in the dataset, run the command below:

     ```
      df["thumbnail"].fillna("NaN", inplace = True)
      df["inaccurate"].fillna("NaN", inplace = True)
      df["takedowndays"].fillna("NaN", inplace = True)
      df["takedownuri"].fillna("NaN", inplace = True)
      ```  
   - Then, run the code below to check if the code still have null data.

     ```
      df.isna().sum()
      ```  

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(4).png" />
     Based on the figure above, there are no longer null data in dataset.

3. Machine Learning (K-Means Clustering)

      ### K-Means Clustering

   - First, extract the columns we want to use. For this project, I decided to use columns 'comments' and 'diggs'.

     ```
      features = df[['comments', 'diggs']]
      features
      ```  

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(5).png" />
   - Then, import all the necessary libraries to do K-Means Clustering algorithm.

     ```
      from sklearn.cluster import KMeans
      import seaborn as sns
      import matplotlib.pyplot as plt
      %matplotlib inline
      from sklearn.metrics import silhouette_samples, silhouette_score
      from sklearn.preprocessing import StandardScaler
      ```  
   - Comments and Diggs are numerical features and it may have been measured in different units. With that, we need to make sure that the values for both features are the same scale. So, to transform the data into the same scale, we need to implement the StandardScaler class.

     ```
      scaler = StandardScaler()
      scaled_features = scaler.fit_transform(features)
      scaled_features
      ``` 

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(6).png" /> 
   - For the K-Means clustering, I want to compare between 9 different clusters. I also did not set the initialization for the centroid. Hence, I put init as random.

      ```
      k_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

      for k in k_values:
          kmeans = KMeans(n_clusters=k, init="random", random_state=42)
          kmeans.fit(scaled_features)
      ``` 
   - Then, get the cluster label and put it in the dataframe.
     
      ```
      cluster_labels = kmeans.labels_
      features['cluster_label'] = cluster_labels
      features
      ``` 

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(7).png" /> 
   - To identify the centroids coordinates for each cluster, run the following code:     

     ```
      kmeans.cluster_centers_
      ``` 

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(8).png" /> 
   - Then, plot a scatter graph to visualise the K-Means clustering for Number of Comments and Number of Diggs.     

     ```
      plt.scatter(features['comments'], features['diggs'], c=features['cluster_label'], cmap='viridis')
      plt.xlabel('Number of Comments')
      plt.ylabel('Number of Diggs')
      plt.title('K-means Clustering')
      plt.colorbar(label='Cluster')
      plt.show()
      ``` 

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(9).png" /> 
   

   ### Optimal Clusters

   Once we have done K-Means Clustering, we need to know the optimal value of k. 
   #### Elbow Method
   - For Elbow method, it is basically comparing the inertia between the clusters, k. Inertia is something that can indicate how well the data points within each cluster are grouped together.

     ```
      range_of_k = range(2,15)

      values = []
      for k in range_of_k:
          kmeans = KMeans(n_clusters=k, init="random", random_state=42)
          kmeans.fit(scaled_features)
          values.append(kmeans.inertia_)
      
      plt.plot(range_of_k, values, marker='o')
      plt.xlabel('Number of Clusters (k)')
      plt.ylabel('Inertia')
      plt.title('K-means Inertia')
      plt.show()
      ``` 

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(11).png" /> 
   #### Silhouette Method
   - Silhouette Method has the same function as Elbow method but it is more to measure of how similar a data point is from the points in its own cluster and how similar it is to data points in other clusters.
     
     ```
      range_of_k = range(2, 15)
      silhouette_scores = []
      
      for k in range_of_k:
          kmeans = KMeans(n_clusters=k, random_state=42)
          cluster_labels = kmeans.fit_predict(scaled_features)
          silhouette_avg = silhouette_score(scaled_features, cluster_labels)
          silhouette_scores.append(silhouette_avg)
      
      
      plt.plot(range_of_k, silhouette_scores, marker='o')
      plt.xlabel('Number of Clusters (k)')
      plt.ylabel('Silhouette Score')
      plt.title('Silhouette Analysis')
      plt.show()
      ``` 

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(12).png" /> 
     
   #### K-Means Clustering using Optimal Cluster.

   Based on the Silhoutte Method, 2 is the optimal k.     

   ```
      k = 2 
      kmeans = KMeans(n_clusters=k, random_state=42)
      kmeans.fit(scaled_features)
      
      
      cluster_labels = kmeans.labels_
      features['cluster_label'] = cluster_labels
      
      plt.scatter(df['comments'], features['diggs'], c=features['cluster_label'], cmap='viridis')
      plt.xlabel('Number of Comments')
      plt.ylabel('Number of Diggs')
      plt.title('K-means Clustering')
      plt.colorbar(label='Cluster')
      plt.show()
      ``` 

     <div><img src="https://github.com/drshahizan/SECP3843/blob/main/submission/myzanazifah/question4/files/images/q4(13).png" /> 


### Conclusion

- I have made the decision to do K-Means clustering based on the features 'diggs' and 'comments'. By doing this algorithm, I can group the stories into clusters based on their popularity level.
- As you can see in the first figure for K-Means clustering, it is not a very good visualization as we cannot see the separation clearly. With that, we need to do Elbow method or/and Silhoutte method to know the optimal k.
- Based on the two graphs, it can be said that Silhoutte method is better than Elbow method as Silhoutte method is more clear in indicating the optimal k. Based on the graph for Elbow method, it was either 3 or 4 as those are the ones that shows most change. To know the optimal k for Elbow method, we need to identify the point which has the most drastic change. Meanwhile, to know the optimal k for Silhoutte method, we need to choose the highest silhoutte average. With that, the optimal k based on the figure for Silhoutte method is 2.
- Lastly, I made a K-Mean clustering based on the optimal k based on the Silhoutte method which is 2. From the graph, we can see that cluster 0 is more tightly packed compared to cluster 1. This may be due to the fact that cluster 0 shares more similar characteristics compared to cluster 1.



## Question 4 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




