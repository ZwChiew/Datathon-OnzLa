from flask import Flask, request, jsonify
from flask_cors import CORS
from Classifier import classify
from sentiment import sentiment

app = Flask(__name__)
CORS(app)

@app.route('/api/sentiment', methods=['POST'])
def get_sentiment_from_react():
    try:
        data = request.get_json()
        user_input = data['data']
        print(user_input)
        article,sentiment_score,pointer = sentiment(user_input)
        return {'article': article, 'sentiment_score': sentiment_score}
    except Exception as e:
        # Handle the error and return an error response
        error_message = str(e)
        return jsonify({'error': error_message}), 500

@app.route('/api/classify', methods=['POST'])
def get_classifier_from_react():
    try:
        data = request.get_json()
        user_input = data['data']
        print(user_input)
        answer = classify(user_input)
        return answer
    except Exception as e:
        # Handle the error and return an error response
        error_message = str(e)
        return jsonify({'error': error_message}), 500

if __name__ == "__main__":
    app.run(debug=False)