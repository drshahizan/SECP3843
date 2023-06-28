
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

## Question 4 
For this case study, I have chosen to perform sentiment analysis on the dataset as it's the most appropriate approach for this type of dataset. The goal is to determine whether each tweet has a positive, negative, or neutral sentiment. I have used Google Colab to perform the sentiment analysis due to it's convenience. Below are the steps taken to perform the sentiment analysis.

You may find the full coding for this sentiment analysis [here](https://github.com/drshahizan/SECP3843/blob/main/submission/HUNK12/question4/files/code/AA_STDE_Q4.ipynb)

### Step 1: Install and import the required libraries
```py
!pip install pymongo
!pip install nltk

import pandas as pd
import numpy as np
import pymongo
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
``` 
### Step 2: Pull data from MongoDB
```py
client = pymongo.MongoClient("mongodb+srv://mikhel:admin@cluster0.kwav8pt.mongodb.net/")
db = client["STDE"]
collection = db["tweets"]
data = list(collection.find())
df = pd.DataFrame(data)
```
### Step 3: Remove other columns
Since we'll only need the `text` column to perform the analysis, we can remove the other columns.
```py
text_df = df.drop(['_id', 'in_reply_to_status_id', 'retweet_count', 'contributors',
       'created_at', 'geo', 'source', 'coordinates', 'in_reply_to_screen_name',
       'truncated', 'entities', 'retweeted', 'place', 'user', 'favorited',
       'in_reply_to_user_id', 'id', 'retweeted_status'], axis=1)
text_df.head()
```
Result:

![image](https://github.com/drshahizan/SECP3843/assets/3646429/f7675407-9706-4970-9e8b-7f3a911cef0e)

### Step 4: Data pre-processing
Since the text contains special characters, links, etc. we'll need to perform some data pre-processing to ensure accurate results. The function below splits the words, removes any links and special characters, then joins them back.
```py
sia = SentimentIntensityAnalyzer()

def preprocess_tweet_text(tweet):
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#', '', tweet)
    
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tokenizer.tokenize(tweet)
    
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words and token.isalpha()]
    
    clean_tweet = ' '.join(tokens)
    
    return clean_tweet
```
### Step 5: Applying sentiment analysis
```py
text_df['clean_text'] = text_df['text'].apply(preprocess_tweet_text)

text_df['sentiment'] = text_df['clean_text'].apply(lambda x: sia.polarity_scores(x)['compound'])

text_df['sentiment_label'] = text_df['sentiment'].apply(lambda x: 'Positive' if x >= 0.05 else 'Negative' if x <= -0.05 else 'Neutral')

print(text_df[['clean_text', 'sentiment_label']].head())
```
Results:

![image](https://github.com/drshahizan/SECP3843/assets/3646429/979c33e9-0122-4a2f-a816-21bc990e56b6)

Below this are the results of the analysis visualized in a bar chart.

![image](https://github.com/drshahizan/SECP3843/assets/3646429/2e053729-e144-4af9-9ad6-3726418f2f5d)

#### *Why are there so many neutral results compared to the other sentiments?*

There are several factors contributing to this.

 1. **Several languages:** 
 The text consist does not only contain English text, rather it contains alot such as Malay, Spanish, Japanese, Korean, etc.
 
 2. **Use of non-comprehensive language:** 
As mentioned, there are several languages present in the dataset. It is common to use abbreviations and shorthand writing when typing informal text such as this. However it reached a point where it has become incomprehensible that the analysis just marks it as neutral. Take for example the text below
```
oky nenek nya rt oky jd anak na yyy rt papanya asil yaaa rt eh tidur sana udah male
mizz u
```
3. **Short tweets:**
Some of the text in this data set only consists of 3 or less words which make it hard to determine the true meaning behind the tweets without any context

Due to the reasons above as well as several others, it has caused the analysis to have alot of neutral results. After attempting several tactics to take into account, I found that the same results are obtained every time.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
