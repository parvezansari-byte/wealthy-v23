import streamlit as st
import pandas as pd

def financial_planner():
    st.title("💼 Financial Planning Suite")

    # =========================
    # BUTTON NAVIGATION
    # =========================
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    if "planner_tab" not in st.session_state:
        st.session_state.planner_tab = "SWP"

    if col1.button("SWP"):
        st.session_state.planner_tab = "SWP"
    if col2.button("STP"):
        st.session_state.planner_tab = "STP"
    if col3.button("EMI"):
        st.session_state.planner_tab = "EMI"
    if col4.button("Retirement"):
        st.session_state.planner_tab = "Retirement"
    if col5.button("Child"):
        st.session_state.planner_tab = "Child"
    if col6.button("Cashflow"):
        st.session_state.planner_tab = "Cashflow"

    tab = st.session_state.planner_tab

    st.divider()

    # =========================
    # SWP TABLE
    # =========================
    if tab == "SWP":
        st.subheader("💸 SWP Calculator (Table View)")

        corpus = st.number_input("Initial Corpus", value=1000000)
        withdrawal = st.number_input("Monthly Withdrawal", value=20000)
        rate = st.number_input("Return (%)", value=8.0)
        years = int(st.number_input("Years", value=10))

        r = rate / 12 / 100
        balance = corpus

        data = []

        for y in range(1, years + 1):
            for _ in range(12):
                balance = balance * (1 + r) - withdrawal

            data.append({
                "Year": y,
                "Corpus (₹)": round(balance)
            })

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    # =========================
    # STP TABLE
    # =========================
    elif tab == "STP":
        st.subheader("🔁 STP Calculator (Table View)")

        corpus = st.number_input("Initial Amount", value=500000)
        transfer = st.number_input("Monthly Transfer", value=20000)
        rate = st.number_input("Return (%)", value=10.0)
        months = int(st.number_input("Months", value=12))

        r = rate / 12 / 100
        value = 0

        data = []

        for m in range(1, months + 1):
            value = (value + transfer) * (1 + r)

            data.append({
                "Month": m,
                "Value (₹)": round(value)
            })

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    # =========================
    # EMI TABLE
    # =========================
    elif tab == "EMI":
        st.subheader("🏦 EMI Calculator (Table View)")

        loan = st.number_input("Loan Amount", value=500000)
        rate = st.number_input("Interest (%)", value=10.0)
        years = int(st.number_input("Years", value=5))

        r = rate / (12 * 100)
        n = years * 12

        emi = loan * r * (1 + r)**n / ((1 + r)**n - 1)

        balance = loan
        data = []

        for m in range(1, n + 1):
            interest = balance * r
            principal = emi - interest
            balance -= principal

            data.append({
                "Month": m,
                "EMI": round(emi),
                "Principal": round(principal),
                "Interest": round(interest),
                "Balance": round(balance)
            })

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    # =========================
    # RETIREMENT TABLE
    # =========================
    elif tab == "Retirement":
        st.subheader("🧓 Retirement Planning")

        expense = st.number_input("Monthly Expense", value=30000)
        inflation = st.number_input("Inflation (%)", value=6.0)
        years = int(st.number_input("Years", value=20))

        data = []

        for y in range(1, years + 1):
            future = expense * ((1 + inflation/100) ** y)

            data.append({
                "Year": y,
                "Future Expense": round(future)
            })

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    # =========================
    # CHILD TABLE
    # =========================
    elif tab == "Child":
        st.subheader("🎓 Child Planning")

        cost = st.number_input("Current Cost", value=1000000)
        inflation = st.number_input("Inflation (%)", value=8.0)
        years = int(st.number_input("Years", value=15))

        data = []

        for y in range(1, years + 1):
            future = cost * ((1 + inflation/100) ** y)

            data.append({
                "Year": y,
                "Future Cost": round(future)
            })

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    # =========================
    # CASHFLOW
    # =========================
    elif tab == "Cashflow":
        st.subheader("💰 Cashflow")

        income = st.number_input("Income", value=100000)
        expenses = st.number_input("Expenses", value=60000)

        savings = income - expenses

        st.metric("Monthly Savings", f"₹{savings:,.0f}")
