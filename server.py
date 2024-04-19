from flask import Flask, request, render_template
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__, template_folder='C:/Users/hp/SAOAR/templates')


# Load your dataset
df = pd.read_csv('amazon.csv')

# Ensure all reviews are strings
df['reviewText'] = df['reviewText'].apply(lambda x: '' if pd.isnull(x) else str(x))

# Apply sentiment analysis
analyzer = SentimentIntensityAnalyzer()
df['sentiment'] = df['reviewText'].apply(lambda review: analyzer.polarity_scores(review))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    score = analyzer.polarity_scores(review)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    if neg > pos:
        sentiment = "Negative"
    elif pos > neg:
        sentiment = "Positive"
    else:
        sentiment = "Neutral"
    return render_template('index.html', prediction_text='Sentiment: {}'.format(sentiment))

if __name__ == '__main__':
    app.run(debug=True)



