#!/usr/bin/python
#coding: utf-8

def toBig(money=0,rmb=None):
    big = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
    rmb = ['分', '角', '圆', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟', '万','拾', '佰', '仟','万','亿']
    if rmb:
        rmb = rmb
        
    #转成字符串
    str_money = str( int(money * 100) )[::-1]
    big_money = ''
    
    #拼大写金额
    for i in xrange(len(str_money)):
        n = ord(str_money[i]) - ord('0')
        big_money = big[n] + rmb[i] + big_money
    
    #去掉零
    rule = ('零仟', '零',
            '零佰', '零',
            '零拾', '零',
            '零亿', '亿',
            '零万', '万',
            '零元', '元',
            '零角', '零',
            '零分', '零',
            '零零', '零',
            '零亿', '亿',
            '零零', '零',
            '零万', '万',
            '零零', '零',
            '零圆', '圆',
            '亿万', '亿',
            '零', '',
            '圆', '圆整')
    
    for i in xrange(0,len(rule),2):
        big_money = big_money.replace(rule[i], rule[i+1])
        
    return big_money
        
    
if __name__ == '__main__':
    print toBig(1200003456.78)