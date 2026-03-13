import pandas as pd
from collections import Counter

# Load dataset
DATA_PATH = "../data/wsb_posts_sentiment.csv"
df = pd.read_csv(DATA_PATH)

# Common stock tickers to search for
tickers_to_track = [
    "GME","AMC","TSLA","AAPL","MSFT","NVDA","SPY","AMZN","META","NFLX"
]

texts = df["clean_text"].astype(str)

ticker_counts = Counter()

for text in texts:
    words = text.upper().split()
    
    for ticker in tickers_to_track:
        if ticker in words:
            ticker_counts[ticker] += 1

ticker_df = pd.DataFrame(
    ticker_counts.items(),
    columns=["ticker","mentions"]
).sort_values(by="mentions", ascending=False)

print("\nTop mentioned tracked tickers:\n")
print(ticker_df)
