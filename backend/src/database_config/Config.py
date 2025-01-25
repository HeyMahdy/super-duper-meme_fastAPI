import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the database engine
engine = create_engine(DATABASE_URL)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Model1Base = declarative_base()

















