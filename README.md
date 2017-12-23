# KBOPredictionAPIService
A micro REST API server that serves KBO prediction-related data

# DataScraper

The data scraper component has one or more parsers, each of which scrapes web pages that contain data of interest. Currently, two parsers are implemented. 

1) The first scrapes match data. That is, which team won on what day against what team and what the score was. e.g. KIA vs SAMSUNG 5:3. 

2) The second parser scrapes match details data. The details include (but are not limited to) for a particular match 1. match scores broken down by each inning, 2. who the starting pitchers were and how they performed, 3. the statistics of each batter by the start of the game and how they performed. The full details can be found in https://github.com/riceluxs1t/KBOPrediction. 

Each scraper runs periodically (most of them daily) and dumps their data into the system via appropriate API end points on the API server.

# Prediction Model

The prediction model component has one or more model that makes predictions based on raw data. Currently, the only type of prediction available is the outcome of a particular match.

# Database

A MySQL instance hosted by the AWS RDS service is used.

# API Server

A Django-REST based RESTful API server hosted on an AWS EC2 instance is conceptually a hub to the system that does the following things.

1. Serves prediction results to data viewers. The data viewers include the front-end website, the Facebook page, etc.

2. Provides an API end-point for the DataScraper component to create new raw data into the system.

3. Serves raw training data to the prediction model

4. Provides an API end-point for the Prediction Model component to create new prediction data into the system.

5. Manages data by writing to and reading from the Database layer.

# View Component
The view component consists of viewers. Each viewer is a logical entity that renders prediction data in its own layout. Viewers include the front-ent website, the Facebook page, etc.

# Service Diagram

An arrow indicates the flow of data. For example, the data scraper component scrapes websites to get raw data and dumps them into the system using the REST api server. Similarly, the prediction model component reads in raw data from the API server, computes prediction results and stores them back into the system via the REST api.  

![Overview of components](../master/doc/diagram.jpg)


### DataScraper -> API Server
puts raw data into the system.

### Prediction Model -> API Server
puts prediction data into the system.

### API Server -> Prediction Model
reads training data from the system. 

### API Server -> View
provides an API end-point for the view component to read prediction data from.

### API Server <-> Database
The database acts as a persistant data storage and serves it to the API server. The API server receives data from other components and puts them into the database.
