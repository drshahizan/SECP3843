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

 6. To further reducing the volume of the data, I will perform aggregation pipeline in MongoDB Atlas. In the new collection, choose **Aggregation**.
    <p align='center'>
       <img width="598" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/ec1b392c-6cea-48c6-a0de-99545b40e8ce">
      </p>

7. Perform aggregation by grouping the data. There are two stage that I create. which are **$group** and **$project** to group the data based on category, get the average, and round the value into certain decimal place.

   <p align='center'>
      <img width="347" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/998dc381-12ba-4df6-8fe1-00171777949c">
   </p>

   This is the pipeline created based on the stage.
   <p align='center'>
       <img width="286" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/0bd3c489-055c-4c02-888c-9d9f66da5f6e">
   </p>

8. Export the pipeline in python language and use it to create new collection.
   <p align='center'>
      <img width="351" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/1f2b90f1-04ea-4fcf-8c2f-078eadd82040">
   </p>

   ```
   from pymongo import MongoClient

   client = MongoClient('mongodb+srv://user1:_________________________@cluster0.evngzba.mongodb.net/test')
   result = client['db_crunchbase']['companies_cleaned'].aggregate([
       {
           '$group': {
               '_id': '$category_code',
               'average_funding': {
                   '$avg': '$total_money_raised'
               },
               'average_employees': {
                   '$avg': '$number_of_employees'
               },
               'average_competitions': {
                   '$avg': '$competitions'
               }
           }
       }, {
           '$project': {
               'average_funding': {
                   '$round': [
                       '$average_funding', 2
                   ]
               },
               'average_employees': {
                   '$round': [
                       '$average_employees', 0
                   ]
               },
               'average_competitions': {
                   '$round': [
                       '$average_competitions', 0
                   ]
               }
           }
       }
   ])

   df2 = pd.DataFrame(result)
   df2.head(5)
   df2.info()
   ```

   <p align='center'>
      <img width="368" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/ea0f4e07-42ef-4394-aaf3-1d14809c33e2">
   </p>

   Based on the info, the memory storage reduce to **1.3+KB**.

   <p align='center'>
      <img width="276" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/3b348bc7-ae2f-48e2-a988-28d1782c8f83">
   </p>

9. Store the aggregate data in a collection.
    ```
    db = client['db_crunchbase']
      collection = db['companies_cleaned_aggregate']
      
      for doc in result:
          collection.insert_one(doc)
    ```
    As we can see, the storage size decreased to **20KB** in the database.
    <p align='center'>
       <img width="588" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/387961c8-62bc-43c8-afb8-6af56ec0158c">
      </p>

   
In conclusion, we can see that after cleaning and aggregating the data, the storage size in the database reduces from **15.4MB** to **168KB** after cleaning, and further decreases to **20KB** after aggregating. From here, we can easily create visualizations without concerning the performance especially if we use the collection with much lesser storage capacity.
  


   


    
      




### Question 5 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

