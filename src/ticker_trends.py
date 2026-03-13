import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
DATA_PATH = "../data/wsb_posts_sentiment.csv"
df = pd.read_csv(DATA_PATH)

# Convert timestamp to datetime
df["date"] = pd.to_datetime(df["utc"], unit="s")

# Tickers we want to track
tickers = ["GME","AMC","TSLA","AAPL","SPY"]

# Create empty dictionary
ticker_trends = {}

for ticker in tickers:
    
    # Find posts mentioning ticker
    mask = df["clean_text"].str.upper().str.contains(rf"\b{ticker}\b", na=False)
    
    # Group by date
    counts = df[mask].groupby(df["date"].dt.date).size()
    
    ticker_trends[ticker] = counts

# Combine into dataframe
trend_df = pd.DataFrame(ticker_trends).fillna(0)

# Plot trends
trend_df.plot(figsize=(12,6))

plt.title("WallStreetBets Stock Mention Trends")
plt.xlabel("Date")
plt.ylabel("Number of Mentions")

# Save the chart
plt.savefig("../reports/ticker_trends.png")

# Display it
plt.show()
