# Main File
from core.mailer import send_basic_email
from dotenv import load_dotenv
import os

load_dotenv()

def main(): # basic main func
    print("🚀 PyMail Automator - Starting up...")

# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
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