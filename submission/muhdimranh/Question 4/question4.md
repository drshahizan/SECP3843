<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: MUHAMMAD IMRAN HAKIMI BIN MOHD SHUKRI
#### Matric No.:A20EC0213
#### Dataset:AIRBNB

## Question 4
--------------------------------------------------------------------------------------
## <b>Sentiment Analysis: Airbnb Listings based on Customer Reviews</b>

The project described in the provided code is focused on improving the functioning of an Airbnb portal by utilizing machine learning techniques for advanced data analysis and visualization. The chosen machine learning approach involves sentiment analysis of customer reviews to classify them into positive, negative, or neutral sentiments. The project aims to provide insights into customer feedback and sentiment distribution.

Here are the steps taken to answer the question:

### Step 1: Install Required Modules

```
!pip install pymongo
!pip install pandas
!pip install langdetect
```

### Step 2: Retrieving Data from MongoDB

The code begins by connecting to a MongoDB database and retrieving data from the "ListingsAndReviews" collection. The data is then converted into a pandas DataFrame, and nested attributes are expanded using the json_normalize function. The "reviews" array is further extracted and normalized into a separate DataFrame. 

```
import pymongo
import pandas as pd
from pandas.io.json import json_normalize


# Connect to MongoDB and retrieve data
client = pymongo.MongoClient("mongodb+srv://muhdimranh:123@sentimentanalysis.5esk2hq.mongodb.net/")
db = client["airbnbportal"]
collection = db["ListingsAndReviews"]
data = list(collection.find())

# Convert to dataframe
df = pd.DataFrame(data)
# Convert nested attributes to separate columns using json_normalize
df = json_normalize(data)
# Extract attributes from the "reviews" array
reviews_df = json_normalize(df["reviews"].explode().tolist())

```

The original DataFrame and the expanded "reviews" DataFrame are merged using pd.concat. Display options are adjusted to show the full contents of the 'comments' column.


```
# Merge the original DataFrame with the expanded "reviews" attributes DataFrame
df2 = pd.concat([df, reviews_df], axis=1)
# Adjust display options to show the full contents of the 'comments' column
pd.set_option('display.max_colwidth', None)

print(df2.head(20))
df2.head()
```

![Q4](files/images/q4.1.png)


### Step 3: Data Pre-Processing 

The NLTK library is utilized for text preprocessing. Special characters, digits, and stopwords are removed from the comments using regular expressions and tokenization. Lemmatization is applied to obtain the base form of words. The preprocessing function is then applied to the 'comments' column.

```
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stopwords = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Clean and preprocess the comments
def preprocess_text(text):
    if isinstance(text, str):  # Check if the text is a string
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize the text
        tokens = text.split()
        # Remove stopwords and perform lemmatization
        clean_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords]
        # Join the tokens back into a single string
        clean_text = ' '.join(clean_tokens)
        return clean_text
    else:
        return ''

# Apply preprocessing to the 'comments' column
df2['comments'] = df2['comments'].apply(preprocess_text)

df2.dropna(subset=['comments'], inplace=True)

print(df2['comments'])
```

### Step 4: Filter non-English comments.

The langdetect library is used to filter out non-English comments from the DataFrame. A language detection function is applied to determine if a comment is in English or not. Rows with empty comments are dropped.

```
from langdetect import detect

# Function to check if a comment is in English
def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

# Apply language detection to filter out non-English comments
df2['comments'] = df2[df2['comments'].apply(is_english)]['comments']

# Drop rows with empty comments
df2.dropna(subset=['comments'], inplace=True)

print(df2['comments'])
```

![Q4](files/images/q4.2.png)


### Step 5: Duplicate Dataframe

The filtered DataFrame is saved as 'df3', and the filtered comments are displayed. This is to avoid having to re-run the comment filtering cell.

```
# Save the filtered DataFrame as df3
df3 = df2.copy()
```

### Step 6: Additional Data Pre-Processing.

Additional preprocessing is performed on the comments in 'df3'. This step removes special characters, digits, and newline characters from the comments.

```
# Clean and preprocess the comments
def preprocess_text(text):
    if isinstance(text, str):  # Check if the text is a string
        # Remove special characters, digits, and newline characters
        text = re.sub(r'[^a-zA-Z ]', '', text.replace('\n', ' ').replace('\r', ' '))
        # Convert to lowercase
        text = text.lower()
        # Tokenize the text
        tokens = text.split()
        # Remove stopwords and perform lemmatization
        clean_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords]
        # Join the tokens back into a single string
        clean_text = ' '.join(clean_tokens)
        return clean_text
    else:
        return ''

# Apply preprocessing to the 'comments' column in df3
df3['comments'] = df3['comments'].apply(preprocess_text)
```

![Q4](files/images/q4.3.png)
![Q4](files/images/q4.4.png)

### Step 7: Using VADER to automatically label sentiment.

I have 11, 000 lines of datasets after preprocessing. Because of time constraint, I will be using VADER to automatically label the sentiment using its pre-trained sentiment model.

