# Database Design (MVP)

## Table 1: applications
Stores each job application.

Fields:
- id (PK, integer)
- company (text, required)
- role (text, required)
- job_url (text, optional)
- status (text, required)  # Applied | Interview | Rejected | Offer
- applied_date (date, optional)
- notes (text, optional)
- created_at (timestamp)
- updated_at (timestamp)

## Table 2: rejections
Stores rejection events for an application.

Fields:
- id (PK, integer)
- application_id (FK -> applications.id, required)
- rejected_date (date, optional)
- reasons (text, optional)  # comma-separated for MVP (later can be separate table)
- notes (text, optional)
- created_at (timestamp)

Relationship:
- One application can have many rejections (usually 1, but we allow many).

## Table 3: feedback
Stores feedback linked to an application (resume/interview/OA).

Fields:
- id (PK, integer)
- application_id (FK -> applications.id, required)
- category (text, required)  # Resume | Interview | OA | Recruiter
- feedback_text (text, required)
- skills (text, optional)  # comma-separated for MVP
- created_at (timestamp)

Relationship:
- One application can have many feedback entries.
