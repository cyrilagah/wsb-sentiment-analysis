import pandas as pd

# Path to dataset (relative path from src folder)
DATA_PATH = "../data/wsb_posts.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Basic inspection
print("Dataset loaded successfully.\n")
print("Shape of dataset:", df.shape)
print("\nColumns:")
print(df.columns)
print("\nFirst 5 rows:")
print(df.head())


