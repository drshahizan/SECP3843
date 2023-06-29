<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nur Syamalia Faiqah Binti Mohd Kamal
#### Matric No.: A20EC0118
#### Dataset : [Analytics Dataset](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 4
In my case study, I will be using 3 different classification models for machine learning. The sources I will retreive from the MongoDB Atlas.

### Tool
The tool that I will be using is:
- Google Colab

### Steps
1. Install related packages. As I mentioned, I will retreive from the MongoDB Atlas. Before loading the data, I need to make sure I already install below packages.
  ```python
  !pip install pymongo
  !pip install dnspython
  ```

2. Load collections. Do not forget to import necessary package before starting any code. In order to load collections from MongoDB database, type below code:
  ```python
  import pymongo

  # Replace the connection string with your MongoDB connection details
  connection_string = "mongodb+srv://cham21:4FatbS01@cluster0.4vcdbcm.mongodb.net/test"
  client = pymongo.MongoClient(connection_string)
  
  # Access the "analytics" database
  db = client.analytics
  ```
- Load the collections to DataFrame: 
  ```python
  import pandas as pd
  
  # Read the "accounts" collection into a DataFrame
  accounts_df = pd.DataFrame(list(db.accounts.find()))
  
  # Read the "customers" collection into a DataFrame
  customers_df = pd.DataFrame(list(db.customers.find()))
  
  # Read the "transactions" collection into a DataFrame
  transactions_df = pd.DataFrame(list(db.transactions.find()))
  ```

3. Check the value/attribute in Dataframe to make sure every data have been retrieved.
  ```python
  accounts_df.head()
  customers_df.head()
  transactions_df.head()
  ```

4. Load sample joined data. In this case study, I will chunk the size of the collections and only join `accounts_df` and `transactions_df`. Chunking data can help me optimized the performance if the data is in big size.
  ```python
  import pandas as pd
  
  # Set the chunk size
  chunk_size = 1000  # Adjust the chunk size as needed
  
  # Initialize an empty DataFrame for the joined data
  join_df = pd.DataFrame()
  
  # Iterate over the chunks
  for i in range(0, len(accounts_df), chunk_size):
      # Select the chunk of data from each DataFrame
      accounts_chunk = accounts_df.iloc[i:i+chunk_size]
      transactions_chunk = transactions_df.iloc[i:i+chunk_size]
  
      # Perform the join on 'account_id'
      chunk_join = pd.merge(accounts_chunk, transactions_chunk, on='account_id')
  
      # Rename '_id_x' column to '_id'
      chunk_join.rename(columns={'_id_x': '_id'}, inplace=True)
  
      # Drop '_id_y' column
      chunk_join.drop('_id_y', axis=1, inplace=True)
  
      # Concatenate the chunk with the previous chunks
      join_df = pd.concat([join_df, chunk_join], ignore_index=True)
  
  # Display the joined DataFrame
  join_df.head(10)
  ```
5. Preprocessing data. Before applying machine learning, I need to make sure all data is clean and make sure the necessary changes had maked.
- Check the information of the join_data:

  <img  src="./files/images/info.png"></img>

- Remove unnecessary columns
  ```python
  columns_to_remove = ['bucket_start_date', 'bucket_end_date', 'transactions']
  join_df = join_df.drop(columns_to_remove, axis=1)
  ```

- Convert the 'products' column to a string
  ```python
  join_df['products'] = join_df['products'].astype(str).str.replace('[', '').str.replace(']', '')
  ```
  
