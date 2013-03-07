import time

start =time.clock()
#code 1 start
s=open('source.txt')
line=s.readlines()
s.close()

line.sort()
t=open('taget.txt','w')
for x in line:
    t.writelines(x)
t.close()
#code 1 end

# code 2 start
#import 


end = time.clock()-start
print end
