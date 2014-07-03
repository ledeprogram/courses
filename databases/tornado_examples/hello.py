import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
tornado.options.parse_command_line()

class HelloHandler(tornado.web.RequestHandler):
	def get(self):
		# your stuff goes here
		self.write('hello there!')

application = tornado.web.Application(handlers=[(r"/hello", HelloHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()

