import re
import urllib2

import cookielib


def letao():
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    email = 'xxx@xxx.com'
    pwd   = 'xxxxx'
    
    #登录..
    print 'login......'
    url = "http://m.letao.com/wap/login/login.aspx"
    postdata = "txt_userName="+email+"&txt_passWord="+pwd
    req = urllib2.Request(url,postdata)
    res = opener.open(req).read()
    print 'succeed!'
    
    #得到当前状态
    s = r'(?s)id="currentStatus">.*?<a ui-async="async" title="([^"]*)'
    match = re.search(s, res, re.DOTALL)
    if match:
        result = match.groups(1)
        print 'current status: ', result[0]

letao() 
