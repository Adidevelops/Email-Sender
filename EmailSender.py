# go over to gmail and setup 2 factor authentication - kglb dqdj lmhi grux
# generate app password 
# generate function for sending email 
from email.message import EmailMessage
import ssl
import smtplib
def send_email():
    email_sender = 'maadivamsisai@gmail.com'
    email_password='kglb dqdj lmhi grux'

    email_receiver ='adivamsi1998@gmail.com'
    subject ="Hello"
    body = '''
    My name is Adi Vamsi 
    '''
    em =EmailMessage()
    em['From']= email_sender
    em['To']=email_receiver
    em['subject']=subject
    em.set_content(body)

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())