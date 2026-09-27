from fastapi import FastAPI
from pydantic import BaseModel
from model import Jobs,Applications,Candidates
from database import Base,engine,LocalSession
app=FastAPI()
Base.metadata.create_all(bind=engine)
class JobRequest(BaseModel):
    job_id:int 
    job_title:str
    company_name:str
    description:str
    required_skills:str
    location:str
    salary:str
    job_type:str
    posted_date:str
    application_last_date:str
    status:bool
class SearchRequest(BaseModel):
    search_value: str
class CandidateRequest(BaseModel):
    candidate_id:int
    name:str
    email:str
    phone:str
    password:str
    skills:str
    qualification:str
    experience:str
    resume_information:str
class ApplicationDetails(BaseModel):
    application_id:int
    job_id:int
    candidate_id:int
    application_date:str
    application_status:str
    resume:str
    cover_letter:str
    updated_at:str
class ApplicationStatus(BaseModel):
    application_id:int
    application_status:str
@app.get("/")
def home():
    return "This is home page"

@app.post("/add_job")
def add_job(request:JobRequest):
    job_id=request.job_id
    job_title=request.job_title
    company_name=request.company_name
    description=request.description
    required_skills=request.required_skills
    location=request.location
    salary=request.salary
    job_type=request.job_type
    posted_date=request.posted_date
    application_last_date=request.application_last_date
    status=request.status
    db=LocalSession()
    add_job=Jobs(job_id=job_id,job_title=job_title,company_name=company_name,
                 description=description,required_skills=required_skills,
                 location=location,salary=salary,job_type=job_type,
                 posted_date=posted_date,application_last_date=application_last_date,
                 status=status)
    db.add(add_job)
    db.commit()
    db.close()
    return add_job

@app.get("/view_jobs")
def view_jobs():
    db=LocalSession()
    jobs=db.query(Jobs)
    if not jobs:
        print("No Jobs Available")
    else:
        for job in jobs:
            print("-----------------------------")
            print("Job ID:", job.job_id)
            print("Job Title:", job.job_title)
            print("Company:", job.company_name)
            print("Description:", job.description)
            print("Required Skills:", job.required_skills)
            print("Location:", job.location)
            print("Salary:", job.salary)
            print("Job Type:", job.job_type)
            print("Posted Date:", job.posted_date)
            print("Application Last Date:", job.application_last_date)
            print("Status:", job.status)
            print("-----------------------------")
    db.commit()
    db.close()
    return "Jobs Found"

@app.patch("/search_jobs")
def search_jobs(request:SearchRequest):
    search_value=request.search_value.strip()
    db = LocalSession()
    if search_value.isdigit():
        job_id = int(search_value)
        jobs = db.query(Jobs).filter(
            Jobs.job_id == job_id
        ).all()
    else:
        jobs = db.query(Jobs).filter(
        (Jobs.job_title == search_value) |
        (Jobs.location == search_value) |
        (Jobs.company_name == search_value) |
        (Jobs.job_type == search_value)
        ).all()
    if not jobs:
        return "Job not found"
    for job in jobs:
        print("-----------------------------")
        print("Job ID:", job.job_id)
        print("Job Title:", job.job_title)
        print("Company:", job.company_name)
        print("Description:", job.description)
        print("Required Skills:", job.required_skills)
        print("Location:", job.location)
        print("Salary:", job.salary)
        print("Job Type:", job.job_type)
        print("Posted Date:", job.posted_date)
        print("Application Last Date:", job.application_last_date)
        print("Status:", job.status)
        print("-----------------------------")
    return "Job found"

@app.post("/register_candidate")
def register_candidate(request:CandidateRequest):
    candidate_id=request.candidate_id
    name=request.name
    email=request.email
    phone=request.phone
    password=request.password
    skills=request.skills
    qualification=request.qualification
    experience=request.experience
    resume_information=request.resume_information
    db=LocalSession()
    register_candidate=Candidates(candidate_id=candidate_id,name=name,email=email,phone=phone,password=password,
        skills=skills,qualification=qualification,experience=experience,resume_information=resume_information)
    db.add(register_candidate)
    db.commit()
    db.close()
    return "Candidate registered successfully"

@app.post("/apply_job")
def apply_job(request: ApplicationDetails):
    db = LocalSession()
    job_id = request.job_id
    job = db.query(Jobs).filter(Jobs.job_id == job_id).first()
    if not job:
        db.close()
        return "Job Not Found"
    db.add(Applications(
        job_id=request.job_id,
        candidate_id=request.candidate_id,
        application_date=request.application_date,
        application_status="Applied",
        resume=request.resume,
        cover_letter=request.cover_letter,
        updated_at=request.application_date
    ))
    db.commit()
    db.close()
    return "Applied Successfully"

@app.get("/view_applications")
def view_applications():
    db=LocalSession()
    applications=db.query(Applications).all()
    if not applications:
        return "Not applied for any jobs"
    else:
        for application in applications:
            print("-----------------------------")
            print("Application ID:",application.application_id)
            print("Job ID:",application.job_id)
            print("Candidate ID:",application.candidate_id)
            print("Application Date:",application.application_date)
            print("Application Status:",application.application_status)
            print("Resume:",application.resume)
            print("Cover Letter:",application.cover_letter)
            print("Updated Application At:",application.updated_at)
            print("-----------------------------")
        return "Applications Found"
@app.patch("/update_application_status")
def update_application_status(request:ApplicationStatus):
    application_id=request.application_id
    application_status=request.application_status
    db=LocalSession()
    application=db.query(Applications).filter(Applications.application_id==application_id).first()
    if application:
        application.application_status=application_status
    db.commit()
    db.close()
    return "Application Status Updated"

@app.get("/sorting_jobs")
def sorting_jobs():
    db=LocalSession()
    jobs=db.query(Jobs).order_by(Jobs.company_name.desc(),Jobs.salary.desc(),Jobs.job_title.asc(),Jobs.location.asc(),
        Jobs.job_type.asc(),Jobs.posted_date.desc()).all()
    for job in jobs:
        print("-----------------------------")
        print("Job ID:",job.job_id)
        print("Job Title:",job.job_title)
        print("Job Salary:",job.salary)
        print("Location:",job.location)
        print("Company name:",job.company_name)
        print("Job Type:",job.job_type)
        print("Posted Date:",job.posted_date)
        print("-----------------------------")
    return "Jobs Sorted Successfully"