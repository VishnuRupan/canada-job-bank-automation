import smtplib as st
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import time
from email import encoders
from validate_email import validate_email



def send_mail(send_from, send_to, subject, message, files, server="smtp.gmail.com", port=587, username='', password='', use_tls=True):
  
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))


    part = MIMEBase('application', "octet-stream")
    try:
        with open(files, 'rb') as file:
            part.set_payload(file.read())
    except:
        print('\nThe filename or file path is inncorrect or does not exist. Please make sure you have the correct path name and try again.')
    
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename="{}"'.format(Path(files).name))
    msg.attach(part)

    smtp = st.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()