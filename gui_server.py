from flask import Flask, request, jsonify, send_from_directory
from simple_sentiment_analyzer import SimpleSentimentAnalyzer
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    blob = SimpleSentimentAnalyzer(text)
    sentiment = blob.sentiment
    
    return jsonify({
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity,
        'label': 'Positive' if sentiment.polarity > 0.1 else ('Negative' if sentiment.polarity < -0.1 else 'Neutral')
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
