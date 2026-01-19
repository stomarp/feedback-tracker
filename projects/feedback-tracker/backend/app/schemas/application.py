from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict


class ApplicationCreate(BaseModel):
    company: str = Field(min_length=1, max_length=200)
    role: str = Field(min_length=1, max_length=200)
    job_url: str | None = None
    status: str = "Applied"
    applied_date: date | None = None
    notes: str | None = None

class ApplicationUpdate(BaseModel):
    # All optional (so we can update only what we want)
    company: str | None = Field(default=None, max_length=200)
    role: str | None = Field(default=None, max_length=200)
    job_url: str | None = None
    status: str | None = None
    applied_date: date | None = None
    notes: str | None = None



class ApplicationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company: str
    role: str
    job_url: str | None
    status: str
    applied_date: date | None
    notes: str | None
    created_at: datetime
    updated_at: datetime
