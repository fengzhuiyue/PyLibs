#!/usr/bin/env python
 
#coding=utf-8
 
from win32com import client as wc
 
word = wc.Dispatch('Word.Application')
 
doc = word.Documents.Open('C:\源代码情景分析.doc')
 
doc.SaveAs('C:\源代码情景分析 终稿.html', 8)
 
doc.Close()
 
word.Quit()

