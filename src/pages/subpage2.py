import streamlit as st
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.callbacks import get_openai_callback

from model import DBSingleton, LLM_Singleton

st.set_page_config(
    page_title="SQL Agent with Reasoning and Act framework (ReaAct) for Advanced Analytics and Interaction with Data",
)

db_singleton = DBSingleton()
llm_singleton = LLM_Singleton()

if "messages3" not in st.session_state:
    st.session_state.messages3 = []

if "agent_executor" not in st.session_state:
    agent_executor = create_sql_agent(
        llm=llm_singleton.llm,
        toolkit=SQLDatabaseToolkit(db=db_singleton.db, llm=llm_singleton.llm),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=False,
    )

st.warning("‼️‼️ Use only when data can be shared with the LLM model. ‼️‼️")
st.title("AI analytics Chatbot 🤖")
st.markdown(
    "This page is for SQL Agent with Reasoning and Act framework (ReaAct) for Advanced Analytics and Interaction with Data"
)
st.markdown("Welcome to AI-lytics: AI-powered analytics chatbot created by Picipolo!")
st.markdown(
    "To get started, simply type your question about the data in the database, and I'll do my best to assist you."
)


if "messages" not in st.session_state:
    st.session_state.messages3 = []

for message in st.session_state.messages3:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages3.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        with get_openai_callback() as cb:
            try:
                response = agent_executor.invoke(prompt)["output"]
            except Exception:
                response = "I'm sorry, I couldn't understand your question. Could you please rephrase it?"
            cost = cb.total_cost if cb.total_cost > 0 else 0.005 * cb.completion_tokens
            st.markdown(f"<small>Query cost: {cost}$</small>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages3.append({"role": "assistant", "content": response})
