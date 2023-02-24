import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.message import EmailMessage
import ssl

# title
subject = 'Python email test'
key = 'tlmhurqyxibqhdjg'
EMAIL_ADDRESS = '1282119512@qq.com'
EMAIL_PASSWORD = key

# content
msg = MIMEText('<html><h1>hello!</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# send
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
smtp.quit()

# context = ssl.create_default_context()
# sender = EMAIL_ADDRESS
# receiver = EMAIL_ADDRESS
#
# subject = 'test email'
# body = 'hello,this is an email sent by python'
# msg = EmailMessage()
# msg['subject'] = subject
# msg['From'] = sender
# msg['To'] = receiver
# msg.set_content(body)
#
# with smtplib.SMTP_SSL('smtp.qq.com', 465, context=context) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)
