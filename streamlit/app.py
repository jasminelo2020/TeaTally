import streamlit as st
import numpy as np
import pandas as pd

st.write("""
# drink tracker
drinks consumed in 2024!!
""")

with st.form('boba_tracker', clear_on_submit=True):
    st.header('add a new drink!')

    month, date, location, drink = st.columns([0.2, 0.1, 0.2, 0.5])

    with month:
        a = st.text_input(label='month:', placeholder='eg: january')
    with date:
        a = st.text_input(label='date:', placeholder='eg: 1')
    with location:
        a = st.text_input(label='location:', placeholder='eg: yun')
    with drink:
        enter_boba = st.text_input(label='drink (format: base with topping 1 and topping 2 (drink name); omitting anything that doesn\'t exist):', 
                                   placeholder='eg: jasmine milk tea with boba (snow jasmine)')

#     drink_rating, topping_rating = st.columns(2)
    
    submit_button = st.form_submit_button('submit')
    
    if submit_button:
        st.write('new boba recorded!')

st.write("""
## current 2024 drink consumption
""")

df = pd.read_csv('data/drinks.csv')

# st.write(df)
st.dataframe(df)
