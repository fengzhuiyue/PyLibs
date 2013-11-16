# -*- coding: utf-8 -*-


import sys
import os
import string
import htmllib
import urllib
import urlparse
import formatter
from sys import argv
from urllib import urlretrieve
from urllib import urlencode
import urllib2
import cookielib
import re
import datetime


	
def write_content(f,content):
    f.write('<description><![CDATA['+content+']]></description>\n')
	
def addtorss(f,name):
    
    file=open(name)
    line = file.readlines()
    
# find the title of the blog entry
    f_title = ''
    data = '<title>'
    j = 0
    for eachLine in line:
        j=j+1
        m = re.search(data,eachLine)
        if m is not None:
            break
    strs = line[j-1]
    n_start = strs.find('<title>')+7
    n_end = strs.rfind('</title>')
    f_title = strs[n_start:n_end]
    
    f.write('\n\n\n<item><title><![CDATA['+ f_title + ']]></title>\n')

    i = 0
    for eachLine in line:
        i = i + 1
        m = re.search('id="blogContent"',eachLine)
        if m is not None:
            break
    f_content = line[i+1]
    write_content(f,f_content)
# find the time of the blog entry
    f_time = ''
    data = '"timestamp"'
    j = 0
    for eachLine in line:
        j=j+1
        m = re.search(data,eachLine)
        if m is not None:
            break
    strs = line[j-1]
    n_start = strs.find('span class="timestamp"')+23
    n_end = strs.rfind('<span class="group">')
    f_time = strs[n_start:n_end]
    gmt_format='%a, %d %b %Y %H:%M:00 GMT+8'
    time_format='%Y-%m-%d %H:%S '
    time=datetime.datetime.strftime(datetime.datetime.strptime(f_time,time_format),gmt_format)
    f.write('<pubDate>'+ time +'</pubDate>\n</item>\n')
    
    
    
def main():
# login to xiaonei
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
	
    opener.addheaders = [
            ("User-agent", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"),
            ("Accept","text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1"),
			("Host","www.renren.com"),
			("Referer","http://home.renren.com/Home.do"),
			('Accept-Language', 'zh-CN,zh;q=0.8'),
			('Accept-Charset', 'GBK,utf-8;q=0.7,*;q=0.3'),
			('Keep-Alive', '300'),
			('Connection', 'keep-alive'),
			('Cache-Control', 'max-age=0')
			]
 
    UserName=raw_input('your email in renren.com:')
    Password=raw_input('your password:')
    data = {
            'email': UserName,
            'password': Password,
			'origURL':"http://www.renren.com/Home.do",
			'submit': '登录'
            }
    urldata = urlencode(data)
    r = opener.open("http://passport.renren.com/PLogin.do", urldata)
    results = r.read()
	#personal homepage is saved as the start.html
    open('start.html', 'w').write(results)
    r = urllib2.urlopen("http://blog.renren.com/blog/0?from=homeleft&__view=async-html")
    results = r.read()
	#blog homepage is saved as the user.txt
    open('user.txt', 'w').write(results)
    
# get the whole article number
    file = open('user.txt')
    line = file.readlines()
    file.close()

    data = '当前显示1-10篇/共\d*篇'
    article_num = 0
	#find the article num below
    for eachLine in line:
        m = re.search(data,eachLine)
        if m is not None: 
            strs = m.group()
            num_start = strs.rfind('共')+3
            num_end = strs.rfind('篇')
            article_num = string.atoi(strs[num_start:num_end],10)
            break
    print 'you have %d articles in total' %(article_num)
            
#download the articles

    #make save xml file
    save_file = open('renrenblog.xml','w')
    save_file.write('\n\n<?xml version="1.0" ?>\n<!--  generator="toyjack"  -->\n <rss version="2.0">\n<channel>\n<title><![CDATA[RENREN日志]]></title>\n<link></link>\n<description>by toyjack@gmail.com</description>\n')
    
    k = 1
    #get the first entry
    file = open('user.txt')
    line = file.readlines()
    file.close()
    data = 'http://blog.renren.com/blog/\d*/\d*\?frommyblog'
    for eachLine in line:
        #print eachLine
        m = re.search(data,eachLine)
        if m is not None:
            strs = m.group()
            print strs
            break
    r = urllib2.urlopen(strs)
    results = r.read()
    open('temp.txt', 'w').write(results)
    print "now downloading the ", k, "th articles"
    addtorss(save_file,'temp.txt')
    #get others
    for k in range(2,article_num+1):
        file = open('temp.txt')
        line = file.readlines()
        file.close()
        data = 'http://blog.renren.com/blog/\d*/\d*\?from=fanyeOld'
        for eachLine in line:
            m = re.search(data,eachLine)
            if m is not None:
                strs = m.group()
                print strs
                break
        r = urllib2.urlopen(strs)
        results = r.read()
        open('temp.txt','w').write(results)
        print "now downloading the ", k, "th articles"
        addtorss(save_file,'temp.txt')
    save_file.write('\n\n</channel>\n</rss>\n')
    save_file.close()
	
    os.remove('temp.txt')
    os.remove('start.html')
    os.remove('user.txt')   
    

if __name__ == '__main__':
    main()
