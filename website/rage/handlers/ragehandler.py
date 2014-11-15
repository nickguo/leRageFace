import tornado.web
from rage.server.image import RageFaceGenerator

class RageHandler(tornado.web.RequestHandler):
    def init(self):
        super(self)
        
    def get(self):
        self.write("/static/img/"+RageFaceGenerator().Generate(self.get_argument('img')));
