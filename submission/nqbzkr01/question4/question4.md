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

## Question 4

- The machine learning approach used in this project is `Content-Based Filtering`.
- `Content-Based Filtering` is a machine learning approach used in recommendation system that focuses on the characteristics and features of items (in this case, `movies`) to make recommendations.
- It analyzes the content or attributes of movies to identify similaritites and make personalized recommnedations to users.
- In this case, `movies.json` dataset will be used to create the movie recommendation system and will be focused on some attributes that available in the dataset which is `title`, `plot` and `genres`.
- So here are the steps on how to implement the machine learning approach:

1. Upload the dataset.
   - `Google Colab` will be used as platform to implement the machine learning process using python.
   - Then upload the dataset which is `movies.json` into `Google Colab Files`.
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/485ad071-2185-482f-8721-a3eac29a69ca)

2. Import `pandas` library.
   - Pandas is a powerful open-source data manipulation and analysis library for Python. It provides data structures and functions to efficiently work with structured data, such as tables or spreadsheets, and perform various data operations.
   - ```
     import pandas as pd
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/b63c76ba-5f02-4ade-96e8-707b144e62cd)
3. Read the json file.
   - Read the `movies.json` that you have been uploaded into Google Colab file.
   - ```
     dataset_path = 'movies.json'
     data = pd.read_json(dataset_path, lines=True)
     ```
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/d0da04fb-4356-422b-88c8-0908baf7037f)
4. Data Preprocessing.
   - Before start the machine learning process, the dataset need to be cleaned to get a suitable format for machine learning tasks.
   - Here is the steps of data pre-processing:
   - First, the dataset will be reduced in order to save processing time and memory.
   - ```
     random_seed = 42
     data = data.sample(n=10000, random_state=random_seed)
     ```
   - Originally, the dataset `movies.json` has 25,000 rows of data.
   - So, it has been reduced into 10,000 rows of data so that we can have an effective machine learning process.
   - Next, we analyze the columns that available in the dataset.
   - ```
     data.columns
     ```
   - It gives the result:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/8d4db5dc-19e9-4a21-863a-4d976742a832)
   - Then, choose the attribute that want to be used for machine learning process.
   - ```
     movies = data[['_id', 'plot', 'genres', 'title']]
     ```
   - The result:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/a3786fd9-10d9-4395-9f5a-4a114ba015bb)
   - Next, create new column which is `tags` that is the combination of `plot` and `genres` attributes.
   - ```
     movies['genres'] = movies['genres'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')
     movies['tags']=movies['plot'] + ' ' + movies['genres']
     ```
   - Here is the result:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/98d52037-fdf7-4d73-813b-a1abee3736b5)
   - Then, create new variable named `new _data` and assign it with `movies` and drop `plot` and `genres`.
   - ```
     new_data = movies.drop(columns=['plot', 'genres'])
     ```
   - Here is the result:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/66a367f9-a4ee-464c-ad5f-9b479283ecf8)
   -So now we have all the variables that can be used for machine learning process.
5. Machine Learning Process.
   - First of all, import the `CountVectorizer` class from `sklearn.feature_extraction.text` module library.
   - The `CountVectorizer` class is used for converting a collection of text documents into a matrix of token counts.
   - ```
     from sklearn.feature_extraction.text import CountVectorizer
     ```
   - Next, set the `max_features` and the `stop_words` in CountVectorizer class.
   - ```
     cv = CountVectorizer(max_features=10000, stop_words='english')
     ```
   - `max_features` is the parameter that controls the maximum number of features that will be extracted from the text data.
   - `stop_words` is the parameter that will ignore the stop words in English words such as `the`, `and`, `is` etc. The `CountVectorizer` will remove the stop words from text data before creating the matrix of token counts.
   - ```
     vector=cv.fit_transform(new_data['title'].values.astype('U')).toarray()
     ```
   - The code converts the text data from the `title` column in the `new_data` dataset into a matrix of token counts represented as a dense NumPy array.
   - ```
     vector.shape
     ```
   - The result:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/05a53692-df88-4a1d-989d-08992e7970b8)
   - `vector.shape` represents the transformed data in the form of a mtrix of token counts.
   - The first value which is `10,000` represent the number of documents, while the second value represnts the number of uniqe words or tokens in the vocabulary derived from the text data.
   - Next, import the `cosine_similarity` from `sklearn.metrics.pairwise` library.
   - ```
     from sklearn.metrics.pairwise import cosine_similarity
     ```
   - `cosine similarity` provides a method to compute the cosine similarity between two vectors or arrays, which is commonly used to measure similarity or distance between data points.
   - ```
     similarity = cosine_similarity(vector)
     ```
   - The result:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/b9c2e5a5-df69-4060-b3d6-a724d488455e)
   - Here can see that `cosine_similarity` generates a similarity matrix.
   - ```
     def recommend(movies):
     index = new_data[new_data['title']==movies].index[0]
     distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
     for i in distance[0:5]:
       print(new_data.iloc[i[0]].title)
     ```
   - The `recommend` function takes a movie title as input, retrieves its index in the `new_data` DataFrame, computes the distances between the specified movie and all other movies using cosine similarity, sorts them in descending order, and prints the titles of the top 5 recommended movies based on similarity.
   - Lastly, test the `recommend` function by inserting `movie title`.
   - ```
     recommend("Barton Fink")
     ```
   - Here is the result:
   - ![image](https://github.com/drshahizan/SECP3843/assets/92329710/3303229b-e3a1-47bb-8b87-a47ccd77603f)












## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




