import streamlit as st
import numpy as np
import pandas as pd


st.write("""
# TeaTally 
### Share Your Boba Status w/ Friends
""")


# Option selection for the user
option = st.selectbox(
    'Create a new friend group or join an existing one?',
    ['Choose an option', 'Create a new group', 'Join an existing group']
)

# Initialize an empty string for the group name
group_name = ''

# Conditional logic based on the user's choice
if option == 'Create a new group':
    # Text input for entering a new group name
    group_name = st.text_input('Enter a name for your new group:')
    if st.button('Create Group'):
        # Here, you would include the logic to create a new group
        # For now, it's just a placeholder print statement
        st.success(f'Group "{group_name}" created successfully!')
        # Add logic to add the group to your database

elif option == 'Join an existing group':
    # Text input for entering the name of an existing group to join
    group_name = st.text_input('Enter the name of the group you want to join:')
    if st.button('Join Group'):
        # Here, you would include the logic to check if the group exists and join it
        # For now, it's just a placeholder print statement
        st.success(f'Joined group "{group_name}" successfully!')
        # Add logic to verify and add the user to the group in your database



# st.write("""
# # drink tracker
# drinks consumed in 2024!!
# """)

# with st.form('boba_tracker', clear_on_submit=True):
#     st.header('add a new drink!')

#     user = st.text_input(label='who is logging a drink?', placeholder='name')

#     month, date, location, drink = st.columns([0.2, 0.1, 0.2, 0.5])

#     with location:
#         enter_location = st.text_input(label='location:', placeholder='eg: yun')
#     with drink:
#         enter_boba = st.text_input(label='drink (format: base with topping 1 and topping 2 (drink name); omitting anything that doesn\'t exist):', 
#                                    placeholder='eg: jasmine milk tea with boba (snow jasmine)')

#     drink_rating, topping_rating, location_rating = st.columns(3)

#     with drink_rating:
#         enter_dr = st.text_input(label='drink rating (1-10):', placeholder='eg: 8')
#     with topping_rating:
#         enter_tr = st.text_input(label='topping rating (1-10):', placeholder='eg: 9')
#     with location_rating:
#         enter_lr = st.text_input(label='location rating (1-10):', placeholder='eg: 8')
    
#     submit_button = st.form_submit_button('submit')
    
#     if submit_button:
#         st.write('new boba recorded!')

# st.write("""
# ## current 2024 drink consumption
# """)

# df = pd.read_csv('data/drinks.csv')

# # st.write(df)
# st.dataframe(df)
