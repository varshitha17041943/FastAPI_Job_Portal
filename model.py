from database import Base
from sqlalchemy import Column,Integer,String,Boolean
class Jobs(Base):
    __tablename__="jobs"
    job_id=Column(Integer,primary_key=True) 
    job_title=Column(String,nullable=False)
    company_name=Column(String,nullable=False)
    description=Column(String,nullable=False)
    required_skills=Column(String,nullable=False)
    location=Column(String,nullable=False)
    salary=Column(String,nullable=False)
    job_type=Column(String,nullable=False)
    posted_date=Column(String,nullable=False)
    application_last_date=Column(String,nullable=False)
    status=Column(String,default=False)

class Candidates(Base):
    __tablename__="candidates"
    candidate_id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    phone=Column(Integer,nullable=False)
    password=Column(String,nullable=False)
    skills=Column(String,nullable=False)
    qualification=Column(String,nullable=False)
    experience=Column(Integer,nullable=False)
    resume_information=Column(String,nullable=False)

class Applications(Base):
    __tablename__ = "applications"
    application_id = Column(Integer, primary_key=True)
    job_id = Column(Integer, nullable=False)
    candidate_id = Column(Integer, nullable=False)
    application_date = Column(String, nullable=False)
    application_status = Column(String, default="Applied")
    resume = Column(String,nullable=False)
    cover_letter = Column(String,nullable=False)
    updated_at = Column(String,nullable=False)
