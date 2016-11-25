# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
def fetchMessageAll():
    dbConenectMessage = MySQLdb.connect(host='192.168.12.155', user='guoliufang', passwd='tiger2108', db='honeycomb',
                                        use_unicode=True, port=5209, charset='utf8')
    messageExecutor = dbConenectMessage.cursor()
    messageExecutor.execute("""select record_time,uuid,content from honeycomb.sms_zthy_analysis""")
    messageContent = messageExecutor.fetchall()
    return messageContent
def fetchMessageByDay(day):
    dbConenectMessage = MySQLdb.connect(host='192.168.12.155', user='guoliufang', passwd='tiger2108', db='honeycomb',
                                        use_unicode=True, port=5209, charset='utf8')
    messageExecutor = dbConenectMessage.cursor()
    dayEnd = day + " 23:59:59"
    sql = """select record_time,uuid,content from honeycomb.sms_zthy_analysis where record_time BETWEEN '""" + day + """' and '""" + dayEnd + """'"""
    messageExecutor.execute(sql)
    messageContent = messageExecutor.fetchall()
    return messageContent
def getValidMessage(message):
    finished = ('点播了', '已', '感谢您使用')
    for i in finished:
        if i in message:
            return True
    return False
def getSubString(message):
    start = message.index('已')
    leng = 28
    targetStr = message[start:start + leng]
    return targetStr
def getStatus(message):
    baoyue=('订购', '定制', '订制', '办理')
    dianbo=('点播', '感谢您使用')
    cancel = ('取消', '退订')
    for i in dianbo:
        if i in message:
            return 1
    for i in baoyue:
        targetStr=getSubString(message)
        if i in targetStr:
            return 2
    for i in cancel:
        targetStr = getSubString(message)
        if i in targetStr:
            return 0
    return -1
def getSpName(message):
    result_list=[]
    for sp_tuple in sp_channels:
        sp_name = sp_tuple[1].encode(encoding='utf-8')
        if sp_name in message:
            ch_code=getChargeConde('-'+sp_name+'-',message)
            if ch_code == -1:
                continue
            else:
                result_list.append((sp_tuple[0],sp_name,ch_code[0],ch_code[1],ch_code[2],ch_code[3]))
    if len(result_list) > 0:
        return result_list
    return -1
def getChargeConde(sp_name,message):
    for charge_tuple in charge_codes:
        sp_charge_str = charge_tuple[2].encode(encoding='utf-8')
        if sp_name in sp_charge_str:
            start = sp_charge_str.index(sp_name)
            targetStr = sp_charge_str[start+len(sp_name):]
            code_list =targetStr.split('-')
            if len(code_list) > 1:
                for code in code_list:
                    if code in message:
                        return (charge_tuple[0],charge_tuple[1],sp_charge_str,code)
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
# messageContent = fetchMessageByDay(sys.argv[1])
# messageContent = fetchMessageByDay('2016-10-01')
messageContent = fetchMessageAll()
csvfile = open("/data/sdg/guoliufang/other_work_space/ResultCsv.txt", mode='wa+')
# csvfile = open("/Users/LiuFangGuo/Downloads/ResultCsv.txt", mode='wa+')
csvlist=[]
for index in range(len(messageContent)):
    message = messageContent[index][2].encode(encoding='utf-8')
    # message = """订购提醒：您好！您已成功订购由北京中天华宇科技有限责任公司提供的税务杂志精编，10元/月（由中国移动代收费），72小时内退订免费。【发送6700至10086每月免费体验10GB咪咕视频定向流量，可以连续体验3个月！详情 http://url.cn/40C8anS 】"""
    isValid = getValidMessage(message)
    if not isValid:
        csvlist.append((messageContent[index][0],messageContent[index][1],messageContent[index][2],-1,-1,-1,-1,-1,-1,-1))
        continue
    else:
        status = getStatus(message)
        if status > -1:
            sp_name = getSpName(message)
            if sp_name == -1:
                csvlist.append((messageContent[index][0], messageContent[index][1], messageContent[index][2], -1,-1,-1,-1,-1,-1,-1))
                continue
            else:
                for i in sp_name:
                    csvlist.append((messageContent[index][0], messageContent[index][1], messageContent[index][2], status, i[0],i[1],i[2],i[3],i[4],i[5]))
        else:
            csvlist.append((messageContent[index][0], messageContent[index][1], messageContent[index][2], -1,-1,-1,-1,-1,-1,-1))
            continue
# write list
# dbWriteResult = MySQLdb.connect(host='192.168.12.155', user='guoliufang', passwd='tiger2108', db='honeycomb',
#                                 use_unicode=True, port=5209, charset='utf8')
# resultExecutor = dbWriteResult.cursor()
for record in csvlist:
    csvfile.write('|'.join(str(e) for e in record)+"\n")
    # sql = 'INSERT INTO honeycomb.sms_zthy_analysis_clearing VALUES (%s)' %var_string
    # print sql
    # resultExecutor.execute(sql)
