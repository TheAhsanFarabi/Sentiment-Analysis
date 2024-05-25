from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    """
    Function to perform sentiment analysis on the given text.
    
    Args:
    text (str): The text to analyze.
    
    Returns:
    sentiment (str): The sentiment of the text, either 'positive', 'negative', or 'neutral'.
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity score
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity score
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_api():
    text = request.json['text']
    sentiment = analyze_sentiment(text)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
