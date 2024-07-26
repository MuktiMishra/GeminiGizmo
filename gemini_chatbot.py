import streamlit as st  # for ui
import os
from dotenv import load_dotenv  # to get env variables loaded into the application

load_dotenv()  # loading of all the env variable

import google.generativeai as genai

# genai config of api
genai.configure(api_key="AIzaSyDzlweKAKtGh4rsr8ewdrvqBjaTlQhixu8")

# initialise the model
model = genai.GenerativeModel('gemini-pro')

# define a function to generate response from llm
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text

# setting up streamlit app
st.set_page_config(
    page_title="Gemini pro Q/A project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# setting up header
st.header("Gemini Gizmo")
st.text("𝗜'𝗺 𝗯𝗲𝘁𝘁𝗲𝗿 𝘁𝗵𝗮𝗻 𝘆𝗼𝘂! 𝗡𝗼𝘁 𝗯𝗲𝗹𝗶𝗲𝘃𝗶𝗻𝗴?")
st.text("𝗧𝗲𝘀𝘁 𝗠𝗲 𝘁𝗵𝗲𝗻...😉")

# input
question = st.text_input("Ask a question: ")

# submit button
if st.button("Submit"):
    response = get_gemini_response(question)
    st.write("User:", question)
    st.write("Bot:", response)
