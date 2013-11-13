import os
cmd = "pscp -r -pw password username@host:/directory/* C:\\download location\\" 
os.popen(cmd)

# import scp

# client = scp.Client(host=xxx, user=xxx, password='xxx')

#and then
# client.transfer('/directory/', './')

