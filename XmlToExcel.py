#!/usr/local/bin/python2.7

# coding: utf-8

'''

Created on 2012/1/31

@author: dennyhsu

@version: 1.0

 

argv[1]:Which column to write. 1,2,3....

argv[2]:CountryName: ar,bg... default:unknow

argv[3]:xmlFilePath default:strings.xml

argv[4]:excelFileName default:output.xls

must install xlwt,xlrd,xlutils

support string, string_array, plurals node

just first time create excel would add String name

For speedup, now .xml must be same sequence

without argv would do nothing

python locate depend on machine

 

'''

import sys

import xml.dom.minidom

from xlwt import Workbook

from xlrd import open_workbook

from xlutils.copy import copy

import os

 

countryMap = {

'default':'English, US',

'ar':'Arabic',

'bg':'Bulgarian',

'ca':'Catalan',

'cs':'Czech',

'da':'Danish',

'de':'German',

'el':'Greek',

'en-rGB':'English, Britain',

'es':'Spanish',

'es-rUS':'Spanish, US',

'fa':'Persian',

'fi':'Finnish',

'fr':'French',

'hr':'Croatian',

'hu':'Hungarian',

'in':'Indonesian',

'it':'Italian',

'iw':'Hebrew',

'ja':'Japanese ',

'ko':'Korean ',

'lt':'Lithuanian',

'lv':'Latvian',

'nb':'Norwegian bokmal',

'nl':'Dutch',

'pl':'Polish',

'pt':'Portuguese',

'pt-rPT':'Portuguese, Portugal',

'rm':'rm',

'ro':'Romanian',

'ru':'Russian',

'sk':'Slovak',

'sl':'Slovenian',

'sr':'Serbian',

'sv':'Swedish',

'th':'Thai',

'tl':'Tagalog',

'tr':'Turkish',

'uk':'Ukrainian',

'vi':'Vietnamese',

'zh-rCN':'Chinese, PRC',

'zh-rTW':'Chinese, Taiwan'

              }

 

xmlFilePath = 'strings.xml'

excelFileName = 'output.xls'

column = 2

countryName = 'unknow'

stringArrayRow = 1

pluralRow = 1

 

def init():

    global ws,ws2,ws3,firstTime,wb,rs

    if os.path.exists(excelFileName):

        rb = open_workbook(excelFileName, formatting_info=True)

        rs = rb.sheet_by_index(0)

        wb = copy(rb)

        ws = wb.get_sheet(0)

        ws2 = wb.get_sheet(1)

        ws3 = wb.get_sheet(2)

        firstTime = False

    else:

        wb = Workbook()

        ws = wb.add_sheet('string')

        ws2 = wb.add_sheet('string_array')

        ws3 = wb.add_sheet('plurals')

        firstTime = True

   

def main(argv = None):

    global column

    global countryName

    global xmlFilePath

    global excelFileName

    if argv == None:

        argv = sys.argv

    if len(argv)>1:

        column = int(argv[1])

        countryName = argv[2]

        if len(argv)>3:

            xmlFilePath = argv[3]

            if len(argv)>4:

                excelFileName = argv[4]

    else:

        print __doc__

        return 0

          

    if not os.path.exists(xmlFilePath):

        print xmlFilePath+' is not exist'

        return 0

   

    init()

    ws.write(0,column,countryMap.get(countryName,'unknow'))

    ws2.write(0,column,countryMap.get(countryName,'unknow'))

    ws3.write(0,column,countryMap.get(countryName,'unknow'))

   

    dom = xml.dom.minidom.parse(xmlFilePath)

    handleResources(dom)

    wb.save(excelFileName)

    return 0

 

def getText(nodelist):

    rc = []

    for node in nodelist:

        if node.nodeType == node.TEXT_NODE:

            rc.append(node.data)

    return ''.join(rc)

 

def handleResources(resources):

    strings = resources.getElementsByTagName("string")

    stringArrays = resources.getElementsByTagName("string-array")

    plurals = resources.getElementsByTagName("plurals")

    handleStrings(strings)

    handleStringArrays(stringArrays)

    handlePlurals(plurals)

   

def handlePlurals(plurals):

    for plural in plurals:

        if firstTime:

            ws3.write(pluralRow,0,plural.getAttribute('name'))        

        pluralItems =  plural.getElementsByTagName("item")

        handlePluralItems(pluralItems)

       

def handlePluralItems(pluralItems):

    global pluralRow

    for item in pluralItems:

        ws3.write(pluralRow,column,handleText(item))

        pluralRow = pluralRow+1

 

def handleStringArrays(stringArrays):

    for stringArray in stringArrays:

        if firstTime:

            ws2.write(stringArrayRow,0,stringArray.getAttribute('name'))

        items =  stringArray.getElementsByTagName("item")

        handleItems(items)

   

def handleItems(items):

    global stringArrayRow

    for item in items:

        ws2.write(stringArrayRow,column,handleText(item))

        stringArrayRow = stringArrayRow+1

       

def handleItem(item):

    return getText(item.childNodes)

 

def handleStrings(strings):

    row=1

    for string in strings:

        # first time add attribute name

        if firstTime:

            ws.write(row,0,string.getAttribute('name'))

            ws.write(row,column,handleText(string))

            row=row+1

        else:  

            try:

                #if attribute name is correct, write value. Otherwise, find the correct attribute name         

                if string.getAttribute('name')==rs.cell(row,0,).value:

                    ws.write(row,column,handleText(string))

                    row=row+1

                else:

                    temprow = row

                    attributeName = string.getAttribute('name')

                    while temprow<rs.nrows:

                        if attributeName!=rs.cell(temprow,0,).value:

                            temprow=temprow+1

                        else:

                            ws.write(temprow,column,handleText(string))

                            row = temprow+1

                            break   

            except IndexError:  

                print 'Number of string is much than default number'         

        

def handleText(string):

    return getText(string.childNodes)

 

if __name__ == '__main__':

    sys.exit(main())
