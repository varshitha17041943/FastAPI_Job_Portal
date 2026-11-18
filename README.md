# Job Portal Backend API

A RESTful job portal backend built with **Python**, **FastAPI**, **SQLAlchemy ORM**, **SQLite**, and **Pydantic**. The API supports job postings, candidate registration, job application tracking, multi-criteria filtering, and multi-field sorting with structured validation and error handling.

---

## Features

- **Job Management:** Create, retrieve, update, and delete job postings with structured Pydantic request/response schemas.
- **Candidate Registration:** Register and manage candidate profiles with field-level input validation.
- **Application Tracking:** Submit job applications linking candidates to specific job openings and track application statuses (`Applied`, `Shortlisted`, `Interviewing`, `Rejected`, `Hired`).
- **Multi-Criteria Search & Filtering:** Filter job listings dynamically by role/title, location, job type, experience level, and salary range.
- **Multi-Field Sorting:** Sort job results dynamically across multiple fields (e.g., posted date, salary, job title) in ascending or descending order.
- **Relational ORM Architecture:** Uses SQLAlchemy ORM with SQLite for clean database modeling and session lifecycle management.
- **Interactive API Docs:** Built-in Swagger UI (`/docs`) and ReDoc (`/redoc`) endpoints for testing all endpoints directly in the browser.

---

## Tech Stack

- **Backend Framework:** Python, FastAPI
- **Validation & Serialization:** Pydantic
- **Database & ORM:** SQLite, SQLAlchemy ORM
- **Server:** Uvicorn

---

## Project Structure

```text
job-portal-fastapi/
├── database.py               # SQLite engine, SessionLocal, and Base configuration
├── models.py                 # SQLAlchemy ORM models (Job, Candidate, Application)
├── schemas.py                # Pydantic request and response validation models
├── main.py                   # FastAPI routes, search/sort logic, and exception handling
└── job_portal.db             # Local SQLite database file (auto-generated on startup)
```

---

## Core API Endpoints

### Jobs
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/jobs` | Create a new job posting |
| `GET` | `/jobs` | Retrieve all jobs with optional multi-criteria filtering and multi-field sorting |
| `GET` | `/jobs/{job_id}` | Retrieve details of a specific job by ID |
| `PUT` | `/jobs/{job_id}` | Update an existing job posting |
| `DELETE` | `/jobs/{job_id}` | Delete a job posting by ID |

### Candidates
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/candidates` | Register a new candidate profile |
| `GET` | `/candidates` | Retrieve all registered candidates |
| `GET` | `/candidates/{candidate_id}` | Retrieve a candidate profile by ID |

### Applications
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/applications` | Submit a job application for a candidate |
| `GET` | `/applications` | View submitted applications (filterable by job or candidate) |
| `PATCH` | `/applications/{application_id}/status` | Update the status of a candidate's application |

---

## Database Schema

- **`jobs`:** `job_id` (PK), `title`, `company`, `location`, `job_type`, `experience_required`, `salary`, `created_at`
- **`candidates`:** `candidate_id` (PK), `name`, `email` (Unique), `skills`, `experience_years`, `resume_url`
- **`applications`:** `application_id` (PK), `job_id` (FK → `jobs.job_id`), `candidate_id` (FK → `candidates.candidate_id`), `status`, `applied_at`

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/varshitha17041943/](https://github.com/varshitha17041943/)<your-job-portal-repo-name>.git
cd <your-job-portal-repo-name>
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```
*(SQLite automatically creates the local `.db` file on startup—no external database server setup required.)*

Open your browser and navigate to:
- **Interactive Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc Documentation:** `http://127.0.0.1:8000/redoc`

---

## Author

**Varshitha Reddy**  
- GitHub: [@varshitha17041943](https://github.com/varshitha17041943)  
- LinkedIn: [N Varshitha](https://www.linkedin.com/in/n-varshitha)
