<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Kelvin Ee
#### Matric No.: A20EC0195
#### Dataset: City Inspections

## Question 5 (a)
Implement caching mechanisms to store and retrieve pre-processed data. This avoids repetitive computations and database queries, enhancing performance. Popular caching solutions include Redis or Django's built-in caching framework. 
Steps to implement cache when dealing with large volumes of JSON data from the dataset, especially during dashboard visualization is shown below:

### 1. Install all required packages by using the following commands
```python
pip install cachetools
```
### 2. Import the necessary classes and functions from cachetools in `views.py`:
```python
from cachetools import cached, TTLCache
```
### 3. Define cache instances for each function
```python
result_by_sector_cache = TTLCache(maxsize=1, ttl=3600)  # Cache for inspections_by_sector
inspections_by_month_cache = TTLCache(maxsize=1, ttl=3600)  # Cache for inspections_by_month
```
### 4. Apply the @cached decorator to the functions
```python
@cached(result_by_sector_cache)
def inspections_by_sector(request):
    
@cached(inspections_by_month_cache)
def inspections_by_month(request):
```
### 5. Verify cache to check if cached data is available 
```python

    cached_data = cache.get('inspections_by_sector')
    if cached_data:
        print("Using cached data")
        result_by_sector = cached_data
    else:
        print("Generating new data")
```

## Question 5 (b)
<b>Dashboard Created at management_dashboard.html</b>
<img src="./files/image/barchart.png">
<img src="./files/image/trend.png">

### Steps to create a dashboard utilizing a JSON dataset

### 1. Install all required packages by using the following commands
```python
pip install matplotlib
pip install numpy
```
### 2. Create Django View function for the visualization script.
- Bar Chart showing `Distribution of Top 5 Results by Top 5 Sectors`
```python
def inspections_by_sector(request):
    # Create a MongoClient instance
    client = MongoClient('mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "city_inspectionsDataset"
    collection = db['city_inspectionsDataset']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Calculate the result_by_sector DataFrame
    result_by_sector = df.groupby(['sector', 'result']).size().unstack().fillna(0)

    # Select top 5 results
    top_results = result_by_sector.sum().nlargest(5).index

    # Select top 5 sectors
    top_sectors = result_by_sector.sum(axis=1).nlargest(5).index

    # Filter the result_by_sector DataFrame based on the top results and sectors
    result_by_sector = result_by_sector.loc[top_sectors, top_results]

    # Increase the figure size and set a wider width
    plt.figure(figsize=(20, 10))

    # Plot the bar chart
    result_by_sector.plot(kind='bar', stacked=True, width=0.8)
    plt.xlabel('Sector')
    plt.ylabel('Number of Inspections')
    plt.title('Distribution of Top 5 Results by Top 5 Sectors')
    plt.xticks(rotation=30)
    plt.subplots_adjust(bottom=0.25)
    plt.subplots_adjust(bottom=0.25, left=0.1, right=0.9, top=0.9)  # Adjust the margins as needed

    # Save the chart to a file
    chart_path = 'q3_app/static/images/chart.png' 
    plt.savefig(chart_path)

    # Pass the chart path to the template
    context = {'chart_path': chart_path}

    # Render the template with the data
    return render(request, 'registrations/management_dashboard.html', context)
```
<img src="./files/image/chart.png">

- Line chart showing `Trends in Inspections by Month`
```python
def inspections_by_month(request):
    # Create a MongoClient instance
    client = MongoClient('mongodb+srv://Kelvin2001:Ooiyj0131@cluster0.cokgc4s.mongodb.net/')

    # Access the MongoDB database
    db = client['AA']

    # Access the collection named "city_inspectionsDataset"
    collection = db['city_inspectionsDataset']

    # Query the collection and retrieve the JSON data
    data = list(collection.find())

    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Extract the month from the 'date' column
    df['month'] = df['date'].dt.month

    # Calculate the number of inspections by month
    inspections_by_month = df.groupby('month').size()

    # Plot the line chart
    plt.plot(inspections_by_month.index, inspections_by_month.values, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Number of Inspections')
    plt.title('Trends in Inspections by Month')
    plt.xticks(range(1, 13))

    # Save the chart to a file
    chart_path = 'q3_app/static/images/inspections_by_month.png'
    plt.savefig(chart_path)

    # Pass the chart path to the template
    context = {'chart_path': chart_path}

    # Render the template with the data
    return render(request, 'registrations/management_dashboard.html', context)
```
<img src="./files/image/inspections_by_month.png">

### 3. Create templates for chart.
```python
 <h1>Number of Inspections by Sector (Top 5)</h1>
      <div class="chart-image">
         <img src="{% static 'images/chart.png' %}" alt="Inspections by Sector" />
      </div>
 <h1>Trends in Inspections by Month</h1>
      <div class="chart-image">
         <img src="{% static 'images/inspections_by_month.png' %}" alt="Inspections by Sector" />
      </div>
```

### 4. Path settings.
In `urls.py`:
```python
path('inspections_by_sector/', inspections_by_sector, name='inspections_by_sector'),
path('inspections_by_month/', inspections_by_month, name='inspections_by_month'),
```
In `settings.py`:
```python
STATIC_URL = '/static/'
```
In `management_dashboard.html`:
```python
{% load static %}
```

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




