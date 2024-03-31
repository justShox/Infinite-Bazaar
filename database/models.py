from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from database import base


# Таблица пользователя
class User(base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    surname = Column(String)
    phone_number = Column(String, unique=True)
    e_mail = Column(String, unique=True)
    password = Column(String)
    points = Column(Integer, default=100)
    products_bought = Column(Integer, default=0)
    created_at = Column(DateTime)


# Таблица продукта
class Products(base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, unique=True)
    product_des = Column(String)
    product_quantity = Column(Integer, default=10)
    product_price = Column(Float, default=10)
    added_at = Column(DateTime)


# Для добавления фото продукта
class ProductPhoto(base):
    __tablename__ = 'product_photos'
    product_id = Column(Integer, ForeignKey('products.product_id'))
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    photo_path = Column(String)

    product_fk = relationship(Products, lazy='subquery')


# Таблица для отзывов
class Review(base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    review_text = Column(Text)
    posted_at = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    product_fk = relationship(Products, lazy='subquery')
