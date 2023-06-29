<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: RADIN DAFINA BINTI RADIN ZULKAR NAIN
#### Matric No.: A20EC0135
#### Dataset: [Supply Store](https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales)

## Question 4 
### Data Preparation

1. In this section, we perform the necessary data preparation steps before conducting any analysis or visualization. We import the required libraries, pandas and numpy, for data manipulation and analysis.

```python
import pandas as pd
import numpy as np
```

2. We also import the json module to load the data from a JSON file into a DataFrame. The data is loaded from the file path /content/drive/MyDrive/supplystore.json using the json.load() function. The loaded data is then converted into a DataFrame using the pd.DataFrame.from_records() function.

```python
import json
from pandas import json_normalize

with open('/content/drive/MyDrive/supplystore.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert JSON data to DataFrame
df = pd.DataFrame.from_records(data)

# Display the DataFrame
display(df)
```

The resulting DataFrame is displayed to get an initial view of the data structure and contents.

<div align="center"><img src="files/images/df1.png" height="300px" /></div>

3. The next steps involve cleaning and transforming the data. We modify specific columns to ensure they have the correct data type and format for further analysis. We make use of lambda functions and pandas methods like apply() and drop() to achieve these transformations.

4. First, we convert the _id column values from a nested dictionary structure to a string format using the str['$oid'] operation. This simplifies the representation of the unique identifier.

```python
df['_id'] = df['_id'].str['$oid']
```

  <div align="center"><img src="files/images/df2.png" height="300px" /></div>

5. Next, we convert the saleDate values to the appropriate data type by extracting the $date value from the nested dictionary and converting it to a long integer format using the lambda x: x['$date']['$numberLong'] operation.

```python
df['saleDate'] = df['saleDate'].apply(lambda x: x['$date']['$numberLong'])
```

6. We then split the customer data into separate columns, such as gender, age, email, and satisfaction, by applying lambda functions to the customer column. These functions handle missing values and nested dictionary structures within the customer data.

```python
# Splitting Customer Data
df['gender'] = df['customer'].apply(lambda x: x['gender'] if pd.notnull(x) else np.nan)
df['age'] = df['customer'].apply(lambda x: x['age']['$numberInt'] if pd.notnull(x) and 'age' in x and '$numberInt' in x['age'] else np.nan)
df['email'] = df['customer'].apply(lambda x: x['email'] if pd.notnull(x) else np.nan)
df['satisfaction'] = df['customer'].apply(lambda x: x['satisfaction']['$numberInt'] if pd.notnull(x) and 'satisfaction' in x and '$numberInt' in x['satisfaction'] else np.nan)

# Drop the original "customer" column
df.drop('customer', axis=1, inplace=True)
```

  <div align="center"><img src="files/images/df4.png" height="300px" /></div>

7. To organize the item-related information, we create new columns, including item_names, item_tags, item_prices, and item_quantities. These columns are populated by extracting relevant data from the items column, which contains a list of dictionaries. We apply lambda functions to iterate over the list and retrieve the desired information. Finally, we drop the original customer and items columns from the DataFrame to remove redundant information and improve data structure.

```python
df['item_names'] = df['items'].apply(lambda x: [item['name'] for item in x] if isinstance(x, list) else [])
df['item_tags'] = df['items'].apply(lambda x: [item['tags'] for item in x] if isinstance(x, list) else [])
df['item_prices'] = df['items'].apply(lambda x: [float(item['price']['$numberDecimal']) for item in x] if isinstance(x, list) else [])
df['item_quantities'] = df['items'].apply(lambda x: [int(item['quantity']['$numberInt']) for item in x] if isinstance(x, list) else [])

# Drop the original "items" column
df.drop('items', axis=1, inplace=True)
```

  <div align="center"><img src="files/images/df3.png" height="300px" /></div>

8. At the end of the data preparation section, we check the shape of the DataFrame to verify the number of rows and columns and display the count of missing values for each column using the isna().sum() method.

```python
df.shape
```
```python
df.isna().sum()
```

  <div align="center"><img src="files/images/df5.png" height="300px" /></div>
  
### Data Visualization

1. In this section, we use the seaborn and matplotlib.pyplot libraries to visualize the data and gain insights. First, we import the necessary libraries, including seaborn and matplotlib.pyplot.
   
```python
import seaborn as sns
import matplotlib.pyplot as plt
```

2. We start by visualizing the gender distribution in the dataset. We count the occurrences of each gender category using value_counts() on the gender column and store the result in the gender_counts variable. We then create a bar plot using sns.barplot() to display the gender distribution, with the x-axis representing the gender categories and the y-axis representing the count. The plot is customized with appropriate labels and a title, and it is displayed using plt.show().
   
