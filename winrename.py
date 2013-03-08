#版权声明：转载时请以超链接形式标明文章原始出处和作者信息及本声明
#http://azrael8.blogbus.com/logs/84552721.html

#因为平时偶尔需要，试着用python编写了一个文件名批量重命名的小程序，源代码如下：
#（本程序运行于windows命令行模式下，用python 2.7编写，只作用于给定路径下的本级目录文件名。）
#--------------------------------------------------------------------------------

# -*- coding:GBK -*-
# 作者：Azrael
# 修改时间：2010-11-18

""" 文件名批量重命名小工具（运行环境要求：windows 系统）
    功能如下：
   （1）批量删除文件名中相同字符
   （2）批量给文件名添加前缀
   （3）批量修改文件扩展名
"""

import os
import os.path

# --------------------工具函数开始--------------------

# 组建新文件名函数(删除相同字符用)
def new_file_name_4del(filename,delstr):
    index_start = filename.find(delstr)
    newname = filename[:index_start]+filename[index_start + len(delstr)+1:]
    return newname

# 组建新文件名函数(添加前缀用)
def new_file_name_4add(filename,addstr):
    newname = addstr + filename
    return newname

# 组建新文件名函数（修改扩展名用）
def new_file_name_4ext(filename,new_ext):
    name = filename.split('.')[0]
    newname = name + '.' + new_ext
    return newname

# 切换到工作目录函数
def gotodir():
    way = raw_input("请输入要批量重命名文件夹的路径：")
    # 判断是否是路径，以及是否存在
    while not (os.path.isdir(way)):
        way = raw_input("你输入的不是合法路径，请重新输入：")
    else:
        os.chdir(way)

# 验证输入的字符是否是合法文件名函数
# 文件名不能包含下面任何字符之一： \/:*?"<>|
def checkstr(addstr):
    signsstr =  '\/:*?"<>|'
    for sign in signsstr:
        if sign in addstr:
            return 0
    else:
        return 1


# --------------------主功能函数开始--------------------

# 删除相同字符函数
def delstr():
    gotodir()  # 切换到工作目录下
    old_name_list = os.listdir('.')
    delstr = raw_input("请输入要删除的相同字符：")
    if (delstr == ''):
        print "程序中止"
    else:
        # 开始批量重命名
        for one_file in old_name_list:
            if (delstr in one_file):
                newname = new_file_name_4del(one_file,delstr)
                os.rename(one_file,newname)
            else:
                print "文件名中无此字符！"
        print "重命名完毕。"

# 添加前缀函数
def addstr():
    gotodir()  # 切换到工作目录下
    old_name_list = os.listdir('.')
    addstr = raw_input("请输入要添加的字符：")
    if (addstr == ''):
        print "程序中止"
    elif(checkstr(addstr)):   #  验证输入的字符是否是合法文件名函数
        # 开始批量重命名
        for one_file in old_name_list:
            newname = new_file_name_4add(one_file,addstr)
            os.rename(one_file,newname)
        print "重命名完毕。"
    else:
        print "输入字符不合法！"

# 批量修改扩展名函数
def rename_ext():
    gotodir()  # 切换到工作目录下
    old_name_list = os.listdir('.')
    old_ext = old_name_list[0].rsplit('.',1)[-1]  # 获得原文件扩展名
    print "原文件的扩展名为：",old_ext
    new_ext = raw_input("请输入新的扩展名(不含'.')：")
    if (new_ext==''):
        print "程序中止"
    else:
        # 开始批量重命名
        for one_file in old_name_list:
            newname = new_file_name_4ext(one_file,new_ext)
            os.rename(one_file,newname)
        print "重命名完毕。"
       

# --------------------主程序开始--------------------

print "＝＝＝＝＝＝＝批量重命名工具＝＝＝＝＝＝＝"
print """请选择要进行的操作：
（1）批量删除文件名中相同字符
（2）批量给文件名添加前缀
（3）批量修改文件扩展名
"""
select = raw_input(":")
while(select!=''):
    if select=='1':
        delstr()      # 调用删除相同字符函数
        break
    elif select=='2':
        addstr()      # 调用添加前缀函数
        break
    elif select=='3':
        rename_ext()  # 调用批量修改扩展名函数
        break
    else:
        print "输入错误，请重新输入！"
        select = raw_input(":")
print "程序结束。"

#-------------------------------------------------------------------------------------

#分享于其他同样需要此功能的朋友。欢迎技术交流~

#PS: 如果是在linux系统中运行python，只需将程序头部分的
# -*- coding:GBK -*-
#修改为：
#! /usr/bin/python
# -*- coding:utf-8 -*-
#即可。

