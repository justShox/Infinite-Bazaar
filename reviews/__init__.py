from pydantic import BaseModel


# Валидатор для добавления отзыва
class AddReviewValidator(BaseModel):
    user_id: int
    product_id: int
    review_text: str


# Валидатор для изменения отзыва
class EditReviewValidator(BaseModel):
    user_id: int
    review_id: int
    change_text: str
