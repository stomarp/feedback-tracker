from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationOut

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=ApplicationOut)
def create_application(payload: ApplicationCreate, db: Session = Depends(get_db)):
    # Create a new Application row from request data
    app_row = Application(
        company=payload.company,
        role=payload.role,
        job_url=payload.job_url,
        status=payload.status,
        applied_date=payload.applied_date,
        notes=payload.notes,
    )

    db.add(app_row)
    db.commit()
    db.refresh(app_row)  # loads generated fields like id, created_at

    return app_row


@router.get("", response_model=list[ApplicationOut])
def list_applications(db: Session = Depends(get_db)):
    # Return all applications (simple MVP)
    return db.query(Application).order_by(Application.id.desc()).all()
