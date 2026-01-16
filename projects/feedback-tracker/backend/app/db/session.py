"""
Database session setup.

This file creates:
- DATABASE_URL (connection details)
- engine (the connection manager)
- SessionLocal (factory to create DB sessions)
- get_db() dependency (FastAPI-friendly way to open/close sessions)
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

# Build a safe SQLAlchemy URL (avoids string parsing issues)
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username="feedback_user",
    password="feedback_pass",
    host="localhost",
    port=5432,
    database="feedback_tracker",
)

# Engine = main entry point SQLAlchemy uses to talk to the DB
# echo=False means we won't print SQL queries in terminal (clean output)
engine = create_engine(DATABASE_URL, echo=False)

# SessionLocal = factory that creates DB sessions
# autoflush=False: don't auto-write changes until we commit
# autocommit=False: we control when commits happen
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    """
    FastAPI dependency that:
    - opens a DB session for a request
    - yields it to the route function
    - closes it after request finishes (even if error)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

