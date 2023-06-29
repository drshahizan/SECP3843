<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Muhammad Naquib Bin Zakaria
#### Matric No.: A20BE0161
#### Dataset: 03 - Movie

## Question 5 (a)
Data preprocessing is one of the approach that can be used to deal with large volumes of JSON data. When working with massive amounts of JSON data, data preprocessing becomes even more crucial in order to optimise performance and efficiency. Data preprocessing refers to the steps taken to clean, transform, and prepare data for visualization.
So, I will use Google Colab to do the data processing task using python language. So here is the steps of data preprocessing.
1. Upload the dataset into Google Colab.
  - ![Screenshot 2023-06-28 084308](https://github.com/drshahizan/SECP3843/assets/92329710/a56493b7-2396-4650-ae32-352f5a2283a6)
  - In this case, dataset `movies.json` has been uploaded into Google Colab directory.
2. Import library.
   - In this case, import `pandas` library and assign it as `pd`.
   - ```
     import pandas as pd
     ```
3. Read the dataset.
   - ```
     dataset_path = 'movies.json'
     data = pd.read_json(dataset_path, lines=True)
     ```
   - Next, view the top 10 of the dataset.
   - ```
     data.head(10)
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/fb0d2910-8007-40ea-a797-bb32a89f535e)
   - View the data info:
   - ```
     data.info()
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/ad9007e9-9eba-4f07-85c7-c197c73467e1)
   - View the data columns:
   - ```
     data.columns
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/39d14dee-c02b-49b0-bef6-7cb2af0146b2)
4. Choose the attributes/columns.
   - ```
     movies = data[['genres', 'runtime', 'cast',
       'title', 'countries', 'directors', 'rated',
       'awards', 'year', 'imdb', 'type',
       'languages', 'writers']]
     ```
   - Next, view the `movies` top 10 data:
   - ```
     movies.head(10)
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/5f2812e6-532d-4c0c-b7bf-a78e4f087a56)
   - Next, view the `movies` info:
   - ```
     movies.info()
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/8f323091-f518-4ba6-9fbc-cf1445b33d99)
   - Then, identify the number of null values in each columns:
   - ```
     movies.isnull().sum()
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/97760027-4e04-4646-8a6b-b6832e001d06)
5. Remove null values.
   - ```
     movies = movies.dropna()
     ```
   - Next, view the `movies` info:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/86f2fe81-ae3c-495d-9d94-b82a193935fe)
- So now, the dataset has been cleaned and ready for further analysis or visualizations.

## Question 5 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




