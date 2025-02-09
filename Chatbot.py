# Importing necessary packages
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google API key
api_key = os.getenv("google_api_key")
genai.configure(api_key=api_key)

# Set the model for the chatbot
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit web app setup
st.set_page_config(page_title="ElangoKannan's Chatbot", page_icon="🧊")
st.title("ElangoKannan's Chatbot")
st.header("Welcome to ElangoKannan's Chatbot")
st.write("Ask me anything, I am here to help you")

# User input
question = st.text_input("Enter your question here")
submit = st.button("Proceed")

# Handle user input
if submit:
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            result = model.generate_content(question)
            st.header("Answer for the question:")
            st.write(result.text)
        except Exception as e:
            st.error(f"Failed to generate a response: {e}")



