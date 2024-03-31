from pydantic import BaseModel


# Валидатор для добавления пользователя
class RegisterUserValidator(BaseModel):
    username: str
    surname: str
    phone_number: str
    password: str
    e_mail: str


# Валидатор для заполнения карты
class UserPointValidator(BaseModel):
    user_id: int
    amount: int


# Валидатор для покупки
class BuyValidator(BaseModel):
    user_id: int
    product_id: int
    amount: int
