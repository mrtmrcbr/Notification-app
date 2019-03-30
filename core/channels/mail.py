import os
import smtplib,ssl
from email.message import EmailMessage

FROM_MAIL = os.getenv("FROM_MAIL")
TO_MAIL = os.getenv("TO_MAIL")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_LOGIN_NAME = os.getenv("SMTP_LOGIN_NAME")
SMTP_LOGIN_PASS = os.getenv("SMTP_LOGIN_PASS")

def send_mail_notification(text):
    msg = EmailMessage()
    mail_body = f"---- için yeni bir kayıt bırakıldı\nIletişime geçmek için;\nEmail Adresi: {text}\n\nTelegram bildirimi olarakta gönderildi."
    msg.set_content(mail_body)
    msg['Subject'] = 'New Person for ---- Product'
    msg['From'] = FROM_MAIL
    msg['To'] = TO_MAIL
    context = ssl.create_default_context()
    s = smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT))
    s.ehlo()
    s.starttls(context=context)
    s.ehlo()
    s.login(LOGIN_NAME, LOGIN_PASS)
    s.send_message(msg)
    s.quit()
