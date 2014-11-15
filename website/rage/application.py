import os
import tornado.web
from rage.handlers.home import HomeHandler


class Application(tornado.web.Application):
    def __init__(self):
        # the current list of tracks that are playable
        self.music = []

        handlers=[
            (r"/", HomeHandler),
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
        )

        tornado.web.Application.__init__(self, handlers, **settings)
