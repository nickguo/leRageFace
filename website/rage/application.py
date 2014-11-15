import os
import tornado.web
from rage.handlers.home import HomeHandler
from rage.handlers.rage import RageHandler


class Application(tornado.web.Application):
    def __init__(self):

        handlers=[
            (r"/rage", RageHandler),
            (r"/", HomeHandler),
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
        )

        tornado.web.Application.__init__(self, handlers, **settings)
