## Sentiment Analysis Tool
This tool analyzes the sentiment (positive, negative, or neutral) of text inputs using a pre-trained transformer model from Hugging Face. It supports batch processing and handles various edge cases like long text and empty inputs.

### Features
- Analyze sentiment of individual or multiple sentences.
- Supports **batch processing** for large datasets.
- Command-line arguments for flexible input/output file handling.
- Handles edge cases:
  - Blank lines in input files are ignored.
  - Long text inputs are truncated to 512 characters.
  - Errors are gracefully caught with meaningful feedback.

### Installation
1. Clone this repository:
   ```bash
   git clone git@github.com:TanyaBuildsAI/sentiment-analysis-tool.git
   cd sentiment-analysis-tool
    
    Installed pip install transformers
    Ensure your Python version is 3.10.x.
---

#### **4. Usage**
```markdown
### Usage
To run the tool, use the following command:
```bash
python sentiment_analysis.py <input_file> <output_file>
- <input_file>: Path to the file containing text inputs (one sentence per line).
- <output_file>: Path to the file where the results will be saved.
Example:
python sentiment_analysis.py reviews.txt results.txt
The results will be saved in results.txt with sentiment labels and confidence scores for each input.
---

#### **5. Demo**
```markdown
### Demo
The repository includes the following sample files for testing:
- **small_input.txt**: A file with a few sentences for quick testing.
- **large_input.txt**: A file with 20–30 sentences, including diverse examples.
- **edge_cases.txt**: A file testing edge cases like:
  - Blank lines.
  - Sentences longer than 512 characters.
  - Mixed positive, negative, and neutral sentiments.

#### **Run Demo**
To test the tool with the provided files:
```bash
python sentiment_analysis.py small_input.txt small_output.txt
python sentiment_analysis.py large_input.txt large_output.txt
python sentiment_analysis.py edge_cases.txt edge_cases_output.txt


---

#### **6. Notes**
```markdown
### Notes
- Sentences longer than 512 characters are truncated to avoid errors.
- Input files must be plain text files with one sentence per line.
- The tool uses the `distilbert-base-uncased-finetuned-sst-2-english` model from Hugging Face for sentiment analysis.

### Next Steps
- Add a simple web interface for the tool (coming in Phase 4).
- Explore integration with other input formats like CSV files.
