import pandas as pd

fake = pd.read_csv("backend/Fake.csv")
true = pd.read_csv("backend/True.csv")
fake["label"] = 0  
true["label"] = 1 
data = pd.concat([fake, true], axis=0)
data = data.sample(frac=1).reset_index(drop=True)
data = data[["text", "label"]]
data.to_csv("combined_news.csv", index=False)
print("Dataset combined successfully!")