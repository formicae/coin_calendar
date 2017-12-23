# KBOPredictionAPIService
A micro REST API server that serves KBO prediction-related data

# Service Diagram

An arrow indicates the flow of data. For example, the data scraper component scrapes websites to get raw data and dumps them into the system using the REST api server. Similarly, the prediction model component reads in raw data from the API server, computes prediction results and stores them back into the system via the REST api.  

![Overview of components](../master/doc/diagram.jpg)


