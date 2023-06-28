<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Low Junyi
#### Matric No.: A20EC0071
#### Dataset: [Airbnb](https://github.com/drshahizan/dataset/tree/main/mongodb/05-airbnb)

## Question 4 
**sentiment analysis** is used for this question.
Do press <a href="https://github.com/drshahizan/SECP3843/blob/main/submission/LowJunyi2001/question4/files/code/AA_Q4_2.ipynb" >here</a> for the code.



## Step 1: Install libraries
Use the code below to install the libraries which include pymongo to connect with MongoDB, textblob to perform sentiment analysis and WordCloud to generate word clouds.
```
!pip install pymongo
!pip install 
!pip install WordCloud
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/d79326bd-9677-4201-bce5-e92261c047fc"></img>



## Step 2: Import libraries
Use the code below to import the libraries.
```
import json
import pymongo
from textblob import TextBlob
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import words
import nltk

# Download stopwords corpus
nltk.download('stopwords')
nltk.download('words')


# Download tokenizer
nltk.download('punkt')
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/78ba2de2-bb9a-4fc3-a833-7f82e5ef0cae"></img>



## Step 3: Load Data
Use the code below to connect with MongoDB to retrieve the JSON data.
```
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client["AA"]
collection = db["db_airbnb"]
dataset = list(collection.find())
first_data = ""

if len(dataset) > 0:
    first_data = dataset[0]
    print(first_data)
else:
    print("No data found in the dataset.")
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/83df7328-b001-4c54-b459-7fcbd0a968cb"></img>



## Step 4: Data Preprocessing
Use the code below to run data preprocessing to ensure the quality of data which involves converting text to lowercase, removing special characters, punctuation, and numbers, tokenization and removing stopwords.
```
processed_descriptions = []

for data in dataset:
    description = data['description']
    
    # Convert text to lowercase
    description = description.lower()
    
    # Remove special characters, punctuation, and numbers
    description = re.sub(r'[^a-zA-Z\s]', '', description)
    
    # Tokenization
    tokens = word_tokenize(description)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back to form text
    processed_description = ' '.join(tokens)
    processed_descriptions.append(processed_description)

# Print the first data's description before and after processing
first_data = dataset[0]
print("Before: ", first_data['description'])
print("After: ", processed_descriptions[0])
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/6d912534-1621-4de8-9f72-0a02999203a4"></img>



## Step 5: Sentiment Analysis
Use the code below to begin sentiment analysis using TextBlob.
```
sentiments = []
sentiment_labels = []

for description in processed_descriptions:
    blob = TextBlob(description)
    sentiment = blob.sentiment.polarity
    sentiments.append(sentiment)

for sentiment in sentiments:
    if sentiment > 0:
        sentiment_labels.append("Positive")
    elif sentiment < 0:
        sentiment_labels.append("Negative")
    else:
        sentiment_labels.append("Neutral")

data = {"description": processed_descriptions, "Sentiment": sentiment_labels}
df = pd.DataFrame(data)

df.tail()
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/a528b033-01b6-4df9-9bda-51e42a38a289"></img>



## Step 6: Analyze the sentiment score
The code below use to count of positive, negative, and neutral description.
```
# Analyze the sentiment scores
positive_count = sum(sentiment > 0 for sentiment in sentiments)
negative_count = sum(sentiment < 0 for sentiment in sentiments)
neutral_count = len(sentiments) - positive_count - negative_count

# Print the sentiment analysis results
print("Positive Feedback Count:", positive_count)
print("Negative Feedback Count:", negative_count)
print("Neutral Feedback Count:", neutral_count)
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/1a763ed8-480f-4fd4-b4c5-1d5103154061"></img>



## Step 7: Visualization
Visualisation can provide better insight with the data
### Sentiment Distribution
Use the code below to visualise sentiment distribution in pie chart using Matplotlib.
```
labels = ['Positive', 'Negative', 'Neutral']
counts = [positive_count, negative_count, neutral_count]

colors = ['#8B4513', '#FFFF00', '#d2b48c']


plt.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Sentiment Distribution')
plt.axis('equal')
plt.show()
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/6f6d5bae-41e7-487c-8ecb-08e1c32c1d40"></img>



### Word Cloud
Used to generate the most frequent words in each sentiment category including neutral, negative and positive.
```
positive_descriptions = [description for description, sentiment in zip(processed_descriptions, sentiments) if sentiment > 0]
negative_descriptions = [description for description, sentiment in zip(processed_descriptions, sentiments) if sentiment < 0]
neutral_descriptions = [description for description, sentiment in zip(processed_descriptions, sentiments) if sentiment == 0]

