import uvicorn
from fastapi import FastAPI
from database import Base, engine
from src.routes import user_router
from src.resume.routes import resume_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all standard HTTP methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(user_router, prefix='/user')
app.include_router(resume_router, prefix='/resume')

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run('app:app', host='0.0.0.0', port=8080, reload=True)
