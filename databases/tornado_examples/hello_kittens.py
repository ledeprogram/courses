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
		# get a collection object...
		db = conn['lede_program']
		collection = db['kittens']
		# exclude "_id" because tornado doesn't know how to json encode it!
		kittens = list(collection.find({}, {"_id": 0}))
		# wrap results in a dictionary
		response = {'results': kittens}
		# tornado will automatically json encode dictionaries passed to self.write
		self.write(response)

application = tornado.web.Application(handlers=[(r"/kittens", KittensHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
