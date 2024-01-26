from transformers import (pipeline,BartForConditionalGeneration,BartTokenizer)

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# Load the summarization model
summarizer = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

def summarize(articleData, keyphrases, minLength, maxLength):
    # summarize_res = summarizer(data, max_length=max, min_length=min, do_sample=False)
    # return ''.join(summary['summary_text'] for summary in summarize_res)  # type: ignore

    summaries = []
    for article in articleData:
        # Combine keyphrases into a single string
        keyphrase_text = " ".join([keyphrase for keyphrase in keyphrases]) # type: ignore

        # Concatenate the article and keyphrases for summarization
        input_text = f"{article} Keyphrases: {keyphrase_text}"
            
        # Tokenize and generate summary
        inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = summarizer.generate(**inputs, max_length = maxLength, min_length = minLength) # type: ignore
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        summaries.append(summary)
        
    final_summary = ''.join(summaries)
    
    return final_summary

    