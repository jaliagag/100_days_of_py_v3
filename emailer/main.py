# source: https://www.youtube.com/watch?v=zxFXnLEmnb4

from email.message import EmailMessage
from passwords import EMAIL_PASSWORD, EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_BODY, EMAIL_SUBJECT
import ssl
import smtplib

email_sender = EMAIL_SENDER
email_password = EMAIL_PASSWORD

#email_receiver = "jmfaliaga@gmail.com"
email_receiver = EMAIL_RECEIVER

subject = EMAIL_SUBJECT

body = """
sending you a dummy email biotchhhhh 
100 days of piton, day 1 :) 
este va a ser el repo que voy a usar para llevar registro, ademas del calendario: https://github.com/jaliagag/100_days_of_py_v3
"""

em = EmailMessage()

em["from"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
