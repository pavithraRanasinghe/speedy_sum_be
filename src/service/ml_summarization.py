from transformers import pipeline

from src.models.text_sum_request import TextSumRequest

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(request: TextSumRequest):
    ARTICLE = request.text
    sum = summarizer(ARTICLE, max_length=request.max, min_length=request.min, do_sample=False)
    return sum