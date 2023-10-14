from transformers import BertTokenizer, BertForSequenceClassification, pipeline
finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
nlp = pipeline("text-classification", model=finbert, tokenizer=tokenizer)

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

def preprocess_essay(essay):

    # Tokenize the essay into words
    words = nltk.word_tokenize(essay)

    # Initialize the WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Remove punctuation and empty spaces, and lemmatize
    processed_words = [lemmatizer.lemmatize(word) for word in words if word.isalnum()]

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in processed_words if word.lower() not in stop_words]
    max_words=470
    print(len(filtered_words))
    if len(filtered_words) > max_words:
        filtered_words = filtered_words[:max_words]
    # Join the words back into a cleaned essay
    cleaned_essay = " ".join(filtered_words)

    return cleaned_essay

def finBert(text): 
    results = nlp(preprocess_essay(text))
    score = (results[0]['score'])
    if score > 0.8: score -= random.uniform(0.15, 0.24)
    elif score < 0.55: score == 0
    if results[0]['label'] == "Negative": return -score
    else: return score
  
