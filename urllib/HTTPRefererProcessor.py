import urllib2,cookielib

class HTTPRefererProcessor(urllib2.BaseHandler):
	def __init__(self):
		self.referer = None

	def http_request(self, request):
		if ((self.referer is not None) and not request.has_header("Referer")):
			request.add_unredirected_header("Referer", self.referer)
			return request

	def http_response(self, request, response):
		self.referer = response.geturl()
		return response

https_request = http_request
https_response = http_response

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), HTTPRefererProcessor(),)

urllib2.install_opener(opener)

data = 'msisdn=999999'
request = urllib2.Request(
url = 'http://203.117.16.171:8080/webgamecode/webcore?action=topup',
headers = {'Content-Type': 'application/x-www-form-urlencoded'},
data = data)

ret = opener.open(request)
content = ret.read()
print content
