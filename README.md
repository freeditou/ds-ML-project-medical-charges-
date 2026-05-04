# Medical Charges Prediction (Machine Learning Project)

## 📌 Project Overview
This project aims to analyze and predict medical insurance charges based on demographic and health-related features using machine learning techniques.

The goal is to identify the most influential factors affecting medical costs and build accurate predictive models.

---

## 📊 Dataset
The dataset includes the following features:
- age
- sex
- bmi (Body Mass Index)
- children
- smoker
- region
- charges (target variable)

---

## ⚙️ Methodology
The project follows a complete machine learning pipeline:

1. Exploratory Data Analysis (EDA)
2. Data preprocessing (encoding, scaling)
3. Model training:
   - Linear Regression
   - Ridge Regression
   - Lasso Regression
   - ElasticNet
4. Model evaluation using RMSE, MAE, and R²
5. Feature selection using backward elimination
6. Comparison between all features vs selected features

---

## 📈 Results
- Best model: **Linear Regression**
- R² score ≈ 0.81
- Smoking is the most significant factor affecting medical charges

---

## 💡 Key Insights
- Smokers have significantly higher medical costs
- Age and BMI positively impact charges
- Some variables (e.g., gender) have minimal influence

---

## 🚀 Practical Application
A Streamlit application was developed to allow users to input their information and receive an instant prediction of medical charges.

---

## ⚠️ Limitations
- Limited dataset size
- Assumption of linear relationships
- Missing potential features (lifestyle, medical history)

---

## 🔮 Future Improvements
- Use non-linear models (Random Forest, XGBoost)
- Feature engineering (interaction terms, polynomial features)
- Larger and more diverse datasets
