# SARIMA Forecasting Model API

This repository contains the code and model for a SARIMA (Seasonal AutoRegressive Integrated Moving Average) forecasting model, packaged in a Flask application, and containerized with Docker for easy deployment. The application provides an HTTP API endpoint that allows users to get predictions from the SARIMA model.

## Project Structure

- `ARIMA-dps.ipynb`: Jupyter notebook with the model creation and evaluation process.
- `df_train.csv`: The dataset used for training the SARIMA model.
- `Dockerfile`: Instructions for Docker on how to build the image.
- `.dockerignore`: Specifies to Docker which files should be ignored in the build process.
- `inference.py`: The Flask application providing the API endpoint.
- `requirements.txt`: A list of Python dependencies necessary to run the Flask app.
- `sarima.pkl`: The serialized SARIMA model ready for predictions.
- `test_point.csv`: An example of a data point to test the API.

## How to Use

### Running Locally

To run the SARIMA model API locally, you will need to have Python and the necessary packages installed. You can install the required packages with:

```bash
pip install -r requirements.txt
```

Then you can run the Flask application:
```bash
python inference.py
```

The application will start on `http://localhost:8080

### Using the API

To get a prediction from the API, send a POST request to `http://localhost:8080/invocations` with the following JSON payload:

```json
{
  "year": 2024,
  "month": 1
}
```
The Dockerfile in the repository allows you to build a Docker image of the application. To build the image, run:
```bash
docker build -t sarima-app .
```

Once the image is built, you can run a container:
```bash
docker run -p 8080:8080 sarima-app
```

This application is designed to be deployed on AWS using Amazon ECS. 


### Historical Analysis
The project began with a visualization and analysis to understand the trends and correlations among different categories of traffic accidents. 

### Model Development Insights
The initial approach involved developing a simple XGBOOST model, which did not perform well. It became clear that a decision tree-based approach would not be able to predict future values while only having past dates as features. An alternative could have been to use data from the past 12 months as features to predict the following month, then use these predictions as features for subsequent forecasts.

However, the decision was made to explore SARIMA models. This presented an opportunity to learn about these models which are popular to predict future data points in a sequence. SARIMA models account for seasonality, trends, and noise in the data, making them a more suitable choice for this type of prediction.

