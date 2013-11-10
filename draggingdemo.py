import wx

class MainPanel(wx.Panel):

	p1 = None
	p2 = None

	def __init__(self, parent):

		wx.Panel.__init__(self, parent=parent)

		self.frame = parent
		#self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
		#self.bg = wx.Bitmap("2.jpg")

		self.Bind(wx.EVT_MOTION, self.OnMouseMove)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
		self.Bind(wx.EVT_PAINT, self.OnPaint)

		self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))

	def OnMouseMove(self, event):
		if event.Dragging() and event.LeftIsDown():
			#self.p2 = event.GetPosition()
			print "dragging"
			self.Refresh()

	def OnMouseDown(self, event):
		self.p1 = event.GetPosition()

	def OnPaint(self, event):
		if self.p1 is None or self.p2 is None: return

		dc = wx.PaintDC(self)
		dc.SetPen(wx.Pen('red', 3, wx.LONG_DASH))
		dc.SetBrush(wx.Brush(wx.Color(0, 0, 0), wx.SOLID))
		dc.DrawRectangle(self.p1.x, self.p1.y, self.p2.x - self.p1.x, self.p2.y - self.p1.y)


class MainFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, size=(600,450))
		panel = MainPanel(self)        
		self.Center()

class Main(wx.App):
	def __init__(self, redirect=False, filename=None):
		wx.App.__init__(self, redirect, filename)
		dlg = MainFrame()
		dlg.Show()

if __name__ == "__main__":
	app = Main()
	app.MainLoop()
