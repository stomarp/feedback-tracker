"""
Database initialization script.

This script:
- imports all models
- tells SQLAlchemy to create tables in PostgreSQL
"""

from app.db.session import engine
from app.models.base import Base

# IMPORTANT:
# Import models so SQLAlchemy knows about them
from app.models.application import Application
from app.models.rejection import Rejection
from app.models.feedback import Feedback


def init_db():
    """
    Create all tables in the database.
    If tables already exist, SQLAlchemy will skip them.
    """
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created")
