import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

conn = sqlite3.connect("wealthy.db", check_same_thread=False)

def master_dashboard():
    st.title("🧠 Advisor 360° Dashboard")

    # =========================
    # CLIENT SELECT
    # =========================
    clients = conn.execute("SELECT * FROM clients").fetchall()

    if not clients:
        st.warning("No clients available")
        return

    names = [f"{c[0]} - {c[1]}" for c in clients]
    selected = st.selectbox("Select Client", names)
    client_id = int(selected.split(" - ")[0])

    st.divider()

    # =========================
    # NET WORTH (STATIC INPUT FOR NOW)
    # =========================
    st.subheader("📊 Net Worth Snapshot")

    col1, col2, col3 = st.columns(3)

    assets = st.number_input("Total Assets (₹)", value=2000000)
    liabilities = st.number_input("Total Liabilities (₹)", value=800000)
    net_worth = assets - liabilities

    col1.metric("Assets", f"₹{assets:,.0f}")
    col2.metric("Liabilities", f"₹{liabilities:,.0f}")
    col3.metric("Net Worth", f"₹{net_worth:,.0f}")

    st.divider()

    # =========================
    # CASHFLOW
    # =========================
    st.subheader("💰 Cashflow Snapshot")

    income = st.number_input("Monthly Income (₹)", value=100000)
    expense = st.number_input("Monthly Expense (₹)", value=70000)

    surplus = income - expense

    col1, col2, col3 = st.columns(3)

    col1.metric("Income", f"₹{income:,.0f}")
    col2.metric("Expense", f"₹{expense:,.0f}")
    col3.metric("Surplus", f"₹{surplus:,.0f}")

    st.divider()

    # =========================
    # GOALS
    # =========================
    st.subheader("🎯 Client Goals")

    goals = conn.execute(
        "SELECT goal_name, target_amount, years FROM goals WHERE client_id=?",
        (client_id,)
    ).fetchall()

    if goals:
        for g in goals:
            st.write(f"🎯 {g[0]} → ₹{g[1]:,.0f} in {g[2]} yrs")
    else:
        st.info("No goals added")

    st.divider()

    # =========================
    # SIMPLE PROJECTION CHART
    # =========================
    st.subheader("📈 Wealth Projection")

    years = list(range(1, 11))
    values = [net_worth * (1.1 ** y) for y in years]

    df = pd.DataFrame({"Year": years, "Value": values})

    fig = px.line(df, x="Year", y="Value", title="Projected Net Worth (10%)")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =========================
    # ADVISOR INSIGHTS
    # =========================
    st.subheader("🧠 Advisor Insights")

    if surplus <= 0:
        st.error("Client has negative cashflow — fix before investing")
    elif surplus < income * 0.2:
        st.warning("Low savings rate — increase SIP capacity")
    else:
        st.success("Healthy financial position")

    if liabilities > assets * 0.6:
        st.warning("High debt ratio")
    else:
        st.success("Debt under control")
