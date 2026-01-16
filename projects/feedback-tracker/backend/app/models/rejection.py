from datetime import date, datetime
from sqlalchemy import Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Rejection(Base):
    """
    Represents a rejection event for a job application.
    Each rejection belongs to exactly one application.
    """

    __tablename__ = "rejections"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign key linking to applications table
    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id", ondelete="CASCADE"),
        nullable=False,
    )

    # Date when rejection happened
    rejected_date: Mapped[date | None] = mapped_column(Date, nullable=True)

    # Reasons for rejection (comma-separated for MVP)
    # Example: "Lack of system design, No React experience"
    reasons: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Additional notes (optional)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timestamp when record was created
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship back to application
    application = relationship(
        "Application",
        back_populates="rejections"
    )
