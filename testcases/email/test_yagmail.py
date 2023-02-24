import yagmail


key = 'tlmhurqyxibqhdjg'
EMAIL_ADDRESS = '1282119512@qq.com'
EMAIL_PASSWORD = key
yag = yagmail.SMTP(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD, host='smtp.qq.com')
contents = ['test yagmail']

yag.send(EMAIL_ADDRESS, 'subject', contents)