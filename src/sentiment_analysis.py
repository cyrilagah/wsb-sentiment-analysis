import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load cleaned dataset
DATA_PATH = "../data/wsb_posts.csv"
df = pd.read_csv(DATA_PATH)

# Clean text column if not already cleaned
import re

def clean_text(text):
    text = re.sub(r"http\S+", "", str(text))          # remove URLs
    text = re.sub(r"@\w+", "", text)                 # remove @mentions
    text = re.sub(r"[^\w\s]", "", text)             # remove punctuation
    text = text.lower()                               # lowercase
    text = re.sub(r"\s+", " ", text).strip()         # remove extra whitespace
    return text

df['clean_text'] = df['text'].apply(clean_text)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Compute sentiment scores
df['sentiment'] = df['clean_text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Simple labeling: positive, negative, neutral
def label_sentiment(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

df['sentiment_label'] = df['sentiment'].apply(label_sentiment)

# Show summary
print(df['sentiment_label'].value_counts())
print("\nFirst 5 posts with sentiment:")
print(df[['clean_text','sentiment_label']].head())

# Optional: save to CSV
df.to_csv("../data/wsb_posts_sentiment.csv", index=False)

