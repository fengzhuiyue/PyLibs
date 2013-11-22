#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【解答】关于BeautifulSoup抓取目标数据的问题
 
http://www.crifan.com/use_python_beautifulsoup_findall_to_find_money_string
 
Author:     Crifan Li
Version:    2013-06-06
Contact:    http://www.crifan.com/contact_me
"""
 
import re;
from BeautifulSoup import BeautifulSoup;
 
def beautifulsoup_capture_money():
    """
        1. answer other's question
        2. demo BeautifulSoup usage: findAll(text=xxx)
    """
    html = """<tr>
    <td width='150px'><strong>报表日期</strong></td>
    <td style='text-align:right;'>2013-03-31</td>
</tr>
<tr>
</tr>
<tr>
    <td colspan='5'><strong>流动资产</strong></td>
</tr>
<tr>
    <td style='padding-left:30px' width='150px'>
        <a target='_blank' href='/corp/view/vFD_FinanceSummaryHistory.php?stockid=002024&type=cbsheet1'>货币资金</a>
    </td>
    <td style='text-align:right;'>24,804,000,000.00</td>
</tr>
<tr>
    <td style='padding-left:30px' width='150px'><a target='_blank' href='/corp/view/vFD_FinanceSummaryHistory.php?stockid=002024&type=cbsheet110'>交易性金融资产</a></td>
    <td style='text-align:right;'>1,511,750,000.00</td>
</tr>
</tbody>""";
    soup = BeautifulSoup(html);
     
    #\d+(,\d+)*\.\d+
    #can match:
    #24,804,000,000.00
    #1,511,750,000.00
    #123,750,000.00
    #123,000.456
    #23400.456
    #...
     
    foundTds = soup.findAll(name="td", attrs={"style":"text-align:right;"}, text=re.compile("\d+(,\d+)*\.\d+"));
     
    # !!! here match only the match re.compile text, not whole td tag
    print "foundTds=",foundTds; #foundTds= [u'24,804,000,000.00', u'1,511,750,000.00']
    if(foundTds):
        for eachMoney in foundTds:
            print "eachMoney=",eachMoney;
            # eachMoney= 24,804,000,000.00
            # eachMoney= 1,511,750,000.00
     
if __name__ == "__main__":
    beautifulsoup_capture_money();