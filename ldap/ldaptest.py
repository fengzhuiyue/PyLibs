#!/usr/bin/python
#-*- coding:utf-8 -*-                          #设置源码文件编码为utf-8

import ldap                        

try:
   conn = ldap.open("server_name")             #server_name为ldap服务器名
   conn.protocol_version = ldap.VERSION3       #设置ldap协议版本
   username = "cn=xxxx,dc=xxx,dc=com"     #用户名
   password = "xxxx"                            #访问密码
   conn.simple_bind(username,password)         #连接

except ldap.LDAPError, e:                      #捕获出错信息
   print e

baseDN = "dc=xxx,dc=com"      #设置目录的搜索路径起点
searchScope = ldap.SCOPE_SUBTREE               #设置可搜索子路径

retrieveAttributes = None                      #None表示搜索所有属性，['cn']表示只搜索cn属性
searchFilter = "cn=xxxx"                       #设置过滤属性，这里只显示cn=test的信息

try:
   ldap_result_id = conn.search(baseDN,searchScope,searchFilter,retrieveAttributes)                                 
#调用search方法返回结果id
   result_set = []
while 1:
   result_type, result_data = conn.result(ldap_result_id, 0)       #通过结果id返回信息
   if result_data == []:
      break
   else:
      if result_type == ldap.RES_SEARCH_ENTRY:
         result_set.append(result_data)                  

   print result_set[0][0][1]['o'][0]       #result_set是一个复合列表，需通过索引返回组织单元(o)信息 

except ldap.LDAPError, e:
   print e
