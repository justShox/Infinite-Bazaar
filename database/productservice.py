from database.models import Products
from datetime import datetime
from database import get_db


# Добавление продукта
def add_product_db(product_name: str, product_des: str, product_price: float, product_quantity: int):
    db = next(get_db())
    check = db.query(Products).filter_by(product_name=product_name).first()
    if check:
        return 'Такой товар уже существует!'
    else:
        new_product = Products(product_name=product_name, product_des=product_des,
                               product_price=product_price,
                               product_quantity=product_quantity, added_at=datetime.now())
        if 0 < new_product.product_quantity <= 9999 and 0 < new_product.product_price <= 999:
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return f'Продукт {product_name} добавлен'
        else:
            return 'Ошибка при заполнении информации'


# Удаление продукт
def delete_product_db(product_id: int):
    db = next(get_db())
    check = db.query(Products).filter_by(product_id=product_id).first()
    if check:
        db.delete(check)
        db.commit()
        return 'Продукт удален'
    else:
        return 'Продукт не найден'


# Получить инфу по определенному продукту
def get_product_db(product_id: int):
    db = next(get_db())
    check = db.query(Products).filter_by(product_id=product_id).first()
    if check:
        return check
    else:
        return 'Товар не найден'


# Добавить количество продукта
def update_product_quantity_db(product_id: int, new_amount: int):
    db = next(get_db())
    check = db.query(Products).filter_by(product_id=product_id).first()
    if check:
        if 0 < new_amount <= 1000:
            check.product_quantity += new_amount
            db.commit()
            return f'Склад {check.product_name} пополнен - {check.product_quantity}'
        else:
            return 'Ошибка количества продукта 0 < x <= 1000'
    else:
        return 'Товар не найден'


# Добавить фото к продукту
def add_photo(product_id: int, photo_path: str):
    db = next(get_db())

    new_photo = Products(product_id=product_id, photo_path=photo_path)
    if new_photo:
        db.add(new_photo)
        db.commit()
        return 'Фото добавлено'
    else:
        return 'Продукт не найден'


# Изменить цену товару
def change_price_db(product_id: int, new_price: float):
    db = next(get_db())
    check = db.query(Products).filter_by(product_id=product_id).first()
    if check:
        if 0 < new_price <= 9999:
            check.product_price = new_price
            db.commit()
            return f'Цена изменена на {new_price}'
        else:
            return 'Ошибка цены товара 0 < x <= 9999'
    else:
        return 'Товар не найден'


# Получить все товары
def get_all_products_db():
    db = next(get_db())
    return db.query(Products).all()
