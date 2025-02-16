#!/bin/bash

echo "🚀 Setting up project directory structure..."

# Create main project folder (if not already inside)
#mkdir -p space-anomaly-detection
#cd space-anomaly-detection

# Create subdirectories
mkdir -p data notebooks src models docs

# Create Python files in src
touch src/data_pipeline.py
touch src/preprocessing.py
touch src/anomaly_detection.py
touch src/prediction.py
touch src/visualization.py
touch src/alerts.py
touch src/__init__.py

# Create README and requirements file
touch README.md
touch requirements.txt

# Setup virtual environment
#echo "🔧 Creating virtual environment..."
#python3 -m venv venv
#source venv/bin/activate

# Install dependencies
#echo "📦 Installing dependencies..."
pip install numpy pandas scipy matplotlib seaborn scikit-learn tensorflow keras torch torchvision flask dash plotly requests pydantic fastapi uvicorn pyserial paho-mqtt

# Deactivate virtual environment
#deactivate

echo "✅ Project setup complete!"
echo "To start, activate the environment using: source venv/bin/activate"
