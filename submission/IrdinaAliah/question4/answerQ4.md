<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NUR IRDINA ALIAH BINTI ABDUL WAHAB
#### Matric No.: A20EC0115
#### Dataset: AIRBNB

## Question 4 (a)
Machine learning can be used to improve the functioning of the portal as well as provide advanced 
data analysis and visualisation tools. Please choose an appropriate machine learning approach or 
algorithm for your case study and describe how it will be used in your case study. You may include 
relevant code snippets and screenshots that illustrate the solution implemented. 
[15 marks]

install required modules
```
!pip install pymongo
!pip install pandas
!pip install langdetect

```

retrieve Data from MongoDB
```
import pymongo
import pandas as pd
from pandas.io.json import json_normalize


# Connect to MongoDB and retrieve data
client = pymongo.MongoClient("mongodb+srv://irdinaaliah2:Freekindome_00@cluster0.o4fadwf.mongodb.net/'
")
db = client["dashboard"]
collection = db["dashboard"]
data = list(collection.find())

# Convert to dataframe
df = pd.DataFrame(data)
# Convert nested attributes to separate columns using json_normalize
df = json_normalize(data)
# Extract attributes from the "reviews" array
reviews_df = json_normalize(df["reviews"].explode().tolist())

```
data preprocess
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
def preprocess(text):
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
df2['description'] = df2['description'].apply(preprocess_text)

df2.dropna(subset=['description'], inplace=True)

print(df2['description'])
# Clean and preprocess the comments
def preprocess(text):
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

model training
<img src="https://github.com/drshahizan/SECP3843/blob/1065b3cb866003907fe13b1b120a512d2af8759a/submission/IrdinaAliah/question4/files/images/result.png" style="width: 700px; height: 200px;">
```
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

labeled = pd.read_csv('sentiment_analysis_results.csv')

# Drop rows with missing values in the preprocessed text
labeled.dropna(subset=["description"], inplace=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(labeled['description'], labeled['sentiment'], test_size=0.2, random_state=42)

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

## Question 4 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





