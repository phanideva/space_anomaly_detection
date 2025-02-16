import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import os

# Disable TensorFlow oneDNN logs
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

DATA_FILE = "data/satellite_telemetry.csv"

# Load telemetry data
def load_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)

        if df.empty:
            print("🚨 No data available for training.")
            return None

        return df[['temperature', 'radiation', 'solar_flux', 'battery_voltage']].values
    else:
        print("🚨 No telemetry data found!")
        return None

# Prepare LSTM model
def create_model():
    model = keras.Sequential([
        keras.layers.LSTM(50, return_sequences=True, input_shape=(10, 4)),
        keras.layers.LSTM(50),
        keras.layers.Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    data = load_data()
    if data is None:
        return

    # Reshape data for LSTM
    X_train = np.array([data[i:i+10] for i in range(len(data)-10)])
    y_train = np.zeros(len(X_train))  # Dummy labels for now

    model = create_model()
    model.fit(X_train, y_train, epochs=10, batch_size=1)

    model.save("models/lstm_model.h5")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()
