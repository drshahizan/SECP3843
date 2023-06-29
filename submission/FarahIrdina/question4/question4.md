<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: FARAH IRDINA BINTI AHMAD BAHARUDIN
#### Matric No.: A20EC0035
#### Dataset: AIRBNB LISTINGS DATASET

## Question 4

For machine learning, I will be using Linear Regression to predict the property price when the users insert the input of property type, room type, number of bedrooms and amenities. The steps to make this machine learning successful have been written below.

### Import libraries

First, import all the libraries that will be used to perform the machine learning.

```
!pip install pymongo
!pip install pandas
import pymongo
import pandas as pd
from bson.decimal128 import Decimal128
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
```

### Data Preparation

Next, for data preparation, import the JSON dataset from MongoDB by using pymongo. Then, 
make the JSON dataset as dataframe using pandas.

```
client = pymongo.MongoClient("mongodb+srv://arasayooo:Irdin%407995335310@newcluster.rdxcnj3.mongodb.net/")
db = client["airbnb"]
collection = db["listings"]
data = list(collection.find())

def decimal_to_str(value):
    if isinstance(value, Decimal128):
        return str(value)
    return value

data = [decimal_to_str(item) for item in data]

# Convert MongoDB data to a pandas DataFrame
df = pd.json_normalize(data)
```

### Data Preprocessing

Clean the dataset that we want to use. For this example, I will be cleaning accommodates, bedrooms, beds, number of reviews, guests included, availability and score rating only. I will drop the rows if there are any 0 value inside the columns. Then, split the dataset into X and Y variables.

```
# Convert Decimal128 values to float
numeric_cols = ['accommodates', 'bedrooms', 'beds', 'number_of_reviews', 'guests_included', 'availability.availability_365', 'review_scores.review_scores_rating']
df = df.dropna(subset=numeric_cols, how='any')
df = df[(df[numeric_cols] != 0).all(axis=1)]
for col in numeric_cols:
    df[col] = df[col].apply(lambda x: float(str(x)))

# Define categorical and numeric columns
categorical_cols = ['property_type', 'room_type', 'bed_type', 'cancellation_policy']

# Create a ColumnTransformer to apply one-hot encoding to categorical columns
preprocessor = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), categorical_cols)],
    remainder='passthrough'
)

# Apply the preprocessing steps and split the data into features (X) and target (y) variables
X = df[categorical_cols + numeric_cols]
y = df['price']

X = preprocessor.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Feature Engineering

Then, I will select the features that will affect the property price. For this example, I will use property type, room type, bedrooms and amenities. 

```
# Select relevant features
selected_features = ['property_type', 'room_type', 'bedrooms', 'amenities']

# Create a new DataFrame with selected features
df_selected = df[selected_features].copy()

# Convert list columns to string representations
df_selected['amenities'] = df_selected['amenities'].apply(','.join)

# Perform any necessary transformations on the features
# Example: Extracting the number of amenities from the amenities column
df_selected['num_amenities'] = df_selected['amenities'].apply(lambda x: len(x.split(',')))

# Perform scaling on numeric features using StandardScaler
numeric_features = ['bedrooms', 'num_amenities']
scaler = StandardScaler()
df_selected[numeric_features] = scaler.fit_transform(df_selected[numeric_features])

# Encode categorical features using one-hot encoding
df_encoded = pd.get_dummies(df_selected, drop_first=True)

# Concatenate encoded categorical features with scaled numeric features
X = pd.concat([df_encoded, df[numeric_cols]], axis=1)

# Assign target variable
y = df['price']
```

### Model Training and Evaluation

Then, split the data into training and testing sets. I chose Linear Regression as my algorithm to predict property price based on the entities that will be inserted by the users. Lastly, it will print the mean squared error and R-squared error.

```
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Handle missing values in the features
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Convert Decimal128 values to float
X_train_imputed = X_train_imputed.astype(float)
y_train = y_train.apply(lambda x: float(str(x)))

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the imputed training set
model.fit(X_train_imputed, y_train)

# Make predictions on the imputed testing set
y_pred = model.predict(X_test_imputed)

# Convert 'y_test' values to string and then to float
y_test = y_test.astype(str).apply(lambda x: float(x))

# Convert 'y_pred' values to float
y_pred = y_pred.astype(float)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared Score:", r2)
```

### Predictions

Finally, we can use the trained model to make predictions of property prices. This code will let users enter the input of Property Type, Room Type, Number of Bedrooms and Amenities. Then it will predict the predicted property price based on the inputs.

```
import numpy as np

# Ask users to input property features
property_type = input("Property Type: ")
room_type = input("Room Type: ")
bedrooms = float(input("Number of Bedrooms: "))
amenities = input("Amenities (comma-separated): ")
num_amenities = len(amenities.split(','))

# Create a DataFrame with the user input
input_data = pd.DataFrame({
    'property_type': [property_type],
    'room_type': [room_type],
    'bedrooms': [bedrooms],
    'amenities': [amenities],
    'num_amenities': [num_amenities]
})

# Perform necessary transformations on the input data
input_data['amenities'] = input_data['amenities'].apply(','.join)
input_data[numeric_features] = scaler.transform(input_data[numeric_features])
input_data_encoded = pd.get_dummies(input_data, drop_first=True)

# Align the input data with the training data columns
input_data_aligned = input_data_encoded.reindex(columns=X.columns, fill_value=0)

# Make the prediction
predicted_price = model.predict(input_data_aligned.values.reshape(1, -1))

# Print the predicted price
print("Predicted Price: $", np.round(abs(predicted_price[0]), 2))
```

### Result

Run the code [here](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question4/files/code/Question_4.ipynb) and insert the values that you want to predict. Then, it will display the predicted price.

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question4/files/images/prediction.png)

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




