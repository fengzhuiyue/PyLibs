2013-03-11 磁针石

#承接软件自动化实施与培训等gtalk：ouyangchongwu#gmail.comqq 37391319 博客:http://blog.csdn.net/oychw
#版权所有，转载刊登请来函联系
# 深圳测试自动化python项目接单群113938272深圳会计软件测试兼职 6089740 
#深圳地摊群 66250781武冈洞口城步新宁乡情群49494279
#自动化测试和python群组： http://groups.google.com/group/automation_testing_python
#参考资料：《The PythonStandard Library by Example 2011》
#http://docs.python.org/2/howto/sockets.html
 
底层的socket库可以直接访问本地Csocket库并且可与任何网络服务通信。select同时监控多个sockets，支持网络服务和多个客户端通信。
 
 
SocketServer框架抽象了很多创建网络服务器的重复工作。该类来可以使用fork或者线程创建服务器，支持TCP或UDP，用户只需要处理应用实际的消息处理。
 
asyncore实现了一个基于回调API的异步网络栈。它封装了轮询循环和缓冲，当接收数据时调用相应的处理程序。asynchat框架在asyncore的基础上简化了创建的双向基于消息协议的过程。
 
socket模块展示了使用BSD socketAPI在网络上进行通信的低级的C API。它包括用于处理实际数据信道socket类，还包括用于与网络相关的任务的功能，比如转换一个服务器的名字为地址和格式化要发送的数据
 
11.1 socket– 网络通信
套接字是程序使用通信信道用来本地或网络上来回传送数据的一个端点。套接字有两个基本属性用来控制发送数据：地址族控制的OSI网络层使用的协议，套接字类型控制输送层协议。
Python支持的3种地址族。最常见的AF_INET，用于IPv4的互联网寻址。几乎目前所有互联网联网使用IP版本4。
AF_INET6用于IPv6互联网寻址。IPv6是“下一代”版本的互联网协议。它支持128位的地址，流量控制和IPv4不支持的路由功能。IPv6有限使用，但持续增长。
AF_UNIX是UNIX域套接字（UDS），是POSIX兼容的系统上进程间的通信协议。UDS的实现通常允许操作系统不用通过网络堆栈在进程间 直接通信。这比使用AF_INET更高效，但使用文件系统被作为命名空间进行寻址，UDS限制在同一系统。吸引力在于在IPC使用UDS，比如命名管道或 共享内存的编程接口和IP网络一致。这应用程序可以使用网络通信同样的代码在单机上实现有效的通信机制。
 
套接字类型通常是为SOCK_DGRAM用户数据报协议（UDP）或SOCK_STREAM传输控制协议（TCP）。 tcp一般用户传送大量数据，udp一般用于传送少量数据或者多播。
Socket展示了使用BSDsocket接口进行网络通信的低层CAPI。它包括socket类，用于处理实际数据通道，还包含网络相关的功能，比如转换服务器名为地址，格式化要发送的数据。
11.1.1 寻址、协议家族和socket类型
 
套接字是程序在本地或者跨因特网来回传递数据的通信通道的端点。Socket有两个控制发送数据的基本属性：addressfamil控制使用OSI网络层协议，sockettype控制传输层协议。
Python支持三种地址家族。最常见的AF_INET用于IPv4的互联网寻址。 IPv4地址是4个字节长，为四个数字，以点分隔（例如，10.1.1.5和127.0.0.1），这些值通常称为“IP地址。”几乎目前所有的互联网网络是使用IPv4。
              AF_INET6是用于IPv6互联网寻址。 IPv6是“下一代”版本在Internet协议，采用128位的地址，它支持IPv4下不支持的流量整形和路由功能。IPv6使用依然有限的，但继续增长。
              AF_UNIX是UNIX域套接字（UDSUNIXDomain Sockets），是POSIX兼容的系统进程交互的通信协议。它常允许操作系统在进程间传递数据，无需通过网络栈，这是比使用POSIX兼容的系统进行更有效率。由于使用了文件系统作为namespace来寻址，UDS
