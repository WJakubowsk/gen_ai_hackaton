import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(
    page_title="AIlytics Chatbot",
    page_icon=":robot_face:",
)

st.title("AI analytics Chatbot 🤖")
st.markdown("Welcome to AI-lytics: AI-powered analytics chatbot created by Picipolo!")
st.markdown(
    "To get started, simply type your question about the data in the database, and I'll do my best to assist you."
)


def get_response(user_query: str) -> str:
    """
    Gets the response from the AI model.
    Args:
        user_query (str): The user query.
    Returns:
        str: The response from the AI model.
    """
    response = requests.post(
        API_URL,
        json={"input": {"question": user_query}},
    )
    return response.json()["output"]["content"]


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        try:
            response = get_response(prompt)
        except Exception:
            response = "I'm sorry, I couldn't understand your query. Please try again."

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
