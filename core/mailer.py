import smtplib
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import mimetypes
from core.logger_config import logger 


# The function created on Phase 1
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
    try: 
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("✅ Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed! Check your app password.")
        logger.error("SMTP Authentication failed — invalid credentials.")

    except Exception as e:
        print(f"❌ Email sending failed: {e}")
        logger.error(f"Unexpected error while sending email: {e}")
        

def send_email_with_attachments(sender_email, sender_password, receiver_email, subject, plain_text, html_content=None, attachments=None):

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(plain_text)

    if html_content:
        msg.add_alternative(html_content, subtype="html")

    # ✅ Add attachments (if any)
    if attachments:
        for file_path in attachments:
            if not os.path.isfile(file_path):
                print(f"⚠️ File not found: {file_path}")
                continue

            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type, mime_subtype = (mime_type or "application/octet-stream").split("/")

            with open(file_path, "rb") as file:
                msg.add_attachment(
                    file.read(),
                    maintype=mime_type,
                    subtype=mime_subtype,
                    filename=os.path.basename(file_path)
                )
            print(f"📎 Attached: {os.path.basename(file_path)}")

    # ✅ Send the email securely
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("✅ Email with attachments sent successfully!")