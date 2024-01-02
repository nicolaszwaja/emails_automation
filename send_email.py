import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 465
EMAIL_SERVER = "smtp.gmail.com"

# Load environment variables
current_dir = Path(__file__).parent if "__file__" in locals() else Path(os.getcwd())
envars = current_dir / ".env"
load_dotenv(envars)

# read environment variables
EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")

def send_email(subject, receiver, name, workshop_date, workshop_time, payment_note):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Lets Dance Studio", EMAIL_ADDRESS))
    msg["To"] = receiver
    msg["BCC"] = EMAIL_ADDRESS
    
    # backup version
    msg.set_content(
        f"""\
        Hi {name},

        We hope all is well with you! Just a friendly reminder about the upcoming dance workshops you've signed up for. We're thrilled to share our passion for dance with you and look forward to growing together.

        Remember, the workshops are scheduled for {workshop_date} at {workshop_time}.
        {payment_note} 
        
        Looking forward to dancing with you!

        Best regards,
        Lets Dance Studio.  
        """
    )
    
    # html version
    msg.add_alternative(
        f"""\
        <p><strong>Hey {name},</strong></p>
        <p>We hope all is well with you! Just a friendly reminder about the upcoming dance workshops you've signed up for.<br>
        We're thrilled to share our passion for dance with you and look forward to growing together.</p>
        <p><strong>{payment_note}</strong></p>
        <p>Remember, the workshops are scheduled for <strong>{workshop_date}</strong> at <strong>{workshop_time}</strong>.</p>
        <p>Looking forward to dancing with you!</p>
        <p><strong>Best regards,<br>
        Lets Dance Studio.</strong></p>
        """,
        subtype="html",
    )
    
    try:
        with smtplib.SMTP_SSL(EMAIL_SERVER, PORT) as server:
            server.ehlo()  # You can include this line, although it may not be necessary for SSL connections
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

    except Exception as e:
        print(f"An error occurred: {e}")

        
if __name__ == "__main__":
    send_email(
        subject="Dance workshop reminder",
        receiver="nicola.szwaja@gmail.com",
        name="name",
        workshop_date="workshop_date",
        workshop_time="workshop_time",
        payment_note="payment_note",
    )    