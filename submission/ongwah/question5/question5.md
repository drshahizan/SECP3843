<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Ong Han Wah
#### Matric No.: A20EC0129
#### Dataset: Mflix Dataset

## Question 5 (a)

- Caching

Caching mechanism can be implemented to store frequently accessed data to avoid redundant computations and faster esponse time.

- Database query optimization

Database queries can be optimized by reducing JOIN, subqueries and select only necessary columns. This can avoid unnecessary data retrieval that can affect performance.

- Database replication and sharding

MongoDB offers replication and sharding for increased performance. Replication increases data availability and provides redundancy. The applications tocan read from multiple servers to help with load balancing among replica sets. Sharding distributes large data sets across multiple servers. We can achieve improved data availability, scalability, load balancing, and performance optimization for the applications by implementing database replication and sharding.

## Question 5 (b)
1. Create a Django app called `dashboard` and include the app in the `INSTALLED_APPS` list in the `settings.py` file.
```
python manage.py startapp dashboard
```

2. Update the code in the `views.py` file of `dashboard` app.
```py
from django.shortcuts import render

def index(request):
    return render(request, "dashboard/index.html")
```

3. Build the dashboard using **MongoDB Atlas Charts**. Login to MongoDB Atlas and navigate to Charts to create a dashboard. The dashboard is built with several charts including:

- A card that show the total number of movies.

<img src="./files/images/num_movies.png">

- Gauge chart that show the average metacritic score

<img src="./files/images/gauge.png">

- Doughnut chart that shows the number and percentages of movies based on their rating. The chart includes top 10 ratings and the others.

<img src="./files/images/doughnut.png">

- A bar chart that shows top 10 genres having highest number of movies.

<img src="./files/images/genres.png">

- A bar chart that shows top 10 languages among the movies.

<img src="./files/images/languages.png">

- A bar chart that shows top 10 movies based on their number of Mflix comments.

<img src="./files/images/topmovies.png">

- A table shows the most awarded directors. The table includes the number of movies, winning and nominations counts for each directors.

<img src="./files/images/directors.png">

- A bar chart that shows the most active actors based on their number of movies involved.

<img src="./files/images/actors.png">

- A combo chart shows the number of movies, average critic and viewer review past the decades.

<img src="./files/images/combo.png">

- A choropleth map can be useful to visualize the average metacritics score of movies in different countries with color scale.

<img src="./files/images/map.png">

4. Create the html file for the dashboard view. Inside the `dashboard` directory, create a directory called `templates`. Then inside the templates directory, create another directory named `dashboard` and put the html files in it. In the MongoDB Atlas Charts page, find the embed option, enable unauthenticated access, configure the embedding setting and then copy the dashboard embed code and paste it in the html file.

<img src="./files/images/option.png">
<img src="./files/images/embed.png">

- `index.html`
```
<h2>Dashboard</h2>

<iframe style="background: #F1F5F4;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);width: 100vw;height: 100vh;"  src="https://charts.mongodb.com/charts-project-0-eouzt/embed/dashboards?id=649d1991-b269-433f-851e-1fa3136c52b1&theme=light&autoRefresh=true&maxDataAge=3600&showTitleAndDesc=false&scalingWidth=fixed&scalingHeight=fixed"></iframe>
```


5. Add the route to the `urls.py` file.
```py
...
from dashboard import views as dashboard_views

urlpatterns = [
    ...
    path('dashboard/', dashboard_views.index, name='dashboard'),
]
```

6. Run server to see the result.
```
python manage.py runserver
```
<img src="./files/images/dashboard1.png">
<img src="./files/images/dashboard2.png">



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




