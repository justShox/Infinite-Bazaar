from database.models import Review
from database import get_db
from datetime import datetime


# Получить все отзывы к товару
def get_all_reviews_db(product_id):
    db = next(get_db())
    check = db.query(Review).all()
    if check:
        return check
    else:
        return 'Что пошло не так'


# Добавить отзыв к продукту
def add_review_db(product_id: int, user_id: int, review_text: str):
    db = next(get_db())

    review = Review(product_id=product_id,
                    user_id=user_id,
                    review_text=review_text,
                    posted_at=datetime.now())
    db.add(review)
    db.commit()
    db.refresh(review)
    return review


# Изменить отзыв
def change_review_db(user_id: int, review_id: int, change_text: str):
    db = next(get_db())
    check = db.query(Review).filter_by(review_id=review_id, user_id=user_id).first()
    if check:
        check.review_text = change_text
        db.commit()
        return 'Отзыв изменен'
    else:
        return 'Текст изменен'


# Удалить отзыв
def delete_review_db(product_id: int, review_id: int):
    db = next(get_db())
    check = db.query(Review).filter_by(review_id=review_id, product_id=product_id).first()
    if check:
        db.delete(check)
        db.commit()
        return 'Успешно удалено'
    else:
        return 'Отзыв не найден'
