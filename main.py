from fastapi import FastAPI
from database import base, engine
from products.product_api import product_router
from reviews.review_api import review_router
from users.user_api import user_router

app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(product_router)
app.include_router(review_router)

base.metadata.create_all(bind=engine)
