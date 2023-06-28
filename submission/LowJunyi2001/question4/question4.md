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
Use the code below to install the libraries which include nltk for natural language processing tasks, scikit-learn for feature extraction and preprocessing, pandas for data manipulation and analysis, matplotlib for data visualization, seaborn for enhancing the visualization aesthetics, numpy for numerical computations, pymongo for connecting with MongoDB, textblob for sentiment analysis and wordcloud for generating word clouds.
```
!pip install nltk
!pip install scikit-learn
!pip install pandas
!pip install matplotlib
!pip install seaborn
!pip install numpy
!pip install pymongo
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/196e27f4-384f-413b-8321-652c95786830"></img>



## Step 2: Import libraries
Use the code below to import the libraries.
```
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymongo
```



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
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import pymongo

def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Remove stopwords and punctuation from each sentence
    stop_words = set(stopwords.words('english'))
    vectorizer = CountVectorizer(stop_words=stop_words)
    
    preprocessed_sentences = []
    for sentence in sentences:
        sentence = sentence.lower()  # Convert to lowercase
        sentence = vectorizer.build_tokenizer()(sentence)  # Tokenize the sentence
        sentence = [word for word in sentence if word.isalpha()]  # Remove punctuation
        sentence = [word for word in sentence if word not in stop_words]  # Remove stopwords
        
        preprocessed_sentences.append(' '.join(sentence))
    
    return preprocessed_sentences

def summarize_text(text):
    # Preprocess the text
    preprocessed_sentences = preprocess_text(text)
    
    # Concatenate the preprocessed sentences into a single string
    preprocessed_text = ' '.join(preprocessed_sentences)
    
    # Perform text summarization
    word_frequencies = {}
    for word in preprocessed_text.split():
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] /= max_frequency
    
    sentence_scores = {}
    for sentence in preprocessed_sentences:
        for word in sentence.split():
            if word in word_frequencies.keys():
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    summary = ' '.join(summary_sentences)
    
    return summary


# Example usage
first_data = dataset[0]
summary = summarize_text(first_data['summary'])
print(summary)
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/0a7edb72-2b7f-408c-a975-89d31244f9b8"></img>



## Step 5: Sentiment Analysis
Use the code below to begin sentiment analysis using TextBlob.
```

from textblob import TextBlob


# Connect to MongoDB and retrieve the data
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client["AA"]
collection = db["db_airbnb"]
dataset = list(collection.find())

# Preprocess summaries and perform sentiment analysis
processed_summaries = []
sentiments = []
sentiment_labels = []

for data in dataset:
    summary = data['summary']
    
    # Perform text preprocessing if needed
    processed_summary = preprocess_text(summary)  # Modify the preprocess_text function according to your needs
    processed_summaries.append(processed_summary)
    
    # Perform sentiment analysis
    blob = TextBlob(summary)
    sentiment = blob.sentiment.polarity
    sentiments.append(sentiment)
    
    # Assign sentiment labels
    if sentiment > 0:
        sentiment_labels.append("Positive")
    elif sentiment < 0:
        sentiment_labels.append("Negative")
    else:
        sentiment_labels.append("Neutral")

# Create a DataFrame with summary and sentiment information
data = {"summary": processed_summaries, "Sentiment": sentiment_labels}
df = pd.DataFrame(data)

# Display the tail of the DataFrame
print(df.tail())
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/9fcd0e0f-24ec-4fd0-b7a9-d322661d0def"></img>



## Step 6: Analyze the sentiment score
The code below use to count of positive, negative, and neutral summary.
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


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/d80012fb-80b5-4398-b9d5-4884b51883a6"></img>



## Step 7: Visualization
Visualisation can provide better insight with the data.
### Sentiment Distribution
Use the code below to visualise sentiment distribution in pie chart using Matplotlib.
```
import matplotlib.pyplot as plt

# Sentiment counts and labels
labels = ['Positive', 'Negative', 'Neutral']
counts = [positive_count, negative_count, neutral_count]

# Colors for the pie chart
colors = ['#8B4513', '#FFFF00', '#d2b48c']

# Plotting the pie chart
plt.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Setting the title and making the chart aspect ratio equal
plt.title('Sentiment Distribution')
plt.axis('equal')

# Display the pie chart
plt.show()
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/72f4549d-de67-4771-b1e0-af22fd192c8e"></img>



### Word Cloud
Used to generate the most frequent words in each sentiment category including neutral, negative and positive.
```
# Positive, negative, and neutral summaries
positive_summaries = [summary for summary, sentiment in zip(processed_summaries, sentiments) if sentiment > 0]
negative_summaries = [summary for summary, sentiment in zip(processed_summaries, sentiments) if sentiment < 0]
neutral_summaries = [summary for summary, sentiment in zip(processed_summaries, sentiments) if sentiment == 0]

# Flatten the nested lists
positive_combined_summary = ' '.join([summary for sublist in positive_summaries for summary in sublist])
negative_combined_summary = ' '.join([summary for sublist in negative_summaries for summary in sublist])
neutral_combined_summary = ' '.join([summary for sublist in neutral_summaries for summary in sublist])



# Generate word clouds
positive_wordcloud = WordCloud(width=800, height=400).generate(positive_combined_summary)
negative_wordcloud = WordCloud(width=800, height=400).generate(negative_combined_summary)
neutral_wordcloud = WordCloud(width=800, height=400).generate(neutral_combined_summary)

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


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/59e1a90b-79e1-4afe-bcc9-07c808e2e57e"></img>



and this code will show three bar charts to show the valid top 10 Summaries for positive, negative and neutral sentiment.
```
import nltk
from nltk.corpus import words

positive_word_freq = positive_wordcloud.process_text(positive_combined_summary)
negative_word_freq = negative_wordcloud.process_text(negative_combined_summary)
neutral_word_freq = neutral_wordcloud.process_text(neutral_combined_summary)

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
axes[0].set_title('Top 10 Summaries - Positive Sentiment')
axes[0].set_xlabel('Summary')
axes[0].set_ylabel('Frequency')
axes[0].set_xticklabels(top_positive_words, rotation=45)

# Negative Sentiment
axes[1].bar(top_negative_words, top_negative_freq)
axes[1].set_title('Top 10 Summaries - Negative Sentiment')
axes[1].set_xlabel('Summary')
axes[1].set_ylabel('Frequency')
axes[1].set_xticklabels(top_negative_words, rotation=45)

# Neutral Sentiment
axes[2].bar(top_neutral_words, top_neutral_freq)
axes[2].set_title('Top 10 Summaries - Neutral Sentiment')
axes[2].set_xlabel('Summary')
axes[2].set_ylabel('Frequency')
axes[2].set_xticklabels(top_neutral_words, rotation=45)

plt.tight_layout()
plt.show()
```


Result:


<img  src="https://github.com/drshahizan/SECP3843/assets/120614501/434337fe-e710-4136-9819-98a5bc631613"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




