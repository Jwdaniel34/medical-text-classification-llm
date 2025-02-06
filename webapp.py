import streamlit as st
import pickle

# load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Title of the web app
st.title("Medication Description Classifier")

# User Input
description = st.text_input("Enter the description of the medication:")

# When the user clicks the button, performs prediction
if st.button('Predict Preferred Medication'):
    if description:
        prediction = model.predict([description])
        st.write(f"The preferred medication for this description"
                 f"is: {prediction[0]}")
    else:
        st.write("Please enter a medication description.")