from fastapi import APIRouter, HTTPException,status, Body
from src.models.text_sum_request import TextSumRequest
from src.service.ml_summarization import summarize
from src.service.scrap_service import scrap_data


router = APIRouter(
    prefix="/sum",
    tags=["summarize"]
)

@router.post("/text", response_description="Summarize", status_code=status.HTTP_200_OK)
async def text_summarize(request: TextSumRequest = Body(...)):
    res = summarize(request.text, request.min, request.max)
    return res

@router.post("/link", response_description="Summarize", status_code=status.HTTP_200_OK)
async def web_page_summarize(request: TextSumRequest = Body(...)):
    try:
        data = scrap_data(request.text)
    except:
        raise HTTPException(status_code=400, detail='Can not access the web page')
    return summarize(data, request.min, request.max)