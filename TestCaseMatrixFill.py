import xlrd
import xlwt

data = xlrd.open_workbook('C:\\Test Case Matrix for 2nd Review.xls') #注意这里的workbook首字母是小写

data.sheet_names()
table = data.sheet_by_name(u'Manage Requests')
#获取行数和列数
nrows = table.nrows
# ncols = table.ncols
#获取整行和整列的值（数组）
# i = 1
# table.row_values(i)
# table.col_values(i)
#循环行,得到索引的列表
for rownum in range(table.nrows):
	print table.row_values(rownum)
#单元格
# for i in range(0,nrows):
	# cell_Priority = table.cell(i,4).value
	# if cell_Priority =='C':
		# table.put_cell(i,)
	# else:
		# print "NOT C"
		
# Num = 0

# for i in range(1,nrows):
	# cell_Priority = table.cell(i,4).value
	# if cell_Priority == 'C' or cell_Priority == 'H' :
		# Num=Num+1
		# table.put_cell(i,0,1,Num,0)
table.put_cell(5,0,1,'TTTTTTTTTT',0)
# cell_C4 = table.cell(2,3).value
#分别使用行列索引
cell_A1 = table.row(0)[0].value
cell_A2 = table.col(1)[0].value
#简单的写入
# row = 0
# col = 0
# ctype = 1 # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
# value = 'lixiaoluo'
# xf = 0 # 扩展的格式化 (默认是0)
# table.put_cell(row, col, ctype, value, xf)
# table.cell(0,0) # 文本:u'lixiaoluo'
# table.cell(0,0).value # 'lixiaoluo'.


# For i in range(1,rows1):
# If priority !=null:
    # i<10:
        # ID=`AAA_BBBB_`+priority+`_00`+i
    # elsif i<100:
        # ID=`AAA_BBBB_`+priority+`_0`+i
    # else:
        # ID=`AAA_BBBB_`+priority+`_0`+i

# For i in range(row1,rows2):
# If priority !=null:
    # i<row1+10:
        # ID=`AAA_CCCC_`+priority+`_00`+i
    # elsif i<row1+100:
        # ID=`AAA_CCCC_`+priority+`_0`+i
    # else:
        # ID=`AAA_CCCC_`+priority+`_0`+i
# Num=0
# For i in range(1,nrows):
# If priority !=null:
    # Num=Num+1
