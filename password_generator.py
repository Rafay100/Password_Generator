import streamlit as st  # Import Streamlit for creating the web-based UI
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include all letters (a-z, A-Z)

    if use_digits:
        characters += string.digits  # Add numbers (0-9) if selected

    if use_special:
        characters += string.punctuation  # Add special characters (!,@,#,$,%,^,&,*)

    # Generate a password by randomly selecting characters based on the length provided
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI setup
st.title("Password Generator") 

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

st.write("---------------------")

st.write("Built  By  SYed Abdul Rafay❤️")
