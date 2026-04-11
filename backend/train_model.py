import pandas as pd
import string
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("combined_news.csv")

# Text Cleaning Function
def clean_text(text):
    text = text.lower()  # lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    return text

# Apply cleaning
data["text"] = data["text"].apply(clean_text)

# Features (X) and Labels (y)
X = data["text"]
y = data["label"]

# Convert text → numbers coz ML models understand numbers better
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)

# Split data (train + test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f" Model Accuracy: {accuracy * 100:.2f}%")

# Save model + vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and Vectorizer saved!")