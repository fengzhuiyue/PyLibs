#!/usr/bin/env python
#coding=utf-8
#COM读写Excel,输出某月日报

from win32com.client import Dispatch 
import win32com.client 
import win32api
import os
class ExcelHelper:
    def __init__(self, filename=None):
		self.xlApp = win32com.client.Dispatch('Excel.Application') 
		if filename:
			self.filename=filename
			if os.path.exists(self.filename):
				self.xlBook=self.xlApp.Workbooks.Open(filename)
			else:
				self.xlBook= self.xlApp.Workbooks.Add()
		else:
			self.xlBook= self.xlApp.Workbooks.Add()
			self.filename='Untitle'
			
    def save(self, newfilename=None):
		if newfilename:
			self.filename = newfilename
		self.xlBook.SaveAs(self.filename)   
           
	def close(self): 
		self.xlBook.Close(SaveChanges=0) 
		del self.xlApp 
   
	def copySheet(self, before): 
		"copy sheet" 
		shts = self.xlBook.Worksheets 
		shts(1).Copy(None,shts(1))
   
	def newSheet(self,newSheetName):
		sheet=self.xlBook.Worksheets.Add()
		sheet.Name=newSheetName
		sheet.Activate()
   
	def activateSheet(self,sheetName):
		self.xlBook.Worksheets(sheetName).Activate()
	   
	def activeSheet(self):
		return self.xlApp.ActiveSheet;   
   
	def getCell(self, row, col,sheet=None): 
		"Get value of one cell" 
		if sheet:
			sht = self.xlBook.Worksheets(sheet) 
		else:
			sht=self.xlApp.ActiveSheet   
		return sht.Cells(row, col).Value 
   
	def setCell(self, row, col, value,sheet=None): 
		"set value of one cell" 
		if sheet:
			 sht = self.xlBook.Worksheets(sheet) 
		else:
			 sht=self.xlApp.ActiveSheet   
		
		sht.Cells(row, col).Value = value 
	   
	def getRange(self, row1, col1, row2, col2,sheet=None): 
		"return a 2d array (i.e. tuple of tuples)" 
		if sheet:
		   sht = self.xlBook.Worksheets(sheet) 
		else:
		   sht=self.xlApp.ActiveSheet   
		return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value 
	
	def mergeCell(self, row1, col1, row2, col2,sheet=None):
		if sheet:
			sht = self.xlBook.Worksheets(sheet) 
		else:
			sht=self.xlApp.ActiveSheet  
		return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Merge() 
	def rowsCount(self):
		"return used rows count"
		sht=self.activeSheet()
		return  sht.UsedRange.Rows.Count
           
    if __name__ == "__main__": 
        pass
