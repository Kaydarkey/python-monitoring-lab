import time
from mailjet_rest import Client
import psutil

api_key="f2804316e7166f204da18e8d100f80a4"
api_secret="708011f0cb7a8d69fd67f09435644acf"

# Define system time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

# Define System thresholds (10% RAM, 50% free disk space, 10% CPU)
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

# Create function to send email alert
def send_alert(subject, message):
    # Instantiate mailjet client
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "sylvester.darkey@amalitech.com",
                    "Name": "24/7 SysMon"
                },
                "To": [
                    {
                        "Email": "darkeykafui@gmail.com",
                        "Name": "Admin"
                    }
                ],
                "Subject": subject,
                "HTMLPart": f"<h3>{message}</h3>"
            }
        ]
    }
    
    try:
        result = mailjet.send.create(data=data)
        print(f"Email sent: {result.status_code}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Check system metrics
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# Create alert message based on threshold breaches
alert_message = ""

if cpu_usage > CPU_THRESHOLD:
    alert_message += f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
    alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"

# Trigger email alert if threshold breached
if alert_message:
    send_alert(f"Python Monitoring Alert - {formatted_time}", alert_message)
else:
    print("All system metrics are within normal limits.")
