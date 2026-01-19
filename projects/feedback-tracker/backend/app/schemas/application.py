from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class ApplicationStatus(str, Enum):
    applied = "Applied"
    interview = "Interview"
    rejected = "Rejected"
    offer = "Offer"



class ApplicationCreate(BaseModel):
    company: str = Field(min_length=1, max_length=200)
    role: str = Field(min_length=1, max_length=200)
    job_url: str | None = None
    status: ApplicationStatus = ApplicationStatus.applied
    applied_date: date | None = None
    notes: str | None = None

class ApplicationUpdate(BaseModel):
    # All optional (so we can update only what we want)
    company: str | None = Field(default=None, max_length=200)
    role: str | None = Field(default=None, max_length=200)
    job_url: str | None = None
    status: ApplicationStatus | None = None
    applied_date: date | None = None
    notes: str | None = None



class ApplicationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company: str
    role: str
    job_url: str | None
    status: ApplicationStatus
    applied_date: date | None
    notes: str | None
    created_at: datetime
    updated_at: datetime
