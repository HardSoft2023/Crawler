# coding:utf8
from email.mime.text import MIMEText

print "草拟吗"
import requests
import smtplib

url = "http://182.92.171.178:8080/food_post.php"
para = {"name": "郭流芳 陈曦 于志远 黄生波 龙潇", "phone": "123456", "message": ""}
response = requests.get(url, params=para)
print response.content
'''
先把餐订上再说
'''
# mail_host = "smtp.qq.com"
mail_host = "email.tigerjoys.com"
# mail_port = 465
mail_port = 587
login_user = "guoliufang@corp.tigerjoys.com"
mail_senter = "guoliufang@tigerjoys.com"
login_password = "goaway0323CAONIMA"
email_content = "今天订餐了吗？"
tolist = ["chenxi1105@126.com", "yuzhiyuan@tigerjoys.com", "xushaohua@tigerjoys.com", "zhaogang@tigerjoys.com"]
message = MIMEText(_text=email_content, _charset="utf-8")
message['Subject'] = "订饭了"
message['To'] = ','.join(tolist)
message['From'] = mail_senter
'''
Try cathch 控制邮箱验证因为经常更换密码
'''
try:
    # smtObj = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
    smtObj = smtplib.SMTP(host=mail_host, port=mail_port)
    smtObj.starttls()
    smtObj.login(user=login_user, password=login_password)
    smtObj.sendmail(from_addr=mail_senter, to_addrs=tolist, msg=message.as_string())
except:
    print "屌丝邮箱验证除了问题"
