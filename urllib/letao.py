#!/usr/bin/python   
#-*-coding:utf-8-*-   
 
import httplib,urllib;  #加载模块   
 
 
username=[]
# for i in range(1,27): 
#定义需要进行发送的数据   
params = urllib.urlencode({'txt_userName':'xxx@xxx.com','txt_passWord':'xxxx'});   
#定义一些文件头   
headers = {"Content-Type":"application/x-www-form-urlencoded",   
           "Connection":"Keep-Alive","Referer":"http://m.letao.com/wap/login/login.aspx"};   
#与网站构建一个连接   
conn = httplib.HTTPConnection("http://m.letao.com/wap/login/");   
#开始进行数据提交   同时也可以使用get进行   
conn.request(method="POST",url="login.aspx",body=params,headers=headers);   
#返回处理后的数据   
response = conn.getresponse();   
#判断是否提交成功   
if response.status == 302:   
    print "发布成功!";   
else:   
    print "发布失败";   
#关闭连接   
conn.close();
