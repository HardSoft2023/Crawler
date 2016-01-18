# coding=utf-8
print '你好'
import re

bigDps = '''译　　 名　远离尘嚣/疯恋佳人(港)/远离尘嚣：珍爱相随(台)<br />◎片　　 名　Far From the Madding Crowd<br />◎年　　 代　2015<br />◎国　　 家　英国/美国<br />◎类　　 别　剧情/爱情<br />◎语　　 言　英语<br />◎字　　幕　中英双字幕<br />◎IMDb评分　7.2/10 from 5,664 users<br />◎文件格式　BD-RMVB<br />◎视频尺寸　1280 x 720<br />◎文件大小　1CD<br />◎片　　 长　118 min<br />◎导　　 演　托马斯&middot;温特伯格 Thomas Vinterberg<br />◎主　　 演　凯瑞&middot;穆里根 Carey Mulligan<br />　　　　　　 马提亚斯&middot;修奈尔 Matthias Schoenaerts<br />　　　　　　 麦克&middot;辛 Michael Sheen<br />　　　　　　 汤姆&middot;斯图里奇 Tom Sturridge<br />　　　　　　 朱诺&middot;坦普尔 Juno Temple<br />　　　　　　 希尔顿&middot;麦克雷 Hilton McRae<br />　　　　　　 杰西卡&middot;巴登 Jessica Barden<br />　　　　　　 布莱德利&middot;豪尔 Bradley Hall<br />　　　　　　 Tilly Vosburgh<br />　　　　　　 马克&middot;温格特 Mark Wingett<br />　　　　　　 Dorian Lough<br />　　　　　　 哈利&middot;皮考克 Harry Peacock<br />　　　　　　 Victor McGuire<br />　　　　　　 Jody Halse<br /><br />◎简　　介<br /><br />　　在维多利亚时代，美丽女孩芭丝谢芭（凯瑞&middot;穆里根 Carey Mulligan 饰）来到一个远离尘嚣的乡村，继承叔叔的遗产。她的坚毅独立，她的自信气质，使三个男人为她倾倒。他们分别是俊朗敦厚的牧羊人加布尔（马提亚斯&middot;修奈尔 Matthias Schoenaerts 饰）、 品味成熟的贵族（麦克&middot;辛 Michael Sheen 饰）以及狂野鲁莽的军官（汤姆&middot;斯图里奇 Tom Sturridge 饰）。三人都真挚地爱着芭丝谢芭，而她会做出怎样的选择? <br /><br />　　影片改编自英国作家托马斯&middot;哈代的成名作《远离尘嚣》。<br /><br /><img border="0" src="http://image17.poco.cn/mypoco/myphoto/20150727/23/175491213201507272322243329330953518_001.jpg" alt="" />
'''
leibie = '译　　 名　(?P<leibie>.*?)<'
# yuyan = '◎语　　言　(?P<yuyan>.*?)<br />◎字　　幕'
# zimu = '◎字　　幕　(.*?)<br />◎IMDb评分'
# pingfen = '◎IMDb评分(&nbsp;)? (?P<pingfen>.*?)/10'

match = re.search(leibie, bigDps)
# if match == None:
#     leibie = '◎类　　型(&nbsp;)?(?P<leibie>.*?)<br />'
#     match = re.search(leibie, bigDps)
# if match == None:
#     leibie = '◎电影类型(&nbsp;)?(?P<leibie>.*?)<br />'
#     match = re.search(leibie, bigDps)
print match.group('leibie')
# print match.group('pianming')
# print match.group('niandai')
# print match.group('guojia')
# print match.group('leibie')
# print match.group('yuyan')
# match = re.search(zimu, bigDps)
# print match.lastgroup
# print match.group('pingfen')
