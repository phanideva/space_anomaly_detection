import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import os
from alerts import check_for_anomalies  # Import the alert system

# Define file path
DATA_FILE = "data/satellite_telemetry.csv"

def detect_anomalies():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)

        if df.empty:
            print("🚨 No data available for anomaly detection.")
            return

        model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        df['anomaly'] = model.fit_predict(df[['temperature', 'radiation', 'solar_flux', 'battery_voltage']])

        # Save results
        df.to_csv(DATA_FILE, index=False)
        print("✅ Anomaly detection complete. Results saved to telemetry file.")
        # Trigger alerts
        check_for_anomalies()
    else:
        print("🚨 No telemetry data found!")

if __name__ == "__main__":
    detect_anomalies()
