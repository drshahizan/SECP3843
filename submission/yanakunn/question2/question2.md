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

Step 1: Prepare the JSON file
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
        elif isinstance(value, dict) and '$numberDecimal' in value:
            cleaned_item[key] = float(value['$numberDecimal'])
        elif isinstance(value, dict) and '$numberInt' in value:
            cleaned_item[key] = int(value['$numberInt'])
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
Step 2: Setup MongoDB server
``` ruby
DATABASES = {
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'db_regex',
        'CLIENT': {
            'host': 'mongodb+srv://cluster0.p1o2mcl.mongodb.net',
            'username': 'your_username',
            'password': 'your_password',
            'authMechanism': 'SCRAM-SHA-1',
            'authSource': 'admin',
        },
    },
}
```

## Question 2 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



