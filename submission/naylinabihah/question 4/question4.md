<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Nayli Nabihah Binti Jasni
#### Matric No.: A20EC0105
#### Dataset: [Companies](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/companies.json)

## Question 4

There are many ways and algorithms that can be chosen when it comes to machine learning. Either choose from unsupervised learning or supervised learning algorithms, all the algorithms has its own purposes and uses that are versatile for various range of datasets. 

The dataset given is about the information of companies that were retrieved from Cruchbase, a company that provides businees information about companies either public or private. This dataset contains 42 columns which most of it is in array form which can be challenging when doing the machine learning. I had chosen to use the `Regression Analysis` that focuses on the total money raised by the companies against the number of competitions they had. `Regression Analysis` is a common supervised learning implemented to find the realationship between two variables that  one act as target variable (dependant) and the other one as predictor variable (independant). Below are the steps I implemented when doing the `Regression Analysis`.

#### Step 1: Import the JSON File into Google Colab
Since earlier on I had already insert the JSON file in MongoDB, now I can retrieve the JSON file using python through a library called `pymongo`.

- Install 'pymongo' library, then import it
  ```
  !pip install pymongo

  import pymongo
  ```

- Connect the database with the python file by declaring the connection string (connection string can be copied in MongoDB Compass)
  ```
  client=pymongo.MongoClient("mongodb+srv://naylinabihah:asdfwe23@cluster0.84cybka.mongodb.net/")
  ```

- Get the Connection to the Collection where the JSON file is stored. I stored it in `stde` database under `aa` collection.
```
db = client ["stde"]
collection = db ["aa"]
comp = list(collection.find())
```

- After successful, now the JSON file can be imported into dataframe using pandas to make it easier when doing machine learning.
```
import pandas as pd

com = pd.DataFrame(comp)

com
```

![s1](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_1.png)

#### Step 2: Study the Dataset Content for Data Cleaning Purposes

- Try finding the possible information that needed like find the number of columns, the datatype and number of missing rows for each column. Below are the lists of example code that can be use to obtain these information:

```
com.info()
```

```
com.columns
```

![s2](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_2.png)

#### Step 3: Remove Some Unwanted Columns
Since this dataset is full of unused arrays, it will be the best if some columns can be dropped.
List of dropped columns:
- `funding_rounds`
- `investments`
- `acquisition`
- `acquisitions`
- `offices`
- `providers`
- `milestones`
- `video_embeds`
- `partners`
- `deadpooled_url`
- `ipo`

Using this code to drop the columns:
```
cols_drop = ['funding_rounds', 'investments', 'acquisition', 'acquisitions', 'offices', 'milestones', 'video_embeds', 'partners', 'deadpooled_url', 'providerships', 'ipo']

com.drop(cols_drop, axis=1, inplace=True)
```

![s3](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_3.png)

#### Step 4: Manipulate the Column
The dataset given does not contain a lot of numeric data type, so, I need to create a new column to count the selected array that has relationship with the vriable I want to measure in the regression. Since I want to do the regression between the number of competitions of a company and the money raised by them, I have manipulated the competitions column by creating a new column named as `competitions_count`. This column will store the count of object in the competitions array for each row. Tod do so, this is the code block I used:

```
com['competitions_count'] = com['competitions'].apply(len)
```

![s4](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_4.png)

#### Step 5: Reformat the Column (total_money_raised)
This column is stored as an array object. From the column the example from one of the row is valued as '$14.9M' and makes it not calculable. To change these, I have created a new column named `money_raised` that only stores the value from the column `total_money_raised`.
Below are the list of dictionary set in the code to change the necessary unusable characters.

- `$` or `€` changed to 1
- `M` is set as 1000000
- `B` is set as 1000000000
- `k` as 1000

Code used to change the characters:

```
import numpy as np


conversion_dict = {'$': 1, '€': 1, 'M': 1000000, 'B': 1000000000, 'k': 1000}

def convert_to_numeric(value):
    try:
        value = value.strip()
        if value == '$0':
            return 0  # Return 0 if value is '$0'
        currency_symbol = value[0]
        number = value[1:-1]
        suffix = value[-1]
        
        return float(number) * conversion_dict[currency_symbol] * conversion_dict[suffix]
    except (ValueError, AttributeError, KeyError):
        return np.nan 

com['money_raised'] = com['total_money_raised'].apply(convert_to_numeric)

com.head(15)
```
![s5](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_5.png)

![conv](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_5_res.png)

#### Step 6: Incorporate the selected machine learning algorithm (Linear Regression/Random Forest Regression/Support Vector Regression)

- Linear Regression
  ![lr](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_6a.png)
- Random Forest Regression
  ![rfr](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_6b.png)
- Support Vector Regression
  ![svr](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_6c.png)
  
#### Step 7: Plot Graph based on the Result Obtained

I used Seaborn to get better visualization

- Linear Regression
  ![lr_plot](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_7a.png)
- Random Forest Regression
  ![rfr_plot](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_7b.png)
- Support Vector Regression
  ![svr_plot](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/images/step_7c.png)

Based on the results obtained from this analysis, the most reliable regression algorithm should be used in this dataset is by implementing Random Forest Regression Algorithm.

#### Step 8: See the Code File

To access the code file, please click [here](https://github.com/drshahizan/SECP3843/blob/main/submission/naylinabihah/question%204/files/source-code/AA_STDE_by_Nayli_Nabihah.ipynb)

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




