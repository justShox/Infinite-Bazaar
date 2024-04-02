from database.models import User, Products
from datetime import datetime
from database import get_db


# Зарегистрировать пользователя
def register_user_db(username: str, surname: str, password: str, e_mail: str, phone_number: str):
    db = next(get_db())
    check = db.query(User).filter_by(phone_number=phone_number).first()
    if check:
        return 'Пользователь с таким номером телефона уже зареган'
    else:
        new_user = User(username=username,
                        surname=surname,
                        password=password,
                        e_mail=e_mail,
                        phone_number=phone_number,
                        created_at=datetime.now())
        db.add(new_user)
        db.commit()
        return 'Успешно зареганы'


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    get_all = db.query(User).all()
    return get_all


# Получить определенного пользователя (по айди)
def get_exact_user_db(user_id: int):
    db = next(get_db())
    get_exact = db.query(User).filter_by(user_id=user_id).first()
    if get_exact:
        return get_exact
    else:
        return 'Такой пользователь не найден'


# Добавить поинты пользователю
def add_points_db(user_id: int, amount: int):
    db = next(get_db())
    check = db.query(User).filter_by(user_id=user_id).first()
    if check:
        if 0 < amount <= 9999999:
            check.points += amount
            db.commit()
            return f'Поинты успешно добавлены! Баланс - {check.points}'
        else:
            return 'Количество указано неправильно'
    else:
        return 'Такой пользователь не найден'


# Просмотр баланса определенного пользователя
def balance_check_db(user_id: int):
    db = next(get_db())
    check = db.query(User).filter_by(user_id=user_id).first()
    if check:
        return f'Ваш баланс - {check.points}'
    else:
        return 'Такой пользователь не найден'


# Удалить пользователя по айди
def delete_user_db(user_id: int):
    db = next(get_db())
    check = db.query(User).filter_by(user_id=user_id).first()
    if check:
        db.delete(check)
        db.commit()
        return 'Пользователь удален'
    else:
        return 'Такой пользователь не найден'


# Купить какой-то продукт
def buy_product_db(user_id: int, product_id: int, amount: int):
    db = next(get_db())
    check_user = db.query(User).filter_by(user_id=user_id).first()
    check_product = db.query(Products).filter_by(product_id=product_id).first()
    if check_user and check_product:
        if check_user.points >= check_product.product_price and 0 < amount <= check_product.product_quantity:
            check_user.points -= (check_product.product_price * amount)
            check_product.product_quantity -= amount
            check_user.products_bought += amount
            db.commit()
            return f'Товар успешно куплен! Остаток баланса - {check_user.points}'
        else:
            return 'Недостаточно поинтов или недостаточно товара на складе'
    else:
        return 'Проверьте введенные айди'
