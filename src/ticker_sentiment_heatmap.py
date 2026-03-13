import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
DATA_PATH = "../data/wsb_posts_sentiment.csv"
df = pd.read_csv(DATA_PATH)

# Tickers to track
tickers = ["GME","AMC","TSLA","AAPL","MSFT","AMZN","NVDA","NFLX","META","SPY"]

results = []

for ticker in tickers:

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
sentiment_df.set_index("ticker", inplace=True)

# Plot heatmap
plt.figure(figsize=(8,5))
plt.imshow(sentiment_df)

plt.xticks(range(len(sentiment_df.columns)), sentiment_df.columns)
plt.yticks(range(len(sentiment_df.index)), sentiment_df.index)

plt.colorbar(label="Sentiment %")

plt.title("Stock Sentiment Heatmap (WallStreetBets)")
plt.xlabel("Sentiment Type")
plt.ylabel("Ticker")

plt.tight_layout()

# Save chart
plt.savefig("../reports/ticker_sentiment_heatmap.png")

# Show chart
plt.show()
