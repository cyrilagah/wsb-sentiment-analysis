# WallStreetBets Sentiment & Stock Trend Analysis

## Project Overview

This project analyzes Reddit posts from the WallStreetBets community to understand retail investor sentiment and stock discussion trends.

Using natural language processing (NLP), the project:

- Cleans and processes social media text data
- Performs sentiment analysis on posts
- Identifies the most discussed stocks
- Visualizes how stock hype evolves over time

The dataset contains over 190,000 WallStreetBets posts.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- VADER Sentiment Analysis
- WordCloud
- Regular Expressions (Regex)

---

## Project Structure

data/  
Raw and processed datasets

src/  
Python scripts for data processing and analysis

notebooks/  
Exploratory analysis

reports/  
Generated charts and visualizations

---

## Analysis Pipeline

1. Load Reddit dataset
2. Clean text data
3. Perform sentiment analysis
4. Visualize sentiment distribution
5. Analyze sentiment trends over time
6. Detect stock ticker mentions
7. Identify most discussed stocks
8. Visualize stock hype trends

---

## Key Findings

- GameStop (GME) dominates WallStreetBets discussions
- AMC is the second most discussed stock
- Retail investor sentiment fluctuates significantly over time
- Social media hype cycles can be visualized using ticker mentions

---

## Example Visualization

See `reports/ticker_trends.png` for stock mention trends over time.

---

## Future Improvements

- Real-time Reddit data ingestion
- AWS + PySpark pipeline for large-scale processing
- Advanced NLP techniques (topic modeling)
- Sentiment analysis per stock ticker
