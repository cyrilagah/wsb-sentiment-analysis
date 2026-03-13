import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment CSV
DATA_PATH = "../data/wsb_posts_sentiment.csv"
df = pd.read_csv(DATA_PATH)

# Count sentiment labels
sentiment_counts = df['sentiment_label'].value_counts()

# Plot
plt.figure(figsize=(6,4))
sentiment_counts.plot(kind='bar', color=['green','grey','red'])
plt.title("Sentiment Distribution of WallStreetBets Posts")
plt.xlabel("Sentiment")
plt.ylabel("Number of Posts")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

