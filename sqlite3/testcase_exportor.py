#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from xlwt import *

con = lite.connect('W:\\SFTestCaseRepository.sqlite')
with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM TestCaseStructure WHERE Proj_Name='xxx'")
    row = cur.fetchone()
    # for row in rows:
        # print row
    SheetName=row[2]
    # print SheetName[0]
# con.close()
# con.close()
wb = Workbook()
t_ws = wb.add_sheet("%s" % SheetName)#写入sheet名称
# style = xlwt.XFStyle()
# styleTitle=easyxf('pattern: pattern solid; font: height 360,bold on;');
styleTitle=easyxf('font: height 360,bold on;');
styleHeader=easyxf('pattern:pattern solid, fore_colour sky_blue; font: bold on;align:wrap on, vert centre, horiz center;border: left thin, bottom thin,top thin, right thin');
styleScenario=easyxf('pattern: pattern solid, fore_colour black; font: color-index white,bold on;');
stylePhase=easyxf('font: height 360,bold on;align:vert centre, horiz center;border: left thin,right thick');
styleScope=easyxf('pattern:pattern solid, fore_colour yellow; font: bold on;align:wrap on, vert centre, horiz center;border: left thin, bottom thin,top thin, right thin');
styleBuild=easyxf('pattern:pattern solid, fore_colour green;align:wrap on, vert centre, horiz center;border: left thin, bottom thin,top thin, right thin');
styleCase=easyxf('align:wrap on, vert centre, horiz center;border: left thin, bottom thin,top thin, right thin');
styleStep=easyxf('align:wrap on;border: left thin, bottom thin,top thin, right thin');
#

t_ws.write(0, 0, SheetName,styleTitle)
t_ws.write_merge(0,0,12,19, 'Phase1',stylePhase)
t_ws.write_merge(0,0,20,25, 'Phase2',stylePhase)
t_ws.write_merge(0,0,26,33, 'Phase3',stylePhase)
t_ws.write_merge(1,2,0,0, 'Test Case ID',styleHeader)
t_ws.write_merge(1,2,1,1, 'Step #',styleHeader)
t_ws.write_merge(1,2,2,2, 'BSD/TAD Section No.',styleHeader)
t_ws.write_merge(1,2,3,3, 'BSD/TAD Section Heading',styleHeader)
t_ws.write_merge(1,2,4,4, 'Purpose/ Description',styleHeader)
t_ws.write_merge(1,2,5,5, 'Smoke Test',styleHeader)
t_ws.write_merge(1,2,6,6, 'Priority',styleHeader)
t_ws.write_merge(1,2,7,7, 'Complexity',styleHeader)
t_ws.write_merge(1,2,8,8, 'Test Steps/Action',styleHeader)
t_ws.write_merge(1,2,9,9, 'Test Data/ Criteria',styleHeader)
t_ws.write_merge(1,2,10,10, 'Expected Results',styleHeader)
t_ws.write_merge(1,2,11,11, 'Esti. Effort (Hrs)',styleHeader)
t_ws.write_merge(1,2,12,12, 'In Scope or Not',styleScope)
for i in range(0,6):
	t_ws.write(1,13+i, 'Build 0%s' %str(i+1),styleBuild)
	t_ws.write(2,13+i, 'Result',styleBuild)
t_ws.write_merge(1,2,19,19, 'Tester',styleScope)
t_ws.write_merge(1,2,20,20, 'In Scope or Not',styleScope)
for i in range(0,4):
	t_ws.write(1,21+i, 'Build 0%s' %str(i+7),styleBuild)
	t_ws.write(2,21+i, 'Result',styleBuild)
t_ws.write_merge(1,2,25,25, 'Tester',styleScope)
t_ws.write_merge(1,2,26,26, 'In Scope or Not',styleScope)
for i in range(0,6):
	t_ws.write(1,27+i, 'Build 0%s' %str(i+11),styleBuild)
	t_ws.write(2,27+i, 'Result',styleBuild)	
t_ws.write_merge(1,2,33,33, 'Tester',styleScope)

FirstScenarioPos=3
t_ws.write(FirstScenarioPos, 0, 'Scenario '+str(row[3])+' - '+row[4],styleScenario)

# NextScenarioPos=TestCaseNo_of_PreScenario*2+Sum_of_TestSteps_of_TestCase_of_PreScenario
#TestCaseNo_of_PreScenario=
# con = lite.connect('W:\\SFTestCaseRepository.sqlite')
with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM TestCaseStructure WHERE Module='%s' and ScenarioID=1" %SheetName)
    row = cur.fetchall()
    # for row in rows:
        # print row
    # print row
    # print SheetName[0]
# con.close()
# 
# row = cur.fetchall()
# 
# Write Case ID
t_ws.write(FirstScenarioPos+1, 0, row[0][5],styleCase)
# Write Case Description


with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM TestCase WHERE TestCaseID='%s'" %row[0][5])
    row = cur.fetchall()
    # for row in rows:
        # print row
    # print row
t_ws.write(FirstScenarioPos+1, 2, str(row[0][3])+'\n'+str(row[0][5]),styleCase)	#BSD/TAD Section No.
t_ws.write(FirstScenarioPos+1, 3, str(row[0][4])+'\n'+str(row[0][6]),styleCase)	#BSD/TAD Section Heading	
t_ws.write(FirstScenarioPos+1, 4, row[0][1],styleCase)	#Purpose/ Description
t_ws.write(FirstScenarioPos+1, 6, row[0][7],styleCase)#Priority
t_ws.write(FirstScenarioPos+1, 7, row[0][8],styleCase)#Complexity
t_ws.write(FirstScenarioPos+1, 11, row[0][9],styleCase)#Esti. Effort (Hrs)
# t_ws.write(FirstScenarioPos+1, 0, row[0][5],styleCase)
with con:    
    cur = con.cursor()    
    cur.execute("SELECT SmokeTest FROM SmokeCase WHERE TestCaseID='%s'" %row[0][0])
    rows = cur.fetchone()	
t_ws.write(FirstScenarioPos+1, 5, row[0][5],styleCase)


with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM TestStep WHERE TestCaseID='%s' order by TestStepID asc" %row[0][0])
    rows = cur.fetchall()
    # for row in rows:
        # print row
    # print row
i=0
for row in rows:
	t_ws.write(FirstScenarioPos+1+1+i, 1, row[1],styleCase)	#Step#
	t_ws.write(FirstScenarioPos+1+1+i, 8, row[2],styleStep)	#Test Steps/Action
	t_ws.write(FirstScenarioPos+1+1+i, 10, row[3],styleStep)	#Test Steps/Action
	i=i+1

	


	

for i in range(1,12):
	t_ws.write(3, i,'',styleScenario)
# t_ws.write(0, 1, )
targetFile="TestCase.xls"
wb.save(targetFile)
