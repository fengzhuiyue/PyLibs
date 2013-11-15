from util import *
import re,urllib,cookielib,urllib2
import socket
socket.setdefaulttimeout(5)
def sortDic(Dict):
        return sorted(Dict.items(),key=lambda e:e[1])

class crawl:
	def __init__(self,ini):
		self.pages=[]
		self.pages.append(ini)
		self.add=True
		
	def PageParser(self,page):
		print page
		directions=re.findall(r'\s*href\s*=\s*"(https?://[^"^\s^\(^\)]*)',page)
#only add new pages when less then 100 pages		
		if len(self.pages)>10:
			self.add=False
		if self.add==True:	
			for direccion in directions:
				if not direccion.endswith(".js") and not direccion.endswith(".css") and not direccion.endswith(".exe") \
				and not direccion.endswith(".pdf"):
					self.pages.append(direccion)
				print self.pages
	
	def PageLoad(self,dir):
		print dir
		page=urllib.urlopen(dir)
		self.PageParser(page.read())
	
	def crawl_pages(self):
		while len(self.pages)!=0:
			self.PageLoad(self.pages.pop(0))

class douban(object):
    def __init__(self):  
        self.app = ''  
        self.signed_in = False  
        self.cj = cookielib.LWPCookieJar()  
        try:  
           self.cj.revert('douban.coockie')  
        except:  
            None  
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))  
        urllib2.install_opener(self.opener)  
    def setinfo(self,username,password,domain,origURL):
                self.name=username
                self.pwd=password
                self.domain=domain
                self.origURL=origURL
    def signin(self):  
        i=0
        params = {'form_email':self.name, 'form_password':self.pwd, 'remember':1}  
        req = urllib2.Request(  
            'http://www.douban.com/login',  
            urllib.urlencode(params)  
        )  
		
        r = self.opener.open(req)
        if r.geturl() == 'http://www.douban.com/':  
            print 'Logged on successfully!'  
            self.cj.save('douban.coockie')  
            self.signed_in = True
            page=urllib.urlopen("http://www.douban.com")
            print page.read()
            return 0
        return 1
dou=douban()
username=raw_input()
password=raw_input()
domain='http://www.douban.com/'
origURL='http://www.douban.com/login'
dou.setinfo(username,password,domain,origURL)
dou.signin()
page=dou.opener.open('http://www.douban.com/contacts/list')
directions=re.findall(r'\s*href\s*=\s*"http://www.douban.com/people/([^/]*)',page.read())
dir={}
dir_book={}
i=0
for direction in directions:
    dir[direction]=0
num=len(dir)
i=0
for nam, nothing in dir.items():
    name="http://book.douban.com/list/"+nam+"/collect"
    print name
    #i=i+1
    print "books of",nam,":"
    page=dou.opener.open(name)
    while True:
        p=page.read()
        books=re.findall(r'href="http://book.douban.com/subject/.*/">\s*([^<]*)',p)
        for book in books:
            print book
            if book in dir_book:
                dir_book[book]=dir_book[book]+1
            else:
                dir_book[book]=1
        ds=re.search(r'</a><span class="next"><a[\n\s]*href="(http://[^"]*)">',p)      
        if ds == None:
            break
        page=dou.opener.open(ds.group(1))     
        
for book_name,times in sortDic(dir_book):
    print book_name+": "+str(times)
print len(dir_book) 
