from typing import Any
from fastapi import APIRouter, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from src.models.history_response import HistoryResponse
from src.models.article import Article
from src.models.summary_response import SummaryResponse
from src.models.text_sum_request import TextSumRequest
from src.services.ml_summarization import summarize
from src.services.scrap_service import scrap_data
from src.services.key_phrase_extraction_service import extract_keys
from src.config.db_config import db

article_collection = db.get_collection("article")
user_collection = db.get_collection("users")

router = APIRouter(
    prefix="/sum",
    tags=["summarize"]
)

@router.post("/text", response_description="Summarize from text", status_code=status.HTTP_200_OK, response_model=SummaryResponse)
async def text_summarize(request: TextSumRequest = Body(...)):
    keyPhrases = extract_keys(request.text)
    summary = summarize([request.text],keyPhrases, request.min, request.max)
    if(request.user != 0):
        await save_history(request.user, request.text, 'TEXT')
           
    return SummaryResponse(summary= summary,keyPhrases= keyPhrases) # type: ignore


@router.post("/link", response_description="Summarize from link", status_code=status.HTTP_200_OK, response_model=SummaryResponse)
async def web_page_summarize(request: TextSumRequest = Body(...)):
    try:
        articleSet = scrap_data(request.text)
        keyPhrases = extract_keys(articleSet)
    except:
        raise HTTPException(status_code=400, detail='Can not read content of the web page')
    summary = summarize(articleSet, keyPhrases, request.min, request.max)
    if(request.user != 0):
        await save_history(request.user, request.text, 'LINK')
    return SummaryResponse(summary= summary,keyPhrases= keyPhrases) # type: ignore


@router.get("/history/{user_id}", response_description="Fetch History", status_code=status.HTTP_200_OK, response_model=list[HistoryResponse])
async def find_history(user_id: int):
    articles = article_collection.find({"user.id": user_id})
    history_list = []
    async for a in articles:
        history_list.append(HistoryResponse(data = a['data'], type = a['type']))
    return history_list

async def save_history(user_id: int, data: str, type: str):
    user = await user_collection.find_one({"id": user_id})
    if(user):
        user['_id'] = str(user['_id'])
        article = Article(
            data=data,
            type=type,
            user= user
        )
        article = jsonable_encoder(article)
        await article_collection.insert_one(article)

