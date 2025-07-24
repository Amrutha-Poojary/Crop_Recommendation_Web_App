import streamlit as st
import pandas as pd
import pickle
from streamlit.components.v1 import html
from time import sleep

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: linear-gradient(135deg, #5cb85c, #3d8b3d);
        color: white;
        padding: 1rem;
        border-radius: 10px 10px 0 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 0 !important;
    }
    
    .input-card {
        background: white;
        padding: 1rem;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-top: 0 !important;
    }

    .parameter-change {
        animation: pulse 0.5s ease-in-out;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .stButton>button {
        background: linear-gradient(135deg, #5cb85c, #3d8b3d);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    .result-card {
        background: linear-gradient(135deg, #e6f7e6, #c8e6c9);
        padding: 2rem;
        border-radius: 10px;
        border-left: 6px solid #4caf50;
        margin-top: 1.5rem;
        text-align: center;
    }

    .success-text {
        color: #2e7d32;
        font-weight: 600;
    }

    .crop-name {
        font-size: 2rem;
        font-weight: 700;
        color: #1b5e20;
        text-transform: uppercase;
        margin: 1rem 0;
    }

    .parameter-display {
        color: #2e7d32;
        font-weight: 500;
        margin-top: 1.5rem;
    }

    .footer {
        margin-top: 3rem;
        text-align: center;
        color: #6c757d;
        font-size: 0.9rem;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for animations
parameter_animation_js = """
<script>
    const sliders = document.querySelectorAll('.stSlider');
    sliders.forEach(slider => {
        slider.addEventListener('input', function() {
            this.classList.add('parameter-change');
            setTimeout(() => {
                this.classList.remove('parameter-change');
            }, 500);
        });
    });
</script>
"""

# Load models
@st.cache_resource
def load_models():
    encoder = pickle.load(open("models/encoder.pkl", 'rb'))
    scaler = pickle.load(open("models/scaler.pkl", 'rb'))
    model_gbc = pickle.load(open("models/model_gbc.pkl", 'rb'))
    return encoder, scaler, model_gbc

encoder, scaler, model_gbc = load_models()

# Prediction function
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                          columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    input_scaled = scaler.transform(input_df)
    prediction_encoded = model_gbc.predict(input_scaled)
    prediction = encoder.inverse_transform(prediction_encoded)
    return prediction[0]

# Header with larger font size
st.markdown("""
<div class="header-container">
    <div>
        <h1 style="margin:0; font-size:2.5rem;">Smart Crop Advisor</h1>
        <p style="margin:0; opacity:0.9; font-size:1rem;">AI-powered crop recommendation system</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Section
st.markdown("""
<div class="input-card">
    <h3 style="color:#2e7d32; margin-top:0.5rem; text-align:center;">🌍 Soil & Environment Analysis</h3>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🌱 Soil Nutrients Profile")
    N = st.slider("⛽ Nitrogen (N) ratio", 0, 100, 50, help="Essential for leaf growth", key="nitrogen")
    P = st.slider("🔶 Phosphorous (P) ratio", 0, 100, 50, help="Important for root development", key="phosphorous")
    K = st.slider("💎 Potassium (K) ratio", 0, 100, 50, help="Vital for fruit quality", key="potassium")
    ph = st.slider("🧪 Soil pH level", 0.0, 14.0, 6.5, 0.1, help="Optimal range is typically 5.5-7.0", key="ph")

with col2:
    st.markdown("#### 🌦️ Climate Conditions")
    temperature = st.slider("🌡️ Temperature (°C)", -10.0, 50.0, 25.0, 0.1, key="temp")
    humidity = st.slider("💧 Humidity (%)", 0, 100, 80, key="humidity")
    rainfall = st.slider("🌧️ Rainfall (mm)", 0, 500, 100, key="rainfall")

# Inject animations
html(parameter_animation_js)

# Predict button
if st.button('🔍 Analyze & Recommend Best Crop'):
    with st.spinner('🔬 Analyzing your farming conditions...'):
        sleep(1)
        crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
        
        st.balloons()
        st.markdown(f"""
        <div class="result-card">
            <h3 style="color:#2e7d32; margin-top:0;">🏆 Best Crop Recommendation</h3>
            <div class="crop-name">🎯 {crop.upper()} 🎯</div>
            <p class="success-text">🌻 This crop has the highest suitability for your specified conditions 🌻</p>
            <div class="parameter-display">
                <p>📊 Parameters used for analysis:</p>
                <p>⛽ N: {N} | 🔶 P: {P} | 💎 K: {K}</p>
                <p>🌡️ Temp: {temperature}°C | 💧 Hum: {humidity}% | 🌧️ Rain: {rainfall}mm</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <hr style="border-top: 1px solid #ddd;">
    <p>🧑‍🌾 Smart Crop Advisor • Powered by Machine Learning 🤖</p>
    <p>⚡ For optimal agricultural decision making ⚡</p>
</div>
""", unsafe_allow_html=True)
