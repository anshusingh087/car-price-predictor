# 🚗 Car Price Prediction & Analytics App

## 📌 Project Overview
This project is an end-to-end Machine Learning web application designed to predict the estimated market selling price of used cars based on multiple vehicle specifications. Built with Python and Scikit-Learn, the application utilizes a Random Forest Regressor integrated into a Streamlit web interface and is fully deployed on Streamlit Community Cloud.

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **Data Analysis & Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn, Plotly
- **Machine Learning:** Scikit-Learn
  - RandomForestRegressor
  - Pipeline & ColumnTransformer
  - OneHotEncoder
  - train_test_split & r2_score
- **Web App Framework:** Streamlit
- **Deployment & Version Control:** GitHub, Streamlit Community Cloud

---

## 📊 Dataset & Features
The model is trained on the Car Details from Car Dekho dataset using key car attributes:
- **Brand:** Manufacturer brand extracted from the car model name
- **Manufacturing Year:** Year of manufacturing
- **Kilometers Driven:** Total distance driven in kilometers
- **Fuel Type:** Petrol, Diesel, CNG, LPG
- **Transmission:** Manual / Automatic
- **Seller Type:** Individual, Dealer, Trustmark Dealer
- **Owner Type:** First Owner, Second Owner, etc.
- **Target Variable:** selling_price (Estimated selling price in INR)

---

## ⚙️ Key Implementation Steps
1. **Data Loading & Inspection:** Inspected shapes, columns, and verified zero missing values.
2. **Feature Engineering:** Extracted brand names from full car names and calculated vehicle age.
3. **Exploratory Data Analysis (EDA):** Analyzed market trends, brand distribution, and price behavior across fuel types and mileage.
4. **Machine Learning Pipeline:** Preprocessed categorical columns using OneHotEncoder and trained a RandomForestRegressor pipeline, achieving an R2 accuracy score of ~74%.
5. **Streamlit Deployment:** Developed a user-friendly 2-column input UI and hosted the live application via Streamlit Cloud connected to GitHub.

---

## 🔗 Project Links
- **Live Application:** https://car-price-predictor-yz7dvie4c6iwckuv5udouu.streamlit.app/
- **GitHub Repository:** https://github.com/anshusingh087/car-price-predictor
-
