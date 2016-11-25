# -*- coding:utf-8 -*-
import requests   
import tushare as ts
import pandas as pd
import csv
import time
import types
 

# 下载所有股票的基本信息
def downAllStock(path):
	print 'Begin download all stocks ...'
	basicData = ts.get_stock_basics()
	print 'get basicDate'
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


# 下载单支股票历史数据，并存入pathSingle
def downSingleStock(stockNo,pathSingle):
	stockSingleTmp = ts.get_hist_data(stockNo)
	if type(stockSingleTmp) == types.NoneType:
		# print 'this stock has no data'
		return False
	singleTemp = pathSingle + stockNo + '.csv'    # 储存该股票历史数据
	stockSingle.to_csv(singleTemp)



# 传入股票代码,计算days[]中三天的股价,返回value
def getSingleStock(stockNo,pathSingle,days):
	print 'Begin get single stock : 【' + stockNo + '】 ...'
	stockSingleTmp = ts.get_hist_data(stockNo)
	if type(stockSingleTmp) == types.NoneType:
		# print 'this stock has no data'
		return 0
	stockSingle = stockSingleTmp.head(40)    # 获取40天的股票信息

	# 获取第1天，第15天，第30天股价
	day = 0  # 第n天的股票数据，最近一天的股票数据作为第1天
	for row in stockSingle['close']:
		if day == days[0]:
			value_1 = row    # 取当天收盘价作为当天价格
			# print 'day:' + str(day) +'  '+'value_1:' + str(value_1) 
		if day == days[1]:
			value_2 = row
			# print 'day:' + str(day) +'  '+'value_2:' + str(value_2)
		if day == days[2]:
			value_3 = row
			# print 'day:' + str(day) +'  '+'value_30:' + str(value_3) 
			# print day
			return [value_1,value_2,value_3]
		day += 1;
	if day < days[2]:
		# print 'Unenough to '+str(days[2])+' days'
		return 0



# 根据三次股票价格，挑选总市值小于50亿的股票，并写入pathRt
# value 为getSingleStock()返回的参数值，row为读取pathSc的一行数据
def chooseStock(value,row,writer):
	# print float(row[6])
	# print value
	valueTotal_1 = float(value[0]) * float(row[6]);
	valueTotal_2 = float(value[1]) * float(row[6]);
	valueTotal_3 = float(value[2]) * float(row[6]);
	# if valueTotal_1 < 500000 and valueTotal_1< 0.95*valueTotal_2 and valueTotal_2< 0.95*valueTotal_3:
	if valueTotal_1 < 550000 and valueTotal_1< 0.90*valueTotal_3 and valueTotal_1< valueTotal_2:
		print 'find the stock !!!!'
		row.append(value[0])
		row.append(value[1])
		row.append(value[2])
		for word in row:
			print word
		writer.writerow(row)
		golds.append(row)
		return True
	return False



# --------------------- 主函数 ------------------------ #

pathSc = 'E:\\Python\\gupiao_API\\down\\all.csv'    # 存储所有股票相关信息
pathRt = 'E:\\Python\\gupiao_API\\down\\result.csv'   # 存储筛选后的相关股票
pathSingle = 'E:\\Python\\gupiao_API\\down\\single\\'  # 存储每只股票相关信息
# pathSc = '/Users/ponycc/Study/test/gupiao_API/down/all.csv'    # 存储所有股票相关信息
# pathRt = '/Users/ponycc/Study/test/gupiao_API/down/result.csv'   # 存储筛选后的相关股票
# pathSingle = '/Users/ponycc/Study/test/gupiao_API/down/single/'  # 存储每只股票相关信息

column = ['id','name','industry','area','pe','outstanding','totals',
	'timeToMarket','value-1','value-2','value-3']

#下载所有股票数据存入pathSc
downAllStock(pathSc)

# 读取fileSc文件数据
fileSc = open(pathSc,'rb')
fileRt = open(pathRt,'wb')
reader = csv.reader(fileSc)
writer = csv.writer(fileRt)
writer.writerow(column)

lines = 0   #当前读取的行数
gold = 0   #符合条件的股票数
golds = [column]  #符合条件的股票
days = [1,12,25]  #挑选股价的三个时间
start = time.clock()

print start

print 'Begin find Gold ...'
for row in reader:
	
	lines += 1
	if lines > 1:
		stockNo = getCode(row[0])
		value = getSingleStock(stockNo,pathSingle,days)
		# sleep(2)
		if value == 0:
			continue
		if type(value) == types.NoneType:
			# print value
			continue
		if chooseStock(value,row,writer):
			gold += 1
			# sleep(5)


fileSc.close()
fileRt.close()
end = time.clock()
print end

print "Used time: %f s" % (end - start)
print 'Find '+str(gold)+' stocks from '+str(lines-1)+' stocks as follow:'
for x in golds:
	for word in x:
		print word