# -*- coding:utf-8 -*-
import requests   
import tushare as ts
import pandas as pd
import csv
import time
 

# 下载所有股票的基本信息
def downAllStock(path):
	print 'Begin download all stocks ...'
	basicData = ts.get_stock_basics()
	basicData.to_csv(path,columns=['name','industry','area','pe','outstanding','totals','timeToMarket'])


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
	print 'Begin get single stock : 【' + stockNo + '】 ...'
	stockSingle = ts.get_hist_data(stockNo).head(40)    # 获取40天的股票信息
	singleTemp = pathSingle + stockNo + '.csv'    # 储存该股票历史数据
	stockSingle.to_csv(singleTemp)
	fileTemp = open(singleTemp,'rb')
	reader = csv.reader(fileTemp)

	# 获取第1天，第15天，第30天股价
	day = 0  # 第n天的股票数据，最近一天的股票数据作为第1天
	for row in reader:
		if day == 1:
			value_1 = row[3]    # 取当天收盘价作为当天价格
			print 'day:' + str(day) +'  '+'value_1:' + value_1 
		if day == 15:
			value_15 = row[3]
			print 'day:' + str(day) +'  '+'value_15:' + value_15
		if day == 30:
			value_30 = row[3]
			print 'day:' + str(day) +'  '+'value_30:' + value_30 
			return [value_1,value_15,value_30]
		day += 1;
	if day < 30:
		print 'Unenough to 30 days'
		return False



# 根据三次股票价格，挑选总市值小于50亿的股票，并写入pathRt
# value 为getSingleStock()返回的参数值，row为读取pathSc的一行数据
def chooseStock(value,row,writer):
	valueTotal_1  = float(value[1]) * float(row[6]);
	valueTotal_15 = float(value[2]) * float(row[6]);
	valueTotal_30 = float(value[3]) * float(row[6]);
	if valueTotal_1 < 500000 and valueTotal_1< 0.9*valueTotal_15 and valueTotal_1< 0.8*valueTotal_30:
		print 'find the stock !!!!'
		print row[1]
		print ' '
		row.append(value[0])
		row.append(value[1])
		row.append(value[2])
		writer.writerow(row)
		golds.append(row)
		return True
	return False



# --------------------- 主函数 ------------------------ #

# pathSc = 'E:\\Python\\gupiao_API\\down\\all.csv'    # 存储所有股票相关信息
# pathRt = 'E:\\Python\\gupiao_API\\down\\result.csv'   # 存储筛选后的相关股票
# pathSingle = 'E:\\Python\\gupiao_API\\down\\single\\'  # 存储每只股票相关信息
pathSc = '/Users/ponycc/Study/test/gupiao_API/down/all.csv'    # 存储所有股票相关信息
pathRt = '/Users/ponycc/Study/test/gupiao_API/down/result.csv'   # 存储筛选后的相关股票
pathSingle = '/Users/ponycc/Study/test/gupiao_API/down/single/'  # 存储每只股票相关信息

column = ['name','industry','area','pe','outstanding',
	'totals','timeToMarket','value-1','value-15','value-30']
# 下载所有股票数据存入pathSc
downAllStock(pathSc)

# 读取fileSc文件数据
fileSc = open(pathSc,'rb')
fileRt = open(pathRt)
reader = csv.reader(fileSc)
writer = csv.writer(fileRt)
writer.writerow(column)

lines = 0   #当前读取的行数
gold = 0   #符合条件的股票数
golds = [columu]  #符合条件的股票

print 'Begin find Gold ...'
for row in reader:
	lines += 1
	if lines > 0:
		stockNo = getCode(str)
		value = getSingleStock(stockNo,pathSingle)
		sleep(2)
		if !value:
			continue
		if chooseStock(value,row,writer):
			gold += 1
			sleep(5)


fileRt.close()

print 'Find '+gold+' stocks from '+lines-1+' stocks as follow:'
for x in golds:
	print x




