import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go
import os

# Define file path for telemetry data
DATA_FILE = "data/satellite_telemetry.csv"

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("🚀 Real-Time Space Telemetry Data"),
    dcc.Interval(id='interval-update', interval=2000, n_intervals=0),  # Update every 2 seconds
    dcc.Graph(id='live-graph')
])

@app.callback(
    dash.Output('live-graph', 'figure'),
    [dash.Input('interval-update', 'n_intervals')]
)
def update_graph(n):
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)

        fig = go.Figure()

        # Add normal telemetry data
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['temperature'], mode='lines', name='Temperature'))
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['radiation'], mode='lines', name='Radiation'))
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['solar_flux'], mode='lines', name='Solar Flux'))
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['battery_voltage'], mode='lines', name='Battery Voltage'))

        # Add anomaly markers (highlighted as red dots)
        anomalies = df[df['anomaly'] == 1]  # Select anomaly points

        if not anomalies.empty:
            fig.add_trace(go.Scatter(
                x=anomalies['timestamp'],
                y=anomalies['temperature'],
                mode='markers',
                marker=dict(color='red', size=8),
                name='Anomaly Detected'
            ))

        fig.update_layout(
            title="📊 Live Space Telemetry Data with Anomaly Detection",
            xaxis_title="Time",
            yaxis_title="Sensor Readings"
        )

        return fig
    else:
        return go.Figure()

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)