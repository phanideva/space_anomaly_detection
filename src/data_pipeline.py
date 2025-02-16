import random
import time
import pandas as pd
import os

# Create a folder to save data if it doesn't exist
DATA_FOLDER = "data"
FILE_PATH = os.path.join(DATA_FOLDER, "satellite_telemetry.csv")
os.makedirs(DATA_FOLDER, exist_ok=True)

# Simulate live telemetry data
def generate_telemetry():
    return {
        "timestamp": pd.Timestamp.now(),
        "temperature": random.uniform(-100, 100),
        "radiation": random.uniform(0, 500),
        "solar_flux": random.uniform(0, 10),
        "battery_voltage": random.uniform(5, 15),
        "thruster_status": random.choice([0, 1])
    }

if __name__ == "__main__":
    for i in range(10):  # Run for only 10 iterations
        data = generate_telemetry()
        df = pd.DataFrame([data])

        # Save telemetry data to CSV
        df.to_csv(FILE_PATH, mode="a", index=False, header=not os.path.exists(FILE_PATH))
        
        print(f"Saved telemetry data: {data}")
        time.sleep(1)  # Simulate real-time data every second

    print(f"✅ Data saved in {FILE_PATH}")
