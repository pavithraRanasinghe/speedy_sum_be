from typing import List
from pydantic import BaseModel

class SummaryResponse(BaseModel):
    summary: str
    keyPhrases: List