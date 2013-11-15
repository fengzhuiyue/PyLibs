#-*- encoding: utf-8 -*-
import HTMLParser

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)        
        
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
            for name,value in attrs:
                if name == 'href':
                    print value
        

if __name__ == '__main__':
    a = '<html><head><title>test</title><body><a href="http://www.163.com">链接到163</a></body></html>'
    
    my = MyParser()
    # 传入要分析的数据，是html的。
    my.feed(a)
