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

class CongressHandler(tornado.web.RequestHandler):
	def get(self):
		db = conn['lede_program']
		collection = db['legislators']

		# use the query string to build a mongo query
		query = {}
		party_query = self.get_argument("party", None)
		if party_query:
			query['party'] = party_query
		type_query = self.get_argument("type", None)
		if type_query:
			query['type'] = type_query
		state_query = self.get_argument("state", None)
		if state_query:
			query['state'] = state_query

		# for readability, write our field-inclusion dictionary as a separate
		# variable
		fields_to_include = {
			'first_name': 1, 'last_name': 1, 'state': 1, 'gender': 1, 'party': 1,
			'type': 1, 'birthday': 1, '_id': 0
		}
		legislators = list(collection.find(query, fields_to_include))
		response = {'results': legislators}
		self.write(response)

application = tornado.web.Application(
		handlers=[(r"/congress", CongressHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
