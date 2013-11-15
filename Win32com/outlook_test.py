#filename: outlook.py
#encoding=utf-8
from time import sleep
import win32com

def outlook(name):
	outlook = win32com.client.Dispatch('Outlook.Application')
	
	mail = outlook.createItem(0)
	mail.Recipients.Add('% s@xxx.com'% name)
	mail.Subject =u"邀请函"
	
	body.append(u'	诚邀您参加于下周五晚六点在公司举行的晚会。')
	
	mail.Body =body
	
	mail.Send()
	
	outlook.Quit()

if __name__=='__mail__':
	names= ['john']
	for name in names:
		outlook(name)
