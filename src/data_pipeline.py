import boto3
import random
import time
import pandas as pd
import os
import config

BUCKET_NAME = "space-telemetry-data"

s3_client = boto3.client("s3", aws_access_key_id=config.AWS_ACCESS_KEY, aws_secret_access_key=config.AWS_SECRET_KEY)

def generate_telemetry():
    """Simulate satellite telemetry data."""
    return {
        "timestamp": pd.Timestamp.now(),
        "temperature": random.uniform(-100, 100),
        "radiation": random.uniform(0, 500),
        "solar_flux": random.uniform(0, 10),
        "battery_voltage": random.uniform(5, 15),
        "thruster_status": random.choice([0, 1])
    }

if __name__ == "__main__":
    data = generate_telemetry()
    df = pd.DataFrame([data])
    file_name = "telemetry.csv"
    df.to_csv(file_name, index=False)

    # Upload to AWS S3
    s3_client.upload_file(file_name, BUCKET_NAME, file_name)
    print(f"✅ Data uploaded to S3: {file_name}")

    #time.sleep(5)  # Every 5 seconds
