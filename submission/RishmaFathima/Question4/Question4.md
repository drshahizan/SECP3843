<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Rishma Fathima Binti Basher
#### Matric No.: A20EC0137
#### Dataset: [Airbnb Listings Dataset](https://github.com/drshahizan/dataset/tree/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/05-airbnb)

## Question 4 (a)
  1. Data packages and import library
      ```ruby
      !pip install pymongo

      import pandas as pd
      import numpy as np
      import pymongo
      ```
     
  3. Get data from MongoDB
     ```ruby
      client = pymongo.MongoClient("mongodb+srv://rf_user:rishma3112@newcluster.vekvrpq.mongodb.net/test")
      db = client["AA_STDE"]
      dataCollection = db["Question4"]
      data = list(dataCollection.find())
      ```

     
  5. Preprocessing of data by dropping irrelevant columns and handle missing values
     ```ruby
      df = pd.DataFrame(data)

      ```
     ```ruby
     df.head(10)

      ```
     ```ruby

     columns_to_drop = ['images', 'host', 'address']
     df = df.drop(columns_to_drop, axis=1)

      ```
     ```ruby

     df = df.fillna('') 
      ```

  7. TF-IDF feature extraction from scikit-learn by using ``TfidfVectorizer``.
      ```ruby

      from sklearn.feature_extraction.text import TfidfVectorizer

      # Combine text-based attributes into a single attribute
      text_attributes = ['name', 'summary', 'space', 'description', 'neighborhood_overview', 'notes', 'transit', 'access']
      df['combined_text'] = df[text_attributes].apply(lambda x: ' '.join(x), axis=1)
      
      # Perform TF-IDF feature extraction
      vectorizer = TfidfVectorizer()
      features = vectorizer.fit_transform(df['combined_text'])
      ```
  9. Train a k-means clustering model with a specified number of clusters ``(num_clusters)`` and the fit() function is used to fit the model to the TF-IDF features.
      ```ruby

       from sklearn.cluster import KMeans
      
      # Train a k-means clustering model
      num_clusters = 5
      kmeans = KMeans(n_clusters=num_clusters)
      kmeans.fit(features)
      ```
  11. Assign clusters to data points by using ``predict()`` function on the k-means model.
      ```ruby

      # Assign clusters to data points
      df['cluster_label'] = kmeans.predict(features)
      ```
  13. Analyze and visualize clusters
       ```ruby

      # Analyze clusters
      cluster_counts = df['cluster_label'].value_counts()
      print(cluster_counts)
      
      # Visualize clusters
      import matplotlib.pyplot as plt
      
      plt.bar(cluster_counts.index, cluster_counts.values)
      plt.xlabel('Cluster')
      plt.ylabel('Number of Listings')
      plt.title('Distribution of Listings across Clusters')
      plt.show()
      ```
  15. The output:
      - The Code and the output can viewed in the Google Colab file.
        
    
  16. Why this machine learning is effective:
      
      Machine learning algorithms can offer users personalised recommendations by examining user behaviour and preferences. Based on the user's prior interactions,          search history, or demographic data, a portal may propose pertinent items, products, or content. By doing this, the user experience is improved and the portal         is used more frequently.
             
  







## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


