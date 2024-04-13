import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

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


def get_response(user_query: str, chat_history: list) -> dict:
    """
    Gets the response from the AI model.
    Args:
        user_query (str): The user query.
        chat_history (list): The chat history.
    Returns:
        dict: The response from the AI model.
    """

    template = """
    Answer the following guestions considering the history of the conversation:
    
    Chat history: {chat_history}

    User question: {user_query}
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI()

    chain = prompt | llm | StrOutputParser()

    return chain.stream({"chat_history": chat_history, "user_query": user_query})


for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)


user_query = st.chat_input("Type your query here")

if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        ai_response = st.write_stream(
            get_response(user_query, st.session_state.chat_history)
        )

    st.session_state.chat_history.append(AIMessage(ai_response))
