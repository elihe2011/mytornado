import tornado.web
import tornado.httpserver
import tornado.ioloop
from sqlalchemy.orm import scoped_session, sessionmaker

from handlers import UserHandler
from models import engine


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/users', UserHandler),
        ]

        settings = dict(
            cookie_secret = 'hard_to_guess'
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection
        self.db = scoped_session(sessionmaker(bind=engine))


if __name__ == '__main__':
    app = Application()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(5000)

    loop = tornado.ioloop.IOLoop.current().start()