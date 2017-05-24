# coding:utf-8
# print("草泥马")
from calendar import monthrange
import psycopg2
import sys
import math


def getFormatStartEnd(yuefen):
    y = yuefen[:4]
    m = yuefen[4:]
    lastday = monthrange(int(y), int(m))
    start = """'""" + str(y) + "-" + str(m) + "-01'"
    end = """'""" + str(y) + "-" + str(m) + "-" + str(lastday[1]) + """ 23:59:59'"""
    return (start, end)


def getRefMap():
    sql_ref = """select * from bdl.honeycomb_sms_bridge_business"""
    gpExecutor.execute(sql_ref)
    ref_tuple_list = gpExecutor.fetchall()
    ref_dict = dict()
    for ref_tuple in ref_tuple_list:
        key = ref_tuple[-1]
        rest = ref_tuple[:-1]
        if key in ref_dict.keys():
            orignal = ref_dict[key]
            orignal.append(rest)
            ref_dict[key] = orignal
        else:
            newList = []
            newList.append(rest)
            ref_dict[key] = newList
    print(ref_dict)
    return ref_dict


def getXiaFa(listTuple, start_end_tp):
    tmpList = []
    restTp = listTuple[0]
    # print("-------------------某一个完整的渠道码" + str(restTp))
    for tp in listTuple:
        # print("这是destnum" + tp[3])
        # print("这是dest_num_code" + tp[4])
        # print("不带*#T的" + str(tp[4])[3:])
        tmp = "'" + str(tp[4])[3:] + "_" + tp[3] + "'"
        tmpList.append(tmp)
    tmpMid = ','.join(tmpList)
    print(tmpMid)
    sql_xifa = """select code_event, count(distinct uuid) from bdl.crab_code_histories where code_union_name in (""" + tmpMid + """) and record_time between """ + \
               start_end_tp[0] + """ and """ + start_end_tp[1] + """ group by code_event order by code_event"""
    print(sql_xifa)
    gpExecutor.execute(sql_xifa)
    xiafa_tuple_List = gpExecutor.fetchall()
    a10 = 0
    a20 = 0
    a30 = 0
    for rTuple in xiafa_tuple_List:
        if rTuple[0] == 10:
            a10 = rTuple[1]
        elif rTuple[0] == 20:
            a20 = rTuple[1]
        elif rTuple[0] == 30:
            a30 = rTuple[1]
    return (tmpMid, a10, a20, a30, restTp[0], restTp[1], restTp[2], restTp[3], restTp[4], restTp[5], restTp[6])


def getWeight(xiafa_result_tuple, sms_count):
    lilun = xiafa_result_tuple[2]
    jiage = xiafa_result_tuple[9]
    z = (jiage - 3.0) / (15.0 - 3.0)
    y = math.log10(lilun)
    w = (sms_count + 0.0) / (xiafa_result_tuple[3] + 0.0)
    return z * y * w


def getStastic(dayStr):
    start_end_tp = getFormatStartEnd(dayStr)
    sql_sms = """select sms_business_text, count(distinct uuid) from bdl.honeycomb_sms_histories_appendix where sms_business_text is not null and status = 'ok' and record_time between """ + \
              start_end_tp[0] + """ and """ + start_end_tp[1] + """ group by sms_business_text"""
    gpExecutor.execute(sql_sms)
    result_records_list = gpExecutor.fetchall()
    for result_tuple in result_records_list:
        # print(result_tuple)
        listTuple = refMap[result_tuple[0]]
        print(listTuple)
        xiafa_result_tuple = getXiaFa(listTuple, start_end_tp)
        weight = getWeight(xiafa_result_tuple, result_tuple[1])
        # recortime,yewuma,xiafa,lilun,sms,shiji,外表连接符，随便其中一个渠道的信息。
        csvlist.append((dayStr, result_tuple[0], result_tuple[1], weight, xiafa_result_tuple[0], xiafa_result_tuple[1],
                        xiafa_result_tuple[2], xiafa_result_tuple[3], xiafa_result_tuple[4], xiafa_result_tuple[5],
                        xiafa_result_tuple[6], xiafa_result_tuple[7], xiafa_result_tuple[8], xiafa_result_tuple[9],
                        xiafa_result_tuple[10]))


# 主程序入口
dbGpsqlConn = psycopg2.connect(database='tjdw', user='tj_root', password='77pbV1YU!T', host='192.168.12.14', port=5432)
gpExecutor = dbGpsqlConn.cursor()
refMap = getRefMap()
csvlist = []
# getStastic('201702')
# getStastic('2017-02')
getStastic(sys.argv[1])
csvfile = open("/data/sdg/guoliufang/mysqloutfile/greeplumResult.txt" + sys.argv[1], mode='wa+')
# csvfile = open("/Users/LiuFangGuo/Downloads/greeplumResult.txt", mode='wa+')
for record in csvlist:
    csvfile.write('|'.join(str(e) for e in record) + "\n")
csvfile.close()
