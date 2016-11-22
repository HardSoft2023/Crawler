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
    messageExecutor.execute("""select record_time,uuid,content from honeycomb.sms_zthy_analysis""")
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
    finished = ('点播了', '已', '感谢您使用')
    for i in finished:
        if i in message:
            return True
    return False
def getStatus(message):
    baoyue=('订购', '定制', '订制', '办理')
    dianbo=('点播', '感谢您使用')
    cancel = ('取消', '退订')
    for i in dianbo:
        if i in message:
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
notfinished = open("/data/sdg/guoliufang/other_work_space/Eception.txt", mode='wa+')
# notfinished = open("/Users/LiuFangGuo/Downloads/Eception.txt", mode='wa+')
for index in range(len(messageContent)):
    message = messageContent[index][2].encode(encoding='utf-8')
    # message = """尊敬的神州行客户，除套餐内包含的业务外，您正在使用的包月业务有：中国移动业务：1、校讯通9元/月；2、和娱乐体验包0元/月；3、和俱乐部0元/月；由中国移动代收费的业务：4、涉税查询(中天华宇)3元/月；5、个税缴纳(中天华宇)5元/月；6、超级乐乐乐(心情互动)15元/月；7、手机支付(手机支付)0元/月；回复业务名称前的数字序号取消对应业务；如需取消多项业务，请回复各业务对应数字序号，中间用逗号分隔。2小时内回复有效，回复免费。以上所列业务资费均为标准资费，实际收费以账单费用为准，您享受的优惠包业务情况请咨询当地营业厅或10086客服热线。查询近五个月已出账账单，可发送“CXZD#年月（如201309）”到10086。中国移动"""
    isValid = getValidMessage(message)
    if not isValid:
        print "-" * 20 + "无效字符串" + "-" * 20
        print message
        notfinished.write(message + "\n")
    else:
        status = getStatus(message)
        if status > -1:
            sp_name = getSpName(message)
            if sp_name == -1:
                print "-" * 20 + "无效字符串" + "-" * 20
                print message
                notfinished.write(message + "\n")
                status = -1
            else:
                print "-" * 20 + "有效字符串" + "-" * 20
                print message
                print str(status)
                for i in sp_name:
                    print i[0]
                    print i[1]
