import requests
from bs4 import BeautifulSoup
import nltk
import re
from nltk.tokenize import sent_tokenize
import re
import spacy
from trial import finBert
nlp = spacy.load("en_core_web_sm")
from model import predict
import string

# Send an HTTP GET request to the URL
response = requests.get("https://www.thestar.com.my/business/business-news/2023/03/27/bonds-are-back")

def sentiment_score(result):
   sentiment = "moderately negative" if result['label'] == 'Negative' and result['score'] < 0.7 else "negative" if result['label'] == 'Negative' else "neutral" if result['label'] == 'Neutral' else "moderately positive" if result['label'] == 'Positive' and result['score'] < 0.7 else "positive"
   return sentiment  

def sentiment(url):
    longest_sentence = ""
    max_sentence_length = 0
    response = requests.get(url)
    paragraphs = []
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all paragraph elements within the article content
        paragraphs = soup.find_all('p')

        if paragraphs:
            # Extract and print the article content
            article_text = '\n'.join([p.get_text() for p in paragraphs])
            # Split the string into an array using double newline as the separator
            paragraphs = article_text.split('\n\n')
            # print(len(paragraphs))
            for sentence in paragraphs:    
            # Remove extra whitespaces and newline characters, and calculate the length
                sentence = sentence.strip()
                sentence_length = len(sentence)
                if sentence_length > max_sentence_length:
                    max_sentence_length = sentence_length
                    longest_sentence = sentence

            remove_dates = lambda text: re.sub(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2}|[A-Z][a-z]+ \d{1,2}(st|nd|rd|th)?, \d{4}|\d{1,2} [A-Z][a-z]+ \d{4}|[A-Z][a-z]+', '', text)
            cleaned_text = longest_sentence.replace('"', '')
            cleaned_text = re.sub(' +', ' ', cleaned_text)
            cleaned_text = remove_dates(cleaned_text)
            cleaned_text = re.sub(r'^[^\w]+', '', cleaned_text)
            cleaned_text = cleaned_text[0].capitalize() + cleaned_text[1:]  
            sentences = sent_tokenize(cleaned_text) 
            sentiment_score = predict(sentences)
            return cleaned_text, finBert(cleaned_text), sentiment_score
        else:
            return("No paragraphs found in the article content."), null, null
    else:
        return(f"Failed to fetch the web page. Status code: {response.status_code}"), null, null