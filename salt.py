import os
from hashlib import sha256
from hmac import HMAC

#http://zhuoqiang.me/a/password-storage-and-python-example
#这里先通过标准随机库生成 64 bits 的随机 salt，使用了标准的 SHA-256 做为基本的 hash 算法，使用标准 HMAC 算法作为 salt 混淆。并且进行了 10 次混淆 hash。最后将 salt 和 hash 结果一起返回。 
def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.
 
    assert 8 == len(salt)
    assert isinstance(salt, str)
 
    if isinstance(password, unicode):
        password = password.encode('UTF-8')
 
    assert isinstance(password, str)
 
    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()
 
    return salt + result

#验证函数 
def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])
	

	
#hashed = encrypt_password('secret password')
#f=open('password.dat','wb')
#f.write(hashed)
#f.close
#f=open('password.dat','rb')
#hashed=f.readlines()
#f.close

hash=encrypt_password('secret password')
#print hashed
print hash
#if hashed==hash:
#	print "match!"
# else:
	# print "not match!"


#assert validate_password(hashed, 'secret password')
