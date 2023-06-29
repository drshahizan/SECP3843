<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Qaisara binti Rohzan
#### Matric No.: A20EC0133
#### Dataset: 04 - Companies

## Question 4 
Machine learning is a branch of computer science that enables computers to learn without having to be explicitly programmed. Machine learning is classified into two types: supervised learning and unsupervised learning. In this question, we will be performing appropriate machine learning approach or algorithm by using Python. I will be including snippets of my Python code from my Google Colab project file here.

**Uploading JSON Dataset**

Upload the **Companies** dataset into Google Drive

```bash
# Pull dataset from google drive
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
```

```bash
link = 'https://drive.google.com/file/d/1Bdvh9UyJrPWyNyD0zG_7BEolr-NLh0Pe/view?usp=sharing'
# to get the id part of the file
id = link.split("/")[-2]

downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('companies.json')
```
<br>

**Read JSON Dataset into DataFrame**

```bash
import pandas as pd
import numpy as np
```
```bash
%%time
df = pd.read_json('companies.json', lines=True)
df.head()
```
```bash
df
```
```bash
df.info()
```
<br>

**Exploratory Data Analysis**
```bash
import numpy as np

# Display  Number of Unique Companies
unique_company = df['name'].nunique()
unique_company
```
Total Number of Unique Companies: **9254**

**Drop Unwanted Columns**

The JSON Dataset columns contains a handful of empty arrays, it will only be best if we dropped the,
> Columns: funding rounds, investments, acquisitions, acquistions, offices, provides, milestones, video embeds, partners, deadpooled_url, ipo
```bash
drop_column = ['funding_rounds', 'investments', 'acquisition', 'acquisitions', 'offices', 'milestones', 'video_embeds', 'partners', 'deadpooled_url', 'providerships', 'ipo']

df.drop(drop_column, axis=1, inplace=True)
```

**Feature Extraction**
```bash
df['total_competitions] = df['competitions].apply(len)
new_fields = df[['name', 'category_code', 'number_of_employees', 'total_competitions']]
new_fields
```

```bash
new_fields = new_fields.dropna()
new_fields
```
Shape before: **(9500, 4)**
Shape after: **(4416, 4)**

**Machine Learning**

Install necessary libraries
```bash
from sklearn.model_selection import train_test_split
 from sklearn.linear_model import LinearRegression
 from sklearn.metrics import mean_squared_error
```

As usual, for machine learning we will have to split the data, in which 70% is trained and 30% is tested
```bash
X = new_fields.drop('total_money_raised', axis=1)
y = new_fields['total_money_raised']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```bash
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




