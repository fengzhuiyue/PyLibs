#!/usr/bin/env python
#coding:utf8
import re
from BaseHTMLProcessor import BaseHTMLProcessor
import urllib

class Dialectizer(BaseHTMLProcessor):
    subs = ()

    def reset(self):
        # extend (called from __init__ in ancestor)
        # Reset all data attributes
        self.verbatim = 0
        BaseHTMLProcessor.reset(self)

    def unknown_starttag(self, tag, attrs):
        self.pieces.append("")
        
    def unknown_endtag(self, tag):
        self.pieces.append("")
        
    def start_title(self, attrs):
        self.pieces.append("title")  
    
    def end_title(self): 
        self.pieces.append("title")
        
    def start_p(self, attrs):
        self.pieces.append("\n")  
    
    def end_p(self): 
        self.pieces.append("")
        
    def start_div(self, attrs):
        strattrs = "".join([value for key, value in attrs])
        self.pieces.append(strattrs)        
       
    
    def end_div(self):  
        self.pieces.append("div") 
    
    def handle_data(self, text):
        self.pieces.append(self.verbatim and text or self.process(text))

    def process(self, text):
        for fromPattern, toPattern in self.subs:
            text = re.sub(fromPattern, toPattern, text)
        return text


def translate(url):    
    import urllib                      
    sock = urllib.urlopen(url)         
    htmlSource = sock.read()           
    sock.close()                    
    parser = Dialectizer()
    #parser.subs=((r"&#26412;",r"aaa"),)
    parser.feed(htmlSource)#进行解析
    parser.close()         
    return parser.output() 

def test(url,filename):
    htmlSource=translate(url)
    #标题
    title=htmlSource[re.search("title",htmlSource).end():]
    title=title[:re.search("title",title).end()-5]
    #内容
    content=htmlSource[re.search("articleBody",htmlSource).end()+2:]
    content=content[:re.search("div",content).end()-3]
    content=re.sub("&nbsp;","",content)
    content=re.sub("nbsp;","",content)
    #文件名称
    fileName=title;
    #输出的文件内容
    fileContent=title+"\n\n\n"+content;    
    fsock = open(filename, "wb")
    fsock.write(fileContent)
    fsock.close()

if __name__ == "__main__":
    test("http://blog.sina.com.cn/s/blog_4bd7b9a20100cpgb.html",'test.txt')
    

