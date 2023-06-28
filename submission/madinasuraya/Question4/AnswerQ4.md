<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

## Special Topic Data Engineering (SECP3843): Alternative Assessment ©️

#### Name: MADINA SURAYA BINTI ZHARIN
#### Matric No.: A20EC0203
#### Dataset: companies.json

### Question 4 

Machine learning approach that I choose is **supervised learning** where I perform a **linear regression** to make prediction on a set of labeled data. For this dataset about companies listed in Crunchbase website, I wanted to make prediction on the total money raised by the companies with the number of employees and number of competitors that they have. Here are few steps that I used using python language:

#### Libraries Installation
```
!pip install pymongo
import pymongo
import pandas as pd
import numpy as np
```
#### Import database from MongoDB
```
client = pymongo.MongoClient("mongodb+srv://user1:___________________@cluster0.evngzba.mongodb.net/test")
db = client["db_crunchbase"]
collection = db["companies"]
data = list(collection.find())
```
#### Create dataframe and understand the data
```
df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
df.head(5)
```
<p align='center'>
<img width="885" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/1b012266-cb7f-4a62-87e6-2622ed949e23">
</p>

```
df.info()
```
<p align='center'>
<img width="161" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/36005e4a-330f-4a2a-a897-0150b41c7c91">
</p>

#### Feature Extraction
```
selected_fields = df[['total_money_raised', 'number_of_employees','competitions']]
selected_fields.head(5)
```
<p align='center'>
<img width="359" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/a79b678a-0373-4a69-b317-03016597c415">
</p>

#### Data Cleaning
1. Get the amount of item in the array of the competitions fields.
    ```
    df['competitions'] = df['competitions'].apply(len)
    selected_fields = df[['total_money_raised',
    'number_of_employees','competitions']]
    selected_fields.head(5)
    ```
    <p align='center'>
      <img width="254" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/601f8061-f119-4937-b18d-e9fef6884cbb">
    </p>
    
2. Drop records that contain null.
   ```
   selected_fields = selected_fields.dropna()
   selected_fields.head(5)
   ```
    Shape before: **(9500, 3)** <br>
    Shape after: **(4448, 3)**

  <p align='center'>
    <img width="250" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/d3c40a21-68ae-47f0-9f2b-cd6308ffb26c">
    </p>
    
3. Convert the dataype to numerical.
   ```
    def convert_money(value):
    try:
        if isinstance(value, float):
            return value
        elif 'B' in value:
            return float(value.replace('B', '').replace('$', '').replace('€', '')) * 1000000000
        elif 'M' in value:
            return float(value.replace('M', '').replace('$', '').replace('€', '')) * 1000000
        elif 'k' in value:
            return float(value.replace('k', '').replace('$', '').replace('€', '')) * 1000
        else:
            return float(value.replace('$', '').replace('€', ''))
    except ValueError:
        return 0.0  # Assign a default value of 0.0 for invalid or unknown values

   selected_fields['total_money_raised'] = selected_fields['total_money_raised'].apply(convert_money).astype(float)
   selected_fields['number_of_employees'] = selected_fields['number_of_employees'].astype(int)
   selected_fields['competitions'] = selected_fields['competitions'].astype(int)
   selected_fields.head(5)
    ```
    <p align='center'>
    <img width="251" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/7d3cbac3-931a-4a57-a16e-8302201f10e7">
    </p>

4. Get information about the data.
   ```
   selected_fields.info()
   ```
   <p align='center'>
    <img width="228" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/4620f32a-26cb-468a-bdcb-4fdcb7dd259d">
    </p>

#### Machine Learning
1. Import machine learning libraries.
   ```
   from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    ```
2. Devide the data into train and test. Here, we train 80% of the data and test 20%
   ```
   X = selected_fields.drop('total_money_raised', axis=1)
   y = selected_fields['total_money_raised']
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   ```
3. Perform linear regression.
    ```
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    ```
  4. Create graph to see the actual and predicted total money raised.
      ```
      import matplotlib.pyplot as plt
      plt.scatter(y_test, y_pred, color='blue', label='Actual vs. Predicted')
      plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', linewidth=2, label='Regression Line')
      
      # Add labels and title
      plt.xlabel('Actual Total Money Raised')
      plt.ylabel('Predicted Total Money Raised')
      plt.title('Linear Regression - Actual vs. Predicted')
      
      # Add legend
      plt.legend()
      
      # Show the plot
      plt.show()
      ```
      
      <p align='center'>
        <img width="319" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/bd0c3e5d-468a-4914-9ecd-2fe89c185a2d">
      </p>
5. Calculate **Mean Squared Error**, **Root Mean Squared Error**, and **R-squared**.
    ```
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r_squared = model.score(X_test, y_test)
    print("Mean Squared Error:", mse)
    print("Root Mean Squared Error:", rmse)
    print("R-squared:", r_squared)
    ```
    <p align='center'>
    <img width="202" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/e7e5f162-0a11-4e92-aa15-68b10aa92a17">
    </p>

#### Conclusions
Based on the scatter plot of the actual vs predicted total money raised, it is mostly concentrated in the range of 0 to 1. This means that the regression model is not accurately predicting the total money raised for higher values. It is proven that the input features (number_of_employees and competitions) and the target variable (total_money_raised) is not linear as the regression line does not closely align with the scatter plot.
The metrics that we get evaluate the performance of the regression model.
- **Means Squared Error (MSE)**: MSE measures the average squared difference between the predicted and actual values. Since the MSE is higher, it shows that the performance of the model is worse.
- **Root Mean Squared Error (RMSE)**: RMSE is the square root of the MSE and provides a more interpretable measure of the average prediction error in the original scale of the target variable. Same as MSE, higher MSE indicates worse performance.
- **R-squared (R^2)**: R-squared represents the proportion of the variance in the target variable (total_money_raised) that is explained by the regression model. A negative R-squared value suggests that the model's performance is worse.

Based on the metrics, it shows that the linear regression model is not performing well in predicting total money raised. High MSE and RMSE indicate a large prediction error and the negative R-squared suggests that the model does not capture the underlying relationship between the input features and the target variable.

Lastly, we can see that the dataset itself has limitations. There are too many fields with null values which is almost half of the records. Thus, performing feature extraction might be the best as we are not involving the data that are much likely can’t be predicted.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
