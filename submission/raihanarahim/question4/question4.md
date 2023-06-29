<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Amirah Raihanah binti Abdul Rahim
#### Matric No.: A20EC0182
#### Dataset: Tweets

## Question 4 (a)
### Machine Learning approach on Tweets Dataset.
The machine learning method I chose is classification which is a supervised machine learning and I used K-Nearest Neighbours algorithm.

<br>

For my case study, I  focused on developing a classification model to determine whether tweets will become trending or not. To obtain the result, I use the feature selection technique to obtain the best features that can contirubute in classifying the tweets. Then, I define what it means by trending or not by using the engagement ratio between `favourites_count` / `followers_count`. 

<br>

The process involved are :
* `Data Cleaning` : The data has JSON format with '{}' and ',' thus data need to be clean to remove those unwanted characters.
* `Defining label for trending` : Defining what it means by trending by using this formula = `favourites_count` / `followers_count`.
* `Feature Selection` : The dataset has many attributes so I choose the ones that can be a feature to identify whether the tweet will be trending or not. This method contributes to obtaining the best result in developing the machine learning model.
* `Apply ML algorithm` : K-NN algorithm is chosen as it is the most suitable algorithm to classify tweets based on the label defined.
* `Analyze results` : After applying the algorithm, the results are analyzed to get insights from the dataset.

## Data Cleaning
1. Import the JSON file
```py
import pandas as pd

# Load the JSON file into a DataFrame
data = '/content/drive/MyDrive/tweetsmodified.json'
df = pd.read_json(data)

# View the DataFrame

pd.set_option('display.max_columns', None)
df.head(5)
```
<img width="1085" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/75401404-d690-4061-a5cb-88417ccc2a6f">

2. Check the number of records and the columns
<img width="397" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/55e77ce0-f3df-467d-b16f-cd3c464acf68">

3. To predict whether tweets will go trending or not; we will determine using few features which are :

* followers count from column user
* friends count from column user
* links count from column text
* words count from column text
* hashtag count from column text
* tweet length from column text
* Hence, other columns will be drop.

```py
drop_cols = ['in_reply_to_status_id', 'geo', 'source', 'coordinates','in_reply_to_screen_name','truncated','place','favorited','in_reply_to_user_id']
df = df.drop(drop_cols, axis=1)
df
```
<img width="1064" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/14e7c2e0-45a6-4b77-82ea-a203dfc66e36">

4. Remove the unwanted {} and element name in column _id, entities, user, id and retweeted status

```py
df['_id'] = df['_id'].str['$oid']
df
```
<img width="515" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/bbdb6f11-db05-488f-8eec-22664e17af13">

5. Seperate items in entities into columns.

```py
df['user_mentions'] = df['entities'].apply(lambda x: x.get('user_mentions', []))
df['urls'] = df['entities'].apply(lambda x: x.get('urls', []))
df['hashtags'] = df['entities'].apply(lambda x: x.get('hashtags', []))
# View the updated DataFrame
print(df.head())
```
<img width="467" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/4829cbc4-e637-4294-8fd4-e3cb53581338">

6. Then, entities column can be dropped.
```py
drop_cols = ['entities']
df = df.drop(drop_cols, axis=1)
df
```
7. Check items in column user.
```py
df.iloc[0]["user"]
```
<img width="527" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/b58107c6-ab1b-4eb0-9e20-abad5cdf9b2c">

8. Since we want to use `friends_count` , `favourites_count` and `followers_count` , extract from column user.
   
```py
df['friends_count'] = df['user'].apply(lambda x: x.get('friends_count', []))
df['followers_count'] = df['user'].apply(lambda x: x.get('followers_count', []))
df['favourites_count'] = df['user'].apply(lambda x: x.get('favourites_count', []))
# View the updated DataFrame
print(df.head())
```
<img width="393" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/7f747bd6-2457-47f5-8d27-2ea5cea9df56">

9. Remove unwanted characters from  `friends_count` , `favourites_count` and `followers_count`.
    
```py
df['friends_count'] = df['friends_count'].str['$numberInt']
df['followers_count'] = df['followers_count'].str['$numberInt']
df["words_count"] = df.apply(lambda tweet: len(tweet["text"].split()),axis=1)
df["tweet_length"] = df.apply(lambda tweet: len(tweet["text"]), axis=1)
df
```
<img width="463" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/59575b57-e192-40e4-9cdd-edb02535f11d">

