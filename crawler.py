# -*- coding: utf-8 -*-
# print "你好"
import re
import requests

url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_3.html'
root = 'http://www.ygdy8.net'
patternBig = '/templets/img/dot_hor.gif(.*?)</table>'
pattern = '<a href="(.*?)" class="ulink".*?<td colspan="2" style="padding-left:3px">(.*?)</td>'
patternDps = '◎(.*?)</p>'
yiming = '◎译　　名 (?P<yiming>.*?)<br />'
pianming = '◎片　　名(&nbsp;)?　(?P<pianming>.*?)<br />'
niandai = '◎年　　代　(?P<niandai>.*?)<br />'
guojia = '◎国　　家　(?P<guojia>.*?)<br />'
leibie = '◎类　　别|型　(?P<leibie>.*?)<br />'
yuyan = '◎语　　言　(?P<yuyan>.*?)<br />'
zimu = '◎字　　幕　(?P<zimu>.*?)<br />'
pingfen = '◎IMD[bB]评分(&nbsp;)? (?P<pingfen>.*?)/10'
for pageNum in range(1, 3, 1):
    newUrl = re.sub('list_7_\d', 'list_7_%d' % pageNum, url)
    print newUrl
    response = requests.get(newUrl)
    bigSection = re.findall(patternBig, response.content, re.S)
    for section in bigSection:
        sectionDe = section.decode('gb2312', 'ignore')
        sectionUtf8 = sectionDe.encode('utf-8')
        contentList = re.findall(pattern, sectionUtf8, re.S)
        for contentGroups in contentList:
            print root + contentGroups[0]
            detailPageUrl = root + contentGroups[0]
            detailPageSource = requests.get(detailPageUrl)
            detailPageSourceContent = detailPageSource.content
            dpscde = detailPageSourceContent.decode('gb2312', 'ignore')
            dpscUtf8 = dpscde.encode('utf-8')
            bigDpsUtf8List = re.findall(patternDps, dpscUtf8, re.S)
            for bigDps in bigDpsUtf8List:
                match = re.search(yiming, bigDps)
                print match.group('yiming')
                match = re.search(pianming, bigDps)
                print match.group('pianming')
                match = re.search(niandai, bigDps)
                print match.group('niandai')
                match = re.search(guojia, bigDps)
                print match.group('guojia')
                match = re.search(leibie, bigDps)
                print match.group('leibie')
                match = re.search(yuyan, bigDps)
                print match.group('yuyan')
                match = re.search(zimu, bigDps)
                print match.group('zimu')
                match = re.search(pingfen, bigDps)
                print match.group('pingfen')
                print "==================================================================="
