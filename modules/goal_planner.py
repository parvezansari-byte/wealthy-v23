import streamlit as st
import pandas as pd

# =========================
# HELPER FUNCTIONS
# =========================
def future_cost(present, inflation, years):
    return present * ((1 + inflation/100) ** years)

def required_sip(goal, rate, years):
    r = rate / 12 / 100
    n = years * 12

    if r == 0:
        return goal / n

    return goal * r / ((1 + r)**n - 1)

# =========================
# MAIN FUNCTION
# =========================
def goal_planner():
    st.title("🎯 Goal-Based Planning Engine")

    goal_type = st.selectbox(
        "Select Goal",
        ["Retirement", "Child Education", "Wealth Creation"]
    )

    col1, col2 = st.columns(2)

    with col1:
        present_cost = st.number_input("Current Cost / Target (₹)", value=1000000)
        years = int(st.number_input("Years to Goal", value=15))

    with col2:
        inflation = st.number_input("Inflation (%)", value=6.0)
        return_rate = st.number_input("Expected Return (%)", value=12.0)

    # =========================
    # CALCULATIONS
    # =========================
    future_value = future_cost(present_cost, inflation, years)
    sip = required_sip(future_value, return_rate, years)

    st.divider()

    # =========================
    # RESULTS
    # =========================
    col1, col2, col3 = st.columns(3)

    col1.metric("Future Cost", f"₹{future_value:,.0f}")
    col2.metric("Required SIP", f"₹{sip:,.0f}")
    col3.metric("Years", years)

    st.divider()

    # =========================
    # YEARLY TABLE
    # =========================
    st.subheader("📊 Goal Projection Table")

    data = []
    value = 0
    r = return_rate / 100

    for y in range(1, years + 1):
        value = (value + sip * 12) * (1 + r)

        data.append({
            "Year": y,
            "Invested (₹)": round(sip * 12 * y),
            "Portfolio Value (₹)": round(value),
            "Goal Target (₹)": round(future_cost(present_cost, inflation, y))
        })

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # =========================
    # GAP ANALYSIS
    # =========================
    final_value = df.iloc[-1]["Portfolio Value (₹)"]
    gap = future_value - final_value

    st.divider()

    if gap > 0:
        st.error(f"⚠️ Shortfall: ₹{gap:,.0f}")
    else:
        st.success("✅ Goal Achievable")

    # =========================
    # DOWNLOAD
    # =========================
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Goal Plan",
        csv,
        "goal_plan.csv",
        "text/csv"
    )
