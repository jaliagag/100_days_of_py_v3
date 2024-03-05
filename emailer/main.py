# source: https://www.youtube.com/watch?v=zxFXnLEmnb4

from email.message import EmailMessage
from passwords import EMAIL_PASSWORD, EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_BODY, EMAIL_SUBJECT
import ssl
import smtplib

email_sender = EMAIL_SENDER
email_password = EMAIL_PASSWORD
email_receiver = EMAIL_RECEIVER
subject = EMAIL_SUBJECT
body = EMAIL_BODY

em = EmailMessage()

em["from"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

for i in email_receiver:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,i,em.as_string())
    print(f"email sent to {i}")
