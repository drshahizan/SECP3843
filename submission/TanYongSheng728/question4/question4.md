<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Tan Yong Sheng
#### Matric No.: A20EC0157
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets">Tweets</a>

## Question 4
It is crucial that apply machine learning in our dataset especially the dataset is very large. This is because it can provide better learning outcome if the dataset is large enough for them to train and test. This will enhance the accuracy of the result and provide a better view on dataset.<br>
Since my dataset assigned is <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/06-tweets">Tweets</a> which contain various type of words instead of number. Therefore I have choosen <strong>Sentiment Analysis</strong> as a machine learning method for this question.<br>
I have chosen 1 type of sentiment analyzer for this project which is :
- <strong>VADER</strong>

#
### 1. Load Data from MongoDB
Since the dataset is stored in MongoDB which results from previous question, we need to retrieve the data from there. 

 - Install Required Library
 ```
 !pip install pymongo
```

 - Connect & Retrieve from MongoDB database 
 ```
from pymongo import MongoClient

# Establish a connection to your MongoDB database
client = MongoClient('mongodb+srv://tys072801:alextys072801AB@tyscluster.tyt40lp.mongodb.net/')
db = client['test']
collection = db['tweets']

# Retrieve the data from the collection
data = list(collection.find())

# Print the first few documents
for document in data[:5]:
    print(document)
 ```

Output:
<p align="center">
<img src="./files/images/output collab.png"></img>
</p>

#
### 2. Data Cleaning
The field that going to use for sentiment analysis is `text`. Therefore we need to clean the data like remove unwanted special character, punctuation, numbers, and url to prevent them from altering the sentiment analysis result.

 - First download resources from NLTK by adding the code below.
 ```
 import nltk
nltk.download('punkt')
 ```

 - Next import the neccessary library and define a function to do data cleaning.
<p align="center">
<img src="./files/images/cleaning def.png"></img>
</p>

 - Now apply the function above into the tweet dataset on text field.

 ```
 # Clean and tokenize the tweet texts
cleaned_data = []
for document in data:
    cleaned_tweet = clean_tweet_text(document['text'])
    document['cleaned_text'] = cleaned_tweet
    cleaned_data.append(document)

Output:
# Print the cleaned texts
for document in cleaned_data[:5]:
    print(document['cleaned_text'])
```

Output:
<p align="center">
<img src="./files/images/cleaned text.png"></img>
</p>

 - From the output we can see that the text is cleaned without any special character, punctuation, numbers, and url.

#
### 3. Vader Sentiment Analysis
Using the VADER to do sentiment analysis using the code below.
```
import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from pymongo import MongoClient

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis and store sentiment labels in a DataFrame
df = pd.DataFrame(cleaned_data)
df['sentiment_score'] = df['cleaned_text'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment_label'] = df['sentiment_score'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')

df_vader = df[['cleaned_text', 'sentiment_label']]
df_vader.head(10)
```

Output:
<p align="center">
<img src="./files/images/vader.png"></img>
</p>

#
### 4. Vader Accuracy
Next we find the model accuracy using the code below. 
```
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define the texts and labels based on your dataset structure
texts = df_vader['cleaned_text']
sentiment_labels = df_vader['sentiment_label']

# Split the data into training and testing sets
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, sentiment_labels, test_size=0.2, random_state=42)

# Perform sentiment analysis on the test data using VADER
sia = SentimentIntensityAnalyzer()
test_sentiment_scores = [sia.polarity_scores(text)['compound'] for text in test_texts]
test_sentiment_labels = ['positive' if score > 0 else 'negative' if score < 0 else 'neutral' for score in test_sentiment_scores]

# Calculate the accuracy of VADER sentiment analysis
accuracy = accuracy_score(test_labels, test_sentiment_labels)
print("Accuracy of VADER sentiment analysis:", accuracy)
```

Output:
<p align="center">
<img src="./files/images/vader accuracy.png"></img>
</p>

From the result we can see that Vader is very accurate by getting `1.0` for accuracy. This means that Vader can predict correctly for each text.

