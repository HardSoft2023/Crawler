# coding=utf-8
print '你好'
import re

str = '''◎译　　名　45周年/四十五周年/四十五年/45年(台) <br />◎片　　名　45 Years <br />◎年　　代　2015<br />◎国　　家　英国<br />◎类　　别　剧情/爱情<br />◎语　　言　英语<br />◎字　　幕　中英双字幕<br />◎IMDB评分 7.5/10 2,511 votes<br />◎文件格式　BD-RMVB<br />◎视频尺寸　1280 x 696<br />◎文件大小　1CD<br />◎片　　长　01:35:12<br />◎导　　演　安德鲁&middot;海格 Andrew Haigh<br />◎主　　演　夏洛特&middot;兰普林 Charlotte Rampling<br />　　　　　　多莉&middot;韦尔斯 Dolly Wells<br />　　　　　　汤姆&middot;康特奈 Tom Courtenay<br />　　　　　　杰拉丁妮&middot;詹姆斯 Geraldine James<br />　　　　　　山姆&middot;亚历山大 Sam Alexander<br />　　　　　　Max Rudd<br />　　　　　　David Sibley<br />　　　　　　Hannah Chalmers<br />　　　　　　Richard Cunningham<br />　　　　　　Kevin Matadeen<br /><br />◎简　　介<br /><br />　　就在凯特（Kate）忙于筹备45周年的结婚纪念日之时，她丈夫杰夫（Geoff）突然接到了一条把他的思绪带回过去的消息，他50年前在瑞士阿尔卑斯山因意外丧生的女友的遗体被找到了。 <br /><br />　　凯特和杰夫的内心都受到了极大的震撼却无法交流彼此深藏的不安。杰夫把自己封闭在回忆的世界里，而凯特则竭力压抑自己的嫉妒和焦虑，她还需要专心为聚会做准备，安排音乐、菜单以及其他诸如此类的东西。 <br /><br />　　表面看来，一切如常，但摄影机却敏锐地捕捉了原本和谐的共存逐渐走向失衡的过程。不论是和杰夫共进早餐还是在镇子里独自漫步，凯特都感觉自己越像是一个陌生人。《45周年》中的夫妇二人被意想不到的情绪攫住，被迫面对自己不熟悉的感觉，在这个过程中，他们曾经的好时光仿佛一去不返。在共同生活了45年之后，在他们的结婚纪念日上究竟哪种情绪会占上风呢？ <br /><br />获奖记录<br /><br />柏林国际电影节(2015；第65届) <br /><br />获奖<br />&middot;银熊奖-最佳男演员汤姆&middot;康特奈 Tom Courtenay&nbsp; <br />&middot;银熊奖-最佳女演员夏洛特&middot;兰普林 Charlotte Rampling&nbsp; <br /><br />提名<br />&middot;金熊奖安德鲁&middot;海格 Andrew Haigh<br /><br />第87届美国国家评论协会奖 (2015)<br />十佳独立电影<br /><br />第21届美国评论家选择电影奖 (2016)<br />最佳女主角(提名) 夏洛特&middot;兰普林<br /><br />第36届波士顿影评人协会奖 (2015)<br />最佳女主角 夏洛特&middot;兰普林<br /><br />第41届洛杉矶影评人协会奖 (2015)<br />最佳女主角 夏洛特&middot;兰普林<br /><br /><img border="0" src="http://i4.tietuku.com/019320faf8de53b6.jpg" alt="" /></p>'''
yuyan = '◎语　　言　(?P<yuyan>.*?)<br />◎字　　幕'
zimu = '◎字　　幕　(.*?)<br />◎IMDb评分'
pingfen = '◎IMDb评分(&nbsp;)? (?P<pingfen>.*?)/10'
match = re.search(yuyan, str)
# print match.group('yiming')
# print match.group('pianming')
# print match.group('niandai')
# print match.group('guojia')
# print match.group('leibie')
print match.group('yuyan')
match = re.search(zimu, str)
print match.lastgroup
# print match.group('pingfen')
