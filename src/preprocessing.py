import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    df = df.dropna()
    scaler = StandardScaler()
    df[['temperature', 'radiation', 'solar_flux', 'battery_voltage']] = scaler.fit_transform(
        df[['temperature', 'radiation', 'solar_flux', 'battery_voltage']]
    )
    return df
