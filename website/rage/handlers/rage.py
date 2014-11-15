import tornado.web

class RageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("static/img/yao.png");
