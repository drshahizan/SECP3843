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

## Question 5 (a)

 Install the necessary library:
 
 `pip install pymongo`
 `pip install pandas`

The selected techniques include pagination, caching, indexing and vectorization. Each technique aims to address different aspects of performance optimization, such as efficient data retrieval, reducing processing time, and enhancing data access speed. By implementing these techniques, we can significantly improve the performance of the portal, allowing users to view data and generate dashboard visualizations more effectively.

1. Pagination

   - Establish a connection to MongoDB database using `pymongo`.
   - Retrieve the data from the collection using `collection.find()`.
   - Convert the data into a pandas DataFrame using `pd.DataFrame()`.
   - Configure the number of items per page.
   - Paginate the DataFrame by iterating over the pages and displaying the data using slicing `(df.iloc[start_index:end_index])`.
   - Prompt the user to continue to the next page and handle user input.



   ```
      import pymongo
      import pandas as pd
   
      client = pymongo.MongoClient("mongodb+srv://jokeryde:adamkaya@jokeryde.cnn7sr4.mongodb.net/")
      db = client["mflix"]
      collection = db["mflixx"]
      
      
      data = list(collection.find())
      
      
      df = pd.DataFrame(data)
      
      
      items_per_page = 100
      
      
      total_items = len(df)
      num_pages = total_items // items_per_page + (1 if total_items % items_per_page > 0 else 0)
      
      
      for page in range(num_pages):
          start_index = page * items_per_page
          end_index = start_index + items_per_page
          page_data = df.iloc[start_index:end_index]
          
       
          print(f"Page {page+1}/{num_pages}")
          display(page_data)
          
          user_input = input("Press Enter to continue...")
          if user_input.lower() == "q":
              break
   ```

 <img src="https://github.com/drshahizan/SECP3843/blob/6571d036a21fc339be9c7382c1c69e8201da8dea/submission/Jokeryde/question5/images/pagination.jpg">




   2. Caching:

      - Establish a connection to MongoDB database using `pymongo`.
      - Configure caching using `joblib.Memory` by specifying the cache directory.
      - Define a function to fetch and process the data from MongoDB, decorated with `@memory.cache`.
      - Retrieve the data from the collection and convert it into a pandas DataFrame within the `fetch_data()` function.
      - Fetch the data using `fetch_data()`, which will utilize caching to avoid redundant fetch operations.


      ```
         import pymongo
         import pandas as pd
         from joblib import Memory
         
         
         client = pymongo.MongoClient("mongodb+srv://jokeryde:adamkaya@jokeryde.cnn7sr4.mongodb.net/")
         db = client["mflix"]
         collection = db["mflixx"]
         
         
         cache_dir = "./cache" 
         memory = Memory(cache_dir, verbose=0)
         
         
         @memory.cache
         def fetch_data():
             
             data = list(collection.find())
             
             
             df = pd.DataFrame(data)
             
             return df
         
         
         df = fetch_data()
         display(df)

      ```

 <img src="https://github.com/drshahizan/SECP3843/blob/6571d036a21fc339be9c7382c1c69e8201da8dea/submission/Jokeryde/question5/images/caching.jpg">


  3. Indexing

     - Connect to MongoDB using `pymongo`.
     - Create an index on the "title" field using `collection.create_index("title")`.
     - Verify the indexes created using `collection.index_information()`.
     - 

     ```
        import pymongo

        
        client = pymongo.MongoClient("mongodb+srv://jokeryde:adamkaya@jokeryde.cnn7sr4.mongodb.net/")
        db = client["mflix"]
        collection = db["mflixx"]

        collection.create_index("titles")

        indexes = collection.index_information()
        print(indexes)

      ```

 <img src="https://github.com/drshahizan/SECP3843/blob/6571d036a21fc339be9c7382c1c69e8201da8dea/submission/Jokeryde/question5/images/index.jpg">



   4. Vectorization

      - Connect to MongoDB and retrieve data using `pymongo`.
      - Convert data to a Pandas DataFrame using `pd.DataFrame()`.
      - Perform vectorized computation using `np.vectorize` and a lambda function to process the "title" column. Handle missing values using `isinstance(x, str)`.
      - Print the processed data.
     
      ```
         import pymongo
         import pandas as pd
         import numpy as np

         client = pymongo.MongoClient("mongodb+srv://jokeryde:adamkaya@jokeryde.cnn7sr4.mongodb.net/")
         db = client["mflix"]
         collection = db["mflixx"]
         data = list(collection.find())

         df = pd.DataFrame(data)

         df['processed_data'] = np.vectorize(lambda x: x.upper() if isinstance(x, str) else '')(df['title'])

         print(df['processed_data'])

      ```

 <img src="https://github.com/drshahizan/SECP3843/blob/6571d036a21fc339be9c7382c1c69e8201da8dea/submission/Jokeryde/question5/images/vectorization.jpg">


## Question 5 (b)

  For the visualization part, I decided to use the MongoDB Atlas Chart.

  1. First open MongoDB Atlas at web browser and login.
  2. Then click on the `charts` tab to open Atlas Charts Page.
  3. Next Click the Add New Dashboard to create the dashboard.
  4. I have created 5 charts:

       a. Geo Heatmap for Theaters which represent the theaters location.

        <img src="https://github.com/drshahizan/SECP3843/blob/709665215c0dc312e46abee64d7b4b90af82c84e/submission/Jokeryde/question5/images/heatmap.png">

        b. Doughnut Chart which represent the number of award nomination gain by each genres

       <img src="https://github.com/drshahizan/SECP3843/blob/709665215c0dc312e46abee64d7b4b90af82c84e/submission/Jokeryde/question5/images/donut.png">


        c. Area chart that shows the number of movie produced from 1891-2020

     <img src="https://github.com/drshahizan/SECP3843/blob/709665215c0dc312e46abee64d7b4b90af82c84e/submission/Jokeryde/question5/images/movie%20produced.jpg">
    

     d. Bar Chart that shows which state in United States of America has the most number of theaters.

     <img src="https://github.com/drshahizan/SECP3843/blob/709665215c0dc312e46abee64d7b4b90af82c84e/submission/Jokeryde/question5/images/theaterss.jpg">

     e. Map Chart that shows the total number of awards won by each countries.

     <img src="https://github.com/drshahizan/SECP3843/blob/709665215c0dc312e46abee64d7b4b90af82c84e/submission/Jokeryde/question5/images/awards.jpg">


<h2>DASHBOARD</h2>

  <img src="https://github.com/drshahizan/SECP3843/blob/072eddf89c6bc5c7fadd5b2d8f3ac6547bef2e9c/submission/Jokeryde/question5/images/dashboard.jpg">


## Contribution 🛠️

Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
