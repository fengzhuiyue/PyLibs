import sys  
import time
import os  
import csv
import xlwt
from openpyxl.reader.excel import load_workbook  


TempList=[]
list=[]
f=open('BOS_RD022820.DAT', 'r')
try:
	list=f.readlines()
finally:
	f.close()            

ListLenth=len(list)
w = csv.writer(file("LIST.CSV", 'wb'))

for i in range(1,ListLenth-1):           
	TempList.append([list[i][1:13]])
	
	
w.writerows(TempList)
