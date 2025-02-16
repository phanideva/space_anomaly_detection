import os

print("🚀 Running the Full Space Anomaly Detection Pipeline...")

# Step 1: Generate telemetry data
print("\n▶️ Generating telemetry data...")
os.system("python src/data_pipeline.py")

# Step 2: Run anomaly detection
print("\n▶️ Running anomaly detection...")
os.system("python src/anomaly_detection.py")

# Step 3: Train and run the prediction model
print("\n▶️ Training ML model...")
os.system("python src/prediction.py")

# Step 4: Start the visualization dashboard
print("\n▶️ Starting real-time visualization (Open http://127.0.0.1:8050/ in browser)...")
os.system("python src/visualization.py")