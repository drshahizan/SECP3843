<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Cai Xuan
#### Matric No.: A20EC0062
#### Dataset: Analytics Dataset

## Question 4

The machine learning used in this case study is linear regression. It is to see the relationship of the training dataset and test dataset for the 'limit' attribute in the Accounts table.

Tool used:
- Jupyter Notebook

Libraries used:
- scikit-learn
- pandas
- json

<h4>Step 1 - Data Preprocessing and Cleaning</h4>

Open the JSON file 

```
#Open JSON file
with open('accounts.json') as f1:
    data1 = json.load(f1)

with open('transactions.json') as f2:
    data2 = json.load(f2)
```

Both JSON file can be joined by the same account_id.

```
#From accounts JSON file
join_dict = {}
for item in data1:
    account_id = str(item['account_id'])  # Convert to string
    join_dict[account_id] = item
```

```
#From transactions JSON file
joined_data = []
for item in data2:
    account_id = str(item['account_id'])  # Convert to string
    if account_id in join_dict:
        joined_item = {**join_dict[account_id], **item}
        joined_data.append(joined_item)
```

Then, the joined data can be written in a file, 'joined_data.json'

```
with open('joined_data.json', 'w') as outfile:
    json.dump(joined_data, outfile, indent=4)
```

Convert it into pandas dataframe

```
import pandas as pd
import json

# Load joined JSON data from file
with open('joined_data.json') as f:
    data = json.load(f)

# Create an empty DataFrame
df = pd.DataFrame()

# Read data in chunks from the JSON file and concatenate into the DataFrame
chunk_size = 1000  # Adjust the chunk size as needed
for i in range(0, len(data), chunk_size):
    chunk = data[i:i + chunk_size]
    df = pd.concat([df, pd.DataFrame(chunk)], ignore_index=True)

# Display the DataFrame
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/1.png" />
</p>

Remove all the unwanted columns.

```
columns_to_remove = ['bucket_start_date', 'bucket_end_date', 'transactions']
df = df.drop(columns_to_remove, axis=1)
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/2.png" />
</p>

Remove the element in the items for each columns. For example, {'$oid': '5ca4bbc1a2dd94ee58161cb1'} will be changed into 5ca4bbc1a2dd94ee58161cb1. Make sure all the column is changed into proper format.

```
df['_id'] = df['_id'].str['$oid']
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/2.png" />
</p>

```
df['account_id'] = df['account_id'].str['$numberInt']
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/3.png" />
</p>

```
df['limit'] = df['limit'].str['$numberInt']
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/5.png" />
</p>

```
df['transaction_count'] = df['transaction_count'].str['$numberInt']
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/6.png" />
</p>

```
df['products'] = df['products'].astype(str).str.replace('[', '').str.replace(']', '')
df
```

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/7.png" />
</p>

Convert datatype of column 'limit' and 'transaction_count' from string to float.

```
df['limit'] = df['limit'].astype(float)
df
```

```
df['transaction_count'] = df['transaction_count'].astype(float)
df
```

<h4>Machine Learning - Linear Regression</h4>

Import the sklearn library.

```
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
```

Perform linear regression by splitting the data in to 20 and 80 percent using the column, 'limit'.

```
X = df.drop(columns=['limit'])  # Features (without 'limit' column)
y = df['limit']  # Target variable ('limit' column)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model using mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
```

Result: Mean Squared Error: 169890.65444598708

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/9.png" />
</p>

<h4>Step 3 - Scatterplot</h4>

Install matplotlib ```!pip install matplotlib```

Plot the scatterplot

```
#Scatterplot
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)

# Add labels and title
plt.xlabel('Training Data')
plt.ylabel('Test Data')
plt.title('Scatterplot of Training Data vs. Test Data')

# Add a diagonal line representing perfect predictions
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')

# Display the plot
plt.show()
```

Result:

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/10.png" />
</p>

Predict value 

```
new_data = [[10000, 20000]]  # Example input data
prediction = model.predict(new_data)

# Print the predicted value
print("Predicted value:", prediction)
```

Result: Predicted value: [65428.603017]

<p align="center">
  <img height="300px" src="https://github.com/drshahizan/SECP3843/blob/main/submission/leecaixuan/question4/files/images/11.png" />
</p>














## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


