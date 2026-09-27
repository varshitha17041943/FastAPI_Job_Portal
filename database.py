from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///./job_portal.db",connect_args={"check_same_thread":False})
LocalSession=sessionmaker(bind=engine,autoflush=True)
Base= declarative_base()
