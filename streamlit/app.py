import streamlit as st
import numpy as np
import pandas as pd

st.write("""
# drink tracker
drinks consumed in 2024!!
""")

with st.form('boba_tracker', clear_on_submit=True):
    st.header('add a new drink!')

    user = st.text_input(label='who is logging a drink?', placeholder='name')

    month, date, location, drink = st.columns([0.2, 0.1, 0.2, 0.5])

    with month:
        enter_month = st.text_input(label='month:', placeholder='eg: january')
    with date:
        enter_date = st.text_input(label='date:', placeholder='eg: 1')
    with location:
        enter_location = st.text_input(label='location:', placeholder='eg: yun')
    with drink:
        enter_boba = st.text_input(label='drink (format: base with topping 1 and topping 2 (drink name); omitting anything that doesn\'t exist):', 
                                   placeholder='eg: jasmine milk tea with boba (snow jasmine)')

    drink_rating, topping_rating, location_rating = st.columns(3)

    with drink_rating:
        enter_dr = st.text_input(label='drink rating (1-10):', placeholder='eg: 8')
    with topping_rating:
        enter_tr = st.text_input(label='topping rating (1-10):', placeholder='eg: 9')
    with location_rating:
        enter_lr = st.text_input(label='location rating (1-10):', placeholder='eg: 8')
    
    submit_button = st.form_submit_button('submit')
    
    if submit_button:
        st.write('new boba recorded!')

st.write("""
## current 2024 drink consumption
""")

df = pd.read_csv('data/drinks.csv')

# st.write(df)
st.dataframe(df)