6. Apply machine learning models and evalute models. I will be using 3 models which are:
   - Random Forest Classifier
   - Logistic Regression
   - Support Vector Machines (SVM)
  ```python
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.linear_model import LogisticRegression
  from sklearn.svm import SVC
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import accuracy_score, precision_score
  
  # One-hot encode the products column
  one_hot_df = pd.get_dummies(join_df['products'].apply(pd.Series).stack()).sum(level=0)
  
  # Combine the one-hot encoded features with other columns
  encoded_df = pd.concat([join_df.drop(['_id', 'products'], axis=1), one_hot_df], axis=1)
  
  # Extract the features and target variable
  X = encoded_df.drop('transaction_count', axis=1)
  y = encoded_df['transaction_count']
  
  # Split the data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  
  # Initialize and train the Random Forest Classifier
  rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
  rf_model.fit(X_train, y_train)
  
  # Make predictions on the testing data
  rf_predictions = rf_model.predict(X_test)
  
  # Compute accuracy and precision for Random Forest Classifier
  rf_accuracy = accuracy_score(y_test, rf_predictions)
  rf_precision = precision_score(y_test, rf_predictions, average='weighted')
  
  # Initialize and train the Logistic Regression model
  lr_model = LogisticRegression(random_state=42)
  lr_model.fit(X_train, y_train)
  
  # Make predictions on the testing data
  lr_predictions = lr_model.predict(X_test)
  
  # Compute accuracy and precision for Logistic Regression model
  lr_accuracy = accuracy_score(y_test, lr_predictions)
  lr_precision = precision_score(y_test, lr_predictions, average='weighted')
  
  # Initialize and train the Support Vector Classifier
  svc_model = SVC(random_state=42)
  svc_model.fit(X_train, y_train)
  
  # Make predictions on the testing data
  svc_predictions = svc_model.predict(X_test)
  
  # Compute accuracy and precision for Support Vector Classifier
  svc_accuracy = accuracy_score(y_test, svc_predictions)
  svc_precision = precision_score(y_test, svc_predictions, average='weighted')
  
  print(f"Random Forest Accuracy: {rf_accuracy}, Precision: {rf_precision}")
  print(f"Logistic Regression Accuracy: {lr_accuracy}, Precision: {lr_precision}")
  print(f"Support Vector Classifier Accuracy: {svc_accuracy}, Precision: {svc_precision}")
  ```

7. Visualize the result to make it easier to analysis.
  ```python
  import matplotlib.pyplot as plt
  
  # Create lists of accuracy and precision values
  accuracy_values = [rf_accuracy, lr_accuracy, svc_accuracy]
  precision_values = [rf_precision, lr_precision, svc_precision]
  models = ['Random Forest', 'Logistic Regression', 'SVM']
  
  # Plot the accuracy values
  plt.figure(figsize=(6, 4))
  plt.bar(models, accuracy_values)
  plt.xlabel('Model')
  plt.ylabel('Accuracy')
  plt.title('Accuracy Comparison of ML Models')
  
  # Add labels to the bars
  for i, value in enumerate(accuracy_values):
      plt.text(i, value, f'{value:.4f}', ha='center', va='bottom')
  
  plt.show()
  
  # Plot the precision values
  plt.figure(figsize=(6, 4))
  plt.bar(models, precision_values)
  plt.xlabel('Model')
  plt.ylabel('Precision')
  plt.title('Precision Comparison of ML Models')
  
  # Add labels to the bars
  for i, value in enumerate(precision_values):
      plt.text(i, value, f'{value:.4f}', ha='center', va='bottom')
  
  plt.show()
  ```
  <img  src="./files/images/ac.png"></img>
  
  <img  src="./files/images/pr.png"></img>
  
### Result

  <img  src="./files/images/result.png"></img>

- Comparing the accuracy scores, the Random Forest model has the highest accuracy (0.0209), followed by the Support Vector Classifier (0.0139), and the Logistic Regression model (0.0105).
- When considering precision, the Random Forest model also has the highest precision (0.0214), followed by the Support Vector Classifier (0.0009), and the Logistic Regression model (0.0007).
- Based on these results, the Random Forest model performs the best among the three models in terms of both accuracy and precision. It provides the highest accuracy and precision scores, indicating better performance in making correct predictions and minimizing false positives.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




