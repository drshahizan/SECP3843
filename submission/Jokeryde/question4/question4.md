<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: ADAM WAFII BIN AZUAR

#### Matric No.: A20EC0003

#### Dataset: MFLIX DATASET

## Question 4

The approach I used is form of content-based filtering, which is a type of recommendation system. Content-based filtering recommends items (in this case, movies) to users based on the similarity of their attributes or content. In this case, I used the movie genres, cast, directors, and plot as the attributes to calculate the similarity between movies and generate recommendations.

Install the necessary libraries:

```
    pip install pymongo
    pip install pandas
```

1.  Retrieve the Mflix datatset from MongoDB
    The code will retrieve the movies data from MongoDB collection named `mflixx`, iterates over each movie and extracts the rating from `imdb` field. It stores all the ratings of the movie. I used the `json_normalize` function that will extract the "rating" attribute from the "imdb" field.

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/1.%20retrive.jpg">

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/1.%20retrive%20result.jpg">

2.  Data Cleaning & Data Preprocessing

         i. Remove the unnecessary clomuns by removing the columns that are not relevant for the recommendation system. Drop teh columns by using the `drop()` function and for "tomatoes" column I'm using the `startwith()` method.



    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/2.%20cleaning.jpg">

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/2.%20cleaning%20result.jpg">


         ii. Remove the rows that contains missing values by using the `dropna()` function.

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/3.%20dropna.jpg">

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/3.%20dropna%20result.jpg">

         iii. Remove special characters, cleaning and preprocessing for column "Plot" and "Genre"

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/4.%20preprocess.jpg">

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/4.%20preprocess%20result.jpg">

3.  Feature Extraction & Representation
    The approach I used is vectorized representation of the item features which will allow efficient computation and comparison of item similarities.

         i. Concatenate the text-based feature columns into a single column. I've used the `apply()` method along with `join()` and also `map(str,row) method.

    <img src="https://github.com/drshahizan/SECP3843/blob/2fdb7483384c69a2dd92476fa56559c874bba55d/submission/Jokeryde/question4/files/images/5.%20features.jpg">

    <img src="https://github.com/drshahizan/SECP3843/blob/dfe4815494305d7cce506e6c2b882568ab05c9e5/submission/Jokeryde/question4/files/images/5.%20features%20result.jpg">

4.  Calculate Similarity
To calculate the similarity between text documents, I've used method cosine similarity by importing TF-IDF vectors.

<img src="https://github.com/drshahizan/SECP3843/blob/dfe4815494305d7cce506e6c2b882568ab05c9e5/submission/Jokeryde/question4/files/images/6.%20matrix.jpg">

5.  Generate Recommendations
    To generate movie recommendations based on the similarity scores, I defined a function that takes a movie title as input and returns a list of recommended movies.

    <img src="https://github.com/drshahizan/SECP3843/blob/dfe4815494305d7cce506e6c2b882568ab05c9e5/submission/Jokeryde/question4/files/images/7.%20recomend.jpg">

    Testing:

    <img src="https://github.com/drshahizan/SECP3843/blob/dfe4815494305d7cce506e6c2b882568ab05c9e5/submission/Jokeryde/question4/files/images/8.%20test%20mdoel.jpg">

## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
