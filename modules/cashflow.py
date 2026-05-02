import streamlit as st
import pandas as pd

def cashflow_planner():
    st.title("💰 Overall Cashflow Analysis")

    st.subheader("📥 Income")

    salary = st.number_input("Salary (₹)", value=80000)
    business = st.number_input("Business Income (₹)", value=0)
    other_income = st.number_input("Other Income (₹)", value=0)

    total_income = salary + business + other_income

    st.subheader("📤 Expenses")

    household = st.number_input("Household Expenses (₹)", value=30000)
    rent = st.number_input("Rent / EMI (₹)", value=15000)
    lifestyle = st.number_input("Lifestyle (₹)", value=10000)
    other_exp = st.number_input("Other Expenses (₹)", value=5000)

    total_expense = household + rent + lifestyle + other_exp

    st.subheader("📊 Investments & Loans")

    sip = st.number_input("Monthly SIP (₹)", value=10000)
    emi = st.number_input("Loan EMI (₹)", value=8000)

    total_outflow = total_expense + sip + emi

    st.divider()

    # =========================
    # SUMMARY
    # =========================
    surplus = total_income - total_outflow

    col1, col2, col3 = st.columns(3)

    col1.metric("Income", f"₹{total_income:,.0f}")
    col2.metric("Outflow", f"₹{total_outflow:,.0f}")
    col3.metric("Surplus", f"₹{surplus:,.0f}")

    st.divider()

    # =========================
    # CASHFLOW HEALTH
    # =========================
    if surplus > total_income * 0.3:
        st.success("Excellent Cashflow 💎")
    elif surplus > 0:
        st.warning("Moderate Cashflow ⚠️")
    else:
        st.error("Negative Cashflow 🚨")

    # =========================
    # YEARLY TABLE
    # =========================
    st.subheader("📊 Yearly Cashflow Projection")

    data = []

    for year in range(1, 11):
        annual_income = total_income * 12 * year
        annual_outflow = total_outflow * 12 * year
        annual_savings = surplus * 12 * year

        data.append({
            "Year": year,
            "Income (₹)": round(annual_income),
            "Outflow (₹)": round(annual_outflow),
            "Savings (₹)": round(annual_savings)
        })

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)

    # =========================
    # DOWNLOAD
    # =========================
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Cashflow",
        csv,
        "cashflow.csv",
        "text/csv"
    )
