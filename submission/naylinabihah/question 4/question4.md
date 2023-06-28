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
#### Dataset: Companies

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

#### Step 2: Study the Dataset Content for Data Cleaning Purposes

- Try finding the possible information that needed like find the number of columns, the datatype and number of missing rows for each column. Below are the lists of example code that can be use to obtain these information:

```
com.info()
```

```
com.columns
```

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

#### Step
#### Step
#### Step
#### Step
#### Step

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




