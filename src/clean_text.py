import pandas as pd
import re

# Load dataset
DATA_PATH = "../data/wsb_posts.csv"
df = pd.read_csv(DATA_PATH)

# Select the text column
texts = df['text'].astype(str)

# Cleaning function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)          # remove URLs
    text = re.sub(r"@\w+", "", text)             # remove @mentions
    text = re.sub(r"[^\w\s]", "", text)          # remove punctuation
    text = text.lower()                           # lowercase
    text = re.sub(r"\s+", " ", text).strip()     # remove extra whitespace
    return text

# Apply cleaning
df['clean_text'] = texts.apply(clean_text)

# Show results
print("First 5 cleaned texts:")
print(df['clean_text'].head())

