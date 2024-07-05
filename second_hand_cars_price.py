import pandas as pd
import sklearn
import datetime
import pickle
import streamlit as st

st.title('Second Hand Cars Price Predictor')

st.subheader('Show Casing The Data',divider = 'rainbow')
df = pd.read_csv('./cars24-car-price.csv')
st.dataframe(df)

# Encoding the categorical variables
encoding_dict ={
    'fuel_type' : {
        'Diesel' :1,
        'Petrol': 2,
        'CNG' : 3,
        'LPG' : 4,
        'Electric' : 5
                   },
    'seller_type' : {
        'Dealer' : 1,
        'Individual' : 2,
        'Trustmark Dealer' : 3
                    },
    'transmission_type' : {
        'Manual' : 1,
        'Automatic' : 2
                         }
}

# prediction function (takes only important variables as input as rest will be fixed)
def model_predict(seller_type,fuel_type,transmission_type,engine,seats):
    # load the file
    with open("car_pred",'rb') as file:
        reg_model = pickle.load(file)

    input_features = [[2018.0, seller_type, 40000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
    return reg_model.predict(input_features)

col1,col2 = st.columns(2)

fuel = col1.selectbox('Fuel Type',
                           ['Diesel','Petrol','CNG','LPG','Electric'])

engine = col1.slider('Power',500, 5000, 100)

seller = col1.selectbox('Seller Type',['Dealer','Individual','Trustmark Dealer'])

transmission = col2.selectbox('Transmission type', ['Manual','Automatic'])

seats = col2.selectbox('Seats', [2,3,4,5,6,7,8])


if st.button('Predict Price'):
    
    seller_type = encoding_dict['seller_type'][seller]
    fuel_type = encoding_dict['fuel_type'][fuel]
    transmission_type = encoding_dict['transmission_type'][transmission]

    price = model_predict(seller_type,fuel_type,transmission_type,engine,seats)
    st.write('Price of the car is :', str(price))


