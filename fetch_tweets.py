# fetch_tweets.py

import os           # To access environment variables
import tweepy        # Library to interact with Twitter/X API
import csv           # To save tweets to a CSV file

# 1. Read the Bearer Token from environment variable
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

if not bearer_token:
    raise ValueError("Bearer token not found! Did you set the environment variable?")

# 2. Authenticate with Tweepy using the Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# 3. Define your search keyword or hashtag
search_query = "NBA"  # You can change this to any keyword or hashtag

# 4. Fetch recent tweets (up to 10 for now)
tweets = client.search_recent_tweets(
    query=search_query, 
    max_results=10, 
    tweet_fields=["created_at","text","author_id"]
)

# 5. Save tweets to a CSV file
csv_file = "tweets.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Tweet ID", "Author ID", "Created At", "Text"])
    
    # Write tweet data
    for tweet in tweets.data:
        writer.writerow([tweet.id, tweet.author_id, tweet.created_at, tweet.text])

print(f"Saved {len(tweets.data)} tweets to {csv_file}")

