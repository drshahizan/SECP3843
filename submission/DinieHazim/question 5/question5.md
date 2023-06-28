<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Muhammad Dinie Hazim Bin Azali
#### Matric No.: A20EC0084
#### Dataset: [Stories](https://github.com/drshahizan/dataset/tree/main/mongodb/07-stories)

## Question 5 (a)
In order to optimize the perfomance of a portal when dealing with large volumes of JSON data for dashboard visualizations, we can consider Data Aggregation.

1. Open MongoDB Compass.
   <img src="./files/images/mongodbCompass.png">
2. Open your Mongo Shell.
3. In my dataset, my `submit_date` and `promote_date` was in Unix timestamp.
4. In order to change it to format that I want, I run this code below in Mongo Shell.
   ```
      db.Stories.updateMany(
        {},
        [
          {
            $set: {
              submit_date: {
                $toDate: {
                  $multiply: ["$submit_date", 1000]
                }
              },
              promote_date: {
                $toDate: {
                  $multiply: ["$promote_date", 1000]
                }
              }
            }
          },
          {
            $set: {
              submit_year: { $year: "$submit_date" },
              promote_year: { $year: "$promote_date" }
            }
          }
        ]
      );
   ```

5. This is the value of `submit_date` and `promote_date` that I get after run the code.
   <img src="./files/images/afteraggregate.png">
6. The first $set stage converts the submit_date and promote_date fields to date format.
7. The second $set stage extracts the years from the converted dates and assigns them to submit_year and promote_year fields

## Question 5 (b)

#### Import JSON dataset into MongoDB

For this step, can refer my [Question 2(a)](https://github.com/drshahizan/SECP3843/blob/10fa31e68212c6819884e25714778b51d031b2e1/submission/DinieHazim/question%202/question2.md) for better insight.

#### Create Dashboard

1. Login to your MongoDB Atlas account by simply go this [link](https://account.mongodb.com/account/login?signedOut=true)
2. In the navigation bar, click on the button named `Charts`.
   <p align="center">
      <img src="./files/images/charts.png">
   </p>
3. It will bring you to the Welcome page and simply click on the Start button.
   <p align="center">
      <img src="./files/images/start.png">
   </p>
4. Select the Chart Builder to create a chart with your own data.
   <p align="center">
      <img src="./files/images/chart_builder.png">
   </p>
5. Select your collection.
   <p align="center">
      <img src="./files/images/select.png">
   </p>
7. It will bring you to this page so that you can start to drag and drop attributes fields to make a chart.
   <p align="center">
      <img src="./files/images/drag_drop.png">
   </p>

#### Charts and Dashboard development

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/mikhel-adam/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
