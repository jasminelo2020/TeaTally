import streamlit as st

# for data wrangling
import numpy as np
import pandas as pd

# for displaying images
import requests
from PIL import Image
from io import BytesIO

# for firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd


st.set_page_config(page_title="TeaTally", page_icon="🍵")

st.markdown("""
        <style>
        .big-font {
            font-size:50px !important;
            font-weight: bold;
        }
        .centered-text {
            text-align: center;
        }
        </style>
        <p class="big-font centered-text">TeaTally</p>
        <p class="centered-text">Share Boba Status w/ Friends</p>
        """, unsafe_allow_html=True)








# Path to your Firebase credentials
cred_path = 'creds.json'

try:
    # Try to retrieve an existing app, replace 'default' with your Firebase app name if you have set one
    firebase_admin.get_app()
except ValueError:
    # If it fails because no app with this name exists, initialize the app
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

def fetch_data_as_dataframe():
    data = []
    docs = db.collection('groupID').stream()  # Use the correct collection name

    for doc in docs:
        doc_dict = doc.to_dict()
        doc_dict['document_id'] = doc.id  # Add the document ID to the dictionary
        data.append(doc_dict)
    
    df = pd.DataFrame(data)
    return df






# Check if the 'joined' flag is set in the session state
if 'joined' not in st.session_state or not st.session_state['joined']:

    # display cat image 
    response = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSipyYY6-YbAdCrJaQYdWiFJwrQTvaIgkFX6Q&usqp=CAU')
    img = Image.open(BytesIO(response.content))

    left, center, right = st.columns([1,2,1])  # The middle column is twice the size of the side columns

    with center:
        st.image(img, use_column_width=True)

    with center:
        group_name = st.text_input('Enter name of group id you want to join:', key='group_name')
        if st.button('Join Group', key='join_group'):
            # Logic for joining the group
            # Here you should include the logic for what happens when the button is pressed
            # For example, check if the group exists, and add the user to the group

            # Set the 'joined' flag to True to indicate the user has joined a group
            st.session_state['joined'] = True
else:
    # If the 'joined' flag is set, display a confirmation message or redirect
    st.write(f"You have joined {st.session_state.group_name}.")
    # You can use st.empty() to clear the previous contents or redirect to another page or state.
    
    # Now you can get your Firestore client
    db = firestore.client()
    # Define a function to fetch data and convert to a DataFrame

    # Use the function to get the data
    df = fetch_data_as_dataframe()
    
    # Now you can use st.dataframe to display the DataFrame in your Streamlit app
    st.dataframe(df)


# # Function to display the initial dropdown menu
# def show_group_selection():
#     # Placeholder for the group selection dropdown
#     option = st.selectbox('Create a new friend group or join an existing one?',
#     ['Choose an option', 'Create a new group', 'Join an existing group'])

#     # Initialize an empty string for the group name
#     group_name = ''
        
#     if option == 'Create a new group':
#         # Text input for entering a new group name
#         group_name = st.text_input('Enter a name for your new group:')
#         # Update the session state to indicate a group has been selected
#         st.session_state.option = group_name  # Save the selected group ID in session state
#         if st.button('Create Group'):
#             # Here, you would include the logic to create a new group
#             # For now, it's just a placeholder print statement
#             st.success(f'Group "{group_name}" created successfully!')
#             # Add logic to add the group to your database

        
#     elif option == 'Join an existing group':
#         # Text input for entering the name of an existing group to join
#         group_name = st.text_input('Enter the name of the group you want to join:')
#         # Update the session state to indicate a group has been selected
#         st.session_state.option = group_name  # Save the selected group ID in session state
#         if st.button('Join Group'):
#             # Here, you would include the logic to check if the group exists and join it
#             # For now, it's just a placeholder print statement
#             st.success(f'Joined group "{group_name}" successfully!')
#             # Add logic to verify and add the user to the group in your database
        
        
#     # If a group ID is selected (and it's not the placeholder choice)
#     if option and option != 'Choose an option':
#         # Update the session state to indicate a group has been selected
#         st.session_state.group_selected = True

# # Function to display content after a group is selected
# def show_group_content():
#     # Assuming 'group_id' is stored in session_state when a group is selected
#     option = st.session_state.get('option', '')
    
#     # Display a message with the selected group ID
#     st.write(f"You're viewing content for group: {option}")
    
#     # Here, you can add more content or functionality specific to the group
#     # For example, display group-specific data, forms, charts, etc.
#     st.write("Here's some content for your group...")
    
    
# # Check if a group has already been selected
# if not st.session_state.get('group_selected', False):
#     # If no group has been selected, show the group selection dropdown
#     show_group_selection()
# else:
#     # If a group has been selected, show the group-specific content
#     show_group_content()
    
    
    
# # Option selection for the user
# option = st.selectbox(
#     'Create a new friend group or join an existing one?',
#     ['Choose an option', 'Create a new group', 'Join an existing group']
# )    

# # Initialize an empty string for the group name
# group_name = ''

# # Conditional logic based on the user's choice
# if option == 'Create a new group':
#     # Text input for entering a new group name
#     group_name = st.text_input('Enter a name for your new group:')
#     if st.button('Create Group'):
#         # Here, you would include the logic to create a new group
#         # For now, it's just a placeholder print statement
#         st.success(f'Group "{group_name}" created successfully!')
#         # Add logic to add the group to your database

# elif option == 'Join an existing group':
#     # Text input for entering the name of an existing group to join
#     group_name = st.text_input('Enter the name of the group you want to join:')
#     if st.button('Join Group'):
#         # Here, you would include the logic to check if the group exists and join it
#         # For now, it's just a placeholder print statement
#         st.success(f'Joined group "{group_name}" successfully!')
#         # Add logic to verify and add the user to the group in your database



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





