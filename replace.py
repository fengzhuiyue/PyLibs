iFile = open ( '.\\ImportBorrowResponse\\_ImportBorrowResponse-request201.ifile.dat','r' )
    oFile = open ( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat','r' )
    tFile = open ( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat','w' )
    iCount = len(iFile.readlines())
    iFile.seek ( 0 )
    oCount = len(oFile.readlines())
    oFile.seek ( 0 )
 
    iFile.readline()
    for i in range(17):
        oLine=oFile.readline()
        tFile.write(oLine)
        
    for i in range(iCount-1):
        iLine=iFile.readline()
        iReplace=iLine[2:22]
        oLine=oFile.readline()
        oReplace=oLine[2:22]
        oLineNew=oLine.replace(oReplace,iReplace)
        tFile.write(oLineNew)
        
    for i in range(oCount-iCount-16):
        oLine=oFile.readline()
        tFile.write(oLine)


import sys
import time
import re
 
t=16
for i in range(16,56):
        f=open('13', 'r')
        w=open(str(t),'w')
        for i in range(0,21):   
                w.write(f.readline())
        context=f.readline()
        replacestr=re.compile('13')
        context=replacestr.sub(str(t),context)
        w.write(context)
        for i in range(23,27):  
                w.write(f.readline())
        w.close()
        f.close()
        t=t+1
 
 
# Borrow_File_Write=getBorrowFile()
# f=open('..\\ImportBorrowResponse\\ImportBorrowResponse-request201_backup.dat', 'r')
# content=f.read()
# content = re.sub('\${Borrow_File}', Borrow_File_Write, content)
# f.close()
# f=open('..\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat', 'w')    
# f.write(content)      
# f.close()


iFile = open ( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.ifile.dat','r' )  
     oFile = open ( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat','r' )  
     tFile = open ( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat','w' )  
     iCount = len(iFile.readlines())  
     iFile.seek ( 0 )  
     oCount = len(oFile.readlines())  
     oFile.seek ( 0 )  
    
     iFile.readline()  
     for i in range(17):  
         oLine=oFile.readline()  
         tFile.write(oLine)  
           
     for i in range(iCount-1):  
         iLine=iFile.readline()  
         iReplace=iLine[2:22]  
         oLine=oFile.readline()  
         oReplace=oLine[2:22]  
         oLineNew=oLine.replace(oReplace,iReplace)  
         tFile.write(oLineNew)  
           
     for i in range(oCount-iCount-16):  
         oLine=oFile.readline()  
         tFile.write(oLine)


csv.register_dialect("dat", dat)
 
iFile = csv.reader(open("T-110302-00005607145.dat"),"dat")
tFile = open("T-110302-00005607145.dat",'r' )
oFile = csv.writer(open("table_export.csv","wb"))
#oFile = csv.writer(open("T-110302-00005607145.csv"),"wb")
 
 
# for Record_Type,Log_Number,Broker,CUSIP,Sec_Desc,Share_Qty,Booked_Shares_Qty,Loan_Number,PRICE,AMOUNT,RATE in reader:
    # print Log_Number, CUSIP,Share_Qty,Booked_Shares_Qty,Loan_Number
 
# for LOG_NUMBER,CUSIP,Share_Qty in reader:
    # print LOG_NUMBER,CUSIP,Share_Qty
#iCount = len(iFile.readlines())
 
iCount = len(tFile.readlines())
 
for iLine in iFile:  
    if iFile.line_num == 1:
        oFile.writerow(['Record_Type','Log_Number','Broker','CUSIP','Sec_Desc','Share_Qty','Booked_Shares_Qty','Loan_Number','PRICE','AMOUNT','RATE'])
        continue
    if iFile.line_num ==iCount:
        Log_Number=iLine[1]
        tCount=iLine[5]
        oDate=iLine[2]
        oTime=iLine[3]
        oSB=iLine[4]
        Loan_Number=Log_Number[14:20]
        oFile.writerow(['9',Log_Number,oDate,oTime,oSB,tCount])
        continue
    Log_Number=iLine[1]
    Share_Qty=iLine[5]  
    Loan_Number=Log_Number[14:20]
    oFile.writerow(['1',Log_Number,'test','testxxxx','',Share_Qty,Share_Qty,Loan_Number,'129.9','7','100.34713'])


import sys
import time
import csv
import os
 
class dat(csv.excel):
    delimiter = ","
csv.register_dialect("dat", dat)
readFileHandle = csv.reader(open(".\\ImportBorrowResponse\\ImportBorrowResponse-request201.ifile.dat"),"dat")
rCountFileHandle = open('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.ifile.dat','r' )
writeFileHandle  = open('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat','w')
rCount = len(rCountFileHandle.readlines())
 
 
for rLine in readFileHandle:  
    if readFileHandle.line_num == 1:
        writeFileHandle.write('Record_Type,Log_Number,Broker,CUSIP,Sec_Desc,Share_Qty,Booked_Shares_Qty,Loan_Number,PRICE,AMOUNT,RATE\n')
        continue        
    if readFileHandle.line_num ==rCount:
        Log_Number=rLine[1]
        wCount=rLine[5]
        wDate=rLine[2]
        wTime=rLine[3]
        wSB=rLine[4]
        wLoan_Number=Log_Number[14:20]
        writeFileHandle.write('9,'+Log_Number+','+wDate+','+wTime+','+wSB+','+wCount+'\n') 
        continue    
    Log_Number=rLine[1]
    Share_Qty=rLine[5]  
    wLoan_Number=Log_Number[14:20]
    writeFileHandle.write('1,'+Log_Number+',test'+',testxxxx,'+Share_Qty+','+Share_Qty+','+wLoan_Number+',129.9,7,100.34713'+'\n')
writeFileHandle.close()
rCountFileHandle.close()
 
copyFristFileHandle = open ('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat','r' )
copySecondFileHandle = open ('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat','r' )
copyToFileHandle = open ('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak2.dat','w' )
copyFristCount = len(copyFristFileHandle.readlines())
print copyFristCount
copyFristFileHandle.seek ( 0 )
for i in range(16):
    copyFristLine=copyFristFileHandle.readline()
    copyToFileHandle.write(copyFristLine)
for i in range(copyFristCount-16-6):
    copySecondLine=copySecondFileHandle.readline()
    copyToFileHandle.write(copySecondLine)   
    copyFristFileHandle.readline()    
for i in range(6):
    copyFristLine=copyFristFileHandle.readline()
    copyToFileHandle.write(copyFristLine)
copyFristFileHandle.close()
copySecondFileHandle.close()
copyToFileHandle.close()
 
 
os.remove( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat')
os.rename('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak2.dat','.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat')


csv.register_dialect("dat", dat)   
    iFile = csv.reader(open(".\\ImportBorrowResponse\\ImportBorrowResponse-request201.ifile.dat"),"dat")
    i2File = open('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.ifile.dat','r' )
    oFile = open ( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat','r' )
    tFile = csv.writer(open(".\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat","wb"),"dat")
    iCount = len(i2File.readlines())
    oCount = len(oFile.readlines())
    oFile.seek ( 0 )
    for i in range(17):
        oLine=oFile.readline()
        tFile.writerow(oLine)
        
    for iLine in iFile:  
       if iFile.line_num == 1:
           tFile.writerow(['Record_Type','Log_Number','Broker','CUSIP','Sec_Desc','Share_Qty','Booked_Shares_Qty','Loan_Number','PRICE','AMOUNT','RATE'])
           continue
       if iFile.line_num ==iCount:
           Log_Number=iLine[1]
           tCount=iLine[5]
           oDate=iLine[2]
           oTime=iLine[3]
           oSB=iLine[4]
           Loan_Number=Log_Number[14:20]
           tFile.writerow(['9',Log_Number,oDate,oTime,oSB,tCount])
           continue
       Log_Number=iLine[1]
       Share_Qty=iLine[5]  
       Loan_Number=Log_Number[14:20]
       tFile.writerow(['1',Log_Number,'test','testxxxx','',Share_Qty,Share_Qty,Loan_Number,'129.9','7','100.34713'])
    
    for i in range(oCount-iCount-16):
        oLine=oFile.readline()
        tFile.writerow(oLine)  
  
    iFile.close()
    oFile.close()
    tFile.close() 
    
    
    os.remove( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat')
    os.rename('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat','.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat')
    
   
    
#===============================================================================
# #These code replaces ${Borrow_File} in ImportBorrowResponse\\ImportBorrowResponse-request201.dat
# #to the string return of DBUtil.getBorrowFile()
#    Borrow_File_Write=DBUtil.getBorrowFile()
# 
#    f=open('.\\ImportBorrowResponse\\ImportBorrowResponse-request201_backup.dat', 'r')
#    content=f.read()
#    content = re.sub('\${Borrow_File}', Borrow_File_Write, content)
#    f.close()
#    f=open('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat', 'w')    
#    f.write(content)      
#    f.close()     
# #----------------------------------- 
#===============================================================================

import sys
import time
import csv
import os
 
class dat(csv.excel):
    delimiter = ","
csv.register_dialect("dat", dat)
readFileHandle = csv.reader(open(".\\ImportBorrowResponse\\ImportBorrowResponse-request201.ifile.dat"),"dat")
rCountFileHandle = open('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.ifile.dat','r' )
writeFileHandle  = open('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat','w')
rCount = len(rCountFileHandle.readlines())
 
 
for rLine in readFileHandle:  
    if readFileHandle.line_num == 1:
        writeFileHandle.write('Record_Type,Log_Number,Broker,CUSIP,Sec_Desc,Share_Qty,Booked_Shares_Qty,Loan_Number,PRICE,AMOUNT,RATE\n')
        continue        
    if readFileHandle.line_num ==rCount:
        Log_Number=rLine[1]
        wCount=rLine[5]
        wDate=rLine[2]
        wTime=rLine[3]
        wSB=rLine[4]
        wLoan_Number=Log_Number[14:20]
        writeFileHandle.write('9,'+Log_Number+','+wDate+','+wTime+','+wSB+','+wCount+'\n') 
        continue    
    Log_Number=rLine[1]
    Share_Qty=rLine[5]  
    wLoan_Number=Log_Number[14:20]
    writeFileHandle.write('1,'+Log_Number+',test'+',testxxx,'+Share_Qty+','+Share_Qty+','+wLoan_Number+',129.9,7,100.34713'+'\n')
writeFileHandle.close()
rCountFileHandle.close()
 
copyFristFileHandle = open ('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat','r' )
copySecondFileHandle = open ('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak.dat','r' )
copyToFileHandle = open ('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak2.dat','w' )
copyFristCount = len(copyFristFileHandle.readlines())
print copyFristCount
copyFristFileHandle.seek ( 0 )
for i in range(16):
    copyFristLine=copyFristFileHandle.readline()
    copyToFileHandle.write(copyFristLine)
for i in range(copyFristCount-16-6):
    copySecondLine=copySecondFileHandle.readline()
    copyToFileHandle.write(copySecondLine)   
    copyFristFileHandle.readline()    
for i in range(6):
    copyFristLine=copyFristFileHandle.readline()
    copyToFileHandle.write(copyFristLine)
copyFristFileHandle.close()
copySecondFileHandle.close()
copyToFileHandle.close()
 
 
os.remove( '.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat')
os.rename('.\\ImportBorrowResponse\\ImportBorrowResponse-request201.bak2.dat','.\\ImportBorrowResponse\\ImportBorrowResponse-request201.dat')
