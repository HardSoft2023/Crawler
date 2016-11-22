# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
def fetchMessageAll():
    dbConenectMessage = MySQLdb.connect(host='192.168.12.155', user='guoliufang', passwd='tiger2108', db='honeycomb',
                                        use_unicode=True, port=5209, charset='utf8')
    messageExecutor = dbConenectMessage.cursor()
    # limit 10
    messageExecutor.execute("""select record_time,uuid,content from honeycomb.sms_zthy_analysis limit 1""")
    messageContent = messageExecutor.fetchall()
    return messageContent
def fetchMessageByDay(day):
    dbConenectMessage = MySQLdb.connect(host='192.168.12.155', user='guoliufang', passwd='tiger2108', db='honeycomb',
                                        use_unicode=True, port=5209, charset='utf8')
    messageExecutor = dbConenectMessage.cursor()
    dayEnd = day + " 23:59:59"
    sql = """select record_time,uuid,content from honeycomb.sms_zthy_analysis where record_time BETWEEN '""" + day + """' and '""" + dayEnd + "'"
    # limit 3
    messageExecutor.execute(sql + """ limit 3""")
    messageContent = messageExecutor.fetchall()
    return messageContent
def getValidMessage(message):
    # 顺序不能变
    finished = ('点播了', '已')
    for i in finished:
        if i in message:
            return True
    return False
def getStatus(message):
    baoyue=('订购', '定制', '订制', '办理')
    dianbo='点播'
    cancel = ('取消', '退订')
    if dianbo in message:
        return 1
    for i in baoyue:
        if (i in message) and (message.index(i) > message.index('已')):
            return 2
    for i in cancel:
        if (i in message) and (message.index(i) > message.index('已')):
            return 0
    print "-" * 20 + "无效字符串" + "-" * 20
    print message
    return -1
def getSpName(message):
    result_list=[]
    for sp_tuple in sp_channels:
        sp_name = sp_tuple[1].encode(encoding='utf-8')
        if sp_name in message:
            ch_code=getChargeConde(sp_name,message)
            if ch_code == -1:
                continue
            else:
                result_list.append((sp_name,ch_code))
    if len(result_list) > 0:
        return result_list
    return -1
def getChargeConde(sp_name,message):
    for charge_tuple in charge_codes:
        sp_charge_str = charge_tuple[2].encode(encoding='utf-8')
        if sp_name in sp_charge_str:
            start = sp_charge_str.index(sp_name)
            targetStr = sp_charge_str[start+len(sp_name)+1:]
            code_list =targetStr.split('-')
            for code in code_list :
                if code in message:
                    return code
    return -1
# ---从这里开始是 main 函数入口
dbConenectReference = MySQLdb.connect(host='192.168.12.66', user='tigerreport', passwd='titmds4sp',
                                      db='TigerReport_production',
                                      use_unicode=True, charset='utf8')
executor = dbConenectReference.cursor()
executor.execute("""select id, name from sp_channels""")
sp_channels = executor.fetchall()
executor.execute("""select id,amount,name from charge_codes""")
charge_codes = executor.fetchall()
print str(sp_channels).decode(encoding='unicode_escape')
print str(charge_codes).decode(encoding='unicode_escape')
# 其实相当于一个二维数组了。
# print charge_codes[1][2]
# messageContent = fetchMessageByDay('2016-10-01')
messageContent = fetchMessageAll()
# print str(messageContent).decode(encoding='unicode_escape')
# print str(messageContent).encode(encoding='utf-8')
# notfinished = open("/data/sdg/guoliufang/other_work_space/Eception.txt", mode='wa+')
notfinished = open("/Users/LiuFangGuo/Downloads/Eception.txt", mode='wa+')
for index in range(len(messageContent)):
    # message = messageContent[index][2].encode(encoding='utf-8')
    message = """尊敬的客户，您向我们反映的问题已处理完毕，现将201605的浙江新万蓝科技有限公司费用计13.00元、201605的北京中天华宇科技有限责任公司梦网费用计1.00元退至您的话费帐户，请注意查收，感谢您的支持! 更多自助便捷服务，请登录浙江移动手机营业
厅 http://t.cn/R5umZFp 。 【业务告知】【优惠提醒】您可以参加加量不加价活动，月费不变，次月及次次月享受50元包1GB的飞享套餐。到期按照50元/月收取。登录手机营业厅办理 http://t.cn/RGdCekj (中国移动)(中国移动)"""
    isValid = getValidMessage(message)
    if not isValid:
        print "-" * 20 + str(isValid) + "-" * 20
        print message
        notfinished.write(message)
    else:
        status = getStatus(message)
        if status > -1:
            print "-" * 20 + "有效字符串" + "-" * 20
            print message
            print str(status)
            sp_name = getSpName(message)
            for i in sp_name:
                print i[0]
                print i[1]