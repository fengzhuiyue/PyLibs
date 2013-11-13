#!/usr/bin/env python  
  
from win32com.client import Dispatch  
  
xlApp = Dispatch("Excel.Application")   
xlApp.Visible = 1  
  
# Check if any workbook exists.   
if xlApp.Workbooks.Count == 0:  
	# If not, create a new one.  
	workbook = xlApp.Workbooks.Add()  
else:  
	# If yes, use the first one.  
	workbook = xlApp.Workbooks[0]  
  
# Check if any sheet exists.  
if workbook.Sheets.Count == 0:  
	# If not, add a sheet to current workbook.  
	sheet = workbook.Sheets.Add()  
else:  
	# If yes, use the first sheet of current workbook.  
	sheet = workbook.Sheets[0]  
	  
# Generate the multiplication table(1x9).   
for i in xrange(1,10):  
		sheet.Cells(1, i).Value = i  
		# Set the font color  
		sheet.Cells(1, i).Font.Color = 0xFF0000  
		  
# Set the background color of row1          
sheet.Rows(1).Interior.ColorIndex = 36  
  
sheet.Name = "Table"  
workbook.SaveAs('test.xls')  
xlApp.Quit()  
