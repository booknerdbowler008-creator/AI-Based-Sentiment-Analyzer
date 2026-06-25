# AI-Based Sentiment Analyzer

## Project Overview
AI-Based Sentiment Analyzer is a website which uses user reviews and determines whether the sentiment expressed is Positive or Negative using Artificial Intelligence and Natural Language Processing (NLP).
The project uses a pre- model for sentiment classification and provides confidence scores for predictions.

## Features
* Analyze user reviews
* Detect Positive and Negative sentiments
* Display prediction confidence score
* Simple and user-friendly web interface
* Powered by pre-trained AI models
* No model training required

## Technologies Used
* Python
* Flask
* Hugging Face Transformers
* PyTorch
* HTML
* CSS

## Installation

### Clone Repository

```bash
git clone https://github.com/booknerdbowler008-creator/AI-Based-Sentiment-Analyser.git
```
### Navigate to Project Folder

```bash
cd AI-Based-Sentiment-Analyzer
```
### Install Dependencies

```bash
pip install flask transformers torch
```
### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

## How It Works
1. User enters a review or comment.
2. Flask sends the text to the Transformer model.
3. The AI model analyzes the sentiment.
4. The result is classified as:
   * POSITIVE or
   * NEGATIVE
5. Confidence score is displayed.
6. Result appears on the webpage.

## Example:
### Positive Review
```text
This product is amazing and works perfectly.
```

Output:

```text
Sentiment: POSITIVE
Confidence: 99%
```

### Negative Review
```text
Worst experience ever. Very disappointed.
```
Output:

```text
Sentiment: NEGATIVE
Confidence: 98%
```

## Applications
* Product Review Analysis
* Customer Feedback Analysis
* Social Media Monitoring
* Brand Reputation Management
* Market Research

## Future Enhancements
* Neutral sentiment detection
* Multi-language support
* Sentiment visualization charts
* Database integration
* User authentication
* Review history tracking

## Author
**Debabrata Santra**

## Conclusion
This project demonstrates the practical application of Artificial Intelligence and Natural Language Processing for sentiment classification using modern Transformer-based models.
