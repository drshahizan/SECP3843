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

### Data Preprocessing
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

## Question 5 (b)

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
