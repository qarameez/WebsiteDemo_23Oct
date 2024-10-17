import streamlit as st

# Title of the app
st.title('Registration Form')

# Create a form
with st.form(key='registration_form'):
    # Input fields
    username = st.text_input('Username')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    if username and email and password:
        # Simulate confirmation message
        st.success(f"Registration Successful for {username}!")
    else:
        # Show error if any field is empty
        st.error("Please fill in all fields.")
