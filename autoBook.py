# coding:utf8
print "草拟吗"
import requests
# import smtplib

url = "http://182.92.171.178:8080/food_post.php"
para = {"name": "郭流芳 陈曦 于志远 黄生波 龙啸", "phone": "123456", "message": "lalala"}
response = requests.get(url, params=para)
print response.content
# receive = "yuzhiyuan@tigerjoys.com"
# send = "guoliufang@tigerjoys.com"
#
# message = """做测试--来自订饭系统"""
#
# # smtObj = smtplib.SMTP("smtp.qq.com", port=25)
# smtObj = smtplib.SMTP("mail.corp.tigerjoys.com", port=25)
# smtObj.sendmail(receive, send, message)
