<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Sakinah Al'izzah Binti Mohd Asri
#### Matric No.: A20EC0142
#### Dataset: [Analytics](https://github.com/drshahizan/dataset/tree/main/mongodb/02-analytics)

## Question 5 (a)

When working with a large amount of JSON data that requires display on a dashboard, optimizing portal performance is essential. To achieve this, consider the following approach as a recommendation:

1. Data Preprocessing and Aggregation

When creating a dashboard, it is critical to conduct a thorough analysis of the requirements and identify the essential data that needs to be visualized. To achieve this, the JSON data must be preprocessed to extract and transform the relevant information needed for the dashboard. This can be done by aggregating the data to reduce its volume and complexity. By summarizing or grouping the data at appropriate levels, unnecessary details can be avoided during visualization. As an example, consider the aggregation of data in a transactions dataset. 
```
# Extract and transform relevant columns information for visualization
processed_data = []
for transaction in transactions:
    account_id = transaction['account_id']
    date = transaction['date']
    amount = transaction['amount']
    processed_item = {
        'account_id': account_id,
        'date': date,
        'amount': amount
    }
    processed_data.append(processed_item)

# Aggregate the data
aggregated_data = {}
for item in processed_data:
    account_id = item['account_id']
    amount = item['amount']
    
    if account_id in aggregated_data:
        aggregated_data[account_id] += amount
    else:
        aggregated_data[account_id] = amount

# Print the aggregated data
for account_id, total_amount in aggregated_data.items():
    print(f"Account ID: {account_id}, Total Amount: {total_amount}")
```

By following these steps, one can create a well-organized and informative dashboard that effectively communicates the necessary data.


2. 


## Question 5 (b)






## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



