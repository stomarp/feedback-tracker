"""
FastAPI app entry point.

This file:
- creates the FastAPI app
- adds middleware (CORS)
- defines basic endpoints (/health, /db-check)
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.settings import settings
from app.db.session import get_db

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
)

# CORS allows the frontend (browser UI) to call our backend APIs.
# For MVP we allow all origins. Later we will restrict this.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    """
    Simple endpoint to confirm API is running.
    """
    return {"status": "ok"}


@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    """
    Simple endpoint to confirm database is reachable.
    Runs: SELECT 1
    """
    db.execute(text("SELECT 1"))
    return {"db": "connected"}
