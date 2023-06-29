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

## Question 4
This case study could use A personalized recommendation system as a machine learning approach. This system would analyze a user's purchase history and provide customized product recommendations. To implement this, a content-based filtering recommendation system in Python can be created using the scikit-learn library.

#### Step 1: Import the sci-kit libraries
- Download the scikit-learn library in the terminal using `pip3 install scikit-library`. Then, define the libraries in the `views.py`.
```ruby
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
```

#### Step 2: Extract meaningful features from the sales data.
In this example, we retrieve a list of products and their descriptions. Then, we apply the TF-IDF vectorizer to transform the product descriptions into a numerical format. We calculate the cosine similarity matrix using the TF-IDF matrix. This matrix provides us with a way to measure the similarity between products.
```ruby
def salesReport(request):

    sales = Sale.objects.using('mongodb').all()

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words='english',
        ngram_range=(1, 2),
        max_features=5000
    )

    item_names = []
    for sale in sales:
        for item in sale['items']:
            item_names.append(item['name'])

    # Build the TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(item_names)
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    recommendations = get_recommendations(item_names)

    context = {
        'item_name': item_name,
        'recommendations': recommendations
    }

    return render(request, 'salesReport.html', context)
```

#### Step 3: Train the Recommendation model
To get recommendations for a product, the `get_recommendations` function will take the product name as the argument. It will retrieve the top N recommended products based on their similarity. The function finds the given product's index in the product list, retrieves the cosine similarity scores, sorts them in descending order, and returns the names of the N most similar products.

```ruby
def get_recommendations(item_name, top_n=5):
    item_index = next((index for (index, name) in enumerate(item_names) if name == item_name), None)
    if item_index is None:
        return []

    item_scores = list(enumerate(cosine_similarities[item_index]))
    item_scores = sorted(item_scores, key=lambda x: x[1], reverse=True)
    top_scores = item_scores[1:top_n+1]
    recommended_items = [item_names[score[0]] for score in top_scores]

    return recommended_items
```
#### Step 4: Evaluation
To determine the effectiveness of the trained model, use suitable evaluation metrics like precision, recall, or mean average precision to validate the model's performance on the validation set to ensure that it provides accurate recommendations.

#### Step 5: Integration and Deployment
The recommendation will be passed to the `salesReport` function to be displayed in the system.

#### Step 5: Monitoring and Iteration
Consistently keep track of how the recommendation system is performing. Gathering feedback from users and examining their engagement with recommended products is necessary for analysis.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




