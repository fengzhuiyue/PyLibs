from threading import Thread
from Queue import Queue
from time import sleep
import datetime,time
import urllib2
import sqlite3 as lite
import os
import csv


con = lite.connect('W:\\AtrackChecker.sqlite')
with con:    
    cur = con.cursor()    
    cur.execute("SELECT AtrackID,Name FROM Member order by EID desc")
    rows = cur.fetchall()



TempList=[]
endtime=time.strftime("%m")+'%2f'+time.strftime("%d")+'%2f'+time.strftime("%Y")
starttime=time.strftime("%m")+'%2f'+str(int(time.strftime("%d"))-5)+'%2f'+time.strftime("%Y")
# starttime='08%2f1%2f2013'
# endtime='08%2f31%2f2013'
urls=(['http://xxx/reports/atr001l.cfm?report_start_date='+starttime+'&report_end_date='+endtime+'&report_id=atr001&output=web&department=&employee_number='+str(row[0])+'%20%20%20%20&department_id=sqa%20%20&emp_department_id=sqa%20%20',row[1]] for row in rows )


q = Queue()
NUM = 20
JOBS = 28
st = time.time()

def do_somthing_using(url):
	page=urllib2.urlopen(url[0]).read()
	location=page.index('Total Hours')
	totalHours=page[location+31:location+37]
	TempList.append([url[1],totalHours])
	
def working():
	for url in urls:
		do_somthing_using(url)
		q.task_done()
		time.sleep(1)
		
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()

for i in range(JOBS):
    q.put(i)
	
q.join()
now = time.strftime("%Y%m%d")
w = csv.writer(file('xxx hours by %s.csv' %now, 'wb'))
w.writerows(TempList)
