import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import rage.application


def main():
    application = rage.application.Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start();

if __name__ == "__main__":
    main()
