from typing import Literal
from pydantic import BaseModel


class TextSumRequest(BaseModel):
    text: str
    min: int
    max: int