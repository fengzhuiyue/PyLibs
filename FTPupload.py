from ftplib import FTP
ftp=FTP()
ftp.set_debuglevel(2)                           #打开调试级别2，显示详细信息
ftp.connect('172.16.13.102',21)                 #连接FTP服务器
ftp.login('','')                                #登录，如果匿名登录则用空串代替即可
print (ftp.getwelcome())                        #显示ftp服务器欢迎信息
#ftp.retrlines('list')                          #PIN出根目录下的所有路径
#ftp.cwd('/13/')                                #选择要操作的目录
ftp.retrlines('list')                           #PIN出所有路径
bufsize = 1024                                  #设置缓冲块大小
fli = open('upload.txt','rb')                   #以读模式在本地打开文件
ftp.storbinary('STOR upload.txt',fli,bufsize)   #上传本地文件到FTP服务器上
ftp.set_debuglevel(0)                           #关闭调试
fli.close()                                     #关闭该文件
ftp.quit()                                      #退出ftp服务器
