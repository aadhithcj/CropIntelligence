# 🌾 CropIntelligence – A Location-Based Crop Recommendation and Yield Prediction System

CropIntelligence is a machine learning-powered web application designed to support intelligent agricultural decision-making for farmers and agricultural planners in **Kerala, India**. The system predicts the most suitable crops for a given location and climate using historical data, and enables users to compare expected yields across multiple crops.

---

## 🚀 Features

- 📍 **Location-Based Crop Recommendation**  
  Suggests the best crop for a district based on climate, soil, and historical data.

- 🌦 **Real-Time Weather Integration**  
  Uses current temperature and rainfall for dynamic yield predictions.

- 📊 **Crop Comparison**  
  Visualize and compare yield potential across various crops in a selected district.

- 🗺 **Kerala Map Integration**  
  Interactive district-level map for intuitive exploration and predictions.

- 🧠 **Machine Learning Model**  
  Logistic Regression model trained on district-wise crop yield, temperature, rainfall, and soil type data.

---

## 🛠 Tech Stack

| Frontend              | Backend              | Machine Learning         | Data              |
|-----------------------|----------------------|--------------------------|-------------------|
| React + Vite          | Flask (Python)       | Logistic Regression (Sklearn) | Kerala district-wise yield, rainfall


---

## 📸 Screenshots

> _(Add screenshots of the Kerala map, yield prediction UI, crop recommendation panel, etc.)_

---

## 🧪 Model & Dataset

- Model: **Logistic Regression** (multi-class classification)
- Features: `district`, `rainfall`
- Labels: Crop categories (e.g., Rice, Banana, Coconut, etc.)

---

## 📦 Installation

```
# Clone the repository
git clone https://github.com/aadhithcj/CropIntelligence.git
cd CropIntelligence

# Backend Setup
cd backend
pip install -r requirements.txt
python app.py

# Frontend Setup
cd ../frontend
npm install
npm run dev

##📧 Contact
Made with ❤️ by Aadhith C J, Akmal Ansari, Ajilash Edward, Arjun Surya
