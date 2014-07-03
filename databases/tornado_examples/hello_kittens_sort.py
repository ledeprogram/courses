import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
tornado.options.parse_command_line()

# connect here to mongodb
conn = pymongo.Connection("localhost")

class KittensHandler(tornado.web.RequestHandler):
	def get(self):
		db = conn['lede_program']
		collection = db['kittens']
		# try to get "sort" param from query string, default to "name"
		sort_field = self.get_argument("sort", "name")
		# use .sort() on query
		kittens = list(collection.find({}, {"_id": 0}).sort(sort_field))
		response = {'results': kittens}
		self.write(response)

application = tornado.web.Application(handlers=[(r"/kittens", KittensHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
