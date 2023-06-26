<a href="https://github.com/drshahizan/SECP3843/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/SECP3843" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/network/members"><img src="https://img.shields.io/github/forks/drshahizan/SECP3843" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/SECP3843" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/issues"><img src="https://img.shields.io/github/issues/drshahizan/SECP3843" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/SECP3843/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/SECP3843?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FSECP3843&labelColor=%23d9e3f0&countColor=%23697689&style=flat)


Don't forget to hit the :star: if you like this repo.

# Special Topic Data Engineering (SECP3843): Alternative Assessment

#### Name: Qaisara binti Rohzan
#### Matric No.: A20EC0133
#### Dataset: 04 - Companies

## Question 1 (a)
The answer to the question is divided into the following segments:
* [Requirements](#-requirements)
* [Integrating Django with JSON dataset](#️-integrating-django-with-json-dataset)

### Requirements

As an IT consultant, it is crucial for me to actively participate in overviewing the critical stages and concerns involved in developing a portal that seamlessly integrates various hardware and software applications. Implementing an amount of **5 servers** in this project is possible, whereby the servers are used as:

1. **Main Web Server**: Apache (Used by Django Web Framework)
2. **Database Server 1**: MySQL
3. **Database Server 2**: MongoDB
4. **Additional Application Server**:  Power BI Report Server
5. **Backup Server**

While implementing **5 servers** can be highly irresistible, there are several factors and questions that I must ask myself before deciding the final requirements needed to carry out this project:

* **Scalability**: Will the project's traffic or data volume significantly increase in the future? If the project has the potential for expansion, having numerous servers can provide scalability and properly share the workload.
> Answer: No, the project’s data volume will remain constant over the future. This is because the given project is based on a single dataset that contains 9,500 records of companies listed on Crunchbase. Having numerous servers will only lead to **wasting resources**. Unused servers consume hardware resources such as CPU, memory, storage, and electricity. This might result in inefficient resource utilisation and excessive maintenance and infrastructure costs.

* **Performance**: Consider the project's estimated load and performance requirements. Having numerous servers can aid in load distribution, assuring optimal performance and responsiveness. It enables the use of dedicated resources for specific activities like web hosting, database management, and redundancy.
> Answer: The database management activities can be considered as minimal as the project only revolves around the existing dataset. Moreover, this project would not require an on-premises Power BI Report Server that generates daily reports. Therefore, excess servers such as the Power BI Report and Backup Server may not be used properly, resulting in **inefficient resource allocation**. Valuable resources may have been diverted to other vital components or used to expand the existing infrastructure where it is most needed.

* **Cost and Resources**: Examine the project's budget and resources. Additional servers result in greater hardware, software licence, and maintenance costs. Determine whether the benefits of having many servers exceed the costs.
> Answer: Since the project can be considered as a low-scaled project, whereby all the software applications can be installed locally into our devices and are open-sourced (does not require any software licence). Additional servers can also lead to the **increase of maintenance and support requirements**. Excess servers necessitate additional maintenance, updates, troubleshootings, administrative and support tasks, which might distract resources and attention away from other project objectives.
  
* **Complexity and Management**: Consider the difficulty of managing and maintaining several servers. More servers necessitate more effort for configuration, monitoring, and troubleshooting. Determine whether the project team has the competence and resources to efficiently manage several servers.
> Answer: The project team does not have the competence and resources to efficiently manage several servers due to the lack of experience. The project's aim to seamlessly integrate the Django web framework, the JSON dataset, the MySQL and MongoDB database is straight-forward. Implementing additional and unnecessary servers will only **increase the project's complexity**. Managing and maintaining additional servers that are not actively used might add to the infrastructure's complexity. This complexity can lead to increased maintenance costs and possible sites of failure.

To mitigate these effects, it is best to re-evaluate the server architecture and make modifications based on portal's real usage and requirements. After careful consideration, implementing **3 SERVERS** for this project is best believe a practical approach, whereby the servers are used as:
1. **Main Web Server**: Apache (Used by Django Web Framework)
2. **Database Server 1**: MySQL
3. **Database Server 2**: MongoDB


### Integrating Django with JSON dataset

## Question 1 (b)
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.





## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/special-topic-data-engineering/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


