from bs4 import BeautifulSoup
import requests

def scrap_data(URL):
    # Get the content of the webpage with HTML tags
    r = requests.get(URL)
    if(r.status_code != 200):
        raise Exception('Can not fetch data from web page')
    # Extract h1 and p tags from the content using beautiful soup
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all(['h1','p'])

    # Remove html tags and make this into the single article
    text = [result.text for result in results]
    ARTICLE = ' '.join(text)

    # Split full article to sentences
    # <eos> END OF SENTENCE tag
    ARTICLE = ARTICLE.replace('.', '.<eos>')
    ARTICLE = ARTICLE.replace('!', '!<eos>')
    ARTICLE = ARTICLE.replace('?', '?<eos>')
    sentences = ARTICLE.split('<eos>')

    # Split the code block with maximum word to 500 this used for long articles
    max_chunk = 500
    current_chunk = 0 
    chunks = []
    # Split to the single words
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            print(current_chunk)
            chunks.append(sentence.split(' '))

    # Combine back into the sentences
    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    return chunks