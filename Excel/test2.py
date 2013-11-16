# -*- coding: gb2312 -*-
import xlrd,sys
from string import Templateclass Account:    
def __init__(self,filename):
	self.fname = filename
	self.head='''<html xmlns:v="urn:schemas-microsoft-com:vml" 
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40"><head>
<meta http-equiv=Content-Type content="text/html; charset=gb2312">
<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 12">
<link id=Main-File rel=Main-File href="../nini.htm">
<link rel=File-List href=filelist.xml>
<link rel=Stylesheet href=stylesheet.css>
<style>
<!--table
    {mso-displayed-decimal-separator:"\.";
    mso-displayed-thousand-separator:"\,";}
@page
    {margin:1.0in .75in 1.0in .75in;
    mso-header-margin:.5in;
    mso-footer-margin:.5in;}
ruby
    {ruby-align:left;}
rt
    {color:windowtext;
    font-size:9.0pt;
    font-weight:400;
    font-style:normal;
    text-decoration:none;
    font-family:宋体;
    mso-generic-font-family:auto;
    mso-font-charset:134;
    mso-char-type:none;
    display:none;}
-->
</style>
<![if !supportTabStrip]><script language="JavaScript">
<!--
function fnUpdateTabs()
 {
  if (parent.window.g_iIEVer>=4) {
   if (parent.document.readyState=="complete"
    && parent.frames['frTabs'].document.readyState=="complete")
   parent.fnSetActiveSheet(0);
  else
   window.setTimeout("fnUpdateTabs();",150);
 }
}if (window.name!="frSheet")
 window.location.replace("../nini.htm");
else
 fnUpdateTabs();
//-->
</script>
<![endif]>
</head><body link=blue vlink=purple class=xl65><table border=0 cellpadding=0 cellspacing=0 width=1412 style='border-collapse:
 collapse;table-layout:fixed;width:1060pt'>
 <col class=xl65 width=83 style='mso-width-source:userset;mso-width-alt:2656;
 width:62pt'>
 <col class=xl65 width=161 style='mso-width-source:userset;mso-width-alt:5152;
 width:121pt'>
 <col class=xl65 width=83 style='mso-width-source:userset;mso-width-alt:2656;
 width:62pt'>
 <col class=xl66 width=98 style='mso-width-source:userset;mso-width-alt:3136;
 width:74pt'>
 <col class=xl65 width=103 style='mso-width-source:userset;mso-width-alt:3296;
 width:77pt'>
 <col class=xl65 width=102 style='mso-width-source:userset;mso-width-alt:3264;
 width:77pt'>
 <col class=xl65 width=83 style='mso-width-source:userset;mso-width-alt:2656;
 width:62pt'>
 <col class=xl65 width=161 style='mso-width-source:userset;mso-width-alt:5152;
 width:121pt'>
 <col class=xl65 width=83 style='mso-width-source:userset;mso-width-alt:2656;
 width:62pt'>
 <col class=xl66 width=97 style='mso-width-source:userset;mso-width-alt:3104;
 width:73pt'>
 <col class=xl65 width=112 style='mso-width-source:userset;mso-width-alt:3584;
 width:84pt'>
 <col class=xl65 width=102 style='mso-width-source:userset;mso-width-alt:3264;
 width:77pt'>
 <col class=xl65 width=72 span=2 style='width:54pt'>'''

 self.tempate =Template('''<tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td colspan=6 height=37 class=xl81 width=630 style='height:27.95pt;
  width:473pt'>发展中心固定资产卡片</td>
  <td class=xl65 width=83 style='width:62pt'></td>
  <td class=xl65 width=161 style='width:121pt'></td>
  <td class=xl65 width=83 style='width:62pt'></td>
  <td class=xl66 width=97 style='width:73pt'></td>
  <td class=xl65 width=112 style='width:84pt'></td>
  <td class=xl65 width=102 style='width:77pt'></td>
  <td class=xl65 width=72 style='width:54pt'></td>
  <td class=xl65 width=72 style='width:54pt'></td>
 </tr>
 <tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td height=37 class=xl67 width=83 style='height:27.95pt;width:62pt'>固定资产编号</td>
  <td class=xl68 width=161 style='width:121pt'>　</td>
  <td class=xl69 width=83 style='width:62pt'>增加方式</td>
  <td class=xl70 width=98 style='width:74pt'>基建移交</td>
  <td class=xl69 width=103 style='width:77pt'>使用<font class="font6">\</font><font
  class="font8">保管部门</font></td>
  <td class=xl71 width=102 style='width:77pt'>$custody</td>
  <td colspan=3 class=xl65 style='mso-ignore:colspan'></td>
  <td class=xl66></td>
  <td colspan=4 class=xl65 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td height=37 class=xl67 width=83 style='height:27.95pt;width:62pt'>名称</td>
  <td class=xl72 width=161 style='width:121pt'>$name</td>
  <td class=xl69 width=83 style='width:62pt'>使用年限</td>
  <td class=xl73 width=98 style='width:74pt'>1<font class="font8">年</font></td>
  <td class=xl69 width=103 style='width:77pt'>责任人</td>
  <td class=xl74 width=102 style='width:77pt'>　</td>
  <td colspan=3 class=xl65 style='mso-ignore:colspan'></td>
  <td class=xl66></td>
  <td colspan=4 class=xl65 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td height=37 class=xl67 width=83 style='height:27.95pt;width:62pt'>规格型号</td>
  <td class=xl75 width=161 style='width:121pt'>$type</td>
  <td class=xl69 width=83 style='width:62pt'>开始使用日期</td>
  <td class=xl76 width=98 style='width:74pt'>$startdate</td>
  <td class=xl69 width=103 style='width:77pt'>使用人\保管人</td>
  <td class=xl74 width=102 style='width:77pt'>　</td>
  <td colspan=3 class=xl65 style='mso-ignore:colspan'></td>
  <td class=xl66></td>
  <td colspan=4 class=xl65 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td height=37 class=xl77 width=83 style='height:27.95pt;width:62pt'>价值(元)</td>
  <td class=xl78 width=161 style='width:121pt'>$price</td>
  <td class=xl69 width=83 style='width:62pt'>生产日期</td>
  <td class=xl73 width=98 style='width:74pt'>$prodate</td>
  <td class=xl69 width=103 style='width:77pt'>验收人</td>
  <td class=xl74 width=102 style='width:77pt'>　</td>
  <td colspan=3 class=xl65 style='mso-ignore:colspan'></td>
  <td class=xl66></td>
  <td colspan=4 class=xl65 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td height=37 class=xl67 width=83 style='height:27.95pt;width:62pt'>其他</td>
  <td class=xl79 width=161 style='width:121pt'>　</td>
  <td class=xl69 width=83 style='width:62pt'>记账凭证号</td>
  <td class=xl76 width=98 style='width:74pt'>　</td>
  <td class=xl69 width=103 style='width:77pt'>存放地点</td>
  <td class=xl80 width=102 style='width:77pt'>$PlaceID</td>
  <td colspan=3 class=xl65 style='mso-ignore:colspan'></td>
  <td class=xl66></td>
  <td colspan=4 class=xl65 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td rowspan=2 height=74 class=xl82 width=83 style='border-bottom:1.0pt solid black;
  height:55.9pt;border-top:none;width:62pt'>资产变动情况记录</td>
  <td colspan=5 rowspan=2 class=xl84 width=547 style='border-right:1.0pt solid black;
  border-bottom:1.0pt solid black;width:411pt'>　</td>
  <td colspan=3 class=xl65 style='mso-ignore:colspan'></td>
  <td class=xl66></td>
  <td colspan=4 class=xl65 style='mso-ignore:colspan'></td>
 </tr>
 <tr height=37 style='mso-height-source:userset;height:27.95pt'>
  <td height=37 colspan=3 class=xl65 style='height:27.95pt;mso-ignore:colspan'></td>
  <td class=xl66></td>
  <td colspan=4 class=xl65 style='mso-ignore:colspan'></td>
 </tr>
 <tr class=xl90 height=37 style='mso-height-source:userset;height:27.95pt'>
  <td colspan=16384 height=37 class=xl90 style='height:27.95pt'>资产管理部门负责人：$manager<font
  class="font6"><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp;&nbsp; </span></font><font
  class="font8">使用人：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font><font class="font6"><span
  style='mso-spacerun:yes'>&nbsp; </span></font><font class="font8">录入人：倪薇</font><font
  class="font6"><span style='mso-spacerun:yes'>&nbsp;&nbsp;&nbsp;&nbsp; </span></font><font
  class="font8">录入日期：$recorddate</font></td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr>''')
        pass    def openExcleFile(self,index):
        self.bk = xlrd.open_workbook(self.fname,)
        self.sh = self.bk.sheets()[index]
        self.nrows = self.sh.nrows
        self.dic = {}
        pass    def openHtmlFile(self,hfile):
        self.htmfile = open(hfile,'a+')
        pass
    
    def writeFile(self,start):
        self.htmfile.write(self.head)
        for i in range(start,self.nrows):
            self.name=self.sh.cell_value(i,1).encode('gbk')
            self.price=self.sh.cell_value(i,2)
            self.Type=""
            if self.sh.cell_type(i,5)==1:
                self.Type=self.sh.cell_value(i,5).encode('gbk')
            else:
                self.Type=self.sh.cell_value(i,5)
            self.prodate=""
            self.startdate=""
            try:
                d1 = xlrd.xldate_as_tuple(self.sh.cell_value(i,8),0)
                self.prodate = str(d1[0])+"--"+str(d1[1])+"--"+str(d1[2])
                #self.prodate =xlrd.xldate_as_tuple(self.sh.cell_value(i,8),0)
                pass
            except:
                pass
            try:
                d2 = xlrd.xldate_as_tuple(self.sh.cell_value(i,6),0)
                self.startdate = str(d2[0])+"--"+str(d2[1])+"--"+str(d2[2])
                pass
            except:
                pass
            self.custody = self.sh.cell_value(i,10).encode('gbk')
            self.recorddate="2011年7月14日"
            self.PlaceID = self.sh.cell_value(i,15).encode('gbk')
            self.manager = "罗隆芒"#self.sh.cell_value(i,14).encode('gbk')
            s=self.tempate.substitute(name=self.name,
                                    price=self.price,
                                    type=self.Type,
                                    prodate=self.prodate,
                                    startdate=self.startdate,
                                    custody=self.custody,
                                    recorddate=self.recorddate,
                                    PlaceID=self.PlaceID,
                                    manager=self.manager)
            self.htmfile.write(s)
            pass
        self.htmfile.write('''<![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=83 style='width:62pt'></td>
  <td width=161 style='width:121pt'></td>
  <td width=83 style='width:62pt'></td>
  <td width=98 style='width:74pt'></td>
  <td width=103 style='width:77pt'></td>
  <td width=102 style='width:77pt'></td>
  <td width=83 style='width:62pt'></td>
  <td width=161 style='width:121pt'></td>
  <td width=83 style='width:62pt'></td>
  <td width=97 style='width:73pt'></td>
  <td width=112 style='width:84pt'></td>
  <td width=102 style='width:77pt'></td>
  <td width=72 style='width:54pt'></td>
  <td width=72 style='width:54pt'></td>
 </tr>
 <![endif]>
</table></body></html>''')
        self.htmfile.close()
        pass
    passif "__main__" == __name__:
    excelFile=Account('d:\\nini.xls')
    excelFile.openExcleFile(0)
    excelFile.openHtmlFile('d:\\nini.files\\sheet001.htm')
    excelFile.writeFile(3)
    pass