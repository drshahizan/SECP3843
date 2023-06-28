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
For the given case study, I will be using Support Vector Machine as a machine learning algorithms for text classification to automatically categorize articles into different topics or containers. This can help in organizing and recommending relevant content to users. SVM performs well in high-dimensional feature spaces, which is often the case in text classification tasks. In text classification, each word or n-gram is considered a feature, and SVM can handle a large number of features efficiently.

#### Set up the environment

1. Open Google Colab and create a new notebook.
2. Import the necessary libraries.
   ```python
      import pandas as pd
      import numpy as np
      from sklearn.model_selection import train_test_split
      from sklearn.feature_extraction.text import TfidfVectorizer
      from sklearn.svm import SVC
      from sklearn.metrics import classification_report
      from pymongo import MongoClient
   ```

#### Connect to MongoDB and retrieve data

1. Install the pymongo library.
   ```python
      !pip install pymongo
   ```

2. Set up a connection to MongoDB database and retrieve the data.
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
   ```

2. Split the data into input (X) and target (y) variables.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
