#coding=utf-8

import sys
import os
import wx
import random
import time
import threading

#在脚本所在目录中，必须存在文件names.txt，人名必须是格式化的：不能有空行，人名后面必须且只能加一个回车
#文件names.txt中的人名，最后一个后面必须且只能加一个回车

class ButtonFrame(wx.Frame):
 def __init__(self):
  wx.Frame.__init__(self,None,-1,'Raffle',size=(600,500))
  panel=wx.Panel(self,-1)
  self.statictext=wx.TextCtrl(panel,-1,'',pos=(6,20),size=(580,75),style=wx.TE_CENTER|wx.TE_NOHIDESEL|wx.TE_READONLY)
  self.font3=wx.FFont(40,wx.DEFAULT,wx.FONTFLAG_BOLD)
  self.statictext.SetFont(self.font3)
  self.statictext.SetForegroundColour('red')
  self.statictext.SetBackgroundColour('black')
  self.statictext.Value='-= UNIMAS =-'
  self.button1=wx.Button(panel,-1,'Start',pos=(60,370),size=(150,80),style=wx.TE_CENTER|wx.TE_NOHIDESEL)
  self.button2=wx.Button(panel,-1,'Stop',pos=(380,370),size=(150,80),style=wx.TE_CENTER|wx.TE_NOHIDESEL)
  self.Bind(wx.EVT_BUTTON,None,self.button1) 
  self.Bind(wx.EVT_BUTTON,None,self.button2)
  self.button1.Bind(wx.EVT_LEFT_DOWN,self.start)
  self.button2.Bind(wx.EVT_LEFT_DOWN,self.stop)
  self.font2=wx.FFont(25,wx.DEFAULT,wx.FONTFLAG_BOLD)
  self.button1.SetFont(self.font2)
  self.button2.SetFont(self.font2)
  self.button1.SetForegroundColour('blue')
  self.button1.SetBackgroundColour('gray')
  self.button2.SetForegroundColour('blue')
  self.button2.SetBackgroundColour('gray')
  self.button1.SetDefault()
  self.button2.SetDefault()
  self.inputText=wx.TextCtrl(panel,-1,'',pos=(6,90),size=(580,250),style=wx.TE_CENTER|wx.TE_NOHIDESEL|wx.TE_READONLY)
  self.font=wx.FFont(105,wx.DEFAULT,wx.FONTFLAG_BOLD)
  self.inputText.SetFont(self.font)
  self.inputText.SetForegroundColour('yellow')
  self.inputText.SetBackgroundColour('black')
  self.inputText.Value='GMT Forum'
  self.mark2=0  #初始化“线程控制”参数
  self.names=open('names.txt','rb')
  self.readnames=self.names.readlines()
  self.names.close()
  self.mark3=0  #初始化“保证页面只有在抽过奖的情况下才会显示该语句”的控制参数
  
 def processunicode(self,value):   #处理unicode类型字符串
  v1=''
  if type(value)==unicode:
   v1=v1+value.encode('utf-8')
  else:
   v1=value
  return v1
 
 def stop(self,event):   #停止函数
  self.mark=1     #设置“启动与停止”的控制参数
  if self.mark3!=0:   #保证页面只有在抽过奖的情况下才会显示该语句
   self.statictext.Value='The winner is：'
 
 def start(self,event):   #开始函数
  if self.mark2==0:   #保证抽奖线程同时只能运行一个
   self._threads=threading.Thread(target=self.OnClick,args=())   #建立开始抽奖线程
   self._threads.start()  #线程启动
   self.mark2=1    #改变“保证抽奖线程同时只能运行一个”的控制参数
   self.mark3=1    #改变“保证页面只有在抽过奖的情况下才会显示该语句”的控制参数
   self.statictext.Value='Processing...'
 
 def OnClick(self):   #抽奖主函数
  self.font=wx.FFont(140,wx.DEFAULT,wx.FONTFLAG_BOLD)
  self.inputText.SetFont(self.font)
  self.old=[]    #初始化“不允许抽奖”的名字列表
  if os.path.exists('values.txt'):   #判断“不允许抽奖”的名字列表文件是否存在
   self.openfile=open('values.txt','rb')
   self.old=self.openfile.readlines()  #读取“不允许抽奖”的名字列表
   self.openfile.close()
  else:
   self.openfile=open('values.txt','wb')
   self.openfile.close()
  
  self.mark=0   #改变“启动与停止”的控制参数
  while self.mark==0:   #抽奖主循环
   self.values=[]   #每次迭代前清空之前的抽奖名单
   for a in self.readnames:     #建立新的抽奖名单
    if (str(a) not in self.values) and (str(a) not in self.old):
     self.values.append(str(a))
   random.shuffle(self.values)    #每次迭代前重新排列名字序列
   for a in self.values:  #迭代抽奖名单
    if self.mark==0:
     self.inputText.Value=self.processunicode(a)
    else:
     break
    time.sleep(0.025)
	#在等待的时间内停止后，防止再次循环。
    if self.mark!=0:
     break
  
  self.openfile=open('values.txt','ab')
  self.openfile.write(str(a))
  #把中奖者的名字写入“不允许抽奖”名单，以防止此人再次参与抽奖
  self.openfile.close()
  #复位“线程控制”参数
  self.mark2=0


if __name__=='__main__':
 app=wx.PySimpleApp()
 fram=ButtonFrame()
 fram.Show()
 app.MainLoop()
