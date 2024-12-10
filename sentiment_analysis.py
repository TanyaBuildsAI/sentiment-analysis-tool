import sys


from transformers import pipeline

# Specify the model explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

# File paths from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Batch size (number of inputs to process at a time)
batch_size = 10

# Read input sentences from the file
with open(input_file, "r") as file:
    texts = [line.strip() for line in file.readlines() if line.strip()]  # Remove blank lines

# Check if the file is empty after cleaning
if not texts:
    print("Error: Input file is empty or contains only blank lines.")
    exit()

# Limit text length to 512 characters (common for models like BERT)
max_length = 512
texts = [text[:max_length] for text in texts]

# Divide inputs into batches
batches = [texts[i:i + batch_size] for i in range(0, len(texts), batch_size)]

# Process each batch and write results to the output file, catch unexpected errors and provide clear messages.
try:
    # Open the output file for writing
    with open(output_file, "w") as file:
        for batch in batches:
            results = sentiment_analyzer(batch)
            for text, result in zip(batch, results):
                file.write(f"Text: {text}\n")
                file.write(f"Sentiment: {result['label']}, Confidence: {result['score']:.2f}\n\n")
except Exception as e:
    print(f"An error occurred during sentiment analysis: {e}")
