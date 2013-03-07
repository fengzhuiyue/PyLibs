import os
cmd = "pscp -r -pw password userid@hostname:/dir/* C:\\dir\\"
os.popen(cmd)

# import scp

# client = scp.Client(host=xxx, user=xxx, password='xxx')

#and then
# client.transfer('/dir/', './')

cmd = "pscp -r -pw %s %s@hostname:/dir .\\" % (password=xxx,user=xxx) 
os.popen(cmd)
