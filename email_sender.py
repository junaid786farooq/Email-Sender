from email.message import EmailMessage
import ssl
import smtplib
# Import the password from a separate file (ensure this file exists and contains the correct password)
from passw import password

# Email credentials
email_sender = "junaid786farooq@gmail.com"
email_password = password

# Recipient's email
email_receiver = "tideda4403@bsomek.com"

# Email content
subject = "Python Project"
body = """
(:This message is send from email-sender project of Python:)
"""

# Creating the email message
email = EmailMessage()
email["From"] = email_sender
email["to"] = email_receiver
email["subject"] = subject
email.set_content(body)

# SSL context for secure connection
context = ssl.create_default_context()

# Sending the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp: # Secure connection to Gmail SMTP server
        smtp.login(email_sender, email_password) # Logging in with sender's email and app-specific password
        smtp.sendmail(email_sender, email_receiver, email.as_string()) # Sending the email
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")