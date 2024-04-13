import os

import requests
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

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


def get_response(user_query: str) -> dict:
    """
    Gets the response from the AI model.
    Args:
        user_query (str): The user query.
    Returns:
        dict: The response from the AI model.
    """

    response = requests.post(
        API_URL,
        json={"input": {"question": user_query}},
    )

    return str(response.json()["output"]["content"])


user_query = st.chat_input("Type your query here")

if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        ai_response = st.write(get_response(user_query))
