from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(data, min, max):
    summarize_res = summarizer(data, max_length=max, min_length=min, do_sample=False)
    return ''.join(summary['summary_text'] for summary in summarize_res)  # type: ignore

    