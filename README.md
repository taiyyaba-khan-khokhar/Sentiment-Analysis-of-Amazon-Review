# Sentiment-Analysis-of-Amazon-Reviews

# Project Overview

This data science project focuses on sentiment analysis of Amazon product reviews using natural language processing (NLP) techniques. The goal is to analyze the sentiment of Amazon reviews to determine whether they are positive, negative, or neutral. The project primarily utilizes NLTK and TextBlob for text preprocessing and sentiment analysis.

## Key Components

### Data Exploration and Preprocessing

We explore the Amazon Customer Reviews Dataset, ensuring data quality and preparing it for sentiment analysis. Text preprocessing techniques from NLTK and TextBlob are applied to clean and preprocess the text data.

### Sentiment Analysis

We employ two main approaches for sentiment analysis:

- **VADER Sentiment Analysis:** Using the VADER lexicon for sentiment analysis, which is a powerful tool in natural language processing for determining sentiment polarity.
- **TextBlob Sentiment Analysis:** Leveraging TextBlob, a Python library for processing textual data, to determine sentiment polarity and subjectivity.

### Flask Backend Server

A Flask server is developed to serve as the backend for the sentiment analysis system. It integrates with the sentiment analysis models built using NLTK and TextBlob, providing real-time sentiment analysis for user-provided reviews.

### Web Interface

A simple web interface is created using minimalistic HTML forms, allowing users to input their Amazon product reviews. The sentiment analysis results are displayed instantly, providing insights into the sentiment of the reviews.

## Technologies Utilized

- Python: The primary programming language for data analysis and web development.
- NLTK and TextBlob: Essential libraries for text preprocessing and sentiment analysis.
- Flask: The backend server for serving HTTP requests and integrating with the sentiment analysis models.

## Deployment

The sentiment analysis system is deployed using Flask, ensuring seamless accessibility for users. By navigating to the designated URL, users can interact with the web interface and gain insights into Amazon product reviews' sentiments.

## Getting Started

1. Clone this repository to your local machine.
2. Set up the Python environment and install the required packages listed in `requirements.txt`.
3. Launch the Flask server by running `python app.py`.
4. Access the web interface in your browser and start analyzing Amazon product reviews' sentiments!

Feel free to explore, contribute, and enhance this project. Happy sentiment analyzing! 🚀📊
