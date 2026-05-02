import streamlit as st
import plotly.graph_objects as go

def future_value_sip(monthly_investment, annual_return, years):
    r = annual_return / 12 / 100
    n = int(years * 12)

    if r == 0:
        return monthly_investment * n

    return monthly_investment * (((1 + r)**n - 1) / r) * (1 + r)

def sip_calculator():
    st.title("📈 SIP Calculator (with Chart)")

    sip = st.number_input("Monthly SIP (₹)", value=10000)
    rate = st.number_input("Expected Return (%)", value=12.0)
    years = st.number_input("Years", value=10)

    # Calculations
    fv = future_value_sip(sip, rate, years)
    invested = sip * 12 * years

    st.metric("Total Invested", f"₹{invested:,.0f}")
    st.metric("Future Value", f"₹{fv:,.0f}")
    st.metric("Wealth Gain", f"₹{fv - invested:,.0f}")

    # 📊 Year-wise chart data
    values = []
    invested_values = []

    for y in range(1, years + 1):
        val = future_value_sip(sip, rate, y)
        values.append(val)
        invested_values.append(sip * 12 * y)

    # 📊 Plotly chart
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=list(range(1, years + 1)),
        y=values,
        mode='lines+markers',
        name='Portfolio Value'
    ))

    fig.add_trace(go.Scatter(
        x=list(range(1, years + 1)),
        y=invested_values,
        mode='lines',
        name='Invested Amount'
    ))

    fig.update_layout(
        title="Wealth Growth Over Time",
        xaxis_title="Years",
        yaxis_title="Amount (₹)",
        template="plotly_dark"
    )
    # 📊 Year-wise data
values = []
invested_values = []

for y in range(1, int(years) + 1):
    val = future_value_sip(sip, rate, y)
    values.append(val)
    invested_values.append(sip * 12 * y)

# 📊 Plotly chart
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=list(range(1, int(years) + 1)),
    y=values,
    mode='lines+markers',
    name='Portfolio Value'
))

fig.add_trace(go.Scatter(
    x=list(range(1, int(years) + 1)),
    y=invested_values,
    mode='lines',
    name='Invested Amount'
))

fig.update_layout(
    title="Wealth Growth Over Time",
    xaxis_title="Years",
    yaxis_title="Amount (₹)",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

    st.plotly_chart(fig, use_container_width=True)
