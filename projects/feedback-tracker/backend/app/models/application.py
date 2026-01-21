from datetime import date, datetime
from sqlalchemy import String, Text, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Application(Base):
    """
    Represents a job application.
    One application can have:
    - multiple rejections
    - multiple feedback entries
    """

    __tablename__ = "applications"

    # Primary key (unique ID for each application)
    id: Mapped[int] = mapped_column(primary_key=True)

    # Company name (required)
    company: Mapped[str] = mapped_column(String(200), nullable=False)

    # Job role/title (required)
    role: Mapped[str] = mapped_column(String(200), nullable=False)

    # Job posting URL (optional)
    job_url: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Current status of application
    # Example: Applied | Interview | Rejected | Offer
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="Applied"
    )

    # Date when application was submitted
    applied_date: Mapped[date | None] = mapped_column(Date, nullable=True)

    # Any extra notes (optional)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timestamp when record was created
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Timestamp when record was last updated
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship: one application → many rejections
    rejections = relationship(
        "Rejection",
        back_populates="application",
        cascade="all, delete-orphan",
    )

    # Relationship: one application → many feedback code app/models/feedback.py

    feedback = relationship(
        "Feedback",
         back_populates="application",
         cascade="all, delete-orphan",
)