```python
# Count the occurrences of each gender
gender_counts = df['gender'].value_counts()

# Plot the gender distribution
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()
```
  <div align="center"><img src="files/images/graph1.png" height="350px" /></div>

3. Next, we explore the age distribution by classifying ages into predefined categories. We convert the age column to numeric values using pd.to_numeric() to handle any inconsistencies or errors. We define age bins and labels to categorize the ages, and we create a new column, age_category, using pd.cut() to assign each age to its corresponding category. We count the occurrences of each age category and store the result in age_counts. We then create a histogram using plt.bar() to visualize the count of each age category. Again, appropriate labels and a title are set, and the plot is displayed.
   
```python
# Convert 'age' column to numeric
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Define age categories
age_bins = [0, 12, 19, 29, 39, 49, 59, 69, 120]
age_labels = ['Child', 'Teenager', '20s', '30s', '40s', '50s', '60s', 'Senior']

# Classify age into categories
df['age_category'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Calculate count of each age category
age_counts = df['age_category'].value_counts().sort_index()

# Create histogram
plt.figure(figsize=(10, 6))
plt.bar(age_labels, age_counts)

# Set labels and title
plt.xlabel('Age Category')
plt.ylabel('Count')
plt.title('Age Distribution by Category')

# Show the plot
plt.show()

```
  <div align="center"><img src="files/images/graph2.png" height="350px" /></div>
  
4. Moving on, we examine the distribution of purchase methods by counting the occurrences of each method using value_counts() on the purchaseMethod column. We create a pie chart using plt.pie() to visualize the distribution, with the purchase method names as labels and the corresponding percentages displayed. A title is set, and the plot is displayed.

```python
# Count the occurrences of each purchase method
purchase_counts = df['purchaseMethod'].value_counts()

# Plot the pie chart for purchase method
plt.figure(figsize=(8, 6))
plt.pie(purchase_counts.values, labels=purchase_counts.index, autopct='%1.1f%%')
plt.title('Purchase Method Distribution')
plt.show()
```

  <div align="center"><img src="files/images/graph3.png" height="350px" /></div>

5. Lastly, we analyze the satisfaction levels of customers. We count the occurrences of each satisfaction level using value_counts() on the satisfaction column and store the result in satisfaction_counts. We create a bar plot using sns.barplot() to visualize the satisfaction levels, with the x-axis representing the satisfaction levels and the y-axis representing the count. Labels and a title are added, and the plot is displayed.
   
```python
# Count the occurrences of each satisfaction level
satisfaction_counts = df['satisfaction'].value_counts()

# Plot the satisfaction levels
plt.figure(figsize=(8, 6))
sns.barplot(x=satisfaction_counts.index, y=satisfaction_counts.values)
plt.xlabel('Satisfaction')
plt.ylabel('Count')
plt.title('Satisfaction Levels')
plt.show()
```

  <div align="center"><img src="files/images/graph4.png" height="350px" /></div>

### Steps for Machine Learning: Random Forest

In this section, we perform machine learning using the Random Forest algorithm. We import the necessary libraries, including train_test_split from sklearn.model_selection, RandomForestClassifier from sklearn.ensemble, and accuracy_score from sklearn.metrics.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
```

1. We start by selecting the features (X) and target variable (y) for the machine learning model. In this case, we choose the age and gender columns as features and the purchaseMethod column as the target variable. To handle categorical variables, we perform one-hot encoding on the features using pd.get_dummies().

2. Next, we split the data into training and testing sets using train_test_split(). The test_size parameter specifies the proportion of data to be allocated for testing, and random_state ensures reproducibility.

3. We create a RandomForestClassifier instance, rf, and fit it to the training data using rf.fit(). We then make predictions on the testing data using rf.predict(), storing the predictions in y_pred.

4. To evaluate the model's performance, we calculate the accuracy score by comparing the predicted labels (y_pred) with the actual labels (y_test) using accuracy_score(). The accuracy score is printed to the console.
```python
# Selecting the features and target variable
X = df[['age', 'gender']]
y = df['purchaseMethod']

# Performing one-hot encoding for categorical variables
X = pd.get_dummies(X)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
  <div align="center"><img src="files/images/ml.png" height="50px" /></div>

5. Finally, we create a confusion matrix using confusion_matrix() from sklearn.metrics to visualize the performance of the model. The confusion matrix represents the number of true positives, true negatives, false positives, and false negatives. We create a heatmap using sns.heatmap() to display the confusion matrix, with annotations and a color map for better interpretation. The plot is labeled and displayed.
```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Create a heatmap of the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.title('Confusion Matrix')
plt.show()
```
  <div align="center"><img src="files/images/graph5.png" height="350px" /></div>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)





