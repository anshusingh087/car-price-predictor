import sqlite3
from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# ==========================================
# 1. DATABASE SETUP FUNCTIONS
# ==========================================


def init_db():
  conn = sqlite3.connect("car_predictions.db")
  cursor = conn.cursor()
  # Table create karna agar pehle se nahi bani ho
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            car_name TEXT,
            year INTEGER,
            km_driven INTEGER,
            fuel TEXT,
            seller_type TEXT,
            transmission TEXT,
            owner TEXT,
            predicted_price REAL
        )
    """)
  conn.commit()
  conn.close()


def insert_prediction(
    name, year, km, fuel, seller, trans, owner, predicted_price
):
  conn = sqlite3.connect("car_predictions.db")
  cursor = conn.cursor()
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  cursor.execute(
      """
        INSERT INTO predictions (
            timestamp, car_name, year, km_driven, fuel, 
            seller_type, transmission, owner, predicted_price
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
      (
          current_time,
          name,
          year,
          km,
          fuel,
          seller,
          trans,
          owner,
          predicted_price,
      ),
  )

  conn.commit()
  conn.close()


def get_all_predictions():
  conn = sqlite3.connect("car_predictions.db")
  # SQL query se DataFrame load karna
  df = pd.read_sql_query(
      "SELECT * FROM predictions ORDER BY id DESC", conn
  )
  conn.close()
  return df


# Database initialize karein
init_db()

# ==========================================
# 2. STREAMLIT APP UI & PREDICTION
# ==========================================

st.title("🚗 Car Price Predictor")

# Input Fields
car_name = st.text_input("Car Model / Name", "Maruti Swift Dzire VDI")
year = st.number_input(
    "Manufacturing Year", min_value=1990, max_value=2026, value=2015
)
km_driven = st.number_input(
    "Kilometers Driven", min_value=0, max_value=1000000, value=50000
)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox(
    "Seller Type", ["Individual", "Dealer", "Trustmark Dealer"]
)
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox(
    "Owner Type",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car",
    ],
)

# Predict Button
if st.button("Predict Price"):
  # Yahan aapka model prediction logic aayega (example: model.predict(...))
  # Example calculation:
  predicted_price = round(float(np.random.uniform(200000, 800000)), 2)

  st.success(f"Estimated Selling Price: ₹ {predicted_price:,.2f}")

  # Database me save karna
  insert_prediction(
      name=car_name,
      year=year,
      km=km_driven,
      fuel=fuel,
      seller=seller_type,
      trans=transmission,
      owner=owner,
      predicted_price=predicted_price,
  )
  st.info("Prediction data successfully database me save ho gaya hai!")

# ==========================================
# 3. DATABASE RECORDS DISPLAY KARNA
# ==========================================

st.markdown("---")
st.subheader("📊 Saved Predictions History (SQLite Database)")

# Refresh button database view ke liye
if st.button("Refresh Database Data"):
  st.rerun()

history_df = get_all_predictions()

if not history_df.empty:
  st.dataframe(history_df, use_container_width=True)
else:
  st.write("Abhi tak koi prediction database me record nahi hui hai.")
    
