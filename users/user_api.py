from fastapi import APIRouter
from users import *
from database.userservice import *


user_router = APIRouter(prefix='/users', tags=['Для работы с пользователями'])


# Регистрация пользователя
@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_db(**data.model_dump())

    if result:
        return f'Успешно зарегистрированы!'
    else:
        return 'Такой пользователь уже имеется'


# Запрос для получения всех пользователей
@user_router.get('/all-user')
async def get_all_users():
    return get_all_users_db()


# Получить определенного пользователя (по айди)
@user_router.get('/exact-user')
async def get_exact_user(user_id: int):
    return get_exact_user_db(user_id)


# Добавить поинты пользователю
@user_router.post('/add-points')
async def add_points(data: UserPointValidator):
    result = add_points_db(**data.model_dump())
    if result:
        return result
    else:
        return 'Что пошло не так'


# Просмотр баланса определенного пользователя
@user_router.get('/check-balance')
async def check_balance(user_id: int):
    result = balance_check_db(user_id)
    return result


# Удалить пользователя по айди
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)
    return result


# Купить какой-то продукт
@user_router.post('/buy-product')
async def buy_product(data: BuyValidator):
    result = buy_product_db(**data.model_dump())
    if result:
        return result
    else:
        return 'Что то пошло не так'
