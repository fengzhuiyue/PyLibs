import Xlib.display
import Xlib.X
import Xlib.ext.xtest

＃ 点击
display = Xlib.display.Display()
def mouse_click(button): #button= 1 left, 2 middle, 3 right
Xlib.ext.xtest.fake_input(display,Xlib.X.ButtonPress, button)
display.sync()
Xlib.ext.xtest.fake_input(display,Xlib.X.ButtonRelease,
button)
display.sync()
＃ 移动
ds = display.Display()
def goto_xy(x, y) :
xtest.fake_input(ds, X.MotionNotify, x = x, y = y) ＃注意x,y参数的写法
ds.flush()