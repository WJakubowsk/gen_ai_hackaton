import requests
import streamlit as st
from const import PROMPT
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks import get_openai_callback
from langchain_experimental.sql import SQLDatabaseChain
from model import DBSingleton, LLM_Singleton

db_singleton = DBSingleton()
llm_singleton = LLM_Singleton()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "db_chain" not in st.session_state:
    memory = ConversationBufferMemory()
    db_chain = SQLDatabaseChain.from_llm(
        llm_singleton.llm, db_singleton.db, prompt=PROMPT, verbose=True, memory=memory
    )

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
        with get_openai_callback() as cb:
            response = db_chain.invoke(prompt)["result"]
            cost = cb.total_cost if cb.total_cost > 0 else 0.005 * cb.completion_tokens
            st.markdown(f"<small>Query cost: {cost}$</small>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
