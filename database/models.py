from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from database import base


# Таблица пользователя
class User(base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    e_mail = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    points = Column(Integer, default=100)
    products_bought = Column(Integer, default=0)
    created_at = Column(DateTime)


# Таблица продукта
class Products(base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    product_name = Column(String, unique=True, nullable=False)
    product_des = Column(String, nullable=False)
    product_quantity = Column(Integer, default=10)
    product_price = Column(Float, default=10)
    added_at = Column(DateTime)


# Для добавления фото продукта
class ProductPhoto(base):
    __tablename__ = 'product_photos'
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    photo_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    photo_path = Column(String)

    product_fk = relationship(Products, lazy='subquery')


# Таблица для отзывов
class Review(base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    review_text = Column(Text, nullable=False)
    posted_at = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    product_fk = relationship(Products, lazy='subquery')
