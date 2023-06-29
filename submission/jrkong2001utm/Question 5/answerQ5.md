<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kong Jia Rou
#### Matric No.: A20EC0198
#### Dataset: Supply store

## Question 5 (a)
There are many ways to optimize the performance of the portal when dealing with large volumes of JSON data from the dataset. Here I will explain 4 ways of performance optimization:

1.Chuncking
When importing the large dataset to perform operations such data preprocessing, data wrangling and data cleaning, it is important to use the chunking technique to minimize the time take for processing. This method will take the dataset and cut it into pieces of chunk for further processing. The number of chunk can be defined by the users. The code are as follows:
```
import pandas as pd

chunk_size = 1000  # Define the number of lines to process at a time

# Read the JSON file as text
with open('sales.json', 'r') as file:
    # Iterate over the file in chunks
    while True:
        try:
            # Read the next chunk of lines
            lines = [next(file) for _ in range(chunk_size)]
        except StopIteration:
            break

        # Join the lines back into a single string
        json_text = ''.join(lines)

        # Convert the JSON chunk to a DataFrame
        df = pd.read_json(json_text, lines=True)

        # Convert the DataFrame to JSON
        json_data = df.to_json(orient='records')
        
with open('sales.json', 'w') as file:
    file.write(json_data)

df = pd.read_json('sales.json')
df
```

2.Data Filtering and Aggregation
It is a good practice to implement filetering and aggregation when fetching and processing the dataset. If we take the whole dataset at once, it will increase the processing time due to the large amount of data which may cause the portal inefficient or not responding.
```
filtered_data = df.loc[df['storeLocation'] == 'Denver']
aggregated_data = filtered_data.groupby('purchaseMethod').agg({'_id': 'count'})

aggregated_data
```

3.Data Pagination
Data pagination is one of the ways to load and process the data in smaller chunk. In this example, I have set the page to display 100 records only instead of the default display setting which will display up to thousands of records.
```
import pandas as pd

page_number = 1
page_size = 100

start_index = (page_number - 1) * page_size
end_index = start_index + page_size

# Fetch a subset of data for the current page
page_data = df.iloc[start_index:end_index]
```

4.Data Compression and Chunked Responses
This method helps a lot when one is trying to export the dataset. Sometime when the dataset is too large, it takes up couples of hours to finish exporting. To solve this problem, we can compress the data using GZIP before exporting it.
```
# Example: Compressing JSON data with gzip
import gzip
import json

import json

# Load the dataset from the file
with open('sales.json', 'r') as file:
    data = json.load(file)
    
compressed_data = gzip.compress(json.dumps(data).encode('utf-8'))

# Save the compressed data to a file
with open('compressed_data.json.gz', 'wb') as file:
    file.write(compressed_data)
```

Please refer to [Q5_SourceCode]() to see the output of the coding.

## Question 5 (b)

<img src="..\Question 5\files\images\dashboard.png">

Bar Chart 1: Total Sales of each Purchase Method
This chart shows the total sales of each purchase method. From the chart, we can conclude that most of the customer purchase method are in store. The least purchase method is using phone.

Pie Chart 2: Total Item Sold by Item Name
This pie chart shows the percentage and the total number of the item sold categorize by item name. The item that has the highest sales is binder while the least is laptop.

Table 3: Customer Satisfaction
This table shows the customer satisfaction on the product they purchased. 1 indicates the lowest level of satisfaction. It can be concluded that half of the customer are satisfied with their services.

Bar Chart 4: Total Sales of the Store in Different Country
This bar chart shows the total sales record of the store group by country. Denver has the highest sales record while the San Diego has the least sales record.

Card 5: Total Sales Record
This card shows the accumulate daily sales record.

Card 6: Total of Coupon Used
This card shows the accumulate number of coupons that have been used by the customers.

Card 7: Store Location by Country
This card shows the total country where the store/merchant is located.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)






