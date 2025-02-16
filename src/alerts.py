import smtplib

def send_alert(message):
    server = smtplib.SMTP("smtp.example.com", 587)
    server.starttls()
    server.login("your_email@example.com", "your_password")
    server.sendmail("your_email@example.com", "recipient@example.com", message)
    server.quit()

def check_for_alerts(df):
    if df['anomaly'].sum() > 0:
        send_alert("Anomaly detected in space telemetry data!")
