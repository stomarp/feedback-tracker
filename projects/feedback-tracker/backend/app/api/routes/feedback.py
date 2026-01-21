from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.application import Application
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate, FeedbackOut

router = APIRouter(prefix="/applications/{app_id}/feedback", tags=["feedback"])


@router.post("", response_model=FeedbackOut)
def create_feedback(app_id: int, payload: FeedbackCreate, db: Session = Depends(get_db)):
    # Check application exists
    app_row = db.query(Application).filter(Application.id == app_id).first()
    if not app_row:
        raise HTTPException(status_code=404, detail="Application not found")

    fb = Feedback(
        application_id=app_id,
        feedback_date=payload.feedback_date,
        interviewer=payload.interviewer,
        rating=payload.rating,
        comments=payload.comments,
    )

    db.add(fb)
    db.commit()
    db.refresh(fb)
    return fb


@router.get("", response_model=list[FeedbackOut])
def list_feedback(app_id: int, db: Session = Depends(get_db)):
    # Check application exists
    app_row = db.query(Application).filter(Application.id == app_id).first()
    if not app_row:
        raise HTTPException(status_code=404, detail="Application not found")

    return (
        db.query(Feedback)
        .filter(Feedback.application_id == app_id)
        .order_by(Feedback.id.desc())
        .all()
    )
