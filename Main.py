import smtplib
import os

# Your email and app-specific password
email = "experbdtwriter@gmail.com"  # Replace with your actual email
password = "qdquzcfatdodhmsk"  # This is your app-specific password
receiver_email = input("RECEIVER EMAIL: ")
subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

try:
    # Use TLS connection (587) or SSL (465)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, receiver_email, text)
    print("Email has been sent to " + receiver_email)
except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication error: {e}")
except smtplib.SMTPException as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()
