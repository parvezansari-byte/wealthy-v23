import streamlit as st
from utils.ai_engine import generate_summary

def ai_summary():
    st.title("🤖 AI Client Summary")

    name = st.text_input("Client Name")
    age = st.number_input("Age", 18, 100)

    if st.button("Generate AI Summary"):
        summary = generate_summary(name, age)
        st.text_area("AI Output", summary, height=200)
