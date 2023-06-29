<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Maizatul Afrina Safiah Binti Saiful Azwan
#### Matric No.: A20EC0204
#### Dataset: City Inspections

## Question 4

[AA_Question4.ipynb](https://github.com/drshahizan/SECP3843/blob/main/submission/maizatulafrina/question4/files/code/AA_Question4.ipynb)

#### 1. Install Necessary Library

Install necessary library such as pymongo, textblob and wordcloud
  
<img width="933" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/e5888d93-a6cf-4434-a79c-0f55d063f041">

#### 2. Import Library

Import related library

<img width="932" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/4937aade-d1e5-4f99-b1ba-45449a5a65d0">

#### 3. Import and Load JSON Dataset from MongoDB

Connect to MongoDB and load the dataset

<img width="926" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/0f7ec563-5eb0-4f16-a6ee-0b339768766e">

Output:

<img width="941" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/38ab2356-0f78-41e3-a9f7-5ec998b93f3e">

#### 4. Data Transfromation

Separate the content in address.

<img width="924" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/f2c31acd-9962-468a-a601-08bfd4a0f77b">

Result:

<img width="929" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/9e44e1e3-6635-4e6e-9102-fcf8d1a5d531">

#### 5. Data Cleaning

Check if there are any null values.

<img width="932" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/d65b6fdc-b3eb-4cb1-b13e-bc587cd081ad">

Check if there are any duplicate value in `Result`.

<img width="936" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/38a75f14-e517-4ee3-8177-912e882a0306">

Transform the datatype of "date" to datetime

<img width="929" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/ce28fc46-66a1-41c7-b64a-b37c42495b5f">


#### 6. Data Visualization

- Percentage of Results from The Inspection

  <img width="928" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/a21c00ab-d2b7-4093-9c1c-b64b194ddb44">

  Result:

  <img width="938" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/a4040839-9454-4d60-893c-571ef7bdba26">

- Number of Inspection by Sectors

  <img width="931" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/ae63bea6-dc07-43b4-86a3-9a1fbb1f3a3a">
  
  Result:

  <img width="934" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/2fd8bd70-0cb3-4276-833c-65727b1a378a">


#### 7. Machine Learning

Create sample data.

<img width="927" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/b9a9ec9b-0b28-49dd-b2dc-632254cccea2">

Result:

<img width="927" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/801c35bb-e161-4686-8e30-0207c2f509d2">


- Prediction of Accuracy of new sector

```
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import classification_report
    from sklearn.preprocessing import LabelEncoder
    from sklearn.feature_extraction.text import CountVectorizer
    
    sectors = sample['sector'].tolist()
    results = sample['result'].tolist()
    
    label_encoder = LabelEncoder()
    encoded_results = label_encoder.fit_transform(results)
    
    # Split the data into training and test 
    X_train, X_test, y_train, y_test = train_test_split(sectors, encoded_results, test_size=0.2, random_state=42)
    
    vectorizer = CountVectorizer()
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)
    
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train_vectors, y_train)
    
    new_sectors = ['Cosmetic']
    new_sectors_vectors = vectorizer.transform(new_sectors)
    
    predicted_results = classifier.predict(new_sectors_vectors)
    
    predicted_labels = label_encoder.inverse_transform(predicted_results)
    
    for sectors, label in zip(new_sectors, predicted_labels):
        print(f"Sector: {sectors}, Predicted Result: {label}")
    
    accuracy = classifier.score(X_test_vectors, y_test)
    print('Accuracy:', accuracy)

```

Result: 

<img width="938" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/a9dc19b1-6826-405c-8b50-e5fbff996dc6">


- Classification Report of the Model

<img width="937" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/170586a0-51d6-431c-801e-17faa76cc99f">

Result:

<img width="921" alt="image" src="https://github.com/drshahizan/SECP3843/assets/120564694/a62c04d8-574c-4f62-b271-9054496d9249">


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




