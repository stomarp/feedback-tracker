# Feedback Tracker API

A production-ready **backend REST API** for tracking job applications, interview feedback, and rejections.  
Built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, following clean architecture and industry best practices.

This project is designed to be **job-market ready**, easy to extend, and clear to explain in interviews.

---

## Project Overview

The Feedback Tracker API helps users:
- Track job applications and their status
- Store interview feedback linked to applications
- Record rejection reasons for future improvement
- Maintain structured, queryable career data

The backend exposes a clean REST interface with validation, persistence, and auto-generated documentation.

---

## Project Structure

```text
feedback-tracker/
├── docker-compose.yml
│   └── Defines PostgreSQL database service using Docker

├── .gitignore
│   └── Excludes virtual environments, cache files, secrets, and logs from Git

├── docs/
│   └── API notes, screenshots, architecture diagrams (optional / future use)

├── projects/
│   └── feedback-tracker/
│       └── backend/
│           ├── app/
│           │
│           │   ├── api/
│           │   │   └── routes/
│           │   │       ├── applications.py
│           │   │       │   └── CRUD APIs for job applications
│           │   │       ├── feedback.py
│           │   │       │   └── APIs to store and retrieve interview feedback
│           │   │       └── rejections.py
│           │   │           └── APIs for rejection tracking
│           │
│           │   ├── db/
│           │   │   ├── session.py
│           │   │   │   └── Creates SQLAlchemy engine and DB sessions
│           │   │   └── init_db.py
│           │   │       └── Initializes database tables from models
│           │
│           │   ├── models/
│           │   │   ├── base.py
│           │   │   │   └── Base SQLAlchemy model class
│           │   │   ├── application.py
│           │   │   │   └── Job application database model
│           │   │   ├── feedback.py
│           │   │   │   └── Interview feedback database model
│           │   │   └── rejection.py
│           │   │       └── Rejection database model
│           │
│           │   ├── schemas/
│           │   │   ├── application.py
│           │   │   │   └── Request/response validation for applications
│           │   │   ├── feedback.py
│           │   │   │   └── Validation schemas for feedback APIs
│           │   │   └── rejection.py
│           │   │       └── Validation schemas for rejection APIs
│           │
│           │   ├── core/
│           │   │   └── Reserved for configuration, security, and settings
│           │
│           │   └── main.py
│           │       └── FastAPI entry point and router registration
│           │
│           ├── requirements.txt
│           │   └── Python dependencies list
│           │
│           └── .venv/
│               └── Python virtual environment
│
└── README.md
    └── Project documentation

```


---

##  Architecture

### High-Level Components

####  Client
- Swagger UI (`/docs`)
- Future frontend (React / Next.js)

####  API Layer (FastAPI)
- Handles HTTP requests and responses
- Routes organized by feature:
  - Applications
  - Feedback
  - Rejections

####  Validation Layer (Pydantic)
- Ensures correct input data
- Controls response shape
- Provides type safety

#### ORM Layer (SQLAlchemy)
- Maps Python classes to database tables
- Manages relationships between entities
- Handles database sessions and transactions

#### Database (PostgreSQL)
- Stores persistent application data
- Runs inside a Docker container

---

### Request Flow

```text
Client
  ↓
FastAPI Route
  ↓
Pydantic Schema
  ↓
SQLAlchemy ORM
  ↓
PostgreSQL Database
```

---

## Features

###  Applications
- Create job applications
- Update application details
- List all applications

### Feedback
- Add interview feedback
- Track interviewer comments
- Associate feedback with applications

### Rejections
- Store rejection reasons
- Link rejections to applications

###  System
- Health check endpoint
- Database connectivity check
- Auto-generated API documentation

---

##  API Documentation

Interactive Swagger UI is available at:

 **http://127.0.0.1:8000/docs**

---

##  API Endpoints

### Applications
- `POST   /applications`
- `GET    /applications`
- `PUT    /applications/{id}`
- `DELETE /applications/{id}`

### Feedback
- `POST /applications/{app_id}/feedback`
- `GET  /applications/{app_id}/feedback`

### Rejections
- `POST /applications/{app_id}/rejections`
- `GET  /applications/{app_id}/rejections`

### Health
- `GET /health`
- `GET /db-check`

---

##  How to Run Locally

###  Clone the Repository
```bash
git clone https://github.com/stomarp/feedback-tracker.git
cd feedback-tracker
```

---

###  Start PostgreSQL with Docker
```bash
docker compose up -d
```

---

###  Backend Setup
```bash
cd projects/feedback-tracker/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
---

###  Initialize Database Tables
```bash
python3 -m app.db.init_db
```
---

###  Run the API Server
```bash
python3 -m uvicorn app.main:app --reload
```
---

##  Current Status
- Applications API
- Feedback API
- Rejections API
- PostgreSQL integration
- Docker-based database
- Validation & error handling

---

##  Future Enhancements
- User authentication (JWT)
- Role-based access control
- Analytics dashboard
- Frontend integration
- Skill trend analysis from feedback

---

##  Author

**Swati**  
Master’s Student – Software Development & AI/ML  
Backend Engineering • REST APIs • Databases







