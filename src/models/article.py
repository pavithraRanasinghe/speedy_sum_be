from pydantic import BaseModel

class Article(BaseModel):
    data: str
    type: str
    user: dict