# coding: utf-8
from xlrd import open_workbook 
from xlrd import Book
from xlwt import *
# from xlwt import Workbook,Formula 
# Book.encoding = "utf-8"
wb = open_workbook('Config.xls')  
ws = wb.sheet_by_index(0)

nrows = ws.nrows
rows=[]
print ws.row(1)
# for i in range(1,nrows):
	# rows.append([ws.row(i)])

# wb=Workbook()

# sheet = wb.add_sheet("ThisMonth") 
# i =0
# for row in rows:
	# sheet.write(i,0,row[1])
	# sheet.write(i,1,row[2])
	# sheet.write(i,2,row[3])
	# sheet.write(i,3,row[0])
	# i=i+1
# wb.save("Report.xls")
