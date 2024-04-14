import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="AIlytics Chatbot",
    page_icon=":robot_face:",
)

show_pages(
    pages=[
        Page("pages/subpage0.py", "SQL Chatbot with Memory"),
        Page(
            "pages/subpage1.py",
            "SQL Chatbot For SQL queries with Memory and Visualization",
        ),
        Page(
            "pages/subpage2.py",
            "SQL Agent with Reasoning and Act framework (ReaAct) for Advanced Analytics and Interaction with Data",
        ),
    ]
)

st.title("AI analytics Chatbot 🤖")
st.markdown("This app serves as an advanced analytics chatbot.")
st.markdown("It consists of three pages:")
st.markdown("1. SQL Chatbot with Memory")
st.markdown("2. SQL Chatbot with Memory and Visualization")
st.markdown(
    "3. SQL Agent with Reasoning and Act framework (ReaAct) for Advanced Analytics and Interaction with Data"
)
st.markdown("Use the sidebar to navigate between the pages.")
