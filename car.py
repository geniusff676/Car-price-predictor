import joblib
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler


model = joblib.load("car.pkl")

st.title("Car Price Predictor")

def user_report():
    year=st.text_input("Enter year of model")
    km_driven = st.text_input("Enter Kilometers Driven")
    mileage = st.text_input("Enter Mileage (kmpl)")
    engine = st.text_input("Enter Engine Capacity (cc)")
    max_power = st.text_input("Enter Maximum Power (bhp)")
    seats = st.text_input("Enter Number of Seats")
    Brand=st.selectbox("Select brand", ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Fiat', 'Datsun', 'Jeep',
       'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 'BMW',
       'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo',
       'Kia', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel', 'Peugeot'] )
    transmission = st.selectbox("Select Transmission", ["Manual", "Automatic"])
    fuel = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
    
   
   
   

    try:
        year=float(year)
        mileage = float(mileage)
        engine = float(engine)
        max_power = float(max_power)
        seats = float(seats)
    except ValueError:

        return None


    fuel_encoded = 0
    if fuel == "Petrol":
        fuel_encoded = 0
    elif fuel == "Diesel":
        fuel_encoded = 1
    elif fuel == "CNG":
        fuel_encoded = 2
    elif fuel == "LPG":
        fuel_encoded = 3

    transmission_encoded = 0
    if transmission == "Manual":
        transmission_encoded = 0
    elif transmission == "Automatic":
        transmission_encoded = 1


    brand_encoded=0
    kk=['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Fiat', 'Datsun', 'Jeep',
       'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 'BMW',
       'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo',
       'Kia', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel', 'Peugeot']
    no_of_brands=32
    dictkeys = kk
    keys = list(dictkeys)
    values = list(range(0,no_of_brands))
    dictionary = dict(zip(keys, values))
   






    user_report_data = {
        'year':year,
        'km_driven': float(km_driven),
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats,
        'Brand':brand_encoded,
       
        'transmission': transmission_encoded,
        'fuel': fuel_encoded
        
    }

    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()

if user_data is not None:
    # Scale numerical features using StandardScaler
    numerical_features = [ 'km_driven', 'mileage', 'engine', 'max_power', 'seats']
    scaler = StandardScaler()
    user_data[numerical_features] = scaler.fit_transform(user_data[numerical_features])


if st.button("Predict Price"):
    car_price = model.predict(user_data)
    st.subheader('The estimated price of this car is approximately ₹ {:.2f}.'.format(car_price[0]))

st.text("")
st.text("")
st.text("")

st.markdown("© All rights reserved.")