The NLTK library's SentimentIntensityAnalyzer is employed for sentiment analysis. The VADER sentiment analyzer is initialized, and a function is defined to obtain sentiment scores using VADER. Sentiment scores and compound scores are extracted from the comments, and sentiment labels are assigned based on the compound scores. The sentiment analysis results are displayed, saved to a new DataFrame, and exported to a CSV file.

```
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to get sentiment scores using VADER
def get_sentiment_scores(text):
    sentiment = sia.polarity_scores(text)
    return sentiment

# Apply sentiment analysis and get sentiment scores
df3['sentiment_scores'] = df3['comments'].apply(get_sentiment_scores)

# Extract compound scores as a measure of overall sentiment
df3['compound_score'] = df3['sentiment_scores'].apply(lambda x: x['compound'])

# Define a function to assign sentiment labels
def assign_sentiment_label(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply the sentiment label function to create a 'sentiment' column
df3['sentiment'] = df3['compound_score'].apply(assign_sentiment_label)

# Print the sentiment analysis results
print(df3[['comments', 'sentiment']])

# Save the sentiment analysis results to a new DataFrame
sentiment_df = df3[['comments', 'sentiment']].copy()

# Save the sentiment analysis results to a CSV file
sentiment_df.to_csv('sentiment_analysis_results.csv', index=False)

```

![Q4](files/images/q4.5.png)

### Step 8: Model Training 

The scikit-learn library is used to build a logistic regression model for sentiment classification. The labeled DataFrame is loaded from the sentiment analysis results CSV file. Rows with missing values in the preprocessed text are dropped. The data is split into training and testing sets. A TF-IDF vectorizer is initialized and fitted on the training data. The logistic regression model is trained, and predictions are made on the testing data. A classification report is printed, showing the precision, recall, and F1-score of the model.

```
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

labeled = pd.read_csv('sentiment_analysis_results.csv')

# Drop rows with missing values in the preprocessed text
labeled.dropna(subset=["comments"], inplace=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(labeled['comments'], labeled['sentiment'], test_size=0.2, random_state=42)

# Initialize a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the training data
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Transform the testing data
X_test_vectorized = vectorizer.transform(X_test)

# Make predictions on the testing data
y_pred1 = model.predict(X_test_vectorized)

# Print the classification report
report_imbalanced = classification_report(y_test, y_pred1)
print(report_imbalanced)
```

![Q4](files/images/q4.6.png)


### Step 9: Handling Class Imbalance

Another machine learning model is employed to address class imbalance. A linear support vector machine (SVM) classifier is trained using the imbalanced dataset. The dataset is balanced using RandomOverSampler, which oversamples the minority class (negative sentiment) to match the majority class. The balanced dataset is then used to train the SVM classifier. Predictions are made on the testing set, and a classification report is printed, showing the evaluation metrics for the balanced model.

```
from imblearn.over_sampling import RandomOverSampler

labeled = pd.read_csv('sentiment_analysis_results.csv')

# Drop rows with missing values in the preprocessed text
labeled.dropna(subset=["comments"], inplace=True)


# Print the count of each sentiment category
sentiment_counts = labeled['sentiment'].value_counts()
print(sentiment_counts)

# Split the dataset into training and testing sets
X = labeled['comments']
y = labeled['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature extraction with TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Apply RandomOverSampler to balance the classes
oversampler = RandomOverSampler(random_state=42)
X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train_tfidf, y_train)

# Train a linear SVM classifier
svm = LinearSVC()
svm.fit(X_train_resampled, y_train_resampled)

# Predict sentiment on the testing set
y_pred2 = svm.predict(X_test_tfidf)

# Evaluate the model
report_balanced = classification_report(y_test, y_pred2)
print(report_balanced)

```

![Q4](files/images/q4.7.png)


### Step 10: Model Evaluation and Visualization

Bar charts are plotted to compare the precision, recall, and F1-score between the imbalanced and balanced models for each sentiment category. The charts provide a visual representation of the performance improvement achieved by balancing the dataset.

