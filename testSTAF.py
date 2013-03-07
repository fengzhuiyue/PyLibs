from PYSTAF import *
import os
import sys
staticHandleNumber = os.environ.get('STAF_STATIC_HANDLE')

result = handle.submit("local", "ping", "ping")
print result
