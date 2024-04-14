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

if "db_chain1" not in st.session_state:
    memory_0 = ConversationBufferMemory()
    db_chain1 = SQLDatabaseChain.from_llm(
        llm_singleton.llm,
        db_singleton.db,
        prompt=PROMPT,
        verbose=True,
        memory=memory_0,
    )


st.title("AI analytics Chatbot 🤖")
st.markdown("This page is for SQL Chatbot with Memory")
st.markdown("Welcome to AI-lytics: AI-powered analytics chatbot created by Picipolo!")
st.markdown(
    "To get started, simply type your question about the data in the database, and I'll do my best to assist you."
)


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
            try:
                response = db_chain1.invoke(prompt)["result"]
            except Exception:
                response = (
                    "I'm sorry, I couldn't understand your question. Please try again."
                )
            cost = cb.total_cost if cb.total_cost > 0 else 0.005 * cb.completion_tokens
            st.markdown(f"<small>Query cost: {cost}$</small>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
