import boto3
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

s3_client = boto3.client("s3")
BUCKET_NAME = "space-telemetry-data"
FILE_NAME = "telemetry.csv"

def lambda_handler(event, context):
    """AWS Lambda function to detect anomalies in satellite telemetry data."""
    
    # Download telemetry data from S3
    s3_client.download_file(BUCKET_NAME, FILE_NAME, "/tmp/telemetry.csv")
    df = pd.read_csv("/tmp/telemetry.csv")

    # Run Anomaly Detection Model
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    df["anomaly"] = model.fit_predict(df[["temperature", "radiation", "solar_flux", "battery_voltage"]])

    # Save updated data back to S3
    df.to_csv("/tmp/analyzed_telemetry.csv", index=False)
    s3_client.upload_file("/tmp/analyzed_telemetry.csv", BUCKET_NAME, "analyzed_telemetry.csv")

    return {"statusCode": 200, "body": "Anomaly detection completed!"}
