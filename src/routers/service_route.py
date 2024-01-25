from typing import Any
from urllib import response
from fastapi import APIRouter, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from src.models.user_model import User
from src.models.article import Article
from src.models.summary_response import SummaryResponse
from src.models.text_sum_request import TextSumRequest
from src.service.ml_summarization import summarize
from src.service.scrap_service import scrap_data
from src.service.key_phrase_extraction_service import extract_keys
from src.config.db_config import db

article_collection = db.get_collection("article")
user_collection = db.get_collection("users")

router = APIRouter(
    prefix="/sum",
    tags=["summarize"]
)

@router.post("/text", response_description="Summarize", status_code=status.HTTP_200_OK, response_model=SummaryResponse)
async def text_summarize(request: TextSumRequest = Body(...)) -> Any:
    keyPhrases = extract_keys(request.text)
    summary = summarize([request.text],keyPhrases, request.min, request.max)
    if(request.user != 0):
        user = await user_collection.find_one({"id": 1})
        if(user):
            user['_id'] = str(user['_id'])
            article = Article(
                data=request.text,
                type='TEXT',
                user= user
            )
            article = jsonable_encoder(article)
            await article_collection.insert_one(article)
           
    return SummaryResponse(summary= summary,keyPhrases= keyPhrases) # type: ignore

@router.post("/link", response_description="Summarize", status_code=status.HTTP_200_OK, response_model=SummaryResponse)
async def web_page_summarize(request: TextSumRequest = Body(...)) -> Any:
    try:
        articleSet = scrap_data(request.text)
        keyPhrases = extract_keys(articleSet)
    except:
        raise HTTPException(status_code=400, detail='Can not read content of the web page')
    summary = summarize(articleSet, keyPhrases, request.min, request.max)
    return SummaryResponse(summary= summary,keyPhrases= keyPhrases) # type: ignore

