from pydantic import BaseModel

class HistoryResponse(BaseModel):
    data: str
    type: str