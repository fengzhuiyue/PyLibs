from ftplib import FTP            
ftp=FTP()
ftp.set_debuglevel(2)                               #打开调试级别2，显示详细信息
ftp.connect('172.16.13.102',21)                     #连接远程FTP服务器
ftp.login('','')                                    #登录，如果匿名登录则用空串代替即可
print (ftp.getwelcome())                            #显示ftp服务器欢迎信息
#ftp.retrlines('list')                              #PIN出所有路径
#ftp.cwd('/13/')                                    #选择操作目录
ftp.retrlines('list')                               #PIN出所有路径
bufsize = 8192                                      #设置缓冲块大小
fli = open('download.txt','wb')                     #以写模式在本地打开文件
ftp.retrbinary('RETR download.txt',fli,bufsize)     #将FTP服务器上的文件下载至本地
ftp.set_debuglevel(0)                               #关闭调试
ftp.quit()                                          #退出ftp服务器
