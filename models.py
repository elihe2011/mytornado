from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost/test', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(75), nullable=False)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return "<User('%s')>" % self.username

    def format(self):
        data = {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }

        return data


users_table = User.__table__
metadata = Base.metadata


def create_all():
    metadata.create_all(engine)


if __name__ == '__main__':
    create_all()

