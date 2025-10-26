# Main File
from core.mailer import send_basic_email


def main(): # basic main func
    print("🚀 PyMail Automator - Starting up...")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    sender = "santhoshkumarv12136@gmail.com"
    password = "Sample"
    receiver = "santhoshkumar212004@gmail.com"

    subject = "Test Email from PyMail-Automator 🚀"
    text = "This is a plain text version of the email."
    html = """
    <html>
        <body>
            <h2 style="color:green;">PyMail-Automator Test</h2>
            <p>This is a <b>test email</b> with HTML support!</p>
        </body>
    </html>
    """

    send_basic_email(sender, password, receiver, subject, text, html)