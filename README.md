## Sentiment Analysis Tool
This tool analyzes the sentiment (positive, negative, or neutral) of text inputs using a pre-trained transformer model from Hugging Face. It supports batch processing and handles various edge cases like long text and empty inputs.

### Features
- Analyze sentiment of individual or multiple sentences.
- **File Upload**: Upload text files for batch sentiment analysis.
- **Table Display**: Results are displayed in a clean, readable table.
- Handles edge cases:
  - Blank lines in input files are ignored.
  - Long text inputs are truncated to 512 characters.
  - Errors are gracefully caught with meaningful feedback.

### Installation
- Clone this repository:
  - git clone git@github.com:TanyaBuildsAI/sentiment-analysis-tool.git
  - cd sentiment-analysis-tool    
- Installed pip install transformers
- Ensure your Python version is 3.10.x.
---

#### Usage
#### Single Text Input
To analyze a single text input, use the form on the home page:
1. Enter your text in the provided text area.
2. Click "Analyze Sentiment."
3. View the sentiment and confidence score directly on the page.
#### File Upload
To analyze multiple lines of text:
1. Use the "Upload File" form on the home page.
2. Upload a plain text file (`.txt`) with one sentence per line.
3. Click "Upload File."
4. Results will be displayed in a table, showing the sentiment and confidence score for each line.
---

#### Demo
The repository includes the following sample files for testing:
- **small_input.txt**: A file with a few sentences for quick testing.
- **large_input.txt**: A file with 20–30 sentences, including diverse examples.
- **edge_cases.txt**: A file testing edge cases like:
  - Blank lines.
  - Sentences longer than 512 characters.
  - Mixed positive, negative, and neutral sentiments.

#### **Run Demo**
To test the tool with the provided files:

- python sentiment_analysis.py small_input.txt small_output.txt
- python sentiment_analysis.py large_input.txt large_output.txt
- python sentiment_analysis.py edge_cases.txt edge_cases_output.txt


---

#### Notes
- Sentences longer than 512 characters are truncated to avoid errors.
- Input files must be plain text files with one sentence per line.
- The tool uses the `distilbert-base-uncased-finetuned-sst-2-english` model from Hugging Face for sentiment analysis.

### Next Steps
- Add a simple web interface for the tool (coming in Phase 4).
- Explore integration with other input formats like CSV files.
