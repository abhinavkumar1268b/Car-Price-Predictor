import streamlit as st
import pickle
import pandas as pd

# Load model (pipeline)
model = pickle.load(open(
    r"D:\Machine learning\Projects\car_price_predict\car_app\model.pkl",
    "rb"
))

# Get categories from OneHotEncoder inside pipeline
# get ColumnTransformer safely (no name assumption)
column_trans = None

for step in model.named_steps.values():
    if hasattr(step, 'named_transformers_'):
        column_trans = step
        break

if column_trans is None:
    raise ValueError("ColumnTransformer not found in pipeline")

# get OneHotEncoder
ohe = column_trans.named_transformers_['ohe']

# get categories
name_list = ohe.categories_[0]
fuel_list = ohe.categories_[1]
company_list = ohe.categories_[2]


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.block-container {
    padding: 2rem;
}
h1 {
    text-align: center;
    color: #00E676;
}
.stButton > button {
    background-color: #00E676;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.stSelectbox, .stNumberInput {
    background-color: #262730;
}
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.title("🚗 Car Price Prediction")

st.markdown("### Select car details")

col1, col2 = st.columns(2)

with col1:
    year = st.selectbox("📅 Manufacturing Year", list(range(2025, 1990, -1)))
    fuel = st.selectbox("⛽ Fuel Type", fuel_list)

with col2:
    kms_driven = st.slider("🛣️ KMs Driven", 0, 300000, step=5000)
    company = st.selectbox("🏭 Company", company_list)

st.markdown("---")

# ---------- PREDICTION ----------
if st.button("Predict Price"):
    input_df = pd.DataFrame({
        'name': [name_list[0]],  # Dummy value, not used in prediction
        'company': [company],
        'year': [year],
        'kms': [kms_driven],
        'fuel': [fuel]
    })

    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {int(prediction[0])}")
