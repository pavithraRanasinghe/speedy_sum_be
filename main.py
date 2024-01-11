from typing import Union
from fastapi import FastAPI

from ml_summarization import summarize

app = FastAPI()


@app.get("/")
def read_root():
    sum = summarize
    return sum


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}