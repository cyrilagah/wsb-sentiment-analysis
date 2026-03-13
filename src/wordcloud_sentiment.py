import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load sentiment CSV
DATA_PATH = "../data/wsb_posts_sentiment.csv"
df = pd.read_csv(DATA_PATH)

# Function to generate a word cloud for a given sentiment
def generate_wordcloud(sentiment_label, df):
    text = " ".join(df[df['sentiment_label'] == sentiment_label]['clean_text'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {sentiment_label.capitalize()} Posts")
    plt.show()

# Generate word clouds for each sentiment
for label in ['positive','neutral','negative']:
    generate_wordcloud(label, df)
