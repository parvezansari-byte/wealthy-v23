import streamlit as st
import numpy as np

# =========================
# HELPER FUNCTIONS
# =========================
def future_value_lumpsum(P, r, n):
    return P * (1 + r/100) ** n

def emi_calc(P, r, n):
    r = r / (12 * 100)
    n = n * 12
    return P * r * (1 + r)**n / ((1 + r)**n - 1)

# =========================
# MAIN MODULE
# =========================
def financial_planner():
    st.title("💼 Financial Planning Suite")

    option = st.selectbox(
        "Select Calculator",
        [
            "SWP Calculator",
            "STP Calculator",
            "EMI Calculator",
            "Retirement Planning",
            "Child Education Planning",
            "Cashflow Planner"
        ]
    )

    # =========================
    # SWP
    # =========================
    if option == "SWP Calculator":
        st.subheader("💸 Systematic Withdrawal Plan")

        corpus = st.number_input("Initial Corpus (₹)", value=1000000)
        withdrawal = st.number_input("Monthly Withdrawal (₹)", value=20000)
        rate = st.number_input("Return (%)", value=8.0)
        years = st.number_input("Years", value=10)

        balance = corpus
        r = rate / 12 / 100

        for _ in range(int(years * 12)):
            balance = balance * (1 + r) - withdrawal

        st.metric("Remaining Corpus", f"₹{balance:,.0f}")

    # =========================
    # STP
    # =========================
    elif option == "STP Calculator":
        st.subheader("🔁 Systematic Transfer Plan")

        corpus = st.number_input("Initial Amount (₹)", value=500000)
        transfer = st.number_input("Monthly Transfer (₹)", value=20000)
        rate = st.number_input("Return (%)", value=10.0)
        months = st.number_input("Months", value=12)

        r = rate / 12 / 100
        value = 0

        for _ in range(int(months)):
            value = (value + transfer) * (1 + r)

        st.metric("Final Value", f"₹{value:,.0f}")

    # =========================
    # EMI
    # =========================
    elif option == "EMI Calculator":
        st.subheader("🏦 EMI Calculator")

        loan = st.number_input("Loan Amount (₹)", value=500000)
        rate = st.number_input("Interest Rate (%)", value=10.0)
        years = st.number_input("Tenure (Years)", value=5)

        emi = emi_calc(loan, rate, years)

        st.metric("Monthly EMI", f"₹{emi:,.0f}")

    # =========================
    # RETIREMENT
    # =========================
    elif option == "Retirement Planning":
        st.subheader("🧓 Retirement Planning")

        current_age = st.number_input("Current Age", value=30)
        retirement_age = st.number_input("Retirement Age", value=60)
        monthly_expense = st.number_input("Current Monthly Expense (₹)", value=30000)
        inflation = st.number_input("Inflation (%)", value=6.0)

        years = retirement_age - current_age
        future_expense = monthly_expense * ((1 + inflation/100) ** years)

        st.metric("Expense at Retirement", f"₹{future_expense:,.0f}")

    # =========================
    # CHILD PLANNING
    # =========================
    elif option == "Child Education Planning":
        st.subheader("🎓 Child Education Planning")

        current_cost = st.number_input("Current Cost (₹)", value=1000000)
        years = st.number_input("Years to Goal", value=15)
        inflation = st.number_input("Inflation (%)", value=8.0)

        future_cost = current_cost * ((1 + inflation/100) ** years)

        st.metric("Future Cost", f"₹{future_cost:,.0f}")

    # =========================
    # CASHFLOW
    # =========================
    elif option == "Cashflow Planner":
        st.subheader("💰 Cashflow Planner")

        income = st.number_input("Monthly Income (₹)", value=100000)
        expenses = st.number_input("Monthly Expenses (₹)", value=60000)

        savings = income - expenses

        st.metric("Monthly Savings", f"₹{savings:,.0f}")

        if savings > 0:
            st.success("Good cashflow 👍")
        else:
            st.error("Negative cashflow ⚠️")
