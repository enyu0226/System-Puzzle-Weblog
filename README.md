# Insight DevOps Engineering System Puzzle: Weblog

# Introduction

Imagine you work for a company that has a web server running. It's highly important to the company's success that the web server is highly available to ensure a great user experience. Unfortunately, the company currently doesn't have data about the availability of the web server. To fix this, they have tasked an engineer to build a pipeline that processes the logs of the web server, and stores the results in a database. Data scientists can then query the database to analyze the availability of the system. The engineer came up with the following solution:
- The logs are ingested into a RabbitMQ queue (for the purpose of this challenge, this is done via reading a given log file with a Python script - in reality, the logs would be sent straight from the webserver)
- A Python script reads the messages from the RabbitMQ queue, processes it, and stores the results in a PostgreSQL database
- An application server built in Flask queries the database to calculate the percentage of GET requests that were successful
- The application server can be accessed via an nginx web server
All of this is developed with the Docker Engine, and put together with Docker Compose.


Unfortunately, the developer is new to many of these tools, and is having a number of issues. The developer needs your help debugging the system and getting it to work properly.

Additionally, the data scientists requested an additional feature to be extracted from the weblogs - it is your job to add this once you have debugged the system.

# Puzzle details

The codebase included in this repo is nearly functional, but has a few bugs that are preventing it from working properly. The first goal of this puzzle is to find these bugs and fix them. To do this, you'll have to familiarize yourself with the various technologies (Docker, RabbitMQ, nginx, Flask, and Postgres). You definitely don't have to be an expert on these, but you should know them well enough to understand what the problem is.

Assuming you have the Docker Engine and Docker Compose already installed, the developer said that the steps for running the system is to open a terminal, `cd` into this repo, and then enter the command:

    docker-compose up -d

At that point, the web application should be visible by going to `localhost:8080` in a web browser. 

## Weblogs

In this challenge, we simulate incoming weblogs by having a Python script reading weblogs from  weblogs.log. The data in this file is real data from a real webserver. It is a great idea to look at the file to familiarize yourself with the format of the log data.
A typical log entry looks like

    local - - [24/Oct/1994:13:43:13 -0600] "GET index.html HTTP/1.0" 200 3185

More details about the weblogs can be found [here.](http://ita.ee.lbl.gov/html/contrib/Calgary-HTTP.html)

When processing these logs, we extract whether it was a GET request and we use the HTTP staus code to determine whether the request was successful. Look at the [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for an overview over all status codes.
For the purpose of this challenge, a request is considered successful if it returns a status code of the form 2XX.

# Assignments

The challenge consists of the following parts:

- **Correct the bugs to have the basic features working** - The weblogs should get processed, the results should be stored in the database and the webapp should display the rate of successful GET requests.
- **(Extra Credit) Extend the functionality:** The data scientists suspect that local GET requests behave differently than remote GET requests. To help them investigate their suspicion, modify the platform so that it determines and displayes the rate of successful GET requests for local and remote requests separately.

 Both the basic features and the extra credit are implemented and tested.