限制在同一系统上的进程。建议在其他的IPC机制上使用UDS，如命名管道或共享内存机制，这样编程接口就和IP网络相同。这意味着应用程序本地可以有效的通信，且使用相同的代码可在网络上发送数据。
套接字是程序使用通信信道用来本地或网络上来回传送数据的一个端点。套接字有两个基本属性用来控制
发送数据：地址族控制的OSI网络层使用的协议，套接字类型控制输送层协议。
Python支持的3种地址族。最常见的AF_INET，用于IPv4的互联网寻址。几乎目前所有互联网联网使用IP版本4。
AF_INET6用于IPv6互联网寻址。 IPv6是“下一代”版本的互联网协议。它支持128位的地址，流量控制和IPv4不支持的路由功能。IPv6有限使用，但继续
增长。
AF_UNIX是UNIX域套接字（UDS），是POSIX兼容的系统上进程间的通信协议。UDS的实现通常允许操作系统不用通过网络堆栈在进程间 直接通信。这比使用AF_INET更高效，但使用文件系统被作为命名空间进行寻址，UDS限制在同一系统。吸引力在于在IPC使用UDS，比如命名管道或 共享内存的编程接口和IP网络一致。这应用程序可以使用网络通信同样的代码在单机上实现有效的通信机制。
套接字类型通常是为SOCK_DGRAM用户数据报协议（UDP）或SOCK_STREAM传输控制协议（TCP）。 tcp一般用户传送大量数据，udp一般用于传送少量数据或者多播。
11.1.1.1查找主机：
socket.gethostbyname(hostname) 
翻译的主机名IPv4地址格式。以字符串形式返回的IPv4地址，如'100.50.200.5“。如果是一个IPv4地址的主机名，它原封不动地 返回。更完整的接口参见gethostbyname_ex()。gethostbyname（）的不支持IPv6名称解析，可以使用 getaddrinfo（）获取IPv4/v6双协议栈支持。
 
   import socket
   for host in [ ’homer’, ’www’, ’www.python.org’, ’nosuchname’ ]:
   try:
       print ’%s : %s’ % (host, socket.gethostbyname(host))
   except socket.error, msg:
       print ’%s : %s’ % (host, msg)
   
   执行结果：
   # python socket_gethostbyname.py
   homer : [Errno -2] Name or service not known
   www : [Errno -2] Name or service not known
   www.python.org : 82.94.164.162
   nosuchname : [Errno -2] Name or service not known    
 
socket.gethostbyname_ex(hostname) 
翻译的主机名IPv4地址格式的扩展接口。返回一个三元组（hostname，aliaslist，ipaddrlist），gethostbyname_ex（）不支持IPv6名称解析，可以使用getaddrinfo（）获取IPv4/v6双协议栈支持。
   import socket
 
   for host in [ 'homer', 'www', 'www.python.org', 'nosuchname' ]:
       print host
       try:
            hostname, aliases, addresses =socket.gethostbyname_ex(host)
            print '  Hostname:', hostname
            print '  Aliases :', aliases
            print ' Addresses:', addresses
       except socket.error as msg:
            print 'ERROR:', msg
       print
       
   执行结果：
   # python socket_gethostbyname_ex.py
   homer
   ERROR: [Errno -2] Name or service not known
 
   www
   ERROR: [Errno -2] Name or service not known
 
   www.python.org
     Hostname: www.python.org
     Aliases : []
    Addresses: ['82.94.164.162']
 
   nosuchname
   ERROR: [Errno -2] Name or service not known
   
socket.getfqdn([name]) 
   返回一个完全的域名。如果名字被省略或为空，默认为本地主机。首先使用gethostbyaddr（）返回的主机名来查找名称，然后是主机的别名。被选中的第一名称，其中包括一个时期。如果没有完全合格的域名，返回的gethostname（）返回的主机名。   
 
   import socket
 
   for host in [ 'homer', 'www' ]:
       print '%6s : %s' % (host, socket.getfqdn(host))  
 
   执行结果：
   $ python socket_getfqdn.py
   homer : homer.hellfly.net
   www : homer.hellfly.net  
 