10. Next, we will create column hashtag_count, word_count and links_count retrieve from text column.

```py
df["hashtag_count"] = df.apply(lambda tweet: tweet["text"].count("#"),axis=1)
df["links_count"] = df.apply(lambda tweet: tweet["text"].count("http"),axis=1)
df['id'] = df['id'].str['$numberLong']
df['favourites_count'] = df['favourites_count'].str['$numberInt']
df
```
11. Next, we will combine all features in one table.
    
```py
features = df[["tweet_length","followers_count","favourites_count","friends_count","links_count","words_count","hashtag_count"]]
features
```
<img width="620" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/b51fef62-91d6-4789-9e48-b1bbb896e1e6">

## Define Trending Tweets

1. Using engagement ratio where a higher engagement ratio may indicate a trending tweet.
<br>
Firstly, change the datatype for both attributes.

```py
# Convert columns to numeric data types
df['favourites_count'] = pd.to_numeric(df['favourites_count'])
df['followers_count'] = pd.to_numeric(df['followers_count'])
df['engagement_ratio_favorites'] = df['favourites_count'] / df['followers_count']
df['engagement_ratio_favorites'] 
```
<img width="456" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/4a1ce584-f9fa-496a-807e-0755ff43010a">

2. Find median of the ratio.
```py
df['engagement_ratio_favorites'] .median()
```
`median` : 0.005714285714285714

3. Then, compare the ratio and the median to obtain whether the record is classified as `is_trending` .
   
```py
import numpy as np # linear algebra
df["is_trending"] = np.where(df["engagement_ratio_favorites"]>df["engagement_ratio_favorites"].median(), 1, 0)
df["is_trending"]
```
<img width="424" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/b068334f-84d1-4583-9057-da625764654b">

5. Define `is_trending`as labels.

```py
labels = df["is_trending"]
labels
```

## Machine Learning

1. Firstly, implement standardization process where the mean of each feature has been subtracted, and the result has been divided by the standard deviation. This is usefuwhen working with features that have different scales or units.

```py
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
scaled_features
```
<img width="480" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/f930350f-cd56-444f-973f-24473059c8ac">

2. Now we will divide the data to Training set and Test set.

```py
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(scaled_features, labels, test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
```
<img width="277" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/3b7d737c-5326-4cd0-bfa2-2839b67c33da">

3. Implement K-NN algorithm to the model and plot scatter plot to view the result.
```py
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
scores = list()
for k in range(1,200):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test,y_test))
plt.style.use('ggplot')
plt.figure(figsize=(12,10))
plt.scatter(range(1,200), scores)
plt.title("The Prediction of KNN vs Number of k Neighbors")
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()
```
<img width="542" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/dc7399a6-8998-4cc8-a1dc-536ed62f51f2">

3. Print the classification report to analyze the machine learning result.
   
```py
from sklearn.metrics import classification_report, confusion_matrix
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
predictions = knn.predict(X_test)
print(classification_report(y_test, predictions))
```
<img width="348" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/1acff2ef-ac72-4949-91cf-8b15f4587b31">

  > From the model, we get 63% accuracy on our classification whether tweets will become trending or not

3. Print the confusion matrix and visualize in heatmap.
   
```py
print(confusion_matrix(y_test, predictions))
import seaborn as sns
plt.figure(figsize=(12,10))
plt.title("Confusion Matrix Result of KNN Predictions")
sns.heatmap(confusion_matrix(y_test, predictions), annot=True, cmap="jet")
```
<img width="459" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/1783de86-007d-4908-8fce-6baeee0e32ef">

> True Negative (TN): 1762 - The number of instances that were correctly predicted as the negative class.<br>
False Positive (FP): 763 - The number of instances that were incorrectly predicted as the positive class when they were actually negative.<br>
False Negative (FN): 1046 - The number of instances that were incorrectly predicted as the negative class when they were actually positive.<br>
True Positive (TP): 1396 - The number of instances that were correctly predicted as the positive class.<br>

> Based on these findings, the model has a moderate level of accuracy (63%) in predicting whether or not tweets would go trending. However, the number of false negatives (1046) is rather large, showing that the model struggles to correctly detect positive events. This shows that the model's performance need to be improved, in terms of lowering false negatives and improving recall.

## Google Collab Code

[Complete Machine Learning Process ](https://github.com/drshahizan/SECP3843/blob/main/submission/raihanarahim/question4/files/code/AA_ML.ipynb)
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
