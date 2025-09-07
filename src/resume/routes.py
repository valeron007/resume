from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.models import Resume, User
from src.resume.schema import ResumeModel, ResumeUpdateModel, ResumeImproveModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from depencies import get_db, get_current_user

resume_router = APIRouter()

@resume_router.post('/create')
def create_resume(resume_data: ResumeModel, db:Session = Depends(get_db), user: User = Depends(get_current_user)):    
    resume = Resume(title=resume_data.title, content=resume_data.content, user=user)
    db.add(resume)
    db.commit()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(resume_data)
    )


@resume_router.get('/lists')
def get_resumes(db:Session = Depends(get_db), user: User = Depends(get_current_user)):
    resumes = db.query(Resume).filter(Resume.user_id == user.id).all()

    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(resumes)
    )


@resume_router.get('/{id}')
def get_resume(id: int, db:Session = Depends(get_db), user: User = Depends(get_current_user)):
    resume = db.query(Resume).filter(Resume.id == id).first()

    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(resume)
    )

@resume_router.delete('/{id}')
def delete_resume(id, db:Session = Depends(get_db), user: User = Depends(get_current_user)):
    resume = db.query(Resume).filter(Resume.id == id, Resume.user_id == user.id).first()
    db.delete(resume)
    db.commit()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "delete resume " + id},
    )

@resume_router.put('/')
def update_task(resume_data: ResumeUpdateModel, db:Session = Depends(get_db), user: User = Depends(get_current_user)):
    resume = db.query(Resume).filter(Resume.id == resume_data.id, Resume.user_id == user.id).first()
    resume.title = resume_data.title
    resume.content = resume_data.content
    db.commit()

    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(resume_data)
    )

@resume_router.post('/{id}/improve')
def create_resume(resume_data: ResumeImproveModel, db:Session = Depends(get_db), user: User = Depends(get_current_user)):    
    
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=(resume_data.content + "[Improved]")
    )


