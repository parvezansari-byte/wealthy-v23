import streamlit as st
from modules.dashboard import show_dashboard
from modules.crm import client_onboarding
from modules.investments import sip_calculator
from modules.pdf_report import pdf_report

st.set_page_config(page_title="Wealthy V23", layout="wide")

st.sidebar.title("💜 Wealthy V23")

page = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Client Onboarding", "SIP Calculator", "PDF Report"]
)

if page == "Dashboard":
    show_dashboard()

elif page == "Client Onboarding":
    client_onboarding()

elif page == "SIP Calculator":
    sip_calculator()
elif page == "PDF Report":
    pdf_report()
