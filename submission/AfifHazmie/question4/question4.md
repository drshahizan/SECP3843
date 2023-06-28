<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Afif Hazmie Arsyad Bin Agus
#### Matric No.: A20EC0176
#### Dataset: Supply Store

## Question 4
   - The machine learning approach used in this project is `logistic regression`.
   - Logistic regression is a `classification algorithm` used to predict the probability of a binary outcome based on one or more independent variables.
   - It is commonly used when the dependent variable is `categorical`.
   - `Logistic regression` is a popular and interpretable algorithm for binary classification tasks.
   - However, it assumes a linear relationship between the independent variables and the log-odds of the outcome.

   1. Firstly, before do any analysis, visualization or machine learning, we must first clean the data. For examples:

      #### Retrieve & Convert data into dataframe
      ```python
      # Connect to MongoDB and retrieve data
      client = pymongo.MongoClient("mongodb+srv://afifhazmiearsyad:abc123456789@noctua.bw9bvzx.mongodb.net/")
      db = client["SupplyStore"]
      collection = db["Sales"]
      data = list(collection.find())
      
      # Convert to dataframe
      df1 = pd.DataFrame(data)
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/df1.jpg">

      #### Splitting the Customer data from dictionary to columns
      ```python
      import numpy as np

      # Splitting Customer Data
      df1['gender'] = df1['customer'].apply(lambda x: x['gender'] if pd.notnull(x) else np.nan)
      df1['age'] = df1['customer'].apply(lambda x: x['age'] if pd.notnull(x) else np.nan)
      df1['email'] = df1['customer'].apply(lambda x: x['email'] if pd.notnull(x) else np.nan)
      df1['satisfaction'] = df1['customer'].apply(lambda x: x['satisfaction'] if pd.notnull(x) else np.nan)
      
      # Drop the original "customer" column
      df1.drop('customer', axis=1, inplace=True)
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/customersplit.jpg">

      #### Splitting the Items data from array to columns
      ```python
      df1['item_names'] = df1['items'].apply(lambda x: [item['name'] for item in x] if isinstance(x, list) else [])
      df1['item_tags'] = df1['items'].apply(lambda x: [item['tags'] for item in x] if isinstance(x, list) else [])
      df1['item_prices'] = df1['items'].apply(lambda x: [item['price'] for item in x] if isinstance(x, list) else [])
      df1['item_quantities'] = df1['items'].apply(lambda x: [item['quantity'] for item in x] if isinstance(x, list) else [])
      
      # Drop the original "items" column
      df1.drop('items', axis=1, inplace=True)
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/itemsplit.jpg">

      #### Clean the splited items column 
      - Clean the items_column by `removing the array bracket`, `sum up value` and `display unique value for item_names and item_tags`.
      ```python
      df1['item_names'] = df1['items'].apply(lambda x: [item['name'] for item in x] if isinstance(x, list) else [])
      df1['item_tags'] = df1['items'].apply(lambda x: [item['tags'] for item in x] if isinstance(x, list) else [])
      df1['item_prices'] = df1['items'].apply(lambda x: [item['price'] for item in x] if isinstance(x, list) else [])
      df1['item_quantities'] = df1['items'].apply(lambda x: [item['quantity'] for item in x] if isinstance(x, list) else [])
      
      # Drop the original "items" column
      df1.drop('items', axis=1, inplace=True)
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/itemclean.jpg">

      #### Checking Null value.
      ```python
      df1.isnull().sum()
      df1.info()
      ```

      #### Drop row contain null value.
      ```python
      df1.dropna(inplace=True)
      df1.info()
      ```

      #### Drop useless columns and convert to suitable datatype.
      ```python
      df1.dropna(inplace=True)
      df1.info()

      # Drop unnecessary columns
      df1 = df1.drop(columns=["_id"])
      
      # Convert saleDate to datetime type
      df1["saleDate"] = pd.to_datetime(df1["saleDate"])
      
      # Convert couponUsed to boolean type
      df1["couponUsed"] = df1["couponUsed"].astype(bool)
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/cleandata.jpg">
      
   2. Machine Learning Approach `Logistic Regression`.
      #### Import the required ML libraries
      ```python
      from sklearn.model_selection import train_test_split
      from sklearn.linear_model import LogisticRegression
      from sklearn.metrics import accuracy_score
      ```

      #### Split the data into testing and training
      ```python
      # Splitting the data into features (X) and target variable (y)
      X = df1[['age', 'gender', 'purchaseMethod']]
      y = df1['satisfaction']
      
      # Convert categorical variables to numerical representation using one-hot encoding
      X_encoded = pd.get_dummies(X)
      
      # Splitting the data into training and testing sets
      X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
      ```

      #### Training and Testing the datasets.
      ```python
      # Initialize and train the logistic regression model
      model = LogisticRegression()
      model.fit(X_train, y_train)
      
      # Make predictions on the test set
      y_pred = model.predict(X_test)
      
      # Evaluate the model's accuracy
      accuracy = accuracy_score(y_test, y_pred)
      print("Accuracy:", accuracy)
      ```
      <p align="center">
         <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/Laccuracy.jpg">
      </p>
      

      #### Visualize the performance of the logistic regression model, use the `bar chart` function from the `seaborn` library.
      ```python
      import matplotlib.pyplot as plt
      import seaborn as sns
      from sklearn.metrics import classification_report
      
      # Create a classification report
      report = classification_report(y_test, y_pred, output_dict=True)
      
      # Extract the accuracy and other metrics from the report
      accuracy = report['accuracy']
      precision = report['weighted avg']['precision']
      recall = report['weighted avg']['recall']
      f1_score = report['weighted avg']['f1-score']
      
      # Create a bar plot
      plt.figure(figsize=(8, 6))
      metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
      values = [accuracy, precision, recall, f1_score]
      sns.barplot(x=values, y=metrics, palette='Blues')
      plt.title("Model Performance")
      plt.xlabel("Value")
      plt.ylabel("Metric")
      plt.show()
      ```
      <p align="center">
         <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/barchart.jpg">
      </p>
      



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




