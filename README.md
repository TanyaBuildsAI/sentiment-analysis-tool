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
The sentiment analysis tool is functional and includes key features like file upload and batch processing. Future enhancements could include:

1. **Web Interface Enhancements**:
   - Add a more polished design using CSS frameworks like Bootstrap or Tailwind.
   - Include an interactive dashboard to visualize sentiment trends.

2. **Expanded Input Support**:
   - Allow file uploads in formats like CSV or Excel.
   - Enable input directly from URLs or APIs (e.g., fetch reviews from social media).

3. **Advanced Features**:
   - Support for multilingual sentiment analysis.
   - Allow users to fine-tune or train custom sentiment analysis models.

4. **Error Handling and Feedback**:
   - Display clear error messages for unsupported file types or large files.
   - Log errors for debugging and monitoring.

5. **Deployment**:
   - Deploy the tool to a cloud platform (e.g., AWS, Heroku, or Google Cloud) to make it accessible online.
   - Set up CI/CD for automated testing and deployment.

6. **Scalability and Performance**:
   - Optimize the backend to handle larger datasets efficiently.
   - Add caching for frequently used models to improve response times.

7. **Integration with Other Tools**:
   - Provide an API for external applications to access sentiment analysis features.
   - Integrate with business tools like Slack or Microsoft Teams to share results.

8. **User Feedback and Analytics**:
   - Add a feedback form for users to rate the tool and suggest improvements.
   - Implement analytics to track usage patterns and improve user experience.

