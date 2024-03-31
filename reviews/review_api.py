from database.reviewservice import *
from reviews import AddReviewValidator, EditReviewValidator
from fastapi import APIRouter

review_router = APIRouter(prefix="/reviews", tags=["Для работы с отзывами"])


# Получить все отзывы к товару
@review_router.get("/get-all-reviews")
async def get_all_reviews(product_id: int):
    result = get_all_reviews_db(product_id)
    return result


# Добавить отзыв к продукту
@review_router.post("/add-review")
async def add_review(data: AddReviewValidator):
    result = add_review_db(**data.model_dump())
    return result


# Изменить отзыв
@review_router.put("/edit-review")
async def edit_review(data: EditReviewValidator):
    result = change_review_db(**data.model_dump())
    if result:
        return 'Успешно изменено'
    else:
        return 'Что то пошло не так'


# Удалить отзыв
@review_router.delete("/delete-review")
async def delete_review(review_id: int, product_id: int):
    result = delete_review_db(review_id, product_id)
    if result:
        return 'Успешно удалено'
    else:
        return 'Что то пошло не так'

