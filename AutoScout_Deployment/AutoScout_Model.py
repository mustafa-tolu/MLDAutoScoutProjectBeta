import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import pickle

html_temp = """
<div style="background-color:#043471;padding:1.5px">
<h1 style="color:white;text-align:center;">CAR PRICE PREDICTION </h1>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)



img = Image.open("AutoScout_Logo.png")
st.image(img, caption="")

st.write("\n\n"*2)

filename = 'Auto_Price_Pred_Model'
model = pickle.load(open(filename, 'rb'))


make_model = st.sidebar.selectbox("Model Selection", ("Audi A3", "Audi A1", "Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster"))
hp_kW = st.sidebar.number_input("Horse Power:",min_value=40, max_value=294, value=120, step=5)
age = st.sidebar.number_input("Age:",min_value=0, max_value=3, value=0, step=1)
km = st.sidebar.number_input("km:",min_value=0, max_value=317000, value=10000, step=5000)
Gears = st.sidebar.number_input("Gears:",min_value=5, max_value=8, value=5, step=1)
Gearing_Type = st.sidebar.radio("Gearing Type", ("Manual", "Automatic", "Semi-automatic"))


my_dict = {"make_model":make_model, "hp_kW":hp_kW, "age":age, "km":km, "Gears":Gears, "Gearing_Type":Gearing_Type}
df = pd.DataFrame.from_dict([my_dict])
st.table(df)

if st.button("Predict"):
    pred = model.predict(df)
    st.write("The estimated value of car price is ")
    st.success(pred[0].astype(int))


st.write("\n\n")

