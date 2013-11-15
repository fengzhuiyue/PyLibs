#!/usr/bin/env python
#coding=utf-8

import os,web,time
import sqlite3 as db

urls = (
        '/', 'hello',
        '/add','add'
        )

class hello:
    def GET(self):
        #实例化sqldb，然后获取内容
        s = ""
        sdb = sqldb()
        rec = sdb.cu.execute("""select * from msgs""")
        dbre = sdb.cu.fetchall()       
        for i in dbre:
            s =  "<p>"+i[2]+"  <span style=\"color: blue\">"+i[1]+' sad: '+r"</span>"+"  <span style=\"color: gray\">"+i[3]+r"</span></p>" + s
       
        sh = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><HTML>
        <HEAD><meta http-equiv="X-UA-Compatible" content="IE=8" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <TITLE> OK!</TITLE> </HEAD> <BODY><h1>Hello World!</h1>
        """
        sb = """
        <h2>add a note</h2>
        <form method="post" action="/add">
        UserName:<INPUT TYPE="text" NAME="uname"><br />
        <textarea name="content" ROWS="20" COLS="60"></textarea><br />
        <button type="submit">save</button></form></BODY></HTML>
        """
        s = sh + s + sb
        return s

class add:
    def POST(self):
        i = web.input('content')
        n = web.input('uname')
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        sdb = sqldb()
        rec = sdb.cu.execute("""select * from msgs""")
        dbre = sdb.cu.fetchall()
        for k in dbre:
            j = k[0]+1
        t = (j,n.uname,date,i.content)
        sdb.cu.execute('insert into msgs values(?,?,?,?)',t)
        sdb.conn.commit()
        return web.seeother('/')

    def GET(self):
        return web.seeother('/')

class sqldb:
    #先验证数据库是否存在
    def __init__(self):
        if os.path.exists("msg.db"):
            #如果数据库存在，就直接连接
            self.conn = db.connect("msg.db")
            self.cu = self.conn.cursor()
        else:
            #如果数据库不存在，连接，并生成表
            self.conn = db.connect("msg.db")
            self.cu = self.conn.cursor()
            self.cu.execute("""create table msgs(
                     id integer primary key,
                     name text,
                     date text,
                     content text) """)
            self.cu.execute("""insert into msgs values(1,'Ahai','2010-05-19 15:11:20','Ahi alaws be ok!')""")
            self.conn.commit()

if __name__=="__main__":

    app = web.application(urls,globals())
    app.run()
