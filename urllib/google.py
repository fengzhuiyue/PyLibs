import urllib
import urllib2
import urlparse
import lxml.html

def url_with_query(url, values):
	parts = urlparse.urlparse(url)
	rest, (query, frag) = parts[:-2], parts[-2:]
	return urlparse.urlunparse(rest + (urllib.urlencode(values), None))

def make_open_http():
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	opener.addheaders = [] # pretend we’re a human — don’t do this
	
def open_http(method, url, values={}):
	if method == "POST":
		return opener.open(url, urllib.urlencode(values))
	else:
		return opener.open(url_with_query(url, values))
	return open_http

open_http = make_open_http()
tree = lxml.html.fromstring(open_http("GET", "http://www.google.com").read())
form = tree.forms[0]
form.fields["q"] = "eplussoft"
form.action="http://www.google.com/search"

response = lxml.html.submit_form(form,open_http=open_http)
html = response.read()
doc = lxml.html.fromstring(html)
lxml.html.open_in_browser(doc)
