# Feedback Tracker — Job Applications & Interview Insights

A personal web app I’m building to track job applications, rejections, and interview feedback so I can spot patterns (recurring rejection reasons, missing skills, and where I drop in the funnel).

## Why I built this
I used to track applications in notes/Excel, but it was hard to connect feedback and outcomes. This project helps me keep everything in one place and later analyze trends.

## Tech Stack
- Backend: FastAPI (Python)
- Database: PostgreSQL (Docker)
- ORM: SQLAlchemy
- Frontend: planned (React/Next.js)

## Current Features (Backend)
- Health check endpoint: `GET /health`
- Database connectivity check: `GET /db-check`
- Database tables created for:
  - applications
  - rejections
  - feedback

## Repo Structure
- `projects/feedback-tracker/backend` — FastAPI backend
- `projects/feedback-tracker/frontend` — frontend (later)
- `projects/feedback-tracker/docs` — design notes

## How to run locally

### 1) Start PostgreSQL (Docker)
From repo root:
```bash
docker compose up -d
docker ps
