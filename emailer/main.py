from email.message import EmailMessage
from passwords import EMAIL_PASSWORD
import ssl
import smtplib

email_sender =  "jaliagadevpythonmailer@gmail.com"
email_password = EMAIL_PASSWORD

email_receiver = "jmfaliaga@gmail.com"

subject = "dummy subject"

body = """
this be a test
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
