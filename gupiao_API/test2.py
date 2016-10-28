# -*- coding:utf-8 -*-

import urllib 
import urllib2 
import requests   
import tushare as ts
import pandas as pd
import csv


# stockSingle = ts.get_hist_data('600848',start='2016-10-01',end='2016-10-28')
# print type(stockSingle)
# print stockSingle


stockSingle = ts.get_hist_data('000875').head(30)
print stockSingle
stockSingle.to_csv('E:\\Python\\gupiao_API\\down\\result.csv')
fileTemp = open('E:\\Python\\gupiao_API\\down\\result.csv','rb')
reader = csv.reader(fileTemp)
for row in reader:
	print type(row)
	print row

