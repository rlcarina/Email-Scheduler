import smtplib
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("email_scheduler.log"),
        logging.StreamHandler()
    ]
)

# Email configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
SENDER_EMAIL = "your_email@example.com"  # Replace with your email
SENDER_PASSWORD = "your_password"  # Replace with your password
RECIPIENT_EMAIL = "recipient@example.com"  # Replace with recipient email
EMAIL_SUBJECT = "Automated Message"
EMAIL_BODY = "This is an automated email sent every 15 minutes."

def send_email():
    """Send an email with the current timestamp"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = EMAIL_SUBJECT
        
        # Add timestamp to body
        body = f"{EMAIL_BODY}\nSent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to server and send
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        logging.info(f"Email sent successfully to {RECIPIENT_EMAIL}")
        return True
    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")
        return False

def main():
    """Main function to run the email scheduler"""
    logging.info("Email scheduler started")
    
    while True:
        try:
            send_email()
            # Sleep for 15 minutes (900 seconds)
            logging.info("Waiting for 15 minutes before sending next email")
            time.sleep(900)
        except KeyboardInterrupt:
            logging.info("Email scheduler stopped by user")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            # Wait 1 minute before retrying after an error
            time.sleep(60)

if __name__ == "__main__":
    main() 
