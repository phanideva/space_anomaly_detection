#import smtplib
import pandas as pd
import os

# Email credentials (Use your own or store in a .env file)
#EMAIL_ADDRESS = "your-email@gmail.com"
#EMAIL_PASSWORD = "your-email-password"
#TO_EMAIL = "recipient-email@gmail.com"

# Define file path
DATA_FILE = "data/satellite_telemetry.csv"

#def send_email_alert(subject, message):
#    """Send an email notification when an anomaly is detected."""
#    try:
#        server = smtplib.SMTP("smtp.gmail.com", 587)
#        server.starttls()
#        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#        email_message = f"Subject: {subject}\n\n{message}"
#        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, email_message)
#        server.quit()
#        print("✅ Email alert sent successfully!")
#    except Exception as e:
#        print(f"❌ Failed to send email: {e}")

def check_for_anomalies():
    """Check for anomalies in telemetry data and send alerts."""
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        anomalies = df[df["anomaly"] == 1]  # Select only anomaly rows

        if not anomalies.empty:
            print("🚨 Anomalies detected! Sending email alert...")
            #subject = "🚀 Space Anomaly Alert!"
            #message = f"Anomalies detected in satellite telemetry data:\n\n{anomalies.to_string(index=False)}"
            #send_email_alert(subject, message)
        else:
            print("✅ No anomalies detected.")
    else:
        print("🚨 No telemetry data found!")

if __name__ == "__main__":
    check_for_anomalies()
