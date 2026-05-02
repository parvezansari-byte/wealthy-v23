import streamlit as st
import pandas as pd
import plotly.express as px

def master_dashboard():
    st.title("🧠 Advisor 360° Dashboard")

    st.divider()

    # =========================
    # NET WORTH
    # =========================
    st.subheader("📊 Net Worth")

    col1, col2 = st.columns(2)
    assets = col1.number_input("Assets (₹)", value=2000000)
    liabilities = col2.number_input("Liabilities (₹)", value=800000)

    networth = assets - liabilities

    st.metric("Net Worth", f"₹{networth:,.0f}")

    fig = px.pie(
        names=["Assets", "Liabilities"],
        values=[assets, liabilities],
        title="Net Worth Split"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =========================
    # CASHFLOW
    # =========================
    st.subheader("💰 Cashflow")

    col1, col2, col3 = st.columns(3)
    income = col1.number_input("Income", value=100000)
    expense = col2.number_input("Expense", value=50000)
    sip = col3.number_input("SIP", value=10000)

    emi = st.number_input("EMI", value=8000)

    outflow = expense + sip + emi
    surplus = income - outflow

    st.metric("Surplus", f"₹{surplus:,.0f}")

    fig = px.bar(
        x=["Income", "Expense", "SIP", "EMI"],
        y=[income, expense, sip, emi],
        title="Cashflow Breakdown"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =========================
    # GOALS
    # =========================
    st.subheader("🎯 Goals")

    goal1 = st.number_input("Goal 1", value=1000000)
    goal2 = st.number_input("Goal 2", value=500000)
    goal3 = st.number_input("Goal 3", value=0)

    total_goal = goal1 + goal2 + goal3

    st.metric("Total Goals", f"₹{total_goal:,.0f}")

    fig = px.bar(
        x=["Goal 1", "Goal 2", "Goal 3"],
        y=[goal1, goal2, goal3],
        title="Goal Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =========================
    # PROJECTION
    # =========================
    st.subheader("📈 Projection")

    years = list(range(1, 11))
    values = [networth * (1.1 ** y) for y in years]

    df = pd.DataFrame({"Year": years, "Value": values})
    fig = px.line(df, x="Year", y="Value", title="Growth @10%")

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =========================
    # INSIGHTS
    # =========================
    st.subheader("🧠 Advisor Insights")

    if surplus <= 0:
        st.error("Negative cashflow")
    elif surplus < income * 0.2:
        st.warning("Low savings")
    else:
        st.success("Healthy financials")
