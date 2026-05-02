import streamlit as st
from modules.dashboard import show_dashboard
from modules.crm import client_onboarding
from modules.investments import sip_calculator
from modules.pdf_report import pdf_report
from modules.investment_dashboard import investment_dashboard

st.markdown("""
<style>

/* App Background */
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #1e293b);
}

/* Titles */
h1, h2, h3 {
    color: #e2e8f0;
}

/* KPI Cards */
.kpi-card {
    background: linear-gradient(135deg, #1e293b, #4c1d95);
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    text-align: center;
    transition: 0.3s;
}

.kpi-card:hover {
    transform: scale(1.05);
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white;
    border-radius: 12px;
    padding: 10px;
    font-weight: bold;
    border: none;
}

div.stButton > button:hover {
    transform: scale(1.05);
}

/* Inputs */
input, textarea {
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)
