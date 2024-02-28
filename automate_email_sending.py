''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''




import datetime
import schedule
import os
import smtplib 
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# import email.utils
import time

def sent_all(subject, body, receivers, attachment_path):
    host = "smtp-mail.outlook.com"
    sender = 'ahmedalkayyal@hotmail.com'
    password =getpass.getpass("Enter password: ")
    # receivers=["ahmedalkayya92@gmail.com"]
    message = MIMEMultipart()
    message['Subject'] = subject
    message["From"] = sender
    message["To"] = ", ".join(receivers)
    message.attach(MIMEText(body, 'plain'))
    

    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
        message.attach(part)
        
        
    try:
        smtp = smtplib.SMTP(host, 587)
        smtp.starttls()
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers, message.as_string())
    except Exception as e:
        print(f"an any error :{e}")
    finally: 
           smtp.quit()
    

def send_reports():
    report_folder = r"C:\Users\ASUS\Desktop\mail"
    recipients = ["ahmedalkayyal92@gmail.com"]  

    for recipient in recipients:
        report_file = os.path.join(report_folder, f"report_for_{recipient}.pdf")
        subject = "Daily Report"
        body = "Please find the attached report for today."
        sent_all(subject, body, [recipient], report_file)
        with open("log.txt", "a") as log_file:
            log_file.write(f"Report sent to {recipient} on {datetime.datetime.now()}\n")
            
send_reports()            

schedule.every().day.at("13:20").do(send_reports)
while True:
    schedule.run_pending()
    time.sleep(60) 
    
    
    
    
    
# The provided code is a Python script that automates the sending of email reports with attachments 
# using the `schedule` library for scheduling and the `smtplib`, `getpass`, and `os` libraries for sending emails and managing file paths.


# 1. Libraries:
#    - `datetime`: Used for working with dates and times.
#    - `schedule`: Used for scheduling the sending of email reports at a specific time.
#    - `os`: Used for interacting with the operating system, specifically for managing file paths.
#    - `smtplib`: Used for sending emails using the Simple Mail Transfer Protocol (SMTP).
#    - `getpass`: Used to securely input the email account password without displaying it on the screen.
#    - `email.mime`: Used to create and manipulate email messages, including attachments.

# 2. Functions:
#    - `sent_all`: This function is responsible for sending an email with an optional attachment. 
#     It takes the subject, body, receivers, and attachment path as input, and then sends the email using the specified SMTP server and login credentials.
#    - `send_reports`: This function is used to send daily reports to specified recipients.
#    It retrieves the report file path, constructs the email subject and body, and then calls the `sent_all` function to send the email with the report attached.

# 3. Main Execution:
#    - The `send_reports` function is called once initially to send the reports immediately.
#    - It then schedules the `send_reports` function to run daily at 13:20 using the `schedule` library. 
#     This scheduling loop runs continuously, checking for pending scheduled tasks every 60 seconds.


# also to add schedule library you in python 3.11 you sould in terminal run code pip install schedule and after that you can import it



# as.string()  
#  |
#  +------------MIMEMultipart  
#               |                                                |---content-type  
#               |                                   +---header---+---content disposition  
#               +----.attach()-----+----MIMEBase----|  
#                                  |                +---payload (to be encoded in Base64)