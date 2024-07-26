import streamlit as st  # for UI
import os
from dotenv import load_dotenv  # to get env variables loaded into the application

load_dotenv()  # loading of all the env variables

import google.generativeai as genai

# Retrieve API key from environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure genai with the API key
genai.configure(api_key=GEMINI_API_KEY)

# Initialise the model
model = genai.GenerativeModel('gemini-pro')

# Define a function to generate response from LLM
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text

# Setting up Streamlit app
st.set_page_config(
    page_title="Gemini Pro Q/A Project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Setting up header
st.header("Gemini Gizmo")
st.text("𝗜'𝗺 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗵𝗮𝗻 𝘆𝗼𝘂! 𝗡𝗼𝘁 𝗯𝗲𝗹𝗶𝗲𝘃𝗶𝗻𝗴?")
st.text("𝗧𝗲𝘀𝘁 𝗠𝗲 𝘁𝗵𝗲𝗻...😉")

# Input
question = st.text_input("Ask a question: ")

# Submit button
if st.button("Submit"):
    response = get_gemini_response(question)
    st.write("User:", question)
    st.write("Bot:", response)
