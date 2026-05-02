import streamlit as st

# =========================
# IMPORT MODULES
# =========================
from modules.dashboard import show_dashboard
from modules.crm import client_onboarding
from modules.client_profile import client_profile
from modules.investments import sip_calculator
from modules.investment_dashboard import investment_dashboard
from modules.pdf_report import pdf_report
from modules.financial_planner import financial_planner

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Wealthy V23",
    layout="wide",
    page_icon="💜"
)

# =========================
# SAFE UI (NO BREAK CSS)
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #020617;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #020617;
}

div.stButton > button {
    background-color: #7c3aed;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("💜 Wealthy V23")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Client Onboarding",
        "Client Profile",
        "SIP Calculator",
        "Investment Dashboard",
        "PDF Report"
        "Financial Planner",
    ]
)

# =========================
# MAIN ROUTER
# =========================
if page == "Dashboard":
    show_dashboard()

elif page == "Client Onboarding":
    client_onboarding()

elif page == "Client Profile":
    client_profile()

elif page == "SIP Calculator":
    sip_calculator()

elif page == "Investment Dashboard":
    investment_dashboard()

elif page == "PDF Report":
    pdf_report()
elif page == "Financial Planner":
    financial_planner()

# =========================
# DEBUG (REMOVE LATER)
# =========================
st.sidebar.caption("Status: App Running ✅")
