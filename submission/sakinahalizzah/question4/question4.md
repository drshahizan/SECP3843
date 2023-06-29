<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Sakinah Al'izzah Binti Mohd Asri
#### Matric No.: A20EC0142
#### Dataset: [Analytics](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 4 
Based on the Analytics dataset, I utilize two machine learning techniques: the Random Forest Classifier and Linear Regression. Through the Random Forest Classifier, I predict the availability of various products for each account, using input features like the account ID and limit. Meanwhile, Linear Regression allows me to forecast the number of accounts a customer possesses, based on age. I executed the machine learning code through Google Colab and have provided the code file [Question4_ML.ipynb](https://github.com/drshahizan/SECP3843/blob/main/submission/sakinahalizzah/question4/files/source-code/Question4_ML.ipynb).

### Step 1: Install the required libraries

Python has several libraries that can help with data manipulation, analysis, and modeling. Some of these include pymongo, pandas, numpy, scikit-learn, scikit-multilearn, statsmodels, and matplotlib. These libraries offer a range of tools for interacting with MongoDB databases, working with structured data, supporting scientific computing, implementing machine learning algorithms, and creating visualizations.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/60e600ca-8bf8-4c79-8873-befcc31e86c3" />

### Step 2: Import the required libraries

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/59e31222-8792-4463-88f1-54eff035b712" />

### Step 2: Load Data from MongoDB

The machine learning applied to dataset accounts and customers.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/4dcd97a9-2467-4838-b763-9a029f44a56a" />

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/94a1ba6e-db9e-4e03-88bb-114008b2aa57" />

### Step 3: Create Random Forest Classifier

The Random Forest Classifier is to predict the presence or absence of different products for each account using the accounts dataset. the code and the output are as below: 

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/080d7ebe-cb32-48fd-9abf-1cb49b1c59a2" />

The results display the labeled predictions for every account and their respective products. Each column denotes a distinct product, with the values indicating whether the product is expected to be present (1) or not (0) for each account.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/4fcd38c6-16a8-498e-836b-78f5ee9ba462" />

The output shows the number of accounts in which each product is predicted to be present. Based on my analysis, it appears that all customers have an account for investment stock products. However, there are 161 customers who also have accounts for Brokerage and Currency Service products. Commodity products have the least amount of subscribers at 142 customers. Interestingly, half of the registered customers have subscribed for Derivatives products. Lastly, 142 customers have subscribed to investment fund accounts.

### Step 4: Linear Regression

Linear Regression is to predict the number of accounts a customer has based on their age. Firstly, convert birthdate to age and count the total accounts for each customer.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/5baa39d2-32cc-4fb4-b088-b85a7fb5d5e8" />

Display the total number of customers with 0 to 6 total accounts based on age.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/6878c5bb-d05e-4ecf-87e6-7e5320b1451e" />

Then, make a stacked bar chart

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/f17f27fb-b1b3-41b4-90bb-556f1ce715ba" />

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/25b979d3-e5ea-40ef-a540-b70e1d3eeda9" />

After that, find the customer with the highest and lowest total accounts based on age.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/8d4a5ec0-1067-42fd-8969-29f2026fa7ef" />

The output indicates that both the highest and lowest total accounts groups consist of 83 customers each. The average age of customers with the highest total accounts is 39 years, while the average age of customers with the lowest total accounts is approximately 41.22 years.

Finally, predict the number of accounts based on the age of customers using linear regression. The data split into training and testing sets using a test size of 20% and a random state of 42 for reproducibility. It trains a linear regression model using the training data and makes predictions on the test set.

<img src="https://github.com/drshahizan/SECP3843/assets/99240177/2bba43d7-ee3a-42e3-aabf-dba47b52847a" />

The Mean Squared Error value of 2.4954 indicates that, on average, the squared difference between the predicted number of accounts and the actual number of accounts is approximately 2.4954. A lower Mean Squared Error value indicates better model performance, as it represents a smaller average squared difference between the predicted and actual values.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



