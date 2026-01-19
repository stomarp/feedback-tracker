from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class RejectionCreate(BaseModel):
    rejected_date: date | None = None
    reasons: str | None = None
    notes: str | None = None


class RejectionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    application_id: int
    rejected_date: date | None
    reasons: str | None
    notes: str | None
    created_at: datetime
