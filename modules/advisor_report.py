import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

def generate_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("WEALTH ADVISORY REPORT", styles["Title"]))
    content.append(Spacer(1, 10))

    for k, v in data.items():
        content.append(Paragraph(f"{k}: ₹{v:,.0f}", styles["Normal"]))
        content.append(Spacer(1, 8))

    doc.build(content)
    buffer.seek(0)
    return buffer


def advisor_report():
    st.title("📄 Advisor Report")

    assets = st.number_input("Assets", value=2000000)
    liabilities = st.number_input("Liabilities", value=800000)
    income = st.number_input("Income", value=100000)
    expense = st.number_input("Expense", value=50000)
    goals = st.number_input("Goals", value=1500000)

    if st.button("Generate PDF"):
        data = {
            "Assets": assets,
            "Liabilities": liabilities,
            "Net Worth": assets - liabilities,
            "Income": income,
            "Expense": expense,
            "Surplus": income - expense,
            "Goals": goals
        }

        pdf = generate_pdf(data)

        st.download_button(
            "Download PDF",
            pdf,
            "advisor_report.pdf",
            "application/pdf"
        )
