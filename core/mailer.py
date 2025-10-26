import smtplib
import ssl
from email.message import EmailMessage
import os

def send_basic_email(sender_email, sender_password, receiver_email, subject, plain_text, html_content=None):
    # Create the email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(plain_text)

    if html_content:
        msg.add_alternative(html_content, subtype="html")

    # Connect securely to SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("✅ Email sent successfully!")