```
import numpy as np
import matplotlib.pyplot as plt

# Define the sentiment categories
sentiments = ['Negative', 'Neutral', 'Positive']

# Define the classification report metrics for the imbalanced model
precision_imbalanced = [0.42, 0.80, 0.99]
recall_imbalanced = [0.52, 0.89, 0.99]
f1_imbalanced = [0.47, 0.84, 0.99]

# Define the classification report metrics for the balanced model
precision_balanced = [0.82, 0.99, 0.98]
recall_balanced = [0.20, 0.63, 1.00]
f1_balanced = [0.32, 0.77, 0.99]

# Set the width of the bars
bar_width = 0.3

# Set the positions of the bars on the x-axis
r1 = np.arange(len(sentiments))
r2 = [x + bar_width for x in r1]

# Plot the precision values
plt.bar(r1, precision_imbalanced, color='b', width=bar_width, label='Imbalanced')
plt.bar(r2, precision_balanced, color='g', width=bar_width, label='Balanced')

# Add x-axis labels and ticks
plt.xlabel('Sentiment')
plt.xticks(r2, sentiments)

# Add y-axis label
plt.ylabel('Precision')

# Add a title
plt.title('Comparison of Precision for Imbalanced and Balanced Models')

# Add a legend
plt.legend()

# Show the plot
plt.show()

# Plot the recall values
plt.bar(r1, recall_imbalanced, color='b', width=bar_width, label='Imbalanced')
plt.bar(r2, recall_balanced, color='g', width=bar_width, label='Balanced')

# Add x-axis labels and ticks
plt.xlabel('Sentiment')
plt.xticks(r2, sentiments)

# Add y-axis label
plt.ylabel('Recall')

# Add a title
plt.title('Comparison of Recall for Imbalanced and Balanced Models')

# Add a legend
plt.legend()

# Show the plot
plt.show()

# Plot the F1-score values
plt.bar(r1, f1_imbalanced, color='b', width=bar_width, label='Imbalanced')
plt.bar(r2, f1_balanced, color='g', width=bar_width, label='Balanced')

# Add x-axis labels and ticks
plt.xlabel('Sentiment')
plt.xticks(r2, sentiments)

# Add y-axis label
plt.ylabel('F1-score')

# Add a title
plt.title('Comparison of F1-score for Imbalanced and Balanced Models')

# Add a legend
plt.legend()

# Show the plot
plt.show()

```

![Q4](files/images/q4.8.png)
![Q4](files/images/q4.9.png)
![Q4](files/images/q4.10.png)

### Step 11: Generating Word Clouds

Word clouds are generated to visualize the most frequent words in each sentiment category. The preprocessed texts are separated based on sentiment, combined into separate strings, and passed to the WordCloud library. The word clouds are displayed for negative, neutral, and positive sentiments.

```
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Separate the preprocessed texts based on sentiment categories
negative_texts = labeled[labeled["sentiment"] == "negative"]["comments"]
neutral_texts = labeled[labeled["sentiment"] == "neutral"]["comments"]
positive_texts = labeled[labeled["sentiment"] == "positive"]["comments"]

# Combine the preprocessed texts for each sentiment category into separate strings
negative_text_combined = " ".join(negative_texts)
neutral_text_combined = " ".join(neutral_texts)
positive_text_combined = " ".join(positive_texts)

# Generate word clouds for each sentiment category
wordcloud_negative = WordCloud().generate(negative_text_combined)
wordcloud_neutral = WordCloud().generate(neutral_text_combined)
wordcloud_positive = WordCloud().generate(positive_text_combined)

# Display the word clouds
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(wordcloud_negative, interpolation="bilinear")
plt.title("Negative Sentiment")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(wordcloud_neutral, interpolation="bilinear")
plt.title("Neutral Sentiment")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(wordcloud_positive, interpolation="bilinear")
plt.title("Positive Sentiment")
plt.axis("off")

plt.tight_layout()
plt.show()
```

> Wordcloud for Negative Sentiment

![Q4](files/images/wordcloud_negative.png)

> Wordcloud for Neutral Sentiment

![Q4](files/images/wordcloud_neutral.png)

> Wordcloud for Positive Sentiment

![Q4](files/images/wordcloud_positive.png)



### Step 12: Generating bar chart for top 20 words.

Lastly, bar charts are created to display the top 20 words and their frequencies for each sentiment category. The most common words are extracted from each category and plotted in separate subplots, providing insights into the most frequent words associated with different sentiments.

```
import matplotlib.pyplot as plt

# Get the top 20 words and their frequencies for each sentiment category
top_negative_words = negative_word_freq.most_common(20)
top_neutral_words = neutral_word_freq.most_common(20)
top_positive_words = positive_word_freq.most_common(20)

# Extract the words and frequencies for plotting
negative_words, negative_freq = zip(*top_negative_words)
neutral_words, neutral_freq = zip(*top_neutral_words)
positive_words, positive_freq = zip(*top_positive_words)

# Create subplots for each sentiment category
fig, axs = plt.subplots(3, 1, figsize=(12, 10))

# Plot the top 20 words for Negative Sentiment
axs[0].barh(negative_words, negative_freq)
axs[0].set_title("Top 20 words for Negative Sentiment")
axs[0].invert_yaxis()

# Plot the top 20 words for Neutral Sentiment
axs[1].barh(neutral_words, neutral_freq)
axs[1].set_title("Top 20 words for Neutral Sentiment")
axs[1].invert_yaxis()

# Plot the top 20 words for Positive Sentiment
axs[2].barh(positive_words, positive_freq)
axs[2].set_title("Top 20 words for Positive Sentiment")
axs[2].invert_yaxis()

# Adjust spacing between subplots
plt.tight_layout()

# Display the chart
plt.show()

```

![Q4](files/images/bar_charts.png)


Overall, the project utilizes machine learning techniques, specifically sentiment analysis, to analyze customer reviews.



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





