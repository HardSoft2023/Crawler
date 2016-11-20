# coding=utf-8
# print "c草拟吗"
import MySQLdb
import re
"""743268270"""

def fetchMessageAll():
    dbConenectMessage = MySQLdb.connect(host='192.168.12.155', user='guoliufang', passwd='tiger2108', db='honeycomb',
                                        use_unicode=True, port=5209)
    messageExecutor = dbConenectMessage.cursor()
    messageExecutor.execute("""select record_time,uuid,content from honeycomb.sms_zthy_analysis limit 10""")
    messageContent = messageExecutor.fetchall()
    return messageContent


def fetchMessageByDay(day):
    dbConenectMessage = MySQLdb.connect(host='192.168.12.155', user='guoliufang', passwd='tiger2108', db='honeycomb',
                                        use_unicode=True, port=5209)
    messageExecutor = dbConenectMessage.cursor()
    dayEnd = day + " 23:59:59"
    sql = """select record_time,uuid,content from honeycomb.sms_zthy_analysis where record_time BETWEEN '""" + day + """' and '""" + dayEnd + "'"
    print "*" * 100
    print sql
    messageExecutor.execute(sql + """ limit 3""")
    messageContent = messageExecutor.fetchall()
    return messageContent


def getValidMessage(message):
    if re.search('已.*成功.{2}', message):
        print message
def getStatus(message):
    sucess=('订购', '定制', '订制')
    cancel = ('取消', '退订')
    start=message.index('已')
    targetString = message[start:start+13]
    for i in sucess:
        if i in targetString:
            return 1
    for i in cancel:
        if i in targetString:
            return 0
    return -1

def getSpName(message):
    for sp_tuple in sp_channels:
        sp_name = sp_channels[1]


dbConenectReference = MySQLdb.connect(host='192.168.12.66', user='tigerreport', passwd='titmds4sp',
                                      db='TigerReport_production',
                                      use_unicode=True)
executor = dbConenectReference.cursor()
executor.execute("""select id, name from sp_channels""")
sp_channels = executor.fetchall()
executor.execute("""select id,amount,name from charge_codes where status = 1""")
charge_codes = executor.fetchall()
print str(sp_channels).decode(encoding='unicode_escape')
print str(charge_codes).decode(encoding='unicode_escape')
# 其实相当于一个二维数组了。
print charge_codes[1][2]

messageContent = fetchMessageByDay('2016-10-01')
# messageContent = fetchMessageAll()
print str(messageContent).decode(encoding='unicode_escape')
print messageContent[0][2]
# 第一步sp_channels哪一个在里面。。返回一个 sp,,拿着这个 sp 去 charge_codes里面把 对应的若干个 charge_code 找到。
# 拿着这若干个 chargecode，再在短信里面确认是那个 charge_code..返回 charge_code...最后，正则里面的费用这个东西。。。转化成为分。。。
# 最后把所有结果转化为一条记录，直接插入到数据库中去。。。
for index in range(len(messageContent)):
    getValidMessage(messageContent[index][2])

