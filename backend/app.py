from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

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