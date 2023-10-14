import pickle
import nltk
nltk.download('punkt')  # Download the necessary data
import numpy as np


filename = "sentiment_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

filename1= "vectorizer.sav"
vectorizer = pickle.load(open(filename1, 'rb'))

def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove newline and carriage return characters
    text = text.replace("\n", "").replace("\r", "")

    doc = nlp(text)
    lemmatized_text = ' '.join(
    [token.lemma_ for token in doc if not token.is_space and not token.is_stop])
    return lemmatized_text

def predict(text):
    arr = []
    new_sentence_vector = vectorizer.transform(text)
    for a in new_sentence_vector: 
        score = loaded_model.predict(a)
        if score >= 0.7 or score <= -0.15: score-=0.4
        arr.append(score)
    arr = np.array(arr)    
    positive_count = np.sum(arr >= 0)
    negative_count = len(arr) - positive_count
    negative_total = np.sum(arr[arr < 0])
    positive_total = np.sum(arr[arr >= 0])
    total_values = np.sum(arr)
    score = 0
    # Calculate the weighted sum for each category
    score= (positive_count * positive_total + (negative_count * negative_total * 5))/(total_values*len(arr))
    return(score)
        