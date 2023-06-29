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

`Colab`: [Naive_Bayes.ipynb](https://github.com/drshahizan/SECP3843/blob/4f20339748c541b7e93a10a8e2b5514f511dc2b6/submission/DinieHazim/question%204/files/code/Naive_Bayes.ipynb)

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

#### Naive Bayes

1. Extract the story descriptions and topic names
   ```python
      descriptions = []
      topic_names = []

      for story in data:
          description = story['description']
          topic_name = story['topic']['name']
          descriptions.append(description)
          topic_names.append(topic_name)
   ```

2. Split the dataset into training and testing sets
   ```python
      X_train, X_test, y_train, y_test = train_test_split(descriptions, topic_names, test_size=0.2, random_state=42)
   ```

3. Create a CountVectorizer to convert text into numerical features
   ```python
      vectorizer = CountVectorizer()
      X_train_vec = vectorizer.fit_transform(X_train)
      X_test_vec = vectorizer.transform(X_test)
   ```

5. Create a Multinomial Naive Bayes classifier
   ```python
      nb_classifier = MultinomialNB()
   ```

7. Train the classifier on the training data
   ```python
      nb_classifier.fit(X_train_vec, y_train)
   ```

9. Make predictions on the testing data
    ```python
      y_pred = nb_classifier.predict(X_test_vec)
    ```

11. Evaluate the performance of the classifier
    ```python
      accuracy = accuracy_score(y_test, y_pred)
      print("Accuracy:", accuracy)
    ```

    ![image](https://github.com/drshahizan/SECP3843/assets/120595244/938f3963-5c99-4f85-b1aa-bbcd97086374)


#### Predict new text topic

   ```python
      new_text = 'Kevin Hart'
      new_text_vec = vectorizer.transform([new_text])
      predicted_topic = nb_classifier.predict(new_text_vec)
      print("Predicted Topic:", predicted_topic)
   ```

![image](https://github.com/drshahizan/SECP3843/assets/120595244/b38953ad-1e3d-42f5-ac43-29cab9d401e0)


   ```python
      new_text = 'Jocelyn Chia'
      new_text_vec = vectorizer.transform([new_text])
      predicted_topic = nb_classifier.predict(new_text_vec)
      print("Predicted Topic:", predicted_topic)
   ```

![image](https://github.com/drshahizan/SECP3843/assets/120595244/8f247033-9044-405a-ad09-6cb8a4716335)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/dinie-hazim-52770514b/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
