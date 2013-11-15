from PIL import Image

from captchaidentifier_360buy import CaptchaIdentifier

import cookielib,StringIO, urllib, urllib2

identify = CaptchaIdentifier()

CAPTHA='http://price.360buy.com/PBD442AC08CA07CD61ABAE5EB1FD22189,3.png'
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
img_file = opener.open(CAPTHA)
tmp = StringIO.StringIO(img_file.read())
image = Image.open(tmp)

#image = Image.open('1549.png')
image.show()
numbers = identify.parse(image)

print numbers
