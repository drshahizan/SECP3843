<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

## Special Topic Data Engineering (SECP3843): Alternative Assessment ©️

#### Name: MADINA SURAYA BINTI ZHARIN
#### Matric No.: A20EC0203
#### Dataset: companies.json

### Question 5 (a)
The performance of the portal need to be optimized when dealing with large volumes of JSON data from the dataset, especially during dashboard visualizations, to improve scalability and performance. When too much data need to be rendered at one time, it will affect the user experience such as lagging and unresponsive page. There are lots of ways on how we can deal with large dataset and here, I will explain one of the best ways, which is **Aggregation Pipeline** using python and MongoDB tools utilization.

1. Import neccessary python libraries.
   ```
   import pandas as pd
   !pip install pymongo
   import pymongo
   ```

2. Get the raw dataset from the database.
   ```
   client = pymongo.MongoClient("mongodb+srv://user1:______________________@cluster0.evngzba.mongodb.net/test")
    db = client["db_crunchbase"]
    collection = db["companies"]

3. Make a dataframe for the data and get the information about the data to monitor the size.

    ```
    data = list(collection.find())
    df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    df.head(5)
    ```

    <p align='center'>
      <img width="884" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/ba846a9e-4a16-46ed-ac9f-734d211e383d">
    </p>
  
    Based on picture below, we can see that the size of the data consume **3.0+MB**  storage memory.
    <p align='center'>
      <img width="285" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/7fbcfd2f-8187-4b38-8a77-ccba28f184cd">
    </p>

4. Select neccessary fields that are needed for analysis and perform data cleaning.
   
   ```
   selected_fields = df[['category_code','total_money_raised', 'number_of_employees','competitions']]
    selected_fields.head(5)
  

  <p align='center'>
    <img width="389" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/1c4536db-90bf-4146-8cec-39536e06653a">
  </p>


  ```
  selected_fields = selected_fields.dropna()

  def convert_money(value):
    try:
        if isinstance(value, float):
            return value
        elif 'B' in value:
            return float(value.replace('B', '').replace('$', '').replace('€', '')) * 1000000000
        elif 'M' in value:
            return float(value.replace('M', '').replace('$', '').replace('€', '')) * 1000000
        elif 'k' in value:
            return float(value.replace('k', '').replace('$', '').replace('€', '')) * 1000
        else:
            return float(value.replace('$', '').replace('€', ''))
    except ValueError:
        return 0.0  # Assign a default value of 0.0 for invalid or unknown values

  selected_fields['total_money_raised'] = selected_fields['total_money_raised'].apply(convert_money).astype(float)
  selected_fields['number_of_employees'] = selected_fields['number_of_employees'].astype(int)
  selected_fields['competitions'] = selected_fields['competitions'].astype(int)
  selected_fields.head(5)
  selected_fields.info()
  ```

  The shape of data reduce from (9500, 4) to (4416, 4) after cleaning.
  <p align='center'>
    <img width="381" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/f078d6bb-aab4-4521-8e4b-368bf809ecf8">
  </p>

  Based on the info, we can see that the memory storage of the data had reduce to **172.5+ KB**
  <p align='center'>
    <img width="276" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/211d8147-a76f-4e42-9b2a-faff26a449b4">
  </p>

5. Store the cleaned data into a collection in the database.
   ```
   mongo_uri = "mongodb+srv://user1:___________@cluster0.evngzba.mongodb.net/test"
   database_name = "db_crunchbase"
   collection_name = "companies_cleaned"

   client = pymongo.MongoClient(mongo_uri)
   db = client[database_name]
   collection = db[collection_name]

   # Convert DataFrame to a list of dictionaries (documents)
   documents = selected_fields.to_dict(orient='records')
   collection.insert_many(documents)
   ```
   In the database, we can see that the storage reduced from **15.4MB** to **168KB**.
   <p align='center'>
      <img width="595" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/e066becb-c322-4478-ba2b-793681fa08a7"><br>
        <img width="602" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/8bf787ac-0bb0-4f3c-a71a-7cfc99b712f9">
   </p>

   




### Question 5 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

