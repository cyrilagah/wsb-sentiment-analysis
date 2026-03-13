# WallStreetBets Reddit Sentiment & Stock Trend Analysis

## Project Overview
This project analyzes posts from the WallStreetBets (WSB) subreddit to understand retail investor sentiment and stock discussion trends. Using natural language processing (NLP) and financial data analysis, it identifies the most mentioned stocks, their sentiment, and visualizes hype trends over time.

## Dataset
- WallStreetBets Reddit posts
- Over 190,000 posts from January–June 2025
- Columns: `text`, `clean_text`, `sentiment_label`, `utc` timestamp

## Technologies & Libraries
- Python 3.x
- Pandas
- Matplotlib
- WordCloud
- VADER Sentiment Analysis
- Regular Expressions (Regex)

## Project Structure
data/        # Raw and processed datasets
src/         # Python scripts for data cleaning, sentiment, and ticker analysis
notebooks/   # Optional exploratory analysis
reports/     # Charts and visual outputs
README.md

## Analysis Pipeline
1. Load Reddit dataset
2. Clean post text
3. Perform sentiment analysis (positive, neutral, negative)
4. Generate sentiment word clouds
5. Detect and count stock ticker mentions
6. Analyze stock hype trends over time
7. Generate ticker sentiment (percentage of positive/neutral/negative)
8. Create heatmaps and trend visualizations

## Key Findings
- **GME** and **AMC** dominate discussions on WSB
- **Tech stocks** (AAPL, TSLA, NVDA) mostly have positive sentiment
- **SPY** shows more neutral/negative sentiment compared to others
- Visualizations reveal clear hype spikes for meme stocks

## Visual Outputs

### Ticker Trends
![Ticker Trends](reports/ticker_trends.png)

### Ticker Sentiment Heatmap
![Ticker Sentiment Heatmap](reports/ticker_sentiment_heatmap.png)

### Most Bullish vs Most Bearish Stocks
![Bullish vs Bearish](reports/bullish_vs_bearish.png)

## Future Improvements
- Real-time Reddit data ingestion
- AWS + PySpark pipeline for large-scale processing
- ML model for predicting sentiment
- Advanced NLP (topic modeling, word embeddings)

## Author
Your Name | Data Science & Machine Learning Portfolio Project


