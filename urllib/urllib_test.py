#!/usr/bin/python
# -*- coding:utf-8 -*-
# urllib_test.py

import os
import urllib
url = "xxx"

def use_urllib():
  import urllib, httplib
  httplib.HTTPConnection.debuglevel = 1 
  page = urllib.urlopen(url)
  print "status:", page.getcode() #200,404
  print "url:", page.geturl()
  print "head_info:\n",  page.info()
  print "Content len:", len(page.read())


def urllib_other_functions():
  astr = urllib.quote('this is "K"')
  print astr
  print urllib.unquote(astr)
  bstr = urllib.quote_plus('this is "K"')
  print bstr
  print urllib.unquote(bstr)

  params = {"a":"1", "b":"2"}
  print urllib.urlencode(params)

  l2u = urllib.pathname2url(r'd:\a\test.py')
  print l2u 
  print urllib.url2pathname(l2u)
  
def  callback_f(downloaded_size, block_size, romote_total_size):
  per = 100.0 * downloaded_size * block_size / romote_total_size
  if per > 100:
    per = 100 
  # print "%.2f%%"% per 

def use_urllib_retrieve():
  import urllib
  local = os.path.join(os.path.abspath("./"), "xxx.html")
  # print local
  urllib.urlretrieve(url,local,callback_f)
  
use_urllib_retrieve()
