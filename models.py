from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random
import string


class Bookmarks(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    link = Column(String)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bookmark_id = Column(Integer, ForeignKey('bookmarks.id'))

engine = create_engine('sqlite:///Bookmarks.db')

Base.metadata.create_all(engine)
