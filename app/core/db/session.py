from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.data import Data


engine = create_engine(
    f'postgresql://Camilapinz18:gR6oQeOBftJ9@ep-muddy-snowflake-466588.us-east-2.aws.neon.tech/neondb',
    pool_size=10,
    max_overflow=2,
    pool_recycle=500,
    pool_timeout=600,
    pool_pre_ping=True,
    pool_use_lifo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
