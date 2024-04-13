import streamlit as st

st.set_page_config(
    page_title="Picipolo - Upload files",
    page_icon="	:page_facing_up:",
)

file = st.file_uploader("Upload file", type=["csv", "xlsx", "xls"])
