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
   - For the given case study, a suitable machine learning approach would be binary classification using `Logistic Regression Algorithm`. Logistic Regression is commonly use use for classification task when the target variables have 2 classes.
   - For example, predicting whether a customer will use a coupon or not in the future and etc...

   1. Firstly, before do any analysis, visualization or machine learning, we must first clean the data. For example
      
      ```python
        # Connect to MongoDB and retrieve data
          client = pymongo.MongoClient("mongodb+srv://afifhazmiearsyad:abc123456789@noctua.bw9bvzx.mongodb.net/")
          db = client["SupplyStore"]
          collection = db["Sales"]
          data = list(collection.find())
          
          # Convert to dataframe
          df = pd.DataFrame(data)
          df.isnull().sum()
          df.info()
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/dfinfo.jpg">
      
      #### Droping rows with missing values
      
      ```python
         # Handle missing values (drop rows with missing values)
         df.dropna(inplace=True)
         df.info()
      ```

      #### Split the Items columns into seprate column
      
      ```python
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
         
         df.head()
      ```
      <img src="https://github.com/drshahizan/SECP3843/blob/main/submission/AfifHazmie/question4/files/images/jsonnormalize.jpg">
      
   2. 




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




