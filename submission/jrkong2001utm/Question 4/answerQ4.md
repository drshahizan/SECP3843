<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kong Jia Rou
#### Matric No.: A20EC0198
#### Dataset: Supply store

## Question 4 
In this question, I choose clustering to perform the machine learning on my dataset.Here are the detailed steps:

[Clustering](https://github.com/drshahizan/SECP3843/blob/main/submission/jrkong2001utm/Question%204/files/sourcecode/Q4_machinelearning.ipynb)

First, import all the relevant libraries.
```
# Import relevant libraries
import json
import pymongo
import pandas as pd
import re
import matplotlib.pyplot as plt
```

Connect to the MongoDB. Type in the databsename and collection name that created. Read and save the data in the `dataset`.
```
# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017')

# MongoDB database name
db = client["salesdb"]

# MongoDB collection name
collection = db["sales"]
dataset = list(collection.find())
first_data = ""

if len(dataset) > 0:
    first_data = dataset[0]
    print(first_data)
else:
    print("No data found in the dataset.")
```

Now, extracted the columns from the dataset.
```
# Create an empty list to store the extracted values
purchase_methods = []
order_id = []

# Iterate over the dataset and extract the values
for data in dataset:
    order_id.append(data['_id'])
    purchase_methods.append(data['purchaseMethod'])

# Create a DataFrame from the extracted values
df = pd.DataFrame({"_id":order_id, "purchaseMethod": purchase_methods})

# Print the DataFrame
print(df.tail())
```

We can now start performing machine learning. Import the necessary libraries.
```
# Import necessary libraries
import numpy as np
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt
%matplotlib inline
```

Apply the Elbow technique. The range is set to 1 to 4. 
```
#Using Elbow method 
cost = []
K = range(1,5)

#Iterate over cluster numbers one through 4
for num_clusters in list(K):
    kmode = KModes(n_clusters=num_clusters, init = "random", n_init = 5, verbose=1)
    kmode.fit_predict(df)
    cost.append(kmode.cost_)

plt.plot(K, cost, 'bx-')
plt.xlabel('No. of clusters')
plt.ylabel('Type')
plt.title('Elbow Method For Optimal k')
plt.show()
```

```
kmode = KModes(n_clusters=3, init = "random", n_init = 5, verbose=1)
clusters = kmode.fit_predict(df)
clusters
```

Test the output of the clustering by inserting the cluster value into the dataframe. Print the records using different value sof cluster.
```
# Insert the cluster column to the DataFrame
df.insert(0, "Cluster", clusters, True)

# Display the head of 10 records where the cluster is 0
df[df['Cluster']==0].head(10)
```

```
# Display the head of 10 records where the cluster is 1
df[df['Cluster']==1].head(10)
```

```
# Display the head of 10 records where the cluster is 2
df[df['Cluster']==2].head(10)
```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





