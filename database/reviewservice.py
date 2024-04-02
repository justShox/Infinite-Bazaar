from database.models import Review, User
from database import get_db
from datetime import datetime


# Получить конкретный отзыв
def get_exact_reviews_db(product_id):
    db = next(get_db())
    check = db.query(Review).filter_by(product_id=product_id).first()
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
    return (f'Ваш id: {review.user_id}, '
            f'ID отзыва: {review.review_id}, '
            f'Ваш коммент: {review.review_text}')


# Изменить отзыв
def change_review_db(user_id: int, review_id: int, change_text: str):
    db = next(get_db())
    check_pr = db.query(Review).filter_by(review_id=review_id).first()
    check_user = db.query(User).filter_by(user_id=user_id).first()
    if check_pr and check_user:
        check_pr.review_text = change_text
        db.commit()
        return 'Отзыв изменен'
    else:
        return 'Ошибка при заполнении инфы'


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


# Получить все отзывы
def get_all_reviews_db():
    db = next(get_db())
    return db.query(Review).all()
