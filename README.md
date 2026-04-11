# 🧠 AI Fake News Detection System

🚀 A full-stack AI-powered web application that detects whether a news article is **Real or Fake** using Machine Learning and NLP.

---

## 📌 Overview

This project uses a trained **Machine Learning model** to analyze news text and classify it as **Real News ✅** or **Fake News ❌** along with a confidence score.

It combines:
- 🧠 AI (Machine Learning)
- ⚙️ Backend (Python + Flask)
- 🌐 Frontend (HTML, CSS, JavaScript)

---

## ✨ Features

- 📰 Paste any news and analyze instantly  
- 🤖 AI-based prediction (Real / Fake)  
- 📊 Confidence score display  
- 🎨 Modern UI with animations  
- ⚡ Fast API response using Flask  

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python 🐍
- Flask 🌶️
- Scikit-learn
- Pandas, NumPy
- Joblib

### 🔹 Frontend
- HTML5
- CSS3 (Glassmorphism UI)
- JavaScript (Fetch API)

---

## 🧠 Machine Learning Model

- Algorithm: **Logistic Regression**
- Vectorization: **TF-IDF**
- Accuracy: ~98%
- Dataset: Fake & Real News Dataset (Kaggle)

---

## ⚙️ Project Architecture

User Input (Frontend)
↓
JavaScript (Fetch API)
↓
Flask API (/predict)
↓
ML Model (TF-IDF + Logistic Regression)
↓
Prediction + Confidence
↓
Frontend Display (UI)

---

## 📂 Project Structure


fake-news-detector/
│
├── backend/
│ ├── app.py
│ ├── train_model.py
│ ├── data_processing.py
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│
├── .gitignore
└── README.md


---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository

git clone https://github.com/deepakdotdevs/Web-Dev-Experiments.git

cd fake-news-detector


---

### 2️⃣ Install Dependencies

pip install flask scikit-learn pandas numpy joblib flask-cors


---

### 3️⃣ Run Backend

cd backend
python app.py


👉 Runs on: http://127.0.0.1:5000/

---

### 4️⃣ Run Frontend

cd ../frontend
open index.html


👉 Or use **Live Server (recommended)**

---

## ⚠️ Note

- Dataset (`.csv`) and model files (`.pkl`) are excluded due to GitHub size limits.
- They can be regenerated using the provided scripts.

---

## 📸 Demo

👉 Paste any news → Click **Analyze** → Get result instantly  

---

## 🔮 Future Improvements

- 🌐 URL-based news detection  
