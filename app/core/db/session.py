from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.data import Data


engine = create_engine(
    #f'postgresql://Camilapinz18:gR6oQeOBftJ9@ep-muddy-snowflake-466588.us-east-2.aws.neon.tech/neondb',
    f'postgresql://sabseg_admin:sabseg@localhost:5432/sabseg_db')
    #f'postgresql://Camilapinz18:swh6GdoLqz8W@ep-white-leaf-37502486.us-east-2.aws.neon.tech/neondb')
    
    
    
    
    #'postgresql://fl0user:yL4Oq5CeEPDW@ep-cool-glade-16399750.us-east-2.aws.neon.tech:5432/sabseg?sslmode=require')
    #f'postgresql://Camilapinz18:fa1W7HZykIQT@ep-white-leaf-37502486.us-east-2.aws.neon.tech/neondb')


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
