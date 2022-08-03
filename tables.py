from email.policy import default
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String)
    access = sa.Column(sa.String, default='Client')
    username = sa.Column(sa.String)
    avatar_id = sa.Column(sa.String, default='default.svg')

    date = sa.Column(sa.Date)
