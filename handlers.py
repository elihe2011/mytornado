import tornado.web

from models import User


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie('user')
        if not user_id:
            return None

        return self.db.query(User).get(user_id)


class UserHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        user = self.db.query(User).filter(User.username == username, User.password == password).first()
        if not user:
            self.set_status(404)
            self.finish({'code': 404, 'reason': 'username or password error'})
        else:
            self.set_secure_cookie('user', str(user.id))
            self.finish(user.format())