<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Singthai Srisoi
#### Matric No.: A20EC0147
#### Dataset: Mflix Dataset

## Question 5 (a)
When dealing with large volumes of JSON data for dashboard visualizations, performance optimization becomes crucial to ensure smooth and responsive user experience. Here's an illustrative solution with code and screenshots to optimize the performance of the portal:

by taking data from MongoDB, w will demonstrate the approaches:
```python
import pandas as pd
import numpy as np
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['mflix']
collection = db['Movies']

movies_data = list(collection.find())

features = []

for movie in movies_data:
    genres = movie.get('genres', [])
    for genre in genres:
        movie_features = [
            genre,
            movie.get('runtime', 0),
            movie.get('imdb', {}).get('rating', 0.0)
        ]
        features.append(movie_features)
```

1. Data Preprocessing and Aggregation:
   - Load the JSON data into a pandas DataFrame.
   - Perform any necessary data cleaning and preprocessing steps.
   - Aggregate the data to reduce its volume and improve query performance. Grouping, filtering, and summarizing operations can be used to create aggregated datasets specifically tailored for the dashboard visualizations.
   
```python
df = pd.DataFrame(features, columns=['genre', 'runtime', 'rating'])

# Perform data cleaning and preprocessing
df = pd.DataFrame(features, columns=['genre', 'runtime', 'rating'])
df['rating'].replace('', np.nan, inplace=True)
df.dropna(axis=0, inplace=True)
df['genre'] = df['genre'].astype('str')
df['runtime'] = df['runtime'].astype('int32')
df['rating'] = df['rating'].astype(float)

# Aggregate the data
aggregated_data = df.groupby('genre').agg({'runtime': 'mean', 'rating': 'mean'}).reset_index()

```
   

2. Data Indexing:
   - Create indexes on the relevant columns of the DataFrame to improve query performance.
   - Indexing allows for faster data retrieval and filtering based on specific criteria, reducing the time required for rendering visualizations.
   
```python
# Create indexes on relevant columns
df.set_index('genre', inplace=True)
```

3. Caching:
   - Implement a caching mechanism to store precomputed results or intermediate data structures. This avoids repetitive computations when generating visualizations and speeds up the rendering process.
   - Consider using technologies like Redis or memcached to cache data.
   
```python
# Implement caching using Redis or memcached
# Example using Redis:
import redis

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379)

# Cache the aggregated data
redis_client.set('aggregated_data', aggregated_data.to_msgpack(compress='zlib'))
```

4. Lazy Loading and Pagination:
   - Implement lazy loading and pagination techniques to load and display the data in small chunks or on-demand.
   - Instead of loading the entire dataset at once, load and display a subset of the data initially and load more data as the user interacts with the dashboard or requests additional information.
   
```python
# Implement lazy loading and pagination using limit and skip
# Example: Load and display 10 movies at a time
page_size = 10
page_number = 1
movies_subset = collection.find().skip((page_number - 1) * page_size).limit(page_size)
```

5. Data Compression and Encoding:
   - Apply compression techniques like gzip or zlib to reduce the size of JSON data before transmission.
   - Utilize efficient encoding schemes like MessagePack or BSON to minimize data size and improve transmission speed.
```python
import gzip
import bson

# Compress the data using gzip
compressed_data = gzip.compress(df.to_csv().encode())

# Encode the data using BSON
encoded_data = bson.dumps(df.to_dict())
```

## Question 5 (b)
[Movie Dashboard](https://singthai-srisoi.github.io/singthai.github.io/AAdashboard)
![image](https://github.com/drshahizan/SECP3843/assets/84219904/95b06b1b-b518-46da-bc7d-519835c5929c)
1. Bar Chart for Genres:
This graph provides insights into the distribution of movies across different genres. The X-axis represents the genres, such as action, comedy, drama, etc. The Y-axis represents the count of movies belonging to each genre. The height of each bar indicates the number of movies in that genre. This chart helps visualize the popularity or prevalence of different genres in the dataset.

2. Scatter Plot for Runtime vs. IMDb Rating:
This graph explores the relationship between the runtime of movies and their IMDb ratings. The X-axis represents the runtime of movies in minutes. The Y-axis represents the IMDb rating of movies. Each data point in the scatter plot represents a movie, with its position determined by its runtime and IMDb rating. This chart helps identify any correlation or patterns between the runtime and IMDb ratings of movies.

3. Pie Chart for Country Distribution:
This graph provides a visual representation of the distribution of movies across different countries.Each country is represented as a slice of the pie chart. The size of each slice corresponds to the proportion of movies produced in that country. This chart helps identify the contribution of each country to the dataset and visualize any dominance or diversity in terms of movie production.

4. Bar Chart for Awards:
This graph showcases the number of wins and nominations for each movie. The X-axis represents the movie id. The Y-axis represents the count of wins and nominations. Each movie is represented by a pair of bars, one indicating the number of wins and the other indicating the number of nominations. This chart helps compare the recognition and success of different movies based on their awards.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




