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
After performing data cleaning and aggregation, I can use this newly created collection to create charts by utilizing MongoDB Atlas features, to visualize it in a portal. Charts in a dashboard can be created using all the collections in the database. There are a total of 3 collections that I created including the raw, cleaned, and aggregate. By clicking ‘Visualize Your Data’ option, I can create charts and a dashboard based on data in this database.

<p align='center'>
   <img width="615" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/515f7ee1-b3ba-4148-bb78-f406b041fed3">
</p>

I can choose my desired collections to be used as a data source for a particular chart.
<p align='center'>
   <img width="576" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/9af78a37-76ef-4753-a89b-d3b1aab0435d">
</p>

There are a total of 5 charts that I create based on this database.

1. **Stacked Column** - Number of Competitors and Employees based on Category
   <p align='center'>
    <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/240ed9d6-93e2-457b-9adc-25f2a9a1930d">
   </p>
   The Crunchbase dataset's competitiveness and employee counts are shown in this graph for each category. It offers a comparison of the competitors and emploee  size across various industry sectors. We can see the link between the number of competitors and the employees in each category by providing us with new information about the level of competition and the nature of employment across different industries. Businesses may use this data to analyze competition possibilities, and make reasoned judgements about market positioning.

   As we can see from the chart, software companies acquire employees the most while web companies get the most competitors among its industry sector.

  <br>
  
2. **Bar graph** - Top 10 Category with Highest Number of Employees
   <p align='center'>
      <img width="956" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/3bfccb42-b2a8-4a4c-8517-f1e42129cfdb">
   </p>
   This graph displays the top 10 industry categories with the most number of employees. The most popular sectors are highlighted, together with information on their potential for hiring. We can determine the industries with the greatest employment levels by illustrating this data, which may be useful for industry research and talent acquisition.
   
   Based on the chart, we can conclude that finance records the highest average number of employees with more than 20,000 people.

<br>

3. **Heatmap** - Employee Distribution by Category and Country
   <p align='center'>
      <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/dfee17de-cc39-4aa2-973b-977c3ad26ca5">
   </p>
   Based on the total number of workers, the heatmap visualisation shows how the categories are distributed throughout different countries. The heatmap shows every category's number of employees in detail and draws attention to any geographical differences. This data may be useful for making strategic decisions, such as finding nations with a large pool of talent or analysing market potential in particular business sectors.

   Based on the heatmap, we can see that USA records the highest number of employees in hardware and software sectors while IND provides one of the highest consulting services.
<br>

4. **Discrete Line** - Top 10 Company with Highest Acquisition Price
   <p align='center'>
      <img width="960" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/c8891a43-9978-4db9-b982-bab1689d96b6">
   </p>

      The top 10 businesses sector with respect to acquisition prices are shown in this graph. Acquisation price is the total expense a business spend in acquiring a new client or purchasing an asset. We can determine which businesses have undergone the most significant acquisition deals, giving us insights into the industry's competitive environment.

   Based on the chart, we can conclude that Sprint Nextel spends the highest for their businesses. We can see that the top 10 are well-known and succesful companies.
   
   <br>

6. **Geospatial Chart** - Number of Companies by Country
   <p align='center'>
      <img width="951" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/f493de47-db63-41c8-a609-c644665ecfb8">
   </p>

      This graph shows how businesses are distributed according to the nation, the total number of active businesses in each nation. Insights into the geographic distribution of businesses may be gained by identifying countries having the highest number of companies. Understanding a company's worldwide footprint and tracking entrepreneurial activity across several geographies are both made easier by this knowledge.
      
   Based on the graph, we can see that the USA shows the most number of companies, along with Canada.

#### Dashboard
 <p align='center'>
      <img width="951" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/033de277-8ced-42e4-a659-0bf5755c1c6a">
   </p>

To visualize this dashboard in a website, I can use this embedded code and insert it into the portal's coding.
 <p align='center'>
     <img width="246" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/92c2efc2-dd25-40d1-95a8-a2424a6b8362"><br>
    <img width="586" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/9642b77b-0964-434f-a366-69ffcfcd6eab">
   </p>

This is the final result, in the website.
 <p align='center'>
     <img width="799" alt="image" src="https://github.com/drshahizan/SECP3843/assets/119557584/43cc86ad-95b3-41b9-b1c2-0d8eddc188d9">
   </p>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)

