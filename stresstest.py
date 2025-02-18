import os
import smtplib
import subprocess
import psutil
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
EMAIL = "navyayandapalli@example.com"
PASSWORD = "vezw hukv jkcl sojb"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587 #tls port

# Threshold values (80% usage)
MEMORY_THRESHOLD = 80


# function to send email alerts
def send_email_alert(subject, message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL, EMAIL, text)
    server.quit()

# Function to check if usage exceeds threshold
def check_thresholds(resource_type, usage, threshold):
    if usage > threshold:
        print(f"{resource_type} usage exceeded {threshold}%! Sending alert...")
        send_email_alert(f"{resource_type} Usage Alert", f"{resource_type} usage has exceeded {threshold}%. Current usage: {usage}%.")

# Memory stress test
def memory_stress_test():
    print("Starting Memory Stress Test...")
    total_memory = psutil.virtual_memory().total / (1024 ** 3)  # GB
    available_memory = psutil.virtual_memory().available / (1024 ** 3)
    stress_memory = total_memory * 0.8  # 80% of total memory

    print(f"Total Memory: {total_memory:.2f} GB, Available Memory: {available_memory:.2f} GB")
    print(f"Stressing memory with {stress_memory:.2f} GB for 60 seconds...")

    # Stress memory using stress tool
    stress_cmd = f"stress --vm 1 --vm-bytes {int(stress_memory)}G --timeout 60"
    subprocess.Popen(stress_cmd, shell=True)

    # Monitor memory usage during the stress test
    start_time = time.time()
    while time.time() - start_time < 60:  # Run for 60 seconds
        memory_usage = psutil.virtual_memory().percent
        print(f"Memory Usage: {memory_usage}%")
        check_thresholds("Memory", memory_usage, MEMORY_THRESHOLD)
        time.sleep(5)  # Check every 5 seconds

    
if __name__ == "__main__":
     memory_stress_test()
