from flask_cors import CORS
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

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