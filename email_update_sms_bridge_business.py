# coding:utf8
# print "草拟吗"
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import requests

max_id_file = "/Users/LiuFangGuo/Downloads/max_id_file"
# 生产环境要用这个
# max_id_file = ""
mail_host = "email.tigerjoys.com"
mail_port = 587
login_user = "guoliufang@corp.tigerjoys.com"
mail_senter = "guoliufang@tigerjoys.com"
login_password = "goaway0323CAONIMA"
tolist = ["guoliufang@tigerjoys.com", "wangqian@tigerjoys.com", "liweizhai@tigerjoys.com"]


def getMaxId(max_id_file):
    with open(max_id_file) as f:
        for line in f:
            return line


def alterMailException():
    smsurl = "http://106.veesing.com/webservice/sms.php?method=Submit"
    smspara = {"account": "cf_wxhdcs456", "password": "wxhdcs@123", "mobile": "15801076287",
               "content": "尊敬的郭流芳先生/女士，恭喜您成功预约短信包月码更新，活动时间：2017！"}
    smsrespone = requests.post(smsurl, smspara)
    print smsrespone.content


def getEmailContent():
    MAX_ID = getMaxId(max_id_file)
    update_sql = "select * from charge_codes where (is_monthly_code=1 or interval_seconds >=2592000) and business_coding=1 and id > " + MAX_ID
    print update_sql
    tiger_report_production_connection = MySQLdb.connect(host='192.168.12.67', user='guoliufang', passwd='d9C83^16Ys',
                                                         db='TigerReport_production', use_unicode=True)
    tiger_report_production_cursor = tiger_report_production_connection.cursor()
    tiger_report_production_cursor.execute(update_sql)
    update_content_list = tiger_report_production_cursor.fetchall()
    header_content = ""
    field_names = [i[0] for i in tiger_report_production_cursor.description]
    for e in field_names:
        header_content += "<th>" + e + "</th>"
    header_html = """<thead><tr>""" + header_content + """</tr></thead>"""
    header_html += """<tbody>"""
    for record_tuple in update_content_list:
        html_table_content = ""
        for e in record_tuple:
            html_table_content += """<td nowrap="nowrap">""" + str(e) + "</td>"
        header_html += "<tr>" + html_table_content + "</tr>"
    header_html += """</tbody>"""
    return header_html


xxtable = getEmailContent()
xxhtml = """
<html><body><p>Hello, Friend.</p>
<p>这是我们本日新增的短信包月码:</p>
<table border="1">
""" + xxtable + """
</tbody>
</table>
<p>Regards,</p>
<p>LiuFangGuo</p>
</body></html>
"""
# message = MIMEText(_text=xxhtml, _charset="utf-8")
# message = MIMEText(_text=email_content, _charset="utf-8")
message = MIMEMultipart("alternative", None, [MIMEText(xxhtml, 'html')])
message['Subject'] = "包月码更新了"
message['To'] = ','.join(tolist)
message['From'] = mail_senter
try:
    # smtObj = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
    smtObj = smtplib.SMTP(host=mail_host, port=mail_port)
    smtObj.starttls()
    smtObj.login(user=login_user, password=login_password)
    smtObj.sendmail(from_addr=mail_senter, to_addrs=tolist, msg=message.as_string())
except:
    print "屌丝邮箱验证除了问题"
    alterMailException()
