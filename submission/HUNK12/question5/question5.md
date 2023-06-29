
  

<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Mikhel Adam Bin Muhammad Ezrin
#### Matric No.: A20EC0237
#### Dataset: [Tweets](https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets)

## Question 5 (a)
There are several ways to optimize performance when dealing with a large volume of JSON data. The following are a few examples on how to do so:

### 1. Data Preprocessing
This is one of the easiest ways to improve performance. All thats needed to do filter and clean the JSON data to eliminate unnecessary information and then converting the JSON data into a more efficient format such as a pandas DataFrame.  In the case of the `Tweets` dataset, what I did was drop all the columns except for the `text` column since thats all is needed to perform the sentiment analysis in [Question 4](https://github.com/drshahizan/SECP3843/blob/main/submission/HUNK12/question4/question4.md#step-3-remove-other-columns) . Below is the code on how to perform the latter:

####  Upload the original dataset and check the file size
```py
import requests

file_url = 'https://raw.githubusercontent.com/drshahizan/SECP3843/main/submission/HUNK12/materials/fixed_tweets.json'

# Download the file
response = requests.get(file_url)
file_content = response.content

# Get the file size in bytes
file_size_bytes = len(file_content)

# Convert bytes to megabytes
file_size_mb = file_size_bytes / (1024 * 1024)

print(f"The file size is: {file_size_mb:.2f} MB")
```
Result:

![image](https://github.com/drshahizan/SECP3843/assets/3646429/3d41b1f3-7de4-4426-9593-5d7ba528fa26)

#### Drop unused columns and save it as a JSON file
```py
df = df.drop(['_id', 'in_reply_to_status_id', 'retweet_count', 'contributors',
       'created_at', 'geo', 'source', 'coordinates', 'in_reply_to_screen_name',
       'truncated', 'entities', 'retweeted', 'place', 'user', 'favorited',
       'in_reply_to_user_id', 'id', 'retweeted_status'], axis=1)

df.to_json('text.json', orient='records')
```

#### Check the new file size
```py
import os

# Get the file size in bytes
file_size_bytes = os.path.getsize('text.json')

# Convert bytes to megabytes
file_size_mb = file_size_bytes / (1024 * 1024)

print(f"The file size is: {file_size_mb:.2f} MB")
```
Result:

![image](https://github.com/drshahizan/SECP3843/assets/3646429/43cc335d-0059-4b34-8c2f-4402988e3f36)

> As we can see, the original size of the dataset was 47.60MB. After preparing the data by dropping the unused columns, the new size became only 2.45MB. That's only about 5% of the orignal size! This means that less resources are needed to load the file thus improvving performance.

### 2. Using libraries to process large data
Using libraries such as Pandas or Dask to read the data is alot more efficient and uses alot less data. Reading a JSON file as a Pandas DataFrame significantly uses less memory. Below are code on how to use some libraries to improve efficiency:

 - **Pandas Chunking:** This allows us to process the data in smaller portions, reducing the memory usage.
```py
import pandas as pd

chunk_size = 1000

df = pd.DataFrame()

for chunk in pd.read_json('tweets.json', lines=True, chunksize=chunk_size):
    df = df.append(chunk)
```

- **Dask for Parallel Processing:** Similar to Pandas Chunking, this allows us to handle large datasets by dividing them into smaller partitions and processing them in parallel.
```py
import dask.dataframe as dd
df = dd.read_json('tweets.json', lines=True)
filtered_df = df[df['text'] > 100]
filtered_df = filtered_df.compute()
```

These are just a few suggestion that could be used to improve efficiency, however these are most likely not needed given how small our dataset is already. Using these methods may not even bring a significant impact to the performance.

## Question 5 (b)
First, let's upload the sentiment analysis data to MongoDB. Continuing from [Question 4](https://github.com/drshahizan/SECP3843/blob/main/submission/HUNK12/question4/question4.md), we'll add the code below to upload the sentiment analysis data to MongoDB:
```py
import json
from pymongo import MongoClient

text_df.to_json('text.json', orient='records')
with open('text.json') as f:
    data = json.load(f)
    
client = pymongo.MongoClient("mongodb+srv://mikhel:admin@cluster0.kwav8pt.mongodb.net/")
db = client["STDE"]
collection = db["tweets_text"]
collection.insert_many(data)
```
Results:

![image](https://github.com/drshahizan/SECP3843/assets/3646429/cfb7b091-9065-4b42-bfcc-1a44a5227113)

![image](https://github.com/drshahizan/SECP3843/assets/3646429/17000905-fd30-48e0-aa85-1cbbd0beb985)

Next, go to the charts.mongodb.com and click on "Charts". Then from there, create charts based on the data that has been uploaded to MongoDB

![image](https://github.com/drshahizan/SECP3843/assets/3646429/d5f3e76c-4300-4ce3-a1dd-819ad7963c7f)

Below is a dashboard I've created which consist of two charts. Why only two charts? I found that these two charts are the only ones that provide any valuable information given the nature of the case study.

![image](https://github.com/drshahizan/SECP3843/assets/3646429/d0c2d8fc-7ae4-482d-9923-5deaa230c0b2)

The first chart shows a bar graph visualizing the sentiment labels. As seen, we can see that most tweets are more positive than negative. The reason for the huge number of neutral sentiments can be read [here](https://github.com/drshahizan/SECP3843/blob/main/submission/HUNK12/question4/question4.md#why-are-there-so-many-neutral-results-compared-to-the-other-sentiments)

![image](https://github.com/drshahizan/SECP3843/assets/3646429/2bf61fb3-fcb9-46e6-b7ef-426e6e34e0dc)

The second chart shows the heatmap of which country the tweets originate from. We can see a huge chunk of the tweets originate somewhere in Europe as well as USA.

![image](https://github.com/drshahizan/SECP3843/assets/3646429/23da2ebf-466d-4c5d-9e3b-b375be83caf8)

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
