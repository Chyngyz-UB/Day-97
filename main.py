import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set your email and password here
EMAIL = 'usubaliev@gmail.com'
APP_SPECIFIC_PASSWORD = '********!'

# Function to send email reminders
def send_email(subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, APP_SPECIFIC_PASSWORD)
        server.sendmail(EMAIL, EMAIL, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

# Function to send task reminder
def remind_task():
    subject = "Task Reminder"
    message = "Don't forget to complete your task today!"
    send_email(subject, message)

# Schedule the task reminder every day at a specific time
schedule.every().day.at("17:17").do(remind_task)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
