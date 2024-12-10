from transformers import pipeline

# Specify the model explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

# File paths
input_file = "input.txt"
output_file = "output.txt"

# Batch size (number of inputs to process at a time)
batch_size = 10

# Read input sentences from the file
with open(input_file, "r") as file:
    texts = [line.strip() for line in file.readlines()]

# Divide inputs into batches
batches = [texts[i:i + batch_size] for i in range(0, len(texts), batch_size)]

# Process each batch and write results to the output file
with open(output_file, "w") as file:
    for batch in batches:
        results = sentiment_analyzer(batch)
        for text, result in zip(batch, results):
            file.write(f"Text: {text}\n")
            file.write(f"Sentiment: {result['label']}, Confidence: {result['score']:.2f}\n\n")

print(f"Batch analysis complete. Results saved to {output_file}")
