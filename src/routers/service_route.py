from fastapi import APIRouter, HTTPException,status, Body
from src.models.text_sum_request import TextSumRequest
from src.service.ml_summarization import summarize
from src.service.scrap_service import scrap_data
from src.service.key_phrase_extraction_service import extract_keys


router = APIRouter(
    prefix="/sum",
    tags=["summarize"]
)

@router.post("/text", response_description="Summarize", status_code=status.HTTP_200_OK)
async def text_summarize(request: TextSumRequest = Body(...)):
    keyPhrases = extract_keys(request.text)
    res = summarize([request.text],keyPhrases, request.min, request.max)
    return res

# @router.post("/link", response_description="Summarize", status_code=status.HTTP_200_OK)
# async def web_page_summarize(request: TextSumRequest = Body(...)):
#     try:
#         articleSet = scrap_data(request.text)
#         keyPhrases = extract_keys(articleSet)
#     except:
#         raise HTTPException(status_code=400, detail='Can not read content of the web page')
#     return summarize(articleSet, keyPhrases, request.min, request.max)

@router.post("/link", response_description="Summarize", status_code=status.HTTP_200_OK)
async def web_page_summarize(request: TextSumRequest = Body(...)):
    scrap_data(request.text)
    return 'Hello'