import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
DATA_PATH = "../data/wsb_posts_sentiment.csv"
df = pd.read_csv(DATA_PATH)

# Convert Unix timestamp to datetime
df['date'] = pd.to_datetime(df['utc'], unit='s')

# Group by date and sentiment label, count posts
daily_sentiment = df.groupby([df['date'].dt.date, 'sentiment_label']).size().unstack(fill_value=0)

# Plot time series
plt.figure(figsize=(12,6))
daily_sentiment.plot(ax=plt.gca(), color=['red','grey','green'])
plt.title("Daily Sentiment Trends - WallStreetBets Posts")
plt.xlabel("Date")
plt.ylabel("Number of Posts")
plt.tight_layout()
plt.show()

