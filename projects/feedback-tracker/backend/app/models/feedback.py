from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Feedback(Base):
    """
    Represents feedback related to a job application.
    Example: interview feedback, resume feedback, OA feedback.
    """

    __tablename__ = "feedback"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign key linking to applications table
    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id", ondelete="CASCADE"),
        nullable=False,
    )

    # Type of feedback
    # Example: Resume | Interview | OA | Recruiter
    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    # Actual feedback text
    feedback_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # Skills mentioned in feedback (comma-separated for MVP)
    # Example: "Python, SQL, System Design"
    skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    # Timestamp when feedback was created
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship back to application
    application = relationship(
        "Application",
        back_populates="feedback_entries"
    )

