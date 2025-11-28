from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    subcategory = Column(String, nullable=True)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String, nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)