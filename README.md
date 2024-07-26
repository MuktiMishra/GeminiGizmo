# GeminiGizmo
# Gemini Pro Chatbot

## Overview
This project implements a chatbot using the Gemini Pro API, allowing users to interact with a large language model. The chatbot is designed to respond to user queries in a natural and coherent manner. The frontend is built using Streamlit.

## Installation

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/MuktiMishra/GeminiGizmo.git>
   cd <repository-directory>

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
 
4. **Set Up Environment Variables**
    Create a .env file in the project root directory.
    Add your Gemini Pro API key to the .env file:
    GEMINI_API_KEY=your_api_key_here

## Usage
 
1. **Run the Streamlit App**
    ```bash
    streamlit run gemini_chatbot.py

2. **Interact with the Chatbot**
   Open your web browser and go to http://localhost:8501.
   Type your question in the input field and click "Submit" to get a response from the chatbot.



