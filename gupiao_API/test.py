# -*- coding:utf-8 -*-

import urllib 
import urllib2 
import requests   
import tushare as ts
import pandas as pd
import csv

# 下载所有股票的基本信息
def downAllStock(path):
	print 'begin download all stocks...'
	basicData = ts.get_stock_basics()
	basicData.to_csv(path,columns=['name','industry','area','pe','outstanding','totals','timeToMarket'])
	print 'finish download'


# 获取csv文件行数
def getlines(file):
	num = 0
	for row in csv.reader(file):
		num = num + 1
	print 'lines :'
	print num
	return num;


# 将股票代码改为6位
def getCode(str):
	length = len(str)
	if length == 6:
		return str
	if length != 6:
		for x in xrange(1,6-length):
			str = '0' + str
		return str


# 传入股票代码,计算第1天，第15天，第30天股价
def getSingleStock(stockNo,pathSingle):
	print 'begin get single stock ' + stockNo + '...'
	stockSingle = ts.get_hist_data(stockNo).head(30)    # 获取30天的股票信息
	singleTemp = pathSingle + stockNo + '.csv'    # 储存该股票历史数据
	stockSingle.to_csv(singleTemp)
	fileTemp = open(singleTemp,'rb')
	reader = csv.reader(fileTemp)

	# 获取第1天，第15天，第30天股价
	day = 0  # 第n天的股票数据，最近一天的股票数据作为第1天
	for row in reader:
		if day == 1:
			value_1 = row[3]    # 取当天收盘价作为当天价格
			print "value_1: " + value_1 
		if day == 15:
			value_15 = row[3]
			print "value_15: " + value_15
		if day == 30:
			value_30 = row[3]
			print "value_30: " + value_30 
		day += 1;

	return [value_1,value_15,value_30]


# 根据三次股票价格，挑选总市值小于50亿的股票，并写入pathRt
# value 为getSingleStock()返回的参数值，row为读取pathSc的一行数据
def chooseStock(value,row,writer):
	valueTotal_1 = float(value[1]) * float(row[6]);
	valueTotal_15 = float(value[2]) * float(row[6]);
	valueTotal_30 = float(value[3]) * float(row[6]);
	if valueTotal_1 < 500000 and valueTotal_1< 0.9*valueTotal_15 and valueTotal_1< 0.8*valueTotal_30:
		print 'find the stock !!!!'
		print row[1]



# --------------------- 主函数 ------------------------ #

pathSc = 'E:\\Python\\gupiao_API\\down\\all.csv'    # 存储所有股票相关信息
pathRt = 'E:\\Python\\gupiao_API\\down\\result.csv'   # 存储筛选后的相关股票
pathSingle = 'E:\\Python\\gupiao_API\\down\\single\\'  # 存储每只股票相关信息

# 下载所有股票数据存入pathSc
downAllStock(pathSc)

# 读取fileSc文件数据
csvfileSc = open(pathSc,'rb')

# 把总市值满足条件的股票写入该文件内
# fileRt = file(pathRt,'wb')
# writer = csv.writer(fileRt)


print 'begin read...'
reader = csv.reader(csvfileSc)
lines = getlines(csvfileSc)
line = 0   # 记录当前读取行数
for rows in reader:
	print 'line = '+line
	if line > 0:
		stockNo = getCode(rows[0])
		print '开始计算股票：'+ stockNo
		value = getSingleStock(stockNo,pathSingle)
		print '得到股票价格：'+ value
		# chooseStock(value,row,writer)
		line += 1



# fileRt.close()









# 读取数据存入二维数组
# def readStock(file):
# 	print 'begin read...'
# 	lines = getlines(file)
# 	print lines
# 	reader = csv.reader(file)
# 	i = 0
# 	j = 0
# 	for row in reader:
# 		for word in row:
# 			# stocks[i][j] = word
# 			test = word
# 			j+=1
# 		i+=1

# 	print 'finish read'
# 	return test


