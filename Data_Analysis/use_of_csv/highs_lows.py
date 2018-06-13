#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-11 10:35:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取最高气温/日期/最低气温
#filename = 'sitka_weather_07-2014.csv'
#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
	#f作为实参对象传递给csv.reader()，创建与文件相关联的阅读器对象reader
	reader = csv.reader(f)
	#将阅读器对象传递给next()，返回文件下一行
	header_row = next(reader)
	#创建空列表
	dates,highs,lows = [],[],[]

	for row in reader:
		'''
		#将包含日期信息的数据（row[0]）转换为datetime对象，并将其附加到列表dates末尾
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)
		#将表示气温的字符串转换成了整型，再将其附加到列表末尾
		high = int(row[1])
		highs.append(high)

		low = int(row[3])
		lows.append(low)
'''

		#增加异常处理
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing date')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

#	print(highs)
    #获取每个元素的索引及值
'''	for index,column_header in enumerate(header_row):
		print(index,column_header)'''

#根据数据绘制图形
fig = plt.figure(dpi = 128,figsize = (10,6))
#将日期、最高气温传递给plot(),颜色透明度alpha
plt.plot(dates,highs,c = 'red',alpha = 0.5)
plt.plot(dates,lows,c = 'blue',alpha = 0.5)
#x值：dates，y值：highs/lows,填充颜色
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.1)
#设置图形的格式
plt.title("Daily high and low temperatures-2014\nDeath Valley,CA",fontsize = 20)
plt.xlabel('',fontsize = 16)
#绘制斜的日期标签
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize = 16)
plt.tick_params(axis = 'both',which = 'major',labelsize = 8)

#保存图表，（文件名，裁剪掉多余）
plt.savefig('temperatures-2014-Death-Valley.png', bbox_inches='tight')

plt.show()
