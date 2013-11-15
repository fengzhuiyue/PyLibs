import sys
import csv
import cx_Oracle
import filecmp
 
# #connection = raw_input("Enter Oracle DB connection (uid/pwd@database) : ")
# orcl = cx_Oracle.connect(u"username/password@host:1521/sid")
 
# printHeader = True # include column headers in each table output
# tableName=u'xxx'
# # output each table content to a separate CSV file
# csv_file_dest = tableName + ".csv"
# outputFile = open(csv_file_dest,'w') # 'wb'
# output = csv.writer(outputFile, dialect='excel')
# #sql = u"select * from " + tableName

# sql =u'Select file_version, source_cd, business_date, transaction_cd, client_cd, investment_manager_cd, fund_cd, sb_broker, trade_country_cd,status, count(1) from xxxdba.xxx_locate_preborrow group by file_version, source_cd, business_date, transaction_cd, client_cd, investment_manager_cd, fund_cd, sb_broker, trade_country_cd,status order by file_version, source_cd, business_date, transaction_cd, client_cd, investment_manager_cd, fund_cd, sb_broker, trade_country_cd,status'

# #print sql
# curs2 = orcl.cursor()
# curs2.execute(sql)

# if printHeader: # add column headers if requested
	# cols = []
	# for col in curs2.description:
		# cols.append(col[0])
	# output.writerow(cols)

# for row_data in curs2: # add table rows
	# output.writerow(row_data)

# outputFile.close()
if cmp('xxx.csv','xxx2.csv'):
	print 'pass'
# csv1=list(csv.DictReader(open()))
# csv2=list(csv.DictReader(open()))
# set1 = set(csv1)
# set2 = set(csv2)
# print set1-set2
# masterlist = [row for row in csvreader2]
# def compare(status):
	# for row1 in csvreader:
		
		# for row2 in masterlist:
			# if row1!=row2:
				# print row1
				# print row2
				# status='fail'
				# return status
# status=compare(status)
# if status!='fail':
	# print "pass"
