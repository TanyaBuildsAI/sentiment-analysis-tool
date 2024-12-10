from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load the sentiment analysis model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["text"]
    result = sentiment_analyzer(text)[0]
    return f"Text: {text}<br>Sentiment: {result['label']}<br>Confidence: {result['score']:.2f}"

if __name__ == "__main__":
    app.run(debug=True)
