import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
tornado.options.parse_command_line()

class UpperHandler(tornado.web.RequestHandler):
	def get(self):
		string = self.get_argument("string")
		self.write(string.upper())

class LowerHandler(tornado.web.RequestHandler):
	def get(self):
		string = self.get_argument("string")
		self.write(string.lower())

# more than one "handler"
application = tornado.web.Application(
		handlers=[(r"/upper", UpperHandler), (r"/lower", LowerHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
