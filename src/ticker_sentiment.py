import pandas as pd

# Load dataset with sentiment
DATA_PATH = "../data/wsb_posts_sentiment.csv"
df = pd.read_csv(DATA_PATH)

# List of tickers we are tracking
tickers = ["GME","AMC","TSLA","AAPL","MSFT","AMZN","NVDA","NFLX","META","SPY"]

results = []

for ticker in tickers:

    # Find posts mentioning the ticker
    mask = df["clean_text"].str.upper().str.contains(rf"\b{ticker}\b", na=False)

    subset = df[mask]

    sentiment_counts = subset["sentiment_label"].value_counts(normalize=True)

    positive = sentiment_counts.get("positive",0) * 100
    neutral = sentiment_counts.get("neutral",0) * 100
    negative = sentiment_counts.get("negative",0) * 100

    results.append({
        "ticker": ticker,
        "positive": positive,
        "neutral": neutral,
        "negative": negative
    })

sentiment_df = pd.DataFrame(results)

print("\nSentiment by ticker:\n")
print(sentiment_df)
