import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

subject = 'Python send email test'
key = 'tlmhurqyxibqhdjg'
EMAIL_ADDRESS = '1282119512@qq.com'
EMAIL_PASSWORD = key
with open('log.txt', 'rb') as f:
    send_att = f.read()

att = MIMEText(send_att, 'text', 'utf-8')
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="log.txt"'

msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
smtp.quit()
