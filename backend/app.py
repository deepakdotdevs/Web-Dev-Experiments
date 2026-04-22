from turtle import pd

from flask_cors import CORS
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
import os

if os.path.exists("model.pkl"):
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
else:
    print("Training model...")


from flask_cors import CORS
from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load model (NO training)
model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))
vectorizer = joblib.load(os.path.join(os.path.dirname(__file__), "vectorizer.pkl"))

@app.route("/")
def home():
    return "Fake News API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["text"]

    transformed = vectorizer.transform([data])
    prediction = model.predict(transformed)[0]
    prob = model.predict_proba(transformed)[0]

    confidence = max(prob) * 100
    result = "Real News" if prediction == 1 else "Fake News"

    return jsonify({
        "prediction": result,
        "confidence": f"{confidence:.2f}"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
    fake = pd.read_csv("Fake.csv")
    true = pd.read_csv("True.csv")

    fake["label"] = 0
    true["label"] = 1

    data = pd.concat([fake, true])
    X = data["text"]
    y = data["label"]

    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump(model, "model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

@app.route("/")
def home():
    return "Fake News API is running!"

# let's create an prediction api 

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["text"]

    # Convert text → numbers
    transformed = vectorizer.transform([data])

    # Predict
    prediction = model.predict(transformed)[0]
    prob = model.predict_proba(transformed)[0]

    confidence = max(prob) * 100

    result = "Real News" if prediction == 1 else "Fake News"

    return jsonify({
        "prediction": result,
        "confidence": f"{confidence:.2f}"
    })
if __name__ == "__main__":
    app.run(debug=True)