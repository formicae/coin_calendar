# KBOPredictionAPIService
A micro REST API server that serves KBO prediction-related data

# DataScraper

The data scraper component has one or more parsers, each of which scrapes web pages that contain data of interest. Currently, two parsers are implemented. The first scrapes match data. That is, which team won on what day against what team and what the score was. e.g. KIA vs SAMSUNG 5:3. The second parser scrapes match details data. The details include (but are not limited to) for a particular match 1. match scores broken down by each inning, 2. who the starting pitchers were and how they performed, 3. the statistics of each batter by the start of the game and how they performed. The full details can be found in https://github.com/riceluxs1t/KBOPrediction. 

Each scraper runs periodically (most of them daily) and dumps their data into the system via appropriate API end points on the API server.

# Prediction Model

The prediction model component has one or more model that makes predictions based on raw data. Currently, the only prediction available is the outcome of a particular match.

# Service Diagram

An arrow indicates the flow of data. For example, the data scraper component scrapes websites to get raw data and dumps them into the system using the REST api server. Similarly, the prediction model component reads in raw data from the API server, computes prediction results and stores them back into the system via the REST api.  

![Overview of components](../master/doc/diagram.jpg)


### DataScraper -> API Server
