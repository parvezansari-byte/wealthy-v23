import streamlit as st
import pandas as pd
import plotly.express as px

def networth_tracker():
    st.title("📊 Asset & Liability Sheet")

    # =========================
    # ASSETS
    # =========================
    st.subheader("💰 Assets")

    equity = st.number_input("Equity / Mutual Funds (₹)", value=500000)
    cash = st.number_input("Bank / Cash (₹)", value=200000)
    property_val = st.number_input("Property (₹)", value=3000000)
    gold = st.number_input("Gold (₹)", value=150000)
    other_assets = st.number_input("Other Assets (₹)", value=50000)

    total_assets = equity + cash + property_val + gold + other_assets

    # =========================
    # LIABILITIES
    # =========================
    st.subheader("📉 Liabilities")

    home_loan = st.number_input("Home Loan (₹)", value=1000000)
    personal_loan = st.number_input("Personal Loan (₹)", value=200000)
    credit_card = st.number_input("Credit Card (₹)", value=50000)
    other_liabilities = st.number_input("Other Liabilities (₹)", value=0)

    total_liabilities = home_loan + personal_loan + credit_card + other_liabilities

    # =========================
    # NET WORTH
    # =========================
    net_worth = total_assets - total_liabilities

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Assets", f"₹{total_assets:,.0f}")
    col2.metric("Total Liabilities", f"₹{total_liabilities:,.0f}")
    col3.metric("Net Worth", f"₹{net_worth:,.0f}")

    st.divider()

    # =========================
    # TABLE
    # =========================
    st.subheader("📋 Net Worth Breakdown")

    data = {
        "Category": ["Equity", "Cash", "Property", "Gold", "Other Assets",
                     "Home Loan", "Personal Loan", "Credit Card", "Other Liabilities"],
        "Amount (₹)": [
            equity, cash, property_val, gold, other_assets,
            -home_loan, -personal_loan, -credit_card, -other_liabilities
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # =========================
    # PIE CHART (ASSETS)
    # =========================
    st.subheader("📊 Asset Allocation")

    asset_data = pd.DataFrame({
        "Asset": ["Equity", "Cash", "Property", "Gold", "Other"],
        "Value": [equity, cash, property_val, gold, other_assets]
    })

    fig = px.pie(asset_data, names="Asset", values="Value", title="Asset Allocation")

    st.plotly_chart(fig, use_container_width=True)
