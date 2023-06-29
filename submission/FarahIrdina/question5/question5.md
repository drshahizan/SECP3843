<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: FARAH IRDINA BINTI AHMAD BAHARUDIN
#### Matric No.: A20EC0035
#### Dataset: AIRBNB LISTINGS DATASET

## Question 5 (a)

Performance of the portable can be optimized when dealing with large volumes of JSON data from the dataset. Since I will be using MongoDB to make visualizations in Django, thus I will optimize using MongoDB Compass.

### Perform aggregations

An aggregation pipeline consists of one or more stages that process documents which can filter data, group data, and calculate its values. JSON dataset from the collection model will enter the pipeline and go through a number of stages, each of which are responsible for a specific operation. There are many operations that can be applied. But in this case, we will be using match, group and sort.

Firstly, open MongoDB Compass and click database and collection that will be used, then click Aggregations`. Add three stage which are:

#### Match
```
{ 
  "availability.availability_90": 
  { $ne: 0 } 
}
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/match.png)

#### Group

```
{
  "_id": "$property_type",
  "total": {"$sum": 1}
}
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/group.png)

#### Sort

```
{"total": -1}
```

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/sort.png)

Then, click Run.

### Result

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/result.png)

## Question 5 (b)

### Dashboard

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/dashboard.png)

#### 1. Number of Listings for Each Country

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/1.png)

The bar chart above shows that United States has the highest number of listings for each country while China has the lowest.

#### 2. Average Price by Rating Score

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/2.png)

The line chart above shows that the rating score with a 50% to 55% has the highest average price while  20% to 25% of rating score has the lowest average price.

#### 3. Average Price by Number of Bedrooms

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/3.png)

The line chart above shows that the bedrooms of value 9 has the highest average price while  the bedrooms of value 1 has the lowest average price.

#### 4. Availability of Properties Over Time by Property Type

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/4.png)

The property type of apartment has the highest availability of properties across the year.

#### 5. Average Property Prices Across Different Room Types and Rating Score

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/5.png)

Mostly, the room type of entire home/apt of rating 90-100 rating score has the highest price.

#### 6. Distribution of Property Types Based on Number of Cancellation Policies

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/6.png)

Apartment has the highest number of cancellation policies while the heritage hotel has the lowest.

#### 7. Total Rating Scores by Country

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/7.png)

Unites States has the highest total rating scores and China has the lowest.

#### 8. Number of Reviews by Rating Scores According to Room Types

![image](https://github.com/drshahizan/SECP3843/blob/main/submission/FarahIrdina/question5/files/images/8.png)

This graph shows that it has a positive correlation because the higher rating scores, the highest number of reviews.

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




