from pydantic import BaseModel

class ResumeModel(BaseModel):
    title: str
    content: str

    