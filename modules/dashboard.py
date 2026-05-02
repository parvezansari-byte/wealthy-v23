import streamlit as st
import sqlite3
import pandas as pd

# DB connection
conn = sqlite3.connect("wealthy.db", check_same_thread=False)

def show_dashboard():
    st.title("📊 Advisor Dashboard")

    df = pd.read_sql("SELECT * FROM clients", conn)

    total_clients = len(df)
    avg_age = int(df["age"].mean()) if not df.empty else 0

    # KPI Cards
    col1, col2 = st.columns(2)

    col1.metric("Total Clients", total_clients)
    col2.metric("Average Age", avg_age)

    st.divider()

    # 📊 Age Distribution Chart
    if not df.empty:
        st.subheader("📊 Client Age Distribution")

        age_counts = df["age"].value_counts().sort_index()

        st.bar_chart(age_counts)

    else:
        st.info("No data available yet")
        st.markdown(f"""
<div class="kpi-card">
    <h3>Total Clients</h3>
    <h1>{total_clients}</h1>
</div>
""", unsafe_allow_html=True)
