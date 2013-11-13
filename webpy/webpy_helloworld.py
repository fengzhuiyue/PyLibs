import web

urls = (
  '/', 'index'
  # '/favicon.ico', 'favicon'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return "Hello, world!"
		
# class favicon:
	# def GET(self): 
		# f=open("static/favicon.ico",'rb')
		# return f.read()
		
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
