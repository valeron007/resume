from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
from src.models import Resume
from src.resume.schema import ResumeModel

from depencies import get_db

resume_router = APIRouter()

@resume_router.post('/resume')
def create_resume(user_data: ResumeModel, db:Session = Depends(get_db)):
    pass

@resume_router.get('/resume')
def get_resumes(db:Session = Depends(get_db)):
    pass


@resume_router.get('/resume/{id}')
def get_resume(user_data: ResumeModel, db:Session = Depends(get_db)):
    pass

resume_router.delete('/resume/{id}')
def delete_resume(id, db:Session = Depends(get_db)):
    pass

@resume_router.put('/resume')
def update_task(user_data: ResumeModel, db:Session = Depends(get_db)):
    pass

