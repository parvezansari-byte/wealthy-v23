import streamlit as st

def future_value_sip(monthly_investment, annual_return, years):
    r = annual_return / 12 / 100
    n = int(years * 12)

    if r == 0:
        return monthly_investment * n

    return monthly_investment * (((1 + r)**n - 1) / r) * (1 + r)

def sip_calculator():
    st.title("📈 SIP Calculator (Advanced)")

    sip = st.number_input("Monthly SIP (₹)", value=10000)
    rate = st.number_input("Expected Return (%)", value=12.0)
    years = st.number_input("Years", value=10)

    fv = future_value_sip(sip, rate, years)
    invested = sip * 12 * years

    st.metric("Total Invested", f"₹{invested:,.0f}")
    st.metric("Future Value", f"₹{fv:,.0f}")
    st.metric("Wealth Gain", f"₹{fv - invested:,.0f}")
