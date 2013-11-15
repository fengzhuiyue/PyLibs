import win32api

try:
    from winxpgui import *
except ImportError:
    from win32gui import *

from win32gui_struct import *
import win32con
import sys, os

def get_curpos():
  	return win32gui.GetCursorPos()
	
print get_curpos()
