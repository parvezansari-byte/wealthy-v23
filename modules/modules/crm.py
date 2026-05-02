import streamlit as st

def client_onboarding():
    st.title("🧾 Client Onboarding")

    name = st.text_input("Client Name")
    age = st.number_input("Age", 18, 100)

    if st.button("Save"):
        st.success(f"{name} saved!")
