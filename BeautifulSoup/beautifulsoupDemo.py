#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【教程】Python中第三方的用于解析HTML的库：BeautifulSoup
 
http://www.crifan.com/python_third_party_lib_html_parser_beautifulsoup
 
Author:     Crifan Li
Version:    2012-12-26
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
     
    # 1. extract content
    # method 1: no designate para name
    #h1userSoup = soup.find("h1", {"class":"h1user"});
    # method 2: use para name
    h1userSoup = soup.find(name="h1", attrs={"class":"h1user"});
    # more can found at:
    #http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#find%28name,%20attrs,%20recursive,%20text,%20**kwargs%29
    print "h1userSoup=",h1userSoup; #h1userSoup= <h1 class="h1user">crifan</h1>
    h1userUnicodeStr = h1userSoup.string;
    print "h1userUnicodeStr=",h1userUnicodeStr; #h1userUnicodeStr= crifan
 
if __name__ == "__main__":
    beautifulsoupDemo();