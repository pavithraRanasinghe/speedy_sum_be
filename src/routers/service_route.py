from fastapi import APIRouter,status, Body
from src.models.text_sum_request import TextSumRequest
from src.service.ml_summarization import summarize


router = APIRouter(
    prefix="/sum",
    tags=["summarize"]
)

@router.post("/text", response_description="Summarize", status_code=status.HTTP_200_OK)
async def text_summarize(text: TextSumRequest = Body(...)):
    return summarize(text)
