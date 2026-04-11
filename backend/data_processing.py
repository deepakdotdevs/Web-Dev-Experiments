import pandas as pd

# Load datasets
fake = pd.read_csv("backend/Fake.csv")
true = pd.read_csv("backend/True.csv")

# Add labels
fake["label"] = 0   # Fake news
true["label"] = 1   # Real news

# Combine both datasets
data = pd.concat([fake, true], axis=0)

# Shuffle data
data = data.sample(frac=1).reset_index(drop=True)

# Keep only news and labels as true or false
data = data[["text", "label"]]

# Save new combined dataset
data.to_csv("combined_news.csv", index=False)

print("Dataset combined successfully!")