socket.gethostbyaddr(ip_address) 
返回一个三元组（hostname，aliaslist，ipaddrlist），支持IPv4和IPv6。   
   import socket
 
   hostname, aliases, addresses = socket.gethostbyaddr('172.23.191.53')
 
   print 'Hostname :', hostname
   print 'Aliases  :', aliases
   print 'Addresses:', addresses
   
   执行结果：
   $ python socket_gethostbyaddr.py
   Hostname : homer.hellfly.net
   Aliases : [‘8.1.168.192.in-addr.arpa’]
   Addresses: [‘192.168.1.8’]

试试google
# pingwww.google.com.hk
PINGwww.google.com.hk (173.194.65.103) 56(84) bytes of data.
64 bytes fromee-in-f103.1e100.net (173.194.65.103): icmp_seq=1 ttl=35 time=421 ms
# python
Python 2.6.6(r266:84292, Jun 18 2012, 14:10:23) 
[GCC 4.4.620110731 (Red Hat 4.4.6-3)] on linux2
Type"help", "copyright", "credits" or"license" for more information.
>>>import socket
>>>socket.gethostbyaddr('173.194.65.103')
('ee-in-f103.1e100.net',[], ['173.194.65.103']
可见返回地址'ee-in-f103.1e100.net'不等于’www.google.com.hk’，不知google被和谐的时候是否可以用'ee-in-f103.1e100.net'来访问，百度实在太垃圾了。

11.1.1.2 查找服务信息：
              socket.getservbyname(servicename[,protocolname]) 
翻译的互联网服务名称和协议的名称为端口号。协议名称，如果有，应该是“TCP”或“UDP”，否则，任何协议都将匹配。
 
    import socket
    from urlparse import urlparse
 
    for url in [ 'http://www.python.org',
                 'https://www.mybank.com',
                 'ftp://prep.ai.mit.edu',
                'gopher://gopher.micro.umn.edu',
                 'smtp://mail.example.com',
                 'imap://mail.example.com',
                 'imaps://mail.example.com',
                 'pop3://pop.example.com',
                 'pop3s://pop.example.com',
                 ]:
        parsed_url = urlparse(url)
        port = socket.getservbyname(parsed_url.scheme)
        print '%6s : %s' % (parsed_url.scheme,port)
        
    执行结果：
    # python socket_getservbyname.py
      http : 80
     https : 443
       ftp : 21
    gopher : 70
      smtp : 25
      imap : 143
     imaps : 993
      pop3 : 110
     pop3s : 995
 
socket.getservbyport(port[,protocolname]) 
翻译的Internet端口号和协议名称为服务名，服务。协议名称，如果有，应该是“TCP”或“UDP”，否则，任何协议都将匹配。
 
    import socket
    import urlparse
 
    for port in [ 80, 443, 21, 70, 25, 143,993, 110, 995 ]:
        print urlparse.urlunparse(
            (socket.getservbyport(port),'example.com', '/', '', '', '')
            )
    执行结果：
    # python socket_getservbyport.py
    http://example.com/
    https://example.com/
    ftp://example.com/
    gopher://example.com/
    smtp://example.com/
    imap://example.com/
    imaps://example.com/
    pop3://example.com/
    pop3s://example.com/ 
 
socket.getprotobyname（protocolname）
翻译的互联网协议名（例如，“ICMP”），为适合的socket（）函数的第三个参数（可选）的常量。这通常只是“原始”模式（SOCK_RAW）需要，普通socket模式会自动选择正确的协议，设置为0或者或略就可。 
    import socket
 
    def get_constants(prefix):
        """Create a dictionarymapping socket module
        constants to their names.
        """
        return dict( (getattr(socket, n), n)
                     for n in dir(socket)
                     if n.startswith(prefix)
                     )
 
    protocols = get_constants('IPPROTO_')
    print protocols
 
    for name in [ 'icmp', 'udp', 'tcp' ]:
        proto_num = socket.getprotobyname(name)
        print proto_num
        const_name = protocols[proto_num]
        print '%4s -> %2d (socket.%-12s =%2d)' % \
            (name, proto_num, const_name,getattr(socket, const_name))
    执行结果：
    # python socket_getprotobyname.py
    {0: 'IPPROTO_IP', 1: 'IPPROTO_ICMP', 2:'IPPROTO_IGMP', 4: 'IPPROTO_IPIP', 6: 'IPPROTO_TCP', 8: 'IPPROTO_EGP', 12:'IPPROTO_PUP', 17: 'IPPROTO_UDP', 22: 'IPPROTO_IDP', 29: 'IPPROTO_TP', 41:'IPPROTO_IPV6', 43: 'IPPROTO_ROUTING', 44: 'IPPROTO_FRAGMENT', 46:'IPPROTO_RSVP', 47: 'IPPROTO_GRE', 50: 'IPPROTO_ESP', 51: 'IPPROTO_AH', 58:'IPPROTO_ICMPV6', 59: 'IPPROTO_NONE', 60: 'IPPROTO_DSTOPTS', 103:'IPPROTO_PIM', 255: 'IPPROTO_RAW'}
    1
    icmp -> 1 (socket.IPPROTO_ICMP =  1)
    17
     udp -> 17 (socket.IPPROTO_UDP  = 17)
    6
     tcp -> 6 (socket.IPPROTO_TCP  =  6)
              协议的数值是标准化的，在socket中以前缀IPPROTO_开头的常量存在。
11.1.1.3 查找服务器地址：
socket.getaddrinfo(host, port, family=0,socktype=0, proto=0, flags=0) 
翻译host/port参数为成一个5元组（包含创建连接至该服务的socket的必需参数）构成的序列。主机是一个域名，IPv4/v6的地址 “或None。端口是一个字符串：服务的名称，如'http'，数字端口号或None。host和port都为None，传递的就是底层cAPI的 NULL。
family可以填写socktype和proto参数以缩写返回地址的列表。0为最大范围。可以有1或者多个AI_*常量构成。比如AI_NUMERICHOST将禁止域名解析。如果主机是一个域名将引发一个错误。
该函数返回一个具有以下结构的5- 元组列表：
(family, socktype, proto, canonname,sockaddr)
family，socktype，proto都是传递给的整数。如果flags包含AI_CANONNAME，canonname表示 canonical名，否则就为空。sockaddr是描述套接字地址的元组：AF_INET返回为(address,port)，AF_INET6返回 为AF_INET6。其格式依赖于返回的家庭（（地址，port）2AF_INET，元组（地址，端口流量信息，范围ID）四元AF_INET6），并会 传递给Socket.connect（）的方法。
下例为www.python.org的地址信息。
>>> import socket
>>>socket.getaddrinfo("www.python.org", 80, 0, 0, socket.SOL_TCP)
[(10, 1, 6, '', ('2001:888:2000:d::a2',80, 0, 0)), (2, 1, 6, '', ('82.94.164.162', 80))]
 
   import socket
 
   def get_constants(prefix):
       """Create a dictionary mapping socket module
       constants to their names.
       """
       return dict( (getattr(socket, n), n)
                    for n in dir(socket)
                     if n.startswith(prefix)
                     )
 
   families = get_constants('AF_')
   types = get_constants('SOCK_')
   protocols = get_constants('IPPROTO_')
 
   for response in socket.getaddrinfo('www.python.org', 'http'):
 
       # Unpack the response tuple
       family, socktype, proto, canonname, sockaddr = response
 
       print 'Family        :',families[family]
       print 'Type          :',types[socktype]
       print 'Protocol      :',protocols[proto]
       print 'Canonical name:', canonname
       print 'Socket address:', sockaddr
       print 
       
   执行结果：
   # python socket_getaddrinfo.py
   Family        : AF_INET6
   Type          : SOCK_STREAM
   Protocol      : IPPROTO_TCP
   Canonical name: 
   Socket address: ('2001:888:2000:d::a2', 80, 0, 0)
 
   Family        : AF_INET6
   Type          : SOCK_DGRAM
   Protocol      : IPPROTO_UDP
   Canonical name: 
   Socket address: ('2001:888:2000:d::a2', 80, 0, 0)
 
   Family        : AF_INET6
   Type          : SOCK_STREAM
   Protocol      :
   Traceback (most recent call last):
     File "socket_getaddrinfo.py", line 32, in <module>
       print 'Protocol      :',protocols[proto]
   KeyError: 132
   
   设置了AI_CANONNAME的实例：
   import socket
 
   def get_constants(prefix):
       """Create a dictionary mapping socket module
       constants to their names.
       """
       return dict( (getattr(socket, n), n)
                     for n in dir(socket)
                     if n.startswith(prefix)
                     )
 
   families = get_constants('AF_')
   types = get_constants('SOCK_')
   protocols = get_constants('IPPROTO_')
 
   for response in socket.getaddrinfo('www.doughellmann.com', 'http',
                                      socket.AF_INET,      # family
                                      socket.SOCK_STREAM,  # socktype
                                      socket.IPPROTO_TCP,  # protocol
                                       socket.AI_CANONNAME, # flags
                                       ):
       
       # Unpack the response tuple
       family, socktype, proto, canonname, sockaddr = response
 
       print 'Family        :',families[family]
       print 'Type          :',types[socktype]
       print 'Protocol      :',protocols[proto]
       print 'Canonical name:', canonname
       print 'Socket address:', sockaddr
       print 
       
   执行结果：
   # python socket_getaddrinfo_extra_args.py
   Family        : AF_INET
   Type          : SOCK_STREAM
   Protocol      : IPPROTO_TCP
   Canonical name: www.doughellmann.com
   Socket address: ('208.97.185.20', 80)
11.1.1.4 IP地址表示：
C网络程序使用structsockaddr来表示IP地址，是二进制，而不是python中常见的二进制。IPv4在python和c之间的切换使用inet_aton()和inet_ntoa()。
 
socket.inet_aton(ip_string)
把字符串格式的ip地址转换为c语言格式，比如‘192.168.1.1’->c0a80101。支持IPV6需要使用inet_pton。
socket.inet_ntoa(packed_ip)和上面的刚好相反：
 
    import binascii
    import socket
    import struct
    import sys
 
    for string_address in [ '192.168.1.1','127.0.0.1' ]:
        packed =socket.inet_aton(string_address)
        print 'Original:', string_address
        print 'Packed  :', binascii.hexlify(packed)
        print 'Unpacked:',socket.inet_ntoa(packed)
        print
    
    注意hexlify是返回2进制数据的16进制表示。
    执行结果：
    # python socket_address_packing.py
    Original: 192.168.1.1
    Unpacked: 192.168.1.1
 
    Original: 127.0.0.1
    Unpacked: 127.0.0.1  
    
    适用于ipv6的例子：
    import binascii
    import socket
    import struct
    import sys
 
    string_address ='2002:ac10:10a:1234:21e:52ff:fe74:40e'
    packed = socket.inet_pton(socket.AF_INET6,string_address)
 
    print 'Original:', string_address
    print 'Packed  :', binascii.hexlify(packed)
    print 'Unpacked:',socket.inet_ntop(socket.AF_INET6, packed)   
    
    执行结果：
    # python socket_ipv6_address_packing.py
    Original:2002:ac10:10a:1234:21e:52ff:fe74:40e
    Packed : 2002ac10010a1234021e52fffe74040e
    Unpacked:2002:ac10:10a:1234:21e:52ff:fe74:40e   
 
注意IPV6本身就是二进制表示的，且inet_pton()and inet_ntop()只适用于linux平台。
参考资料：IPv6(http://en.wikipedia.org/wiki/IPv6)
OSI NetworkingModel (http://en.wikipedia.org/wiki/OSI_model)
AssignedInternet Protocol Numbers
(www.iana.org/assignments/protocol-numbers/protocol-numbers.xml)
 

