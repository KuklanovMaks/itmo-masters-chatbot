from pydantic import BaseModel

class UserQuestion(BaseModel):
    question: str
    context: str | None = None