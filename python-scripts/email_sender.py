# python-scripts/email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

if __name__ == "__main__":
    subject = sys.argv[1]
    body = sys.argv[2]
    to_email = sys.argv[3]
    from_email = sys.argv[4]
    smtp_server = sys.argv[5]
    smtp_port = int(sys.argv[6])
    password = sys.argv[7]
    send_email(subject, body, to_email, from_email, smtp_server, smtp_port, password)
