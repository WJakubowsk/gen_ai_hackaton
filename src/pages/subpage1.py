import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks import get_openai_callback
from langchain_experimental.sql import SQLDatabaseChain

from const import PROMPT
from model import DBSingleton, LLM_Singleton
from utils import create_df, generate_plot

st.set_page_config(
    page_title="SQL Chatbot with Memory and Visualization",
)

db_singleton = DBSingleton()
llm_singleton = LLM_Singleton()

if "messages2" not in st.session_state:
    st.session_state.messages2 = []

if "db_chain2" not in st.session_state:
    memory_1 = ConversationBufferMemory()
    db_chain2 = SQLDatabaseChain.from_llm(
        llm_singleton.llm,
        db_singleton.db,
        prompt=PROMPT,
        verbose=True,
        memory=memory_1,
        return_sql=True,
    )

st.title("AI analytics Chatbot 🤖")
st.markdown("This page is for SQL Chatbot with Memory and Visualization")
st.markdown("Welcome to AI-lytics: AI-powered analytics chatbot created by Picipolo!")
st.markdown(
    "To get started, simply type your question about the data in the database, and I'll do my best to assist you."
)


def get_sql_query(user_query: str):
    """
    Gets the SQL query for a given user query
    Args:
        user_query (str): The user query
    Returns:
        str: The SQL query
    """
    result = db_chain2.invoke(user_query)
    return result["result"]


if "messages2" not in st.session_state:
    st.session_state.messages2 = []

for message in st.session_state.messages2:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages2.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        with get_openai_callback() as cb:
            try:
                response = db_chain2.invoke(prompt)["result"]
            except Exception:
                response = (
                    "I'm sorry, I couldn't understand your question. Please try again."
                )
            cost = cb.total_cost if cb.total_cost > 0 else 0.005 * cb.completion_tokens
            st.markdown(f"<small>Query cost: {cost}$</small>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages2.append({"role": "assistant", "content": response})

    df = create_df(response)
    print(df)

    query_for_plot = f"Create plot out of this data"
    plot = generate_plot(df, query_for_plot)
    st.set_option("deprecation.showPyplotGlobalUse", False)
    st.pyplot()
