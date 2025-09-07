from pydantic import BaseModel

class ResumeModel(BaseModel):
    title: str
    content: str


class ResumeUpdateModel(BaseModel):
    id: int
    title: str
    content: str

class ResumeImproveModel(BaseModel):
    content: str
