# Importing necessary packages
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Configure Google API key
api_key = os.getenv("google_api_key")
genai.configure(api_key=api_key)

# Set the model for the storyteller
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit web app setup
st.set_page_config(page_title="ElangoKannan's AI Storyteller", page_icon="📖")
st.title("ElangoKannan's AI Storyteller")
st.header("Welcome to ElangoKannan's AI Storyteller")
st.write("Create your own stories with a few simple prompts!")

# User input
prompt = st.text_input("Enter your story prompt here")
submit = st.button("Generate Story")

# Handle user input
if submit:
    if prompt.strip() == "":
        st.warning("Please enter a story prompt.")
    else:
        try:
            # Generate story using prompt
            result = model.generate_content({
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            })
            st.header("Generated Story:")
            st.write(result.text)
        except Exception as e:
            st.error(f"Failed to generate a story: {e}")

