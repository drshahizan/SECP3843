<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Lee Jia Xian
#### Matric No.: A20EC0200
#### Dataset: <a href="https://github.com/drshahizan/dataset/tree/main/mongodb/01-sales" >Supply Store Dataset</a>

## Question 4 

### Overview
  In this case study, machine learning is utilized to improve the functioning of the portal by predicting customer satisfaction based on various features such as customer gender, age, coupon usage, purchase method, and store location. This prediction can provide valuable insights for businesses to enhance their decision-making processes and improve customer experiences.

### Approach
  The chosen machine learning algorithm for this case study is the Random Forest Classifier. This algorithm is an ensemble learning method that combines multiple decision trees to make predictions. It is well-suited for classification tasks and can handle both numerical and categorical features effectively.

### Data Preprocessing 
  The sales data collected from the portal is initially stored in a MongoDB database. To prepare the data for the machine learning model, it is extracted from the database and converted into a pandas DataFrame. Categorical columns are one-hot encoded, and irrelevant columns are dropped to create a clean and suitable dataset for training the model.
  <img  src="./files/images/cleaning1.JPG"></img>

  result:
  <img  src="./files/images/cleaning2.JPG"></img>

### Training the Model
  The dataset is split into training and test sets using the train_test_split function from the sklearn.model_selection module. The Random Forest Classifier model is then instantiated and trained on the training data using the fit method.
  <img  src="./files/images/train1.JPG"></img>

### Prediction
  To predict customer satisfaction, user input is collected from the portal's form, including features like customer gender, age, coupon usage, purchase method, and store location. The user input is then converted into a DataFrame, one-hot encoded, and aligned with the trained model's columns. Finally, the model's predict method is used to make the prediction.
    <img  src="./files/images/predict1.JPG"></img>

### Result and Visualization
  The predicted customer satisfaction label is obtained from the model, and a human-readable label is mapped to it. This result is then displayed on the portal's form page, providing immediate feedback to the user.

  form.html:
  <img  src="./files/images/form1.JPG"></img>

  interface:
  <img  src="./files/images/interface1.JPG"></img>

 Result 1: <br>
   <img  src="./files/images/result1.JPG"></img> 
 <br> Result 2: <br>
   <img  src="./files/images/result2.JPG"></img>
<br>  Result 3: <br>
   <img  src="./files/images/result3.JPG"></img>

### Conclusion
  By utilizing machine learning techniques, specifically the Random Forest Classifier algorithm, I have developed a solution to predict customer satisfaction based on various features collected from the portal. This predictive capability can help businesses gain insights into customer preferences and make informed decisions to enhance their services and improve overall customer satisfaction.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