positive_combined_description = ' '.join(positive_descriptions)
negative_combined_description = ' '.join(negative_descriptions)
neutral_combined_description = ' '.join(neutral_descriptions)

positive_wordcloud = WordCloud(width=800, height=400).generate(positive_combined_description)
negative_wordcloud = WordCloud(width=800, height=400).generate(negative_combined_description)
neutral_wordcloud = WordCloud(width=800, height=400).generate(neutral_combined_description)

# Plot the word clouds
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(positive_wordcloud, interpolation='bilinear')
axes[0].set_title('Positive Sentiment')
axes[0].axis('off')

axes[1].imshow(negative_wordcloud, interpolation='bilinear')
axes[1].set_title('Negative Sentiment')
axes[1].axis('off')

axes[2].imshow(neutral_wordcloud, interpolation='bilinear')
axes[2].set_title('Neutral Sentiment')
axes[2].axis('off')

plt.tight_layout()
plt.show()
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/333d403f-b037-4d05-abe3-7637be327252"></img>



and this code will show three bar charts to show the valid top 10 words for positive, negative and neutral sentiment.
```
positive_word_freq = positive_wordcloud.process_text(positive_combined_description)
negative_word_freq = negative_wordcloud.process_text(negative_combined_description)
neutral_word_freq = neutral_wordcloud.process_text(neutral_combined_description)

english_words = set(words.words())

def filter_valid_words(word_freq, min_length=1):
    valid_word_freq = {}
    for word, freq in word_freq.items():
        if word in english_words and len(word) > min_length:
            valid_word_freq[word] = freq
    return valid_word_freq

positive_valid_word_freq = filter_valid_words(positive_word_freq)
negative_valid_word_freq = filter_valid_words(negative_word_freq)
neutral_valid_word_freq = filter_valid_words(neutral_word_freq, min_length=3)

positive_sorted_word_freq = dict(sorted(positive_valid_word_freq.items(), key=lambda x: x[1], reverse=True))
negative_sorted_word_freq = dict(sorted(negative_valid_word_freq.items(), key=lambda x: x[1], reverse=True))
neutral_sorted_word_freq = dict(sorted(neutral_valid_word_freq.items(), key=lambda x: x[1], reverse=True))

top_positive_words = list(positive_sorted_word_freq.keys())[:10]
top_positive_freq = list(positive_sorted_word_freq.values())[:10]

top_negative_words = list(negative_sorted_word_freq.keys())[:10]
top_negative_freq = list(negative_sorted_word_freq.values())[:10]

top_neutral_words = list(neutral_sorted_word_freq.keys())[:10]
top_neutral_freq = list(neutral_sorted_word_freq.values())[:10]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Positive Sentiment
axes[0].bar(top_positive_words, top_positive_freq)
axes[0].set_title('Top 10 Descriptions - Positive Sentiment')
axes[0].set_xlabel('Description')
axes[0].set_ylabel('Frequency')
axes[0].set_xticklabels(top_positive_words, rotation=45)

# Negative Sentiment
axes[1].bar(top_negative_words, top_negative_freq)
axes[1].set_title('Top 10 Descriptions - Negative Sentiment')
axes[1].set_xlabel('Description')
axes[1].set_ylabel('Frequency')
axes[1].set_xticklabels(top_negative_words, rotation=45)

# Neutral Sentiment
axes[2].bar(top_neutral_words, top_neutral_freq)
axes[2].set_title('Top 10 Descriptions - Neutral Sentiment')
axes[2].set_xlabel('Description')
axes[2].set_ylabel('Frequency')
axes[2].set_xticklabels(top_neutral_words, rotation=45)

plt.tight_layout()
plt.show()
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/1ef62caa-1fe0-4d5b-a614-cafc33ba5f5f"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




