<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Eddie Wong Chung Pheng
#### Matric No.: A20EC0031
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/04-companies" >Companies</a>

## Question 4 (a)
Based on my dataset, it contain a lot of information about different companies, such as founded_day,founded_month, founded_year, offices, number_of_employees, etc. So, I decided to use regression algorithm as it is commonly used for predicting continuous numerical values, such as predicting the year a company was founded or the year it was deadpooled. Some popular regression algorithms include linear regression, decision tree regression, random forest regression, and support vector regression.  

Code: <a href="./files/code/Question4.ipynb">Question4.ipynb</a>

### Step 1: Install the required libraries
```
!pip install pymongo
```

### Step 2: Import the required libraries
```
import pandas as pd
import numpy as np
import pymongo
```

### Step 3: Connect to MongoDB and Load Data 
Make sure the collection does exist in the Cluster server so that the pymongo can load the data.
<img  src="./files/images/mongodb.png"></img>

```
client = pymongo.MongoClient("mongodb+srv://prowong42:eddie2001@cluster0.hdgexg2.mongodb.net/")
db = client["test"]
collection = db["companies"]
data = list(collection.find())

#Convert to Dataframe
df = pd.DataFrame(data)

df.head(10)
```
<img  src="./files/images/df.png"></img>

### Step 4: Data Cleaning
Checking Null Data
```
 df.isna().sum()
```

<img  src="./files/images/before_clean.png"></img>

Clean the data
```
 df["category_code"].fillna("NaN", inplace = True)
 df["number_of_employees"].fillna("NaN", inplace = True)
 df["founded_day"].fillna("NaN", inplace = True)
 df["founded_year"].fillna("NaN", inplace = True)
 df["founded_month"].fillna("NaN", inplace = True)
 df["deadpooled_year"].fillna("NaN", inplace = True)
 df["tag_list"].fillna("NaN", inplace = True)
 df["alias_list"].fillna("NaN", inplace = True)
 df["founded_month"].fillna("NaN", inplace = True)
 df["deadpooled_month"].fillna("NaN", inplace = True)
 df["deadpooled_day"].fillna("NaN", inplace = True)
 df["deadpooled_url"].fillna("NaN", inplace = True)
```

Drop some unwanted column & rows that contain NaN data 
```
 columns_to_drop = ['email_address', 'phone_number','description','overview','image','ipo','twitter_username','acquisition','homepage_url','blog_url','blog_feed_url']
 df = df.drop(columns_to_drop, axis=1)
 df.dropna(inplace=True)
```

Check again
```
df.isna().sum()
```

<img  src="./files/images/after_clean.png"></img>

### Step 5: Apply Regression Algorithm
For my case, I will use the linear regression and x-axis will be founded_year (independent variable) and y-axis will be duration (dependent variable).

Import all the necessary libraries
```
 from sklearn.linear_model import LinearRegression
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import mean_squared_error
```

Calculate the duration
```
 df['founded_year'] = df['founded_year'].apply(lambda x: int(re.findall(r'\d+', str(x))[0]) if re.findall(r'\d+', str(x)) else None)
 df['deadpooled_year'] = df['deadpooled_year'].apply(lambda x: int(re.findall(r'\d+', str(x))[0]) if re.findall(r'\d+', str(x)) else None)
 df['duration'] = df['deadpooled_year'] - df['founded_year']
```  

Create the feature matrix X and target variable y
```
 from sklearn.linear_model import LinearRegression
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import mean_squared_error
```

Split the training and test data
```
 X = df[['founded_year']]
 y = df['duration']
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Create a LinearRegression model to fit the training data & make prediction
```
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

Evaluate the model using mean squared error (MSE)
```
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
```

Final Result: 
<img  src="./files/images/result.png"></img>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




