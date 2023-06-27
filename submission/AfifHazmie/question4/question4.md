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
   - For the given case study, a suitable machine learning approach could be `classification` using a `Decision Tree Algorithm`. Decision trees are versatile and can be used for both prediction and data analysis tasks.
   - The decision tree classifier is a suitable choice due to its interpretability and ability to handle nonlinear relationships.
   - Decision trees provide a clear and intuitive representation of the decision-making process, allowing to easily understand and explain the model's predictions.
   - The resulting tree structure can be visualized, enabling to trace the path of decision-making and gain insights into the factors influencing the predictions.

   1. Firstly, before do any analysis, visualization or machine learning, we must first clean the data. For examples:
      
      ```python
        # Connect to MongoDB and retrieve data
          client = pymongo.MongoClient("mongodb+srv://afifhazmiearsyad:abc123456789@noctua.bw9bvzx.mongodb.net/")
          db = client["SupplyStore"]
          collection = db["Sales"]
          data = list(collection.find())
          
          # Convert to dataframe
          df = pd.DataFrame(data)
          df
          data = df
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/df.jpg">
      
      #### Checking null rows
      
      ```python
         data.isnull().sum()
         data.info()
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/dfinfo.jpg">
      
      #### Droping rows with missing values
      
      ```python
         df.dropna(inplace=True)
      ```
      
      #### Droping rows with missing values
      
      ```python
      # Drop unnecessary columns
      data = data.drop(columns=["_id"])
         
      # Convert saleDate to datetime type
      data["saleDate"] = pd.to_datetime(data["saleDate"])
         
      # Convert couponUsed to boolean type
      data["couponUsed"] = data["couponUsed"].astype(bool)
         
      # Print the cleaned DataFrame
      data.head()
      ```

      #### Split the Items columns into seprate column using `json_normalize`
      
      ```python
      # Convert the 'items' column into separate columns
      df_items = pd.json_normalize(data['items'])
         
      # Rename the columns
      new_columns = {}
      for col in df_items.columns:
          new_columns[col] = f'item{col}'
      df_items.rename(columns=new_columns, inplace=True)
         
      # Merge the item columns with the original DataFrame
      data = pd.concat([data, df_items], axis=1)
         
      # Drop the original 'items' column
      data.drop('items', axis=1, inplace=True)
         
      data.head()
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/jsonnormalize.jpg">
      
   2. Machine Learning Approach `Decision Tree`.
      #### Import the required ML libraries
      ```python
      from sklearn.model_selection import train_test_split
      from sklearn.tree import DecisionTreeClassifier
      from sklearn.metrics import accuracy_score
      ```

      #### Split the data into testing and training sets
      ```python
      X = data[['couponUsed']]
      y = data['purchaseMethod']
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
      ```

      #### Training and Testing the datasets.
      ```python
      # Create a decision tree classifier
      clf = DecisionTreeClassifier()
      
      # Train the classifier on the training data
      clf.fit(X_train, y_train)
      
      # Make predictions on the testing data
      y_pred = clf.predict(X_test)
      
      # Evaluate the accuracy of the model
      accuracy = accuracy_score(y_test, y_pred)
      print("Accuracy:", accuracy)
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/accuracy.jpg">

      #### Visualize the decision tree classifier, you can use the `plot_tree` function from the `sklearn.tree` module.
      ```python
      import matplotlib.pyplot as plt
      from sklearn import tree
      
      # Visualize the decision tree
      fig, ax = plt.subplots(figsize=(12, 12))
      tree.plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True, ax=ax)
      
      plt.show()
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/dcplot.jpg">



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




