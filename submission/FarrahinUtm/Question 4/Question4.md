![Screenshot (283)](https://github.com/drshahizan/SECP3843/assets/121208097/116c493d-98b9-4bb4-91a6-9f216d2548c7)<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURFARRAHIN BINTI CHE ALIAS
#### Matric No.: A20EC0121
#### Dataset: Mflix

## Question 4
- The project's machine learning methodology is called **content-based filtering**.
- A recommendation system that employs content-based filtering focuses on the qualities and features of things (in this case, movies) to provide recommendations.
- It examines the characteristics or substance of films to find similarities and provide users with tailored recommendations.
- The title, storyline, and genre attributes that are included in the movies.json dataset will be the primary focus of the movie recommendation engine that will be developed.
- for this part, i'll be using google collab as it is easier to do the content-based filtering

  
  **1.Import Pandas library.**
  ```
  import panda as pd
  ```

  **2.Upload and read the json file.**

Examine the movies.json file that you uploaded to Google Colab.

  ```
  dataset_path = 'movies.json'
data = pd.read_json(dataset_path, lines=True)
  ```

**3.Data Cleaning and Preprocessing**

- The dataset will first be shrunk in order to conserve memory and processing time.

```
random_seed = 42
data = data.sample(n=10000, random_state=random_seed)
```

-The dataset's available columns are then examined.

```
data.columns
```

![Screenshot (281)](https://github.com/drshahizan/SECP3843/assets/121208097/b6eedda9-617c-492c-800d-2b8ab609cb32)
this is the list of the available columns

- After that, decide which attribute you wish to include in the machine learning process.

```
movies = data[['_id', 'plot', 'genres', 'title']]
```

![Screenshot (282)](https://github.com/drshahizan/SECP3843/assets/121208097/da723ec3-5198-460f-8740-a11b87a7ead5)
this is the results of the selected columns that has been filtered

- Next, create new column which is tags that is the combination of plot and genres attributes.
```
movies['genres'] = movies['genres'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')
movies['tags']=movies['plot'] + ' ' + movies['genres']
```

- Assign to a new dataset and drop the genres and plot collumns

```
new_movies = movies.drop(columns=['plot', 'genres'])
```
![Screenshot (285)](https://github.com/drshahizan/SECP3843/assets/121208097/09578b83-0107-40e4-998c-138ad954b113)


and your dataset is ready for the machine learning process


**4.Machine Learning Process**

- The CountVectorizer class from the sklearn.feature_extraction.text module library should first be imported.

```
from sklearn.feature_extraction.text import CountVectorizer
```

- Next, modify the CountVectorizer class's max_features and stop_words settings.

  ```
  cv = CountVectorizer(max_features=10000, stop_words='english')
  ```
  
The maximum number of features that can be extracted from the text data is controlled by the option max_features.
The stop words in English terms like the, and, is, etc. will not be taken into account by the stop_words argument. Before generating the matrix of token counts, the CountVectorizer will remove stop words from text data.

```
vector=cv.fit_transform(new_movies['title'].values.astype('U')).toarray()
```
- Next, import the cosine_similarity from sklearn.metrics.pairwise library.

- The code converts the text data from the title column in the new_movies dataset into a matrix of token counts represented as a dense NumPy array.

  ![Screenshot (283)](https://github.com/drshahizan/SECP3843/assets/121208097/17bd3186-765a-44d3-808c-a89ef1121fe1)

- The method of computing the cosine similarity between two vectors or arrays, which is frequently used to gauge the proximity or separation of data points, is provided by the concept of cosine similarity.
  
```
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)
```
![Screenshot (287)](https://github.com/drshahizan/SECP3843/assets/121208097/8babd31a-ec10-4402-8af0-3ff79d683101)



- The recommend function accepts a movie title as input, finds the index of the movie in the new_movies DataFrame, uses cosine similarity to calculate the distances between the movie and all other movies, sorts them in descending order, and outputs the titles of the top 5 recommended movies.
```
def recommend(movies):
index = new_movies[new_movies['title']==movies].index[0]
distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
for i in distance[0:5]:
  print(new_movies.iloc[i[0]].title)

```
Choose a movie title to test the suggestion:

```
recommend("Singapore Sling")
```
![Screenshot (288)](https://github.com/drshahizan/SECP3843/assets/121208097/4ae73e0f-f53f-4f50-b557-ac9ea4cec461)



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


