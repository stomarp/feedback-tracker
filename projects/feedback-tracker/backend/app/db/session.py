from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

DATABASE_URL = URL.create(
    "postgresql+psycopg",
    username="feedback_user",
    password="feedback_pass",
    host="localhost",
    port=5432,
    database="feedback_tracker",
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
