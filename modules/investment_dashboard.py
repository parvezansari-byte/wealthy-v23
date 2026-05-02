import streamlit as st
import plotly.express as px

def investment_dashboard():
    st.title("📊 Investment Dashboard")

    years = list(range(1, 11))
    values = [10000 * y * 1.2 for y in years]

    df = {"Year": years, "Value": values}

    fig = px.line(df, x="Year", y="Value", title="Portfolio Growth")

    st.plotly_chart(fig, use_container_width=True)
