from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.application import Application
from app.models.rejection import Rejection
from app.schemas.rejection import RejectionCreate, RejectionOut

router = APIRouter(prefix="/applications/{app_id}/rejections", tags=["rejections"])


@router.post("", response_model=RejectionOut)
def create_rejection(app_id: int, payload: RejectionCreate, db: Session = Depends(get_db)):
    # Make sure application exists
    app_row = db.query(Application).filter(Application.id == app_id).first()
    if not app_row:
        raise HTTPException(status_code=404, detail="Application not found")

    rej = Rejection(
        application_id=app_id,
        rejected_date=payload.rejected_date,
        reasons=payload.reasons,
        notes=payload.notes,
    )

    db.add(rej)
    db.commit()
    db.refresh(rej)
    return rej


@router.get("", response_model=list[RejectionOut])
def list_rejections(app_id: int, db: Session = Depends(get_db)):
    # Make sure application exists
    app_row = db.query(Application).filter(Application.id == app_id).first()
    if not app_row:
        raise HTTPException(status_code=404, detail="Application not found")

    return (
        db.query(Rejection)
        .filter(Rejection.application_id == app_id)
        .order_by(Rejection.id.desc())
        .all()
    )