#
### 5. Determine Label Count
Now we need to obtain the label count for each category to better understand our data. Below code store each label count to a variable which can be used later on.
```
label_counts = df_vader.groupby('sentiment_label').size().to_dict()

positive_count = label_counts.get('positive', 0)
neutral_count = label_counts.get('neutral', 0)
negative_count = label_counts.get('negative', 0)

print("Positive count:", positive_count)
print("Neutral count:", neutral_count)
print("Negative count:", negative_count)
```
Output:
<p align="center">
<img src="./files/images/label count.png"></img>
</p>

#
### 6. Visualization
After getting the count, we will need to make visualization on the result we obtain to have a better view and easily analyze from the visual.<br>
 - First we make a `donut chart` to visualize the count using the code below.

 ```
import matplotlib.pyplot as plt

# Compute label counts
label_counts = df_vader['sentiment_label'].value_counts()

# Create a donut chart
labels = label_counts.index
sizes = label_counts.values

# Set color scheme
colors = ['green', 'gray', 'red']

# Create a pie chart with a hole in the center
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Add a circle in the center to create a donut chart
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(center_circle)

# Add a title
plt.title('Sentiment Distribution')

# Display the chart
plt.show()

 ```

Output:
 <p align="center">
<img src="./files/images/donut sentiment.png"></img>
</p>

 - Now we add another bar chart to see the individual word for each category to have better preview. Below is the code for it.
```
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words

english_words = set(words.words())
stopwords_set  = set(stopwords.words('english'))

def filter_valid_words(word_freq, min_length=2):
    valid_word_freq = {}
    for word, freq in word_freq.items():
        if word in english_words and len(word) > min_length:
            valid_word_freq[word] = freq
    return valid_word_freq

sentiments = ['positive', 'negative', 'neutral']
colors = ['green', 'red', 'blue']

plt.figure(figsize=(15, 6))

for i, sentiment in enumerate(sentiments):
    texts = df_vader[df_vader['sentiment_label'] == sentiment]['cleaned_text']
    word_counts = pd.Series(' '.join(texts).split()).value_counts()
    word_counts = word_counts[~word_counts.index.isin(stopwords_set)]
    valid_word_counts = filter_valid_words(word_counts)
    
    # Convert valid_word_counts to a pandas Series
    valid_word_counts = pd.Series(valid_word_counts)
    
    plt.subplot(1, 3, i+1)
    valid_word_counts.head(10).sort_values(ascending=False).plot(kind='bar', color=colors[i])
    plt.xlabel('Count')
    plt.ylabel(f'{sentiment.capitalize()} Words')
    plt.title(f'Top 10 {sentiment.capitalize()} Words')

plt.tight_layout()
plt.show()
```

Output:
<p align="center">
<img src="./files/images/bar sentiment.png"></img>
</p>

#
### 7. Conclusion
I have gain several insight after conducting analysis on tweets dataset. The code above demonstrates sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis technique and the NLTK (Natural Language Toolkit) library. Below are the summary of the key points:

1. The VADER sentiment analysis technique, implemented through the `SentimentIntensityAnalyzer` class from NLTK, is used to analyze the sentiment of text data.
2. The code retrieves tweet data from a MongoDB collection and performs data cleaning by removing unwanted special characters, punctuation, and numbers from the tweet text.
3. The cleaned tweet data is then classified into sentiment labels (positive, negative, or neutral) based on their sentiment scores obtained from VADER.
4. The sentiment labels and cleaned tweet data are stored in a pandas DataFrame for further analysis and visualization.
5. The code includes visualizations to analyze the top positive, negative, and neutral words in the cleaned tweet data using horizontal bar charts.
6. Stopwords, common words that are often removed from text analysis, are utilized to filter out irrelevant words from the word counts.
7. The NLTK library is used for various tasks such as sentiment analysis, data cleaning, and retrieving stopwords.
8. Matplotlib is employed for creating the bar charts to visualize the top words for each sentiment category.

#

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




