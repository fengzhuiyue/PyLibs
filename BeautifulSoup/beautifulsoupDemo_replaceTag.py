#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【教程】Python中第三方的用于解析HTML的库：BeautifulSoup
 
http://www.crifan.com/python_third_party_lib_html_parser_beautifulsoup
 
Author:     Crifan Li
Version:    2013-02-01
Contact:    admin at crifan dot com
"""
 
from BeautifulSoup import BeautifulSoup;
 
def beautifulsoupDemo():
    demoHtml = """
<html>
<body>
<div class="icon_col">
        <h1 class="h1user">crifan</h1>
 </div>
 </body>
</html>
""";
    soup = BeautifulSoup(demoHtml);
    print "type(soup)=",type(soup); #type(soup)= <type 'instance'>
    print "soup=",soup;
     
    print '{0:=^80}'.format(" 1. extract content ");
    # method 1: no designate para name
    #h1userSoup = soup.find("h1", {"class":"h1user"});
    # method 2: use para name
    h1userSoup = soup.find(name="h1", attrs={"class":"h1user"});
    # more can found at:
    #http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#find%28name,%20attrs,%20recursive,%20text,%20**kwargs%29
    print "h1userSoup=",h1userSoup; #h1userSoup= <h1 class="h1user">crifan</h1>
    h1userUnicodeStr = h1userSoup.string;
    print "h1userUnicodeStr=",h1userUnicodeStr; #h1userUnicodeStr= crifan
     
    print '{0:=^80}'.format(" 2. demo change tag value and property ");
    print '{0:-^80}'.format(" 2.1 can NOT change tag value ");
    print "old tag value=",soup.body.div.h1.string; #old tag value= crifan
    changedToString = u"CrifanLi";
    soup.body.div.h1.string = changedToString;
    print "changed tag value=",soup.body.div.h1.string; #changed tag value= CrifanLi
    print "After changed tag value, new h1=",soup.body.div.h1; #After changed tag value, new h1= <h1 class="h1user">crifan</h1>
 
    print '{0:-^80}'.format(" 2.2 can change tag property ");  
    soup.body.div.h1['class'] = "newH1User";
    print "changed tag property value=",soup.body.div.h1; #changed tag property value= <h1 class="newH1User">crifan</h1>
 
if __name__ == "__main__":
    beautifulsoupDemo();