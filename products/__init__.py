from pydantic import BaseModel


# Валидатор для добавления товара
class AddValidator(BaseModel):
    product_name: str
    product_des: str
    product_price: float
    product_quantity: int


# Валидатор для изменения количества
class QuantityValidator(BaseModel):
    product_id: int
    new_amount: int


# Валидатор для изменения цены товара
class ProductPriceValidator(BaseModel):
    product_id: int
    new_price: float
