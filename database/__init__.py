from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///bazaar.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionOpen = sessionmaker(bind=engine)
base = declarative_base()


def get_db():
    db = SessionOpen()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
