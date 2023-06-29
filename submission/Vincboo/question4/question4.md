<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Vincent Boo Ee Khai
#### Matric No.: A20EC0231
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 4 
### 1. Install all related package
```
!pip install pymongo
!pip install pandas
```
### 2. Import all the libraries that will be needed to used
```
import pymongo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
```

### 3. Build Connection to mongoDB
```
cs = pymongo.MongoClient("mongodb+srv://boo2001:AR5Dev64-n@cluster0.bgjcppf.mongodb.net/")
db = cs["AA"]
collection = db["stories"]
data = list(collection.find())
```

### 4. Data Cleaning
1. First of all we will check inport the dataset into a dataframeand normalize it.
```
df = pd.DataFrame(data)
df = json_normalize(data)
```

2. Then, we check for Na value in each colum of the dataframe
``` 
df.isnull().sum()
```

3. Drop rows that contain Na value and check again
```
df.dropna(axis='columns', inplace = True)
df.isnull().sum()
```

### 5. Naive Bayes (Machine Learning)
1. Extract the story descriptions
```
desc = []
tpc_names = []

for story in data:
    description = story['description']
    tpc_name = story['topic']['name']
    desc.append(description)
    tpc_names.append(tpc_name)
```

3. Create an instance of CountVectorizer
```
vectorizer = CountVectorizer()
```

3. Vectorizw 'description' and make it into bag.
```
features = vectorizer.fit_transform(desc)
```

4. Create instance
```
classifier = MultinomialNB()
```

5. Train classifier and encoded topic labels
```
classifier.fit(features, tpc_names)
```

### 6. Data Prediction

1. Split the Extracted data
```
X_train, X_test, y_train, y_test = train_test_split(descriptions, tpc_names, test_size=0.2, random_state=42)
```
2. vectorize the splited data
```
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
```

3. Fit the training data into classifier.
```
classifier.fit(X_train_vec, y_train)
```

4. Make Predict for tested data
```
y_pred = nb_classifier.predict(X_test_vec)
```

5. View Accuracy
```
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the prediction is:", accuracy)
```
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




