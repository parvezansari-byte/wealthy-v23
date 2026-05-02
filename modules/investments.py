import streamlit as st

def sip_calculator():
    st.title("📈 SIP Calculator")

    sip = st.number_input("Monthly SIP", value=10000)
    rate = st.number_input("Return %", value=12.0)
    years = st.number_input("Years", value=10)

    future_value = sip * 12 * years * (1 + rate/100)

    st.metric("Future Value", f"₹{future_value:,.0f}")
