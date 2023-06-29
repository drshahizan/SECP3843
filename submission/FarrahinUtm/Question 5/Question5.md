<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: NURFARRAHIN BINTI CHE ALIAS
#### Matric No.: A20EC0121
#### Dataset: Mflix

## Question 5 (a)
a.	How can the performance of the portal be optimized when dealing with large volumes of JSON data from the dataset, especially during dashboard visualizations? Please provide an illustrative solution with code and screenshots.

We can take the following actions to improve a portal's efficiency while handling big amounts of JSON data during dashboard visualisations:

1. decrease the dataset size: If at all possible, try to decrease the size of the JSON dataset by removing extraneous information or combining the information at the server level before sending it to the site.

2. Implement server-side pagination: Based on the requested page size, receive only a portion of the JSON data using server-side pagination rather than obtaining the entire set at once. Performance is enhanced because less data is delivered to the gateway.

3. Utilise downsampling or data sampling methods: When working with extremely large datasets, sampling the data can give visualisations a good approximation without having to load and analyse the complete dataset. It is possible to speed up calculation and rendering via stratified sampling or by randomly selecting samples.

4. Improve JSON parsing and rendering: To prevent any performance snags, make sure that the JSON data is efficiently parsed on the client side. Additionally, optimise the rendering process by rendering only the viewable area of the dashboard using methods like virtualization to shorten the rendering time and improve performance.

## Question 5 (b)
Create a dashboard utilizing a JSON dataset, and provide a comprehensive description of its functionalities. You may include relevant code snippets and screenshots that illustrate the solution implemented.
I will be using MongoDB Charts

**Prerequisite**
- Register for a MongoDB Atlas account
- Setup databases and collections while creating a project.

1.GOt to MONGODB ATLAS and click charts

![Screenshot (302)](https://github.com/drshahizan/SECP3843/assets/121208097/44053d00-7b02-495e-980c-240adad5c480)


2.Click on chart builder
![Screenshot (289)](https://github.com/drshahizan/SECP3843/assets/121208097/7969f0df-3d10-4742-aa6e-e8ba9c5a8d2c)

3.Click the Add New Dashboard to create the dashboard. I named it Visualization

**1st chart: geo scatter for location of theaters**

![Screenshot (305)](https://github.com/drshahizan/SECP3843/assets/121208097/89541145-99ac-4c70-bd4b-73da60d4add1)

**2nd chart: group combo chart**

![Screenshot (306)](https://github.com/drshahizan/SECP3843/assets/121208097/cec74b0f-5ae2-4cd2-a9b0-ea4037bffbcf)

**3rd chart: gauge for sum of comments**

![Screenshot (307)](https://github.com/drshahizan/SECP3843/assets/121208097/1951150f-1293-4733-b1ce-be5c14b770ec)

**4th chart: doughnout chart**

![Screenshot (308)](https://github.com/drshahizan/SECP3843/assets/121208097/ac4b621e-338f-4865-8237-3bb3fa10f07a)

**Here is the finalised dashboard**

![Screenshot (309)](https://github.com/drshahizan/SECP3843/assets/121208097/33066bbb-d2b1-490a-b90d-c143ab082eb0)


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


