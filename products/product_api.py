from fastapi import APIRouter, UploadFile
from database.productservice import *
from products import AddValidator, QuantityValidator, ProductPriceValidator

product_router = APIRouter(prefix='/products', tags=['Для работы с продуктами'])


# Добавить продукт
@product_router.post('/add-product')
async def add_product(data: AddValidator):
    result = add_product_db(**data.model_dump())
    if result:
        return 'Товар закинут на склад'
    else:
        return 'Что то пошло не так'


# Удаление продукта
@product_router.put('/delete-product')
async def delete_product(product_id: int):
    result = delete_product_db(product_id=product_id)
    return result


# Получение инфы по продукту по айди
@product_router.get('/get-product')
async def get_product(product_id: int):
    result = get_product_db(product_id=product_id)
    return result


# Добавить количество продукта
@product_router.put('/add-amount')
async def add_amount(data: QuantityValidator):
    result = update_product_quantity_db(**data.model_dump())
    if result:
        return 'Добавлено на склад'
    else:
        return 'Что то пошло не так'


# Добавление фото продукта
@product_router.put('/add-photo')
async def add_photo(product_id: int, photo_path: UploadFile = False):
    with open(f'media/{photo_path.filename}', mode='wb') as file:
        product_photo = await photo_path.read()
        file.write(product_photo)

    result = add_photo(product_id=product_id, photo_path=f'media/{photo_path.file}')
    if result:
        return 'Фото добавлено'

    else:
        return 'Что то пошло не так'


# Изменить цену товару
@product_router.put('/change-price')
async def change_price(data: ProductPriceValidator):
    result = change_price_db(**data.model_dump())
    if result:
        return result
    else:
        return 'Что то пошло не так'
