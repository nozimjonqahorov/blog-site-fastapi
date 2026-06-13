from sqlalchemy import Column, String, Integer, DateTime, func, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = 'authors' 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable= False,index = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    posts = relationship('Post', back_populates='author')


class Category(Base):
    __tablename__ = 'categories' 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable= False,index = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    posts = relationship('Post', back_populates='category')

class Post(Base):
    __tablename__ = 'posts' 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable= False,index = True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    author_id = Column(Integer, ForeignKey("authors.id", ondelete='CASCADE'))
    category_id = Column(Integer, ForeignKey("categories.id", ondelete='CASCADE'))

    author = relationship('Author', back_populates='posts')
    category = relationship('Category', back_populates='posts')
    comments = relationship('Comment', back_populates='post')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    usename = Column(String(50), nullable = False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    post_id = Column(Integer, ForeignKey("posts.id", ondelete='CASCADE'))

    post = relationship('Post', back_populates='comments')


class Saved(Base):
    __tablename__ = 'saved_posts'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String(50), nullable = False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete='CASCADE'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    post = relationship('Post')