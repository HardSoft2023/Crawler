# -*- coding: utf-8 -*-
# print "你好"
import re
import requests

url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_3.html'
root = 'http://www.ygdy8.net'
patternBig = '/templets/img/dot_hor.gif(.*?)</table>'
pattern = '<a href="(.*?)" class="ulink".*?<td colspan="2" style="padding-left:3px">(.*?)</td>'
patternDps = '◎(.*?)</p>'
yiming = '译　　 ?名(&nbsp;)?(?P<yiming>.*?)<'
pianming = '片　　 ?名(&nbsp;)?(?P<pianming>.*?)<'
niandai = '◎年　　 ?代(&nbsp;)?(?P<niandai>.*?)<'
guojia = '◎国　　 ?家(&nbsp;)?(?P<guojia>.*?)<'
leibie = '◎类　　 ?别(&nbsp;)?(?P<leibie>.*?)<'
yuyan = '◎语　　 ?言(&nbsp;)?(?P<yuyan>.*?)<'
zimu = '◎字　　 ?幕(&nbsp;)?(?P<zimu>.*?)<'
pingfen = '◎[iI]MD[bB]评分(&nbsp;)? (?P<pingfen>.*?)/10'
for pageNum in range(1, 27, 1):
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
                print bigDps
                match = re.search(yiming, bigDps)
                if match is not None:
                    print match.group('yiming')
                else:
                    yiming1 = '中 文 名(&nbsp;)?(?P<yiming1>.*?)<'
                    match = re.search(yiming1, bigDps)
                    if match is not None:
                        print match.group('yiming1')
                    else:
                        print '-1'
                match = re.search(pianming, bigDps)
                if match is not None:
                    print match.group('pianming')
                else:
                    pianming1 = '英 文 名(&nbsp;)?(?P<pianming1>.*?)<'
                    match = re.search(pianming1, bigDps)
                    if match is not None:
                        print match.group('pianming1')
                    else:
                        print '-1'
                match = re.search(niandai, bigDps)
                if match is not None:
                    print match.group('niandai')
                else:
                    print '-1'
                match = re.search(guojia, bigDps)
                if match is not None:
                    print match.group('guojia')
                else:
                    guojia1 = '◎地　　区(&nbsp;)?(?P<guojia1>.*?)<'
                    match = re.search(guojia1, bigDps)
                    if match is not None:
                        print match.group('guojia1')
                    else:
                        print '-1'
                match = re.search(leibie, bigDps)
                if match is not None:
                    print match.group('leibie')
                else:
                    leibie1 = '◎类　　型(&nbsp;)?(?P<leibie1>.*?)<'
                    match = re.search(leibie1, bigDps)
                    if match is not None:
                        print match.group('leibie1')
                    else:
                        leibie2 = '◎电影类型(&nbsp;)?(?P<leibie2>.*?)<'
                        match = re.search(leibie2, bigDps)
                        if match is not None:
                            print match.group('leibie2')
                        else:
                            print '-1'
                match = re.search(yuyan, bigDps)
                if match is not None:
                    print match.group('yuyan')
                else:
                    print '-1'
                match = re.search(zimu, bigDps)
                if match is not None:
                    print match.group('zimu')
                else:
                    print '-1'
                match = re.search(pingfen, bigDps)
                if match is not None:
                    print match.group('pingfen')
                else:
                    print '-1'
                print "==================================================================="
