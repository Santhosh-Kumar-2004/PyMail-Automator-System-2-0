# Main File
from core.mailer import send_basic_email
from dotenv import load_dotenv
import os
from core.mailer import send_email_with_attachments

load_dotenv()

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

        send_basic_email(sender, password, receiver, subject, text, html)


# The Second function added on Phase 2   
def sending_with_files():
    # if __name__ == "__main__":
    print("🚀 PyMail Automator - Sending email with attachments...")
    load_dotenv()

    sender = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

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


    
if __name__ == "__main__":
    main()
    # basic_email_sender()
    # send_email_with_attachments()