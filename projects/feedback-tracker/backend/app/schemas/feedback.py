from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class FeedbackCreate(BaseModel):
    feedback_date: date | None = None
    interviewer: str | None = None
    rating: int | None = None  # 1–5 scale (we’ll validate later)
    comments: str | None = None


class FeedbackOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    application_id: int
    feedback_date: date | None
    interviewer: str | None
    rating: int | None
    comments: str | None
    created_at: datetime
