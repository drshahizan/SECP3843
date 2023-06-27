<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Adrina Asyiqin Binti Md Adha
#### Matric No.: A20EC0174
#### Dataset: sales.json

## Question 4 

### Step 1:Data Cleaning
- In this part, I execute all code in Google Colab
- Load sales.json data from mongodb
  ```py
  !pip install pymongo
  import pymongo
  import pandas as pd

  # Connect to MongoDB and retrieve data
  password = "Adrina857600"
  client = pymongo.MongoClient("mongodb+srv://cluster0.yvk5zzq.mongodb.net/", username="adrinaasyiqin", password=password)
  db = client["salesdatabase"]
  collection = db["salessample"]
  data = list(collection.find())

  # Convert to DataFrame
  df = pd.DataFrame(data)

  # Check the DataFrame
  print(df.head())
  df.info()
  ```

- Data cleaning and preparation. Some of the data cleaning I did is `handling missing values`,`removing duplicates`, and `convert items column into seperate columns`

  ```py
  # Handling Missing Values
  # Drop rows with missing values
  df.dropna(inplace=True)

  # Replace missing values with a specified value
  df.fillna(value=0, inplace=True)

  # Removing Duplicates
  df.drop_duplicates(subset='_id', inplace=True)

  # Convert the 'items' column into separate columns
  df_items = pd.json_normalize(df['items'])

  # Rename the columns
  new_columns = {}
  for col in df_items.columns:
      new_columns[col] = f'item{col}'
  df_items.rename(columns=new_columns, inplace=True)

  # Merge the item columns with the original DataFrame
  df = pd.concat([df, df_items], axis=1)

  # Drop the original 'items' column
  df.drop('items', axis=1, inplace=True)

  ```

### Step 2 :Data viusalisation
- Create bar graph
  ```py
  import matplotlib.pyplot as plt

  # Count the number of sales by store location
  sales_by_location = df['storeLocation'].value_counts()

  # Create a bar chart
  plt.figure(figsize=(10, 6))
  plt.bar(sales_by_location.index, sales_by_location.values)
  plt.xlabel('Store Location')
  plt.ylabel('Number of Sales')
  plt.title('Sales Distribution by Store Location')
  plt.xticks(rotation=45)
  plt.show()

  ```

- Create pie chart
  ```py
  import matplotlib.pyplot as plt

  # Count the number of sales by purchase method
  sales_by_purchase_method = df['purchaseMethod'].value_counts()

  # Create a pie chart
  plt.figure(figsize=(8, 8))
  plt.pie(sales_by_purchase_method.values, labels=sales_by_purchase_method.index, autopct='%1.1f%%', startangle=90)
  plt.axis('equal')
  plt.title('Sales Distribution by Purchase Method')
  plt.show()

  ```

### Step 3:Macbine Learning
  ```py
  # Drop the unnecessary columns
  df.drop(['item1','item2','item3','item4','item5','item6','item7','item8','item9','item0'], axis=1, inplace=True)
  df.info()

  from sklearn.model_selection import train_test_split
  from sklearn.linear_model import LinearRegression
  from sklearn.metrics import mean_squared_error

  selected_fields = df[['couponUsed']]

  X = selected_fields.drop('couponUsed', axis=1)
  y = selected_fields['couponUsed']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  model = LinearRegression()
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  ```




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
