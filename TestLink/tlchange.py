# -*- coding: utf-8 -*-

"""
tlchange
by Kevin Zhang, mailto: zhang.jie8@gmail.com

在csv和符合TestLink要求的xml文件之间相互转换
需安装python，使用方法，在命令行中输入下面的命令
python tlchange.py filename
"""

import os, sys, codecs
from xml.dom import minidom

def csv2xml(cf, xf):
try:
file = codecs.open(cf, 'r', encoding = 'utf-8')
except IOError, message:
print u'无法打开文件：', message
return

buffer = file.read()
file.close()

ls = buffer.split("\'\n\'")

#a special trick
s = ls[0][1:]
ls[0] = s
#print len(ls)

xmldoc = minidom.Document()
root = xmldoc.createElement(u'testsuite')
root.setAttribute(u'name', u'')
xmldoc.appendChild(root)
detailsNode = xmldoc.createElement(u'details')
cdata = xmldoc.createCDATASection(u'\n')
detailsNode.appendChild(cdata)
root.appendChild(detailsNode)

suite1 = None
suite2 = None

for s in ls:
suitename1, suitename2, name, summary, steps, expectedresults = s.split("\',\'")
#print suitename1
caseNode = xmldoc.createElement(u'testcase')
caseNode.setAttribute(u'name', name)
summaryNode = xmldoc.createElement(u'summary')
cdata = xmldoc.createCDATASection(summary)
summaryNode.appendChild(cdata)
caseNode.appendChild(summaryNode)
stepsNode = xmldoc.createElement(u'steps')
cdata = xmldoc.createCDATASection(steps)
stepsNode.appendChild(cdata)
caseNode.appendChild(stepsNode)
resultsNode = xmldoc.createElement(u'expectedresults')
cdata = xmldoc.createCDATASection(expectedresults)
resultsNode.appendChild(cdata)
caseNode.appendChild(resultsNode)

if not suite1:
suite1 = createSuite(xmldoc, suitename1)

if suite2:
if suite2.getAttribute(u'name') != suitename2:
suite1.appendChild(suite2)
suite2 = createSuite(xmldoc, suitename2)
else:
suite2 = createSuite(xmldoc, suitename2)

if suite1.getAttribute(u'name') != suitename1:
suite1.appendChild(suite2)
root.appendChild(suite1)
suite1 = createSuite(xmldoc, suitename1)

suite2.appendChild(caseNode)

suite1.appendChild(suite2)
root.appendChild(suite1)

try:
file = codecs.open(xf, 'w', encoding = 'utf-8')
except IOError, message:
print u'无法打开文件：', message
return

xmldoc.writexml(file)
file.close()

def createSuite(xmldoc, name):
suite2 = xmldoc.createElement(u'testsuite')
suite2.setAttribute(u'name', name)
detailsNode = xmldoc.createElement(u'details')
cdata = xmldoc.createCDATASection(u'\n')
detailsNode.appendChild(cdata)
suite2.appendChild(detailsNode)
return suite2

def xml2csv(xf, cf):
xmldoc = minidom.parse(xf)

root = xmldoc.firstChild
if root.nodeName != u'testsuite':
print u'错误：指定的xml文件不是TestLink能识别的'
return

caselist = []

for i in root.childNodes: #testsuite level 1
if i.nodeName == u'details':
continue
if i.nodeName == u'testsuite':
suitename1 = i.getAttribute(u'name')
#print suitename1
for j in i.childNodes: #testsuite level 2
if j.nodeName == u'details':
continue
if j.nodeName == u'testsuite':
suitename2 = j.getAttribute(u'name')
#print suitename2
for k in j.childNodes: #testcase
if k.nodeName == u'details':
continue
if k.nodeName == u'testcase':
name = k.getAttribute(u'name')
summary = u''
steps = u''
expectedresults = u''
for m in k.childNodes:
if m.nodeName == u'summary':
summary = m.firstChild.nodeValue
if m.nodeName == u'steps':
steps = m.firstChild.nodeValue
if m.nodeName == u'expectedresults':
expectedresults = m.firstChild.nodeValue
#print suitename1, suitename2, name, steps, expectedresults
ls = "\'" + suitename1 + "\',\'" + suitename2 + "\',\'" + name + "\',\'" + summary + "\',\'" + steps + "\',\'" + expectedresults + "\'\n"
caselist.append(ls)
#print len(caselist)
try:
file = codecs.open(cf, 'w', encoding = 'utf-8')
except IOError, message:
print u'无法打开文件：', message
return

for case in caselist:
file.write(case)

file.close()
print u'操作成功'


def main():
try:
fn = sys.argv[1]
except IndexError:
print __doc__
return

ls = fn.lower().split('.')
if ls[-1] == 'csv':
xml_file = fn[0:-3] + 'xml'
csv2xml(fn, xml_file)
elif ls[-1] == 'xml':
csv_file = fn[0:-3] + 'csv'
xml2csv(fn, csv_file)
else:
print u'错误：此工具只能转换csv和xml格式的文件'
return


if __name__ == '__main__':
main() 
