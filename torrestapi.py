import tornado.web
import tornado.ioloop

 
class GetUserName(tornado.web.RequestHandler):
    def get(self, uname):
        response = 'Hello, '+ uname
        self.write(response)
 
application = tornado.web.Application([
    (r"/user/([a-zA-Z0-9]+)", GetUserName)
])
 
if __name__ == "__main__":
	try:
		application.listen(8000)
		tornado.ioloop.IOLoop.instance().start()
		
	except KeyboardInterrupt:
	
         print("\nStop the username service")