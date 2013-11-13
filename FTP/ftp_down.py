#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
 
from ftplib import FTP
import base64 
import os
 
def ftp_up(filename = "20120904.rar"): 
	ftp=FTP() 
	ftp.set_debuglevel(2)#打开调试级别2，显示详细信息;0为关闭调试信息 
	ftp.connect('192.168.0.1','21')#连接 
	ftp.login('admin','admin')#登录，如果匿名登录则用空串代替即可 
	#print ftp.getwelcome()#显示ftp服务器欢迎信息 
	#ftp.cwd('xxx/xxx/') #选择操作目录 
	bufsize = 1024
	file_handler = open(filename,'rb')
	ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize) 
	ftp.set_debuglevel(0) 
	file_handler.close() 
	ftp.quit() 
	print "ftp up OK" 
 
def ftp_down(filename): 
	ftp=FTP() 
	ftp.set_debuglevel(2) 
	ftp.connect('ftp ip','21') 
	ftp.login('username','password')
		
	#print ftp.getwelcome()#显示ftp服务器欢迎信息 
	#ftp.cwd('xxx/xxx/') #选择操作目录 
	bufsize = 1024 
	#filename = "20120904.rar" 
	f= open(filename,'wb') 
	ftp.sendcmd("TYPE A")
	#ftp.retrbinary('RETR %s' % os.path.basename(filename),f.write,bufsize)
	ftp.retrlines('RETR %s' % os.path.basename(filename),f.write)
	ftp.set_debuglevel(0) 
	f.close() 
	ftp.quit() 
	print "ftp down OK" 	


# This script exist one issue: retr file will be different with the source file. Need check the root cause.
ftp_down("'directory.filename'")
# ftp_down("'directory.filename'")
