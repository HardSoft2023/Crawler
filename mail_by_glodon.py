# coding:utf8
from email.mime.text import MIMEText
from sys import argv
print "草拟吗"
import smtplib


# --------main--------------
mail_host = "mail.glodon.com"
mail_port = 587
login_user = "guolf@glodon.com"
mail_senter = "guolf@glodon.com"
login_password = ""
email_content = argv[3]
message = MIMEText(_text=email_content, _charset="utf-8")
message['Subject'] = argv[2]
'''
Try cathch 控制邮箱验证因为经常更换密码
'''
# try:
    # smtObj = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
smtObj = smtplib.SMTP(host=mail_host, port=mail_port)
#smtObj.starttls()
smtObj.login(user=login_user, password=login_password)
smtObj.sendmail(from_addr=mail_senter, to_addrs=argv[1], msg=message.as_string())
# except:
    # print "屌丝邮箱验证除了问题"
