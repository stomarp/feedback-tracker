# Base class for all SQLAlchemy models
# Every table will inherit from this

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database models.
    SQLAlchemy uses this to collect table metadata.
    """
    pass
