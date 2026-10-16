import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

@st.cache_data
def load_data():
    data = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
    data['brand'] = data['name'].apply(lambda x: str(x).split(' ')[0])
    return data

df = load_data()

@st.cache_resource
def get_trained_model(data):
    features = ['brand', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner']
    X = data[features]
    y = data['selling_price']

    cat_cols = ['brand', 'fuel', 'seller_type', 'transmission', 'owner']
    preprocessor = ColumnTransformer(
        transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)],
        remainder='passthrough'
    )

    pipe = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipe.fit(X, y)
    return pipe

model = get_trained_model(df)

st.title("🚗 Car Price Prediction App")
st.write("Enter car details below and click **Predict Price** to get the estimated market value of your car.")

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Brand", sorted(df['brand'].unique()))
    fuel = st.selectbox("Fuel Type", df['fuel'].unique())
    seller_type = st.selectbox("Seller Type", df['seller_type'].unique())
    year = st.number_input("Manufacturing Year", min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=2017, step=1)

with col2:
    transmission = st.selectbox("Transmission", df['transmission'].unique())
    owner = st.selectbox("Owner Type", df['owner'].unique())
    km_driven = st.number_input("Kilometers Driven (km)", min_value=500, max_value=800000, value=45000, step=1000)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔮 Predict Car Price", use_container_width=True):
    input_row = pd.DataFrame([{
        'brand': brand,
        'year': year,
        'km_driven': km_driven,
        'fuel': fuel,
        'seller_type': seller_type,
        'transmission': transmission,
        'owner': owner
    }])
    pred = model.predict(input_row)[0]
    st.success(f"### Estimated Selling Price: ₹ {int(pred):,}")
