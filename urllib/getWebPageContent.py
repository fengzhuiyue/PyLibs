import urllib2

def getWebPageContent(url): 
	f = urllib.urlopen(url) 
	data = f.read() 
	f.close() 
	return data 

url = 'http://m.letao.com/wap/myletao/myorder.aspx?uuid1314082638&ltsession=3331812830842197' 
content = getWebPageContent(url) 
print content
