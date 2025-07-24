# 🌾 Smart Crop Advisor – Crop Recommendation System 🌾 

Welcome to Smart Crop Advisor, an AI-powered crop recommendation system that assists farmers and agricultural analysts in identifying the most suitable crop to cultivate based on soil and climatic conditions.


🧑‍🌾 Powered by machine learning for smarter farming decisions.

# 🚀 Features
🔍 Predicts the best crop based on real-time input for :

  - Soil Nutrients : Nitrogen (N), Phosphorus (P), Potassium (K)

  - Soil pH Level

  - Temperature, Humidity & Rainfall

🎨 Beautiful and responsive Streamlit UI

📊 Backend powered by a Gradient Boosting Classifier

🧠 Data-driven using Crop Recommendation Dataset

💾 Model is pre-trained and loaded using Pickle

# 🧪 Tech Stack

| Tool                          | Purpose                    |
| ----------------------------- | -------------------------- |
| Streamlit                     | UI development             |
| Pandas                        | Data handling              |
| Scikit-learn                  | ML model training          |
| Pickle                        | Model serialization        |
| Matplotlib/Seaborn (optional) | EDA (in training notebook) |


# 📊 Dataset
Source : Kaggle - Crop Recommendation Dataset

| Feature     | Description                |
| ----------- | -------------------------- |
| N           | Nitrogen content in soil   |
| P           | Phosphorus content in soil |
| K           | Potassium content in soil  |
| temperature | Temperature in °C          |
| humidity    | Relative humidity in %     |
| ph          | pH value of the soil       |
| rainfall    | Rainfall in mm             |
| label       | Recommended crop           |



# 📌 Model Information

Model Used : Gradient Boosting Classifier

  - Preprocessing : Label encoding (for crop names), MinMax scaling

  - Accuracy Achieved : ~98% on test data

Stored Models :

  - encoder.pkl : Label encoder

  - scaler.pkl : Feature scaler

  - model_gbc.pkl : Classifier model


# 🚀 Getting Started
1. Clone the Repository

        git clone https://github.com/Amrutha-Poojary/crop-recommendation-app.git

        cd crop-recommendation-app

2. Install Requirements

        pip install streamlit pandas scikit-learn

3. Launch the App

        streamlit run app.py

# ✅ Conclusion

Smart Crop Advisor helps farmers choose the right crop based on soil and weather conditions using machine learning. It’s simple to use, accurate, and can support better farming decisions. This project is a great example of how AI can make agriculture smarter and more efficient.



