<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Rishma Fathima Binti Basher
#### Matric No.: A20EC0137
#### Dataset: [Airbnb Listings Dataset](https://github.com/drshahizan/dataset/tree/c8e9f4a7cbdb0c1b78ca2c73915ff56ceeb50e70/mongodb/05-airbnb)

## Question 5 (a)

The code that explained below is to provide a web API that pulls paginated JSON data from a MongoDB database and uses gzip to compress the response. The goal of this  is to improve a portal's responsiveness when handling substantial amounts of JSON data for dashboard visualisations.

  1. Get the libraries
     ```ruby
     from flask import Flask, jsonify, request
     import json
     import gzip
     from pymongo import MongoClient
     ```
  3. Create a Flask application and establish a connection to MongoDB, created a Flask application object and establish a connection to MongoDB using the MongoClient         class from PyMongo
     ```ruby
      app = Flask(__name__)

      # Connect to MongoDB
      client = pymongo.MongoClient("mongodb+srv://rf_user:rishma3112@newcluster.vekvrpq.mongodb.net/test")
      db = client["AA_STDE"]
      dataCollection = db["Question4"]
     ```
  5. Define the API endpoint for retrieving paginated JSON data defined with the /api/data endpoint, which accepts page and limit parameters as query parameters. These       parameters determine the pagination settings. The find() method is used to retrieve the paginated data from the MongoDB collection. The skip() method skips the          specified number of documents (based on the start index), and the limit() method limits the number of documents returned.The retrieved data is then compressed           using gzip with gzip.compress().
     
     ```ruby
      @app.route('/api/data')
      def get_paginated_data():
      page = int(request.args.get('page', 1))
      limit = int(request.args.get('limit', 10))
  
      start_index = (page - 1) * limit
      end_index = page * limit
  
      # Retrieve paginated data from MongoDB
      paginated_data = list(collection.find().skip(start_index).limit(limit))
  
      # Compress the response using gzip
      compressed_data = gzip.compress(json.dumps(paginated_data).encode('utf-8'))
  
      # Set the appropriate headers for gzip response
      response_headers = {
          'Content-Encoding': 'gzip',
          'Content-Type': 'application/json',
          'Content-Length': str(len(compressed_data))
      }

      return compressed_data, 200, response_headers
     ```
     
  7. Run the Flask application
     ```ruby
      if __name__ == '__main__':
      app.run()
     ```
     The implemented code can be viewed [here](https://github.com/drshahizan/SECP3843/blob/f9655c899e5daaec41394091dc46b7013e36c07c/submission/RishmaFathima/Question5/files/source-code/AA_Question5(a).ipynb)
     
## Question 5 (b)
  1. In order to start working with the visualization, I have chosen the MongoDB Atlas Charts to generate the charts and dashboard
     
          
 
  2. Log into MongoDB Atlas and choose the charts to start working with the charts and dashboard
     
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.1.png">
          
 
  3. Click on the ``Add Chart`` to add a new chart
     
      <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.2.png">
      
  4. Pick the JSON file which was already uploaded in MongoDB.
     
      <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.3.png">
  5. The first visualization is ``Maximum Night Stayed based on the price`` where the selected axis Y and X are shown below along with the attributes:
      
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.4.png">
       
        Chart:
        
     <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/6b1c1f8843c704fbc5b2638b73dc6673c2873d99/submission/RishmaFathima/Question5/files/images/Maximum%20Night%20stayed%20based%20on%20the%20Price.png">
       
  6. The second visualization is ``The number of Accommodates`` where the selected axis Y and X are shown below along with the attributes:
      
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.5.png">
       
      Chart:
        
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/6b1c1f8843c704fbc5b2638b73dc6673c2873d99/submission/RishmaFathima/Question5/files/images/The%20Number%20of%20accomodates.png">
       
       
  7. The third visualization is ``Accommodates vs the number of bed selected`` where the selected axis Y and X are shown below along with the attributes:
      
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.6.png">

        Chart:
        
     <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/a8fd1fbf51f082e9df0fc4db7a09ad51ad94f972/submission/RishmaFathima/Question5/files/images/Accommodates%20vs%26nbsp%3B%20the%20Number%20of%20Bed%20selected%20.png">
       
       
  8. The fourth visualization is ``The number of bedroom choices for Accommodates `` where the selected axis Y and X are shown below along with the attributes:
      
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.7.png">

       Chart:
        
     <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/aa40393df700df388fd3aa641cd23471f9f60e30/submission/RishmaFathima/Question5/files/images/Number%20of%20bedroom%20Choices%26nbsp%3B%20of%20accomodates.png">
       
       
  9. The fiffth visualization is ``The total user`` where the attributes shown below:
      
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.8.png">

     Chart:
        
      <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/aa40393df700df388fd3aa641cd23471f9f60e30/submission/RishmaFathima/Question5/files/images/Total%20User.png">
       
  10. The sixth visualization is ``Accommodation `` where the attributes shown below:
      
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.9.png">

       Chart:
        
         <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/717dc9faac4953a7beb19456f83c7cf5d3954e29/submission/RishmaFathima/Question5/files/images/Accommodation%20.png">
       
  11. Dashboard View:
      
       <img width="600" alt="image" src="https://github.com/drshahizan/SECP3843/blob/bd5ecf1ed0ba6041244ad4045398da553a0a5ca4/submission/RishmaFathima/Question5/files/images/5.10.png">
  12. Dashboard View file:
      Download the [Dashboard file](https://github.com/drshahizan/SECP3843/blob/6b1c1f8843c704fbc5b2638b73dc6673c2873d99/submission/RishmaFathima/Question5/files/images/Question5_AA.pdf) 




## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


