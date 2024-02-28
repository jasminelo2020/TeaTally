import streamlit as st
import numpy as np
import pandas as pd


st.write("""
# TeaTally 
### Share Your Boba Status w/ Friends
""")


# Function to display the initial dropdown menu
def show_group_selection():
    # Placeholder for the group selection dropdown
    option = st.selectbox('Create a new friend group or join an existing one?',
    ['Choose an option', 'Create a new group', 'Join an existing group'])

    # Initialize an empty string for the group name
    group_name = ''
        
    if option == 'Create a new group':
        # Text input for entering a new group name
        group_name = st.text_input('Enter a name for your new group:')
        # Update the session state to indicate a group has been selected
        st.session_state.option = group_name  # Save the selected group ID in session state
        if st.button('Create Group'):
            # Here, you would include the logic to create a new group
            # For now, it's just a placeholder print statement
            st.success(f'Group "{group_name}" created successfully!')
            # Add logic to add the group to your database

        
    elif option == 'Join an existing group':
        # Text input for entering the name of an existing group to join
        group_name = st.text_input('Enter the name of the group you want to join:')
        # Update the session state to indicate a group has been selected
        st.session_state.option = group_name  # Save the selected group ID in session state
        if st.button('Join Group'):
            # Here, you would include the logic to check if the group exists and join it
            # For now, it's just a placeholder print statement
            st.success(f'Joined group "{group_name}" successfully!')
            # Add logic to verify and add the user to the group in your database
        
        
    # If a group ID is selected (and it's not the placeholder choice)
    if option and option != 'Choose an option':
        # Update the session state to indicate a group has been selected
        st.session_state.group_selected = True

# Function to display content after a group is selected
def show_group_content():
    # Assuming 'group_id' is stored in session_state when a group is selected
    option = st.session_state.get('option', '')
    
    # Display a message with the selected group ID
    st.write(f"You're viewing content for group: {option}")
    
    # Here, you can add more content or functionality specific to the group
    # For example, display group-specific data, forms, charts, etc.
    st.write("Here's some content for your group...")
    
    
# Check if a group has already been selected
if not st.session_state.get('group_selected', False):
    # If no group has been selected, show the group selection dropdown
    show_group_selection()
else:
    # If a group has been selected, show the group-specific content
    show_group_content()
    
    
    
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
