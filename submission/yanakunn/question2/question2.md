<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURARISSA DAYANA BINTI MOHD SUKRI
#### Matric No.: A20EC0120
#### Dataset: SALES

## Question 2 (a)
To successfully upload the sales.json dataset into MongoDB, the JSON file must have the proper structure for MongoDB documents. We can begin by restructuring the sales.json dataset using Python to achieve this.

### Step 1: Prepare the JSON file
1. Load the sales data from the sales.json file.
    ``` ruby
    import json
    json_data = []
    with open('/Documents/stde/sales.json') as file:
        for line in file:
            json_data.append(json.loads(line))
    ```
2. Remove the special MongoDB operators and convert them to regular values
    ``` ruby
    def clean_data(item):
        cleaned_item = {}
        for key, value in item.items():
            if isinstance(value, dict) and '$oid' in value:
                cleaned_item[key] = value['$oid']
            elif isinstance(value, dict) and '$date' in value:
                cleaned_item[key] = value['$date']['$numberLong']
            elif key == "items":
                cleaned_item[key] = []
                for item_data in value:
                    cleaned_item_data = {}
                    for item_key, item_value in item_data.items():
                        if isinstance(item_value, dict) and '$numberDecimal' in item_value:
                            cleaned_item_data[item_key] = float(item_value['$numberDecimal'])
                        elif isinstance(item_value, dict) and '$numberInt' in item_value:
                            cleaned_item_data[item_key] = int(item_value['$numberInt'])
                        else:
                            cleaned_item_data[item_key] = item_value
                    cleaned_item[key].append(cleaned_item_data)
            elif key == "customer":
                cleaned_item[key] = {}
                for customer_key, customer_value in value.items():
                    if isinstance(customer_value, dict) and '$numberInt' in customer_value:
                        cleaned_item[key][customer_key] = int(customer_value['$numberInt'])
                    else:
                        cleaned_item[key][customer_key] = customer_value
            else:
                cleaned_item[key] = value
        return cleaned_item
    ```
3. Save the cleaned data to a new file
    ``` ruby
    
    cleaned_data = [clean_data(item) for item in json_data]
    with open('/Documents/stde/newsales.json', 'w') as file:
        json.dump(cleaned_data, file, indent=2)
    ```
### Step 2: Setup MongoDB server
1. Log in to MongoDB Atlas.
2. Create a new project.
3. Create a cluster in the project.
4. Click "Connect" and select "Drivers" to connect the application with MongoDB Driver. Since we are using the Django web framework, choose "Python" as the driver with the correct version.
5. Copy the connection string provided to establish a connection with the MongoDB database server.
<img width="700" alt="Screenshot 2023-06-29 at 11 49 15 AM" src="https://github.com/drshahizan/special-topic-data-engineering/assets/76076543/0b46061a-7c2c-4ad1-9623-c3e28192928e">


### Step 3: Import data to MongoDB Database
1. Import MongoClient and JSON library
    ```ruby
    from pymongo import MongoClient
    import json
    ```
2. Read the new JSON file `newsales.json`
    ```ruby
    with open('/Documents/stde/newsales.json') as file:
        json_data = json.load(file)
    ```
3. Establish a connection to the MongoDB server and insert records into the MongoDB collection.
    ```ruby
    uri = "mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(uri)
    db = client['<db_name>']
    collection = db['<collection_name>']
    
    # Insert each sale record into the collection
    for sale in json_data:
        collection.insert_one(sale)
    ```
### Result
<img width="900" alt="Screenshot 2023-06-27 at 4 42 24 PM" src="https://github.com/yanakunn/SECP3843/assets/76076543/7450197e-2461-4b02-abb8-22acbbdf11b2">

## Question 2 (b)

Connect to the MongoDB server and select the database and collection.
```ruby
from pymongo import MongoClient
client = MongoClient('mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/?retryWrites=true&w=majority')
db = client['<db_name>']
collection = db['<collection_name>']
```
- Create query: Add a new object with the id "newobject123" and define all the details.
```ruby
sale = {
    "_id": "newobject123",
    "saleDate": "1550091249812",
    "items": [
        {
            "name": "notebook",
            "tags": ["office", "writing", "school"],
            "price": 12.99,
            "quantity": 3
        },
        {
            "name": "pencil",
            "tags": ["writing", "office", "school", "stationary"],
            "price": 1.99,
            "quantity": 10
        }
    ],
    "storeLocation": "New York",
    "customer": {
        "gender": "F",
        "age": 35,
        "email": "example@example.com",
        "satisfaction": 4
    },
    "couponUsed": True,
    "purchaseMethod": "Online"
}

collection.insert_one(sale)
print("Sale inserted successfully")
print(sale)
```
<img width="1100" alt="Screenshot 2023-06-27 at 5 06 31 PM" src="https://github.com/drshahizan/SECP3843/assets/76076543/837079c2-7eba-4c06-8ae6-9572191962c8">

- Read query: Print items bought by male customers at the store in Denver.
    ```ruby
    query = {"storeLocation": "Denver", "customer.gender": "M"}
    results = collection.find(query)
    for result in results:
        print(result["items"])
    ```
<img width="900" alt="Screenshot 2023-06-27 at 5 00 00 PM" src="https://github.com/drshahizan/SECP3843/assets/76076543/f5edad4d-0ea5-491e-a823-772b9b55d506">

- Update queries
    - Update the value of an object's quantity
```ruby
filter_query = {"_id": "5bd761dcae323e45a93ccfea", "items.name": "pens"}
update_query = {"$inc": {"items.$.quantity": 2}}
collection.update_one(filter_query, update_query)
print(collection.find_one(filter_query))
```
<img width="900" alt="Screenshot 2023-06-27 at 5 03 37 PM" src="https://github.com/drshahizan/SECP3843/assets/76076543/6d6b1068-82f5-4fdd-81e6-a17f8c88d860">
- Update queries
    - Update the value of an object's purchase method
    
```ruby
filter_query = {"_id": "5bd761dcae323e45a93ccfeb"}
update_query = {"$set": {"purchaseMethod": "In store"}}
collection.update_one(filter_query, update_query)
print(collection.find_one(filter_query))
```
<img width="900" alt="Screenshot 2023-06-27 at 5 12 03 PM" src="https://github.com/drshahizan/SECP3843/assets/76076543/239ef038-1eb0-4ab1-b20f-703baf75d1ee">

- Delete an item
```ruby
filter_query = {"_id": "newobject123"}
collection.delete_one(filter_query)
```
<img width="400" alt="Screenshot 2023-06-27 at 5 10 08 PM" src="https://github.com/drshahizan/SECP3843/assets/76076543/f97707e3-4999-4859-acb5-a5cb7ba98cb1">

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



