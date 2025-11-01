# Main File
import time
import random
from dotenv import load_dotenv
import os
from core.mailer import send_basic_email
from core.mailer import send_email_with_attachments
from core.csv_reader import load_recipients
# from core.csv_reader import \
from core.logger_config import logger

load_dotenv()

# logger = get_logger(__name__)

# sample root function which shows the python runnning state
def main(): # basic main func
    print("🚀 PyMail Automator - Starting up...")




# The first function added on Phase 1
def basic_email_sender():
    if __name__ == "__main__":

        load_dotenv()

        sender = os.getenv("SENDER_EMAIL")
        password = os.getenv("SENDER_PASSWORD")
        receiver = os.getenv("RECEIVER_EMAIL")

        subject = "Test Email from PyMail-Automator 🚀"
        text = "This is a plain text version of the email."
        html = """
        <html>
            <body>
                <h1 style="color:red;">Santhosh's PyMail Test</h1>
                <h2 style="color:green;">PyMail-Automator</h2>
                <p>This is a <b>test email</b> with HTML support!</p>
            </body>
        </html>
        """
        print("Completed the Email sending operation!")

        send_basic_email(sender, password, receiver, subject, text, html)

# Helps to run the first basic function
# if __name__ == "__main__": 
#     main()
    # basic_email_sender()
    # sending_with_files()


# The Second function added on Phase 2   
def sending_with_files():
    if __name__ == "__main__":
        print("🚀 PyMail Automator - Sending email with attachments...")
        load_dotenv()

        sender = os.getenv("SENDER_EMAIL")
        password = os.getenv("SENDER_PASSWORD")
        receiver = os.getenv("RECEIVER_EMAIL3")

        subject = "Test Email with Attachments 📎"
        text = "This email includes one or more attachments."
        html = """
        <html>
            <body>
                <h3>PyMail Automator - Attachment Test</h3>
                <p>This email contains attachments. Please check below.</p>
            </body>
        </html>
        """

        # ✅ Add one or more attachments
        attachments = [
            # "sample.pdf",       
            # "example.jpg",
            "data.txt"

        ]

        send_email_with_attachments(sender, password, receiver, subject, text, html, attachments)

#Helps to run the second function attachment
# if __name__ == "__main__":
#     main()
#     # basic_email_sender()
#     sending_with_files()

def loading_recipients():
    if __name__ == "__main__":
        recipients = load_recipients()
        print("Loaded recipients:", recipients)

if __name__ == "__main__":
    main()
    # loading_recipients()

def loopy_email_sender():
    print("🚀 PyMail Automator - Bulk Email Sending Phase...")
    
    sender = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")
    csv_path = "data/recipients.csv"

    # Read recipients from CSV
    recipients = load_recipients(csv_path)

    subject = "Special Announcement from PyMail Automator 🚀"
    text_template = "Hi {name},\nThis is a personalized test email!"
    html_template = """
    <html>
        <body>
            <h2 style="color:blue;">Hello {name},</h2>
            <p>This is a <b>personalized</b> HTML email from PyMail Automator. Be happy to connect with the future!</p>
        </body>
    </html>
    """

    for recipient in recipients:
        name = recipient["name"]
        email = recipient["email"]

        text = text_template.format(name=name)
        html = html_template.format(name=name)

        try:
            send_basic_email(sender, password, email, subject, text, html)
            logger.info(f"Email sent successfully to {name} ({email}) ✅")

        except Exception as e:
            logger.error(f"Failed to send email to {name} ({email}) ❌ | Error: {e}")

        # Random delay between 3–7 seconds
        delay = random.uniform(3, 7)
        logger.info(f"⏳ Waiting {delay:.2f} seconds before next email...")
        time.sleep(delay)

    print("✅ All emails in a loopy format processed successfully!")