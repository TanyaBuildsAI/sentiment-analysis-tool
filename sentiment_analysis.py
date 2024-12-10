from transformers import pipeline

# Load HuggingFace pre-trained sentiment analysis model and specifiy model explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

# Step 1: Read input sentences from a file
input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    texts = file.readlines()

# Step 2: Analyze sentiment for each sentence
results = sentiment_analyzer([text.strip() for text in texts])

# Step 3: Write results to an output file
with open(output_file, "w") as file:
    for text, result in zip(texts, results):
        file.write(f"Text: {text.strip()}\n")
        file.write(f"Sentiment: {result['label']}, Confidence: {result['score']:.2f}\n\n")

print(f"Sentiment analysis results saved to {output_file}")
