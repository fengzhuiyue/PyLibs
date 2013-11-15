import win32com
from win32com.client import Dispatch, constants

# w = win32com.client.Dispatch('Word.Application')
# 或者使用下面的方法，使用启动独立的进程：
w = win32com.client.DispatchEx('Word.Application')

# 后台运行，显示程序界面，不警告
w.Visible = 1 #这个至少在调试阶段建议打开，否则如果等待时间长的话，它至少给你耐心。。。
w.DisplayAlerts = 0

# 打开新的文件
#worddoc = w.Documents.Open(file_name) #这句话用来打开已有的文件，当然，在此之前你最好判断文件是否真的存在。。。
doc = w.Documents.Add() # 创建新的文档，我用的更多的是这个，因为我要的是创建、然后保存为。。

# 插入文字
myRange = doc.Range(0,0) #这句话让你获取的是doc的最前面位置,如果想要获取到其他位置，就要改变Range中的参数，两个参数分别代表起始点，结束点。。。
myRange.InsertBefore('Hello from Python!')

'''
以下一段是增加10个新页，然后跳转到新页中增加内容。。。。
'''
# section_index = 0
# for i in range(0, 10):
	# 由于增加页的使用如此频繁，我们最好将其提取为一个函数，类似def NewTable(self)：
	# pre_section = doc.Secitons(section_index)
	# new_seciton = doc.Range(pre_section.Range.End, pre_section.Range.End).Sections.Add()
	# new_range = new_seciton.Range

	# content_pg = new_range.Paragraphs.Add()
	# content_pg.Range.Font.Name,content_pg.Range.Font.Size = 'Times New Roman',24
	# caption_pg.Range.ParagraphFormat.Alignment = 0 # 0,1,2 分别对应左对齐、居中、右对齐
	# caption_pg.Range.InsertBefore('Hello,Page ' + str(i+1))

	# section_index = section_index + 1 #记录这个的目的是为了方便的找到doc的尾端，不然的话，我还真没有想到怎么搞。。。

# 正文文字替换
# w.Selection.Find.ClearFormatting()
# w.Selection.Find.Replacement.ClearFormatting()
# w.Selection.Find.Execute(OldStr, False, False, False, False, False, True, 1, True, NewStr, 2)

#设置页眉文字，如果要设置页脚值需要把SeekView由9改为10就可以了。。。
# w.ActiveWindow.ActivePane.View.SeekView = 9 #9 - 页眉； 10 - 页脚
# w.Selection.ParagraphFormat.Alignment = 0
# w.Selection.Text = 'New Header'
# w.ActiveWindow.ActivePane.View.SeekView = 0 # 释放焦点，返回主文档

# 页眉文字替换
# w.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
# w.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
# w.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(OldStr, False, False, False, False, False, True, 1, False, NewStr, 2)

# 在文档末尾新增一页，并添加一个表格。。。
# pre_section = doc.Secitons(section_index)
# new_seciton = doc.Range(pre_section.Range.End, pre_section.Range.End).Sections.Add()
# new_range = new_seciton.Range
# new_table = new_range.Tables.Add(doc.Range(new_range.End,new_range.End), 5, 5) #在文档末尾添加一个5*5的表格
#接下来Table怎么操作，这里就不细说了，检索Table对象参照就OK了。。。

# 表格操作
# doc.Tables[0].Rows[0].Cells[0].Range.Text ='123123'
# worddoc.Tables[0].Rows.Add() # 增加一行

# 转换为html
# wc = win32com.client.constants
# w.ActiveDocument.WebOptions.RelyOnCSS = 1
# w.ActiveDocument.WebOptions.OptimizeForBrowser = 1
# w.ActiveDocument.WebOptions.BrowserLevel = 0 # constants.wdBrowserLevelV4
# w.ActiveDocument.WebOptions.OrganizeInFolder = 0
# w.ActiveDocument.WebOptions.UseLongFileNames = 1
# w.ActiveDocument.WebOptions.RelyOnVML = 0
# w.ActiveDocument.WebOptions.AllowPNG = 1
# w.ActiveDocument.SaveAs( FileName = filenameout, FileFormat = wc.wdFormatHTML )

# 打印
# doc.PrintOut()

# 关闭
# doc.Close()
w.ActiveDocument.SaveAs("C:\data\Test.doc")
w.Documents.Close()
w.Quit()
