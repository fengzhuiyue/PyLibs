#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import paramiko
import base64 
import os

t = paramiko.Transport(("hostname",22)) #--- 端口不需要引号；
t.connect(username=base64.decodestring('username_base64ed'),password=base64.decodestring('password_base64ed'))
sftp = paramiko.SFTPClient.from_transport(t)

remotepath='/direc/'

filenames=sftp.listdir(remotepath)
for name in filenames:
	filenames[filenames.index(name)]=name[-3:]
	if name[-3:]=='DAT':
		PosFile=name
localpath =R'C:\\DATA\\' #IOError ：【Error 22】 请加R，或r
sftp.get(remotepath+PosFile,localpath+PosFile) #下载服务器路径，到本地 get；
t.close()
