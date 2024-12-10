 
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from transformers import pipeline

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")  # Use the environment variable, fallback to default


# Set up Flask and upload folder
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for("home"))
    
    file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("home"))
    
    if file:
        # Save the uploaded file to the server
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Read and clean the file contents
        with open(filepath, "r") as f:
            texts = [line.strip() for line in f.readlines() if line.strip()]
        
        # Analyze sentiment for each line
        results = sentiment_analyzer(texts)
        
        # Render the results in the results.html template
        return render_template("results.html", texts=texts, results=results, zip=zip)
    
    # Default fallback
    flash("Something went wrong")
    return redirect(url_for("home"))


# Load the sentiment analysis model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        text = request.form["text"]
        result = sentiment_analyzer(text)[0]
        return f"Text: {text}<br>Sentiment: {result['label']}<br>Confidence: {result['score']:.2f}"
    else:
        # If it's a GET request, redirect to the home page
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
