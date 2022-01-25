import smtplib
import ssl
from email.message import EmailMessage

sender_email = input("enter your email ")
receiver_email = input("enter the receiver ")
subject = input("enter the subject ")
body = input("enter the body ")
password = input("password ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("success")