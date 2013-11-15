#coding=utf-8
from ctypes import *
from ctypes.wintypes import BOOL, HWND, LPARAM

#加载user32.dll
user32 = windll.LoadLibrary("user32")

#定义回调函数
@WINFUNCTYPE(BOOL, HWND, LPARAM)
def print_title(hwnd,extra):
    title = create_string_buffer(1024)
	#根据句柄获得窗口标题
    user32.GetWindowTextA(hwnd,title,255)
    title = title.value
    if title!="":
        print title
    return 1
	
#枚举窗口
user32.EnumWindows(print_title,0)
