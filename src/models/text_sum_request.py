from pydantic import BaseModel

class TextSumRequest(BaseModel):
    text: str
    min: int
    max: int
    user: int