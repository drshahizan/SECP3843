<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Amirah Raihanah binti Abdul Rahim
#### Matric No.: A20EC0182
#### Dataset: Tweets

## Question 5 (a)
### Optimizing Portal Performance when dealing with large volume JSON dataset.

1. `Data Cleaning and Processing` : Remove unecessary column that will not be use in the visualizations. Also, remove unwanted character and standardize the format of the dataset.

2. `Use streaming JSON parser` : Instead of loading the entire file, the JSON parser will only parse the receiving data.

3. `Use JSON caching` : This will allow the portal to use cache data compared to requesting data everytime which is time consuming and not effective.

4. `Use suitable library to process the data` : There are many libraries that can cater the size of your data. For instance Dask, Modin, PySpark and Koalas

### 1. Data Cleaning and Processing

* Remove unused column to reduce the size of dataset.
Take this scenario where I want to analyze and visualize `user` details data from the Tweets JSON dataset. Hence I will drop all other columns.
<br>
Steps :

i) Import the JSON file 
```
import pandas as pd

# Load the JSON file into a DataFrame
data = '/content/drive/MyDrive/tweetsmodified.json'
df = pd.read_json(data)

# View the DataFrame

pd.set_option('display.max_columns', None)
df.head(5)
```
<img width="930" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/1bf218f6-ba16-4ce2-b12d-363706da5ff8">


ii) Check the initial JSON file size : 

```
import os
import math

# Save the DataFrame as a JSON file
df.to_json('data_output.json')

# Get the file size of the JSON file
file_size = os.path.getsize('data_output.json')

# Convert the file size to a human-readable format
def convert_size(size_bytes):
    # 2**10 = 1024
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

# Print the file size
print(f"JSON file size: {convert_size(file_size)}")
```
<img width="330" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/432b1bda-d7b3-4127-8b83-77db68911017">

iii) Then, drop the other columns.

```
# Select only the 'user' column
df_user = df[['user']].copy()

# Drop all other columns
df_user.drop(df_user.columns.difference(['user']), axis=1, inplace=True)

# Print the updated DataFrame
print(df_user)
```
<img width="624" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/ca02e25f-4160-4464-a0f5-74fab0d079ea">


iv) After other columns has dropped, check again the file size.


```
# Save the DataFrame as a JSON file
df_user.to_json('data_output2.json')

# Get the file size of the JSON file
file_size = os.path.getsize('data_output2.json')

# Convert the file size to a human-readable format
def convert_size(size_bytes):
    # 2**10 = 1024
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

# Print the file size
print(f"JSON file size: {convert_size(file_size)}")
```
<img width="260" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/882ae4d2-478b-4cd9-8b68-9d4d123df277">

> According to the code above, after dropping the other columns the file size from `46.45MB` has reduced to `28.29MB`. Thus, this will optimize the performance of the Portal as it does not need to load large volume JSON data.

### 2. Use streaming JSON parser

* Instead of loading the entire JSON data, streaming parsers parse the JSON data after being received. This help to reduce memory usage and also improve the parsing speed.
<br>
Steps :

i) Load the JSON data.
```
import pandas as pd

# Load the JSON file into a DataFrame
data = '/content/drive/MyDrive/tweetsmodified.json'
df = pd.read_json(data)

# View the DataFrame

pd.set_option('display.max_columns', None)
df.head(5)
```
<img width="930" alt="image" src="https://github.com/drshahizan/SECP3843/assets/73205963/1bf218f6-ba16-4ce2-b12d-363706da5ff8">

ii) Run the following code to parse the JSON file.
```
import json

def parse_json_stream(json_data):
    parser = json.JSONDecoder()
    buffer = ""
    
    for chunk in json_data:
        buffer += chunk
        try:
            while buffer:
                obj, idx = parser.raw_decode(buffer)
                yield obj
                buffer = buffer[idx:].lstrip()
        except json.JSONDecodeError:
            # Incomplete JSON, wait for more data
            continue
    
    # Handle any remaining buffered data
    if buffer:
        obj, _ = parser.raw_decode(buffer)
        yield obj

# Example usage
with open('/content/drive/MyDrive/tweetsmodified.json', 'r') as file:
    json_data_chunks = file.readlines()

# Simulating receiving JSON data in chunks
for obj in parse_json_stream(json_data_chunks):
    print(obj)
```
> JSON data succesfully parsed thus we can see that  less time taken needed to accomplish parsing.

### 3. Use JSON caching
* Caching JSON data reduce the time taken to fetch data. This is because it will retrieve the data from cache instead of having to retrieve from memory. This caching method will improve portal performance significantly.
<br>
Steps :

i) Choose caching mechanism

* In this example, we will use Redis as our caching mechanism. The configuration is to have 100 items, time to live of 1 minute and LRU as the eviction policy.
```
import redis

cache = redis.Redis()

# Set the size of the cache to 100 items
cache.set_max_entries(100)

# Set the time to live for cached items to 1 minute
cache.set_expire(60)

# Set the eviction policy to LRU
cache.set_eviction_policy('lru')
```

ii) Use the cached memory

* To use the cache memory, we will implement the code below. The code below shows that it will first check the data if it has been cached or not. If its not cached, it will retrieve from the database.

```
import redis

cache = redis.Redis()

def get_data(key):
    data = cache.get(key)
    if data is None:
        data = fetch_data_from_database(key)
        cache.set(key, data)
    return data
```
> Caching data in the portal will improve performance by retrieving it much more quickly than fetching it from the database.

### 4. Use suitable library to process the data


## Question 5 (b)
### Dashboard on Tweets dataset.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




