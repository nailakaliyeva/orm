import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Users (Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    handle = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    registrationDate = Column(Integer)
    img = Column(String)


class Followers (Base):
    __tablename__ = 'followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    recordId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.userId'))
    followingWho = Column(Integer, ForeignKey('users.userId'))


class Posts (Base):
    __tablename__ = 'posts'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    postId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.userId'))
    commentId = Column(Integer, ForeignKey('comments.commentId'))
    img = Column(String)
    likes = Column(Integer, ForeignKey('likes.likeId'))


class Comments (Base):
    __tablename__ = 'comments'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    commentId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.userId'))
    postId = Column(Integer, ForeignKey('posts.postId'))
    img = Column(String)
    likes = Column(Integer, ForeignKey('likes.likeId'))


class Likes (Base):
    __tablename__ = 'likes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    likeId = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('posts.postId'))
    userId = Column(Integer, ForeignKey('users.userId'))
    commentId = Column(Integer, ForeignKey('comments.commentId'))


class Conversations (Base):
    __tablename__ = 'conversations'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    messageId = Column(Integer, primary_key=True)
    conversationId = Column(Integer)
    userId = Column(Integer, ForeignKey('users.userId'))
    theMessageContent = Column(String(500))


    #def to_dict(self):
    #    return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')