import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("medical-charges.csv")

# Preprocessing
df = df.drop_duplicates()
df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)

# Features / target
X = df.drop('charges', axis=1)
y = df['charges']

# Train model
model = LinearRegression()
model.fit(X, y)

# UI
st.title("💊 Medical Charges Prediction App")

st.write("Enter patient information to estimate medical charges:")

# Inputs
age = st.slider("Age", 18, 65, 30)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)

sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "southeast", "southwest"])

# Convert input to dataframe
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'sex_male': [1 if sex == "male" else 0],
    'smoker_yes': [1 if smoker == "yes" else 0],
    'region_northwest': [1 if region == "northwest" else 0],
    'region_southeast': [1 if region == "southeast" else 0],
    'region_southwest': [1 if region == "southwest" else 0],
})

# Prediction
if st.button("Predict Charges"):
    prediction = max(0, model.predict(input_data)[0])
    
    st.success(f"💰 Estimated Medical Charges: ${prediction:,.2f}")

    if smoker == "yes":
        st.warning("⚠️ Smoking significantly increases medical costs!")