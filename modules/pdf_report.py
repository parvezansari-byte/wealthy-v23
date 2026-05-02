import streamlit as st
import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

conn = sqlite3.connect("wealthy.db", check_same_thread=False)

def generate_pdf(name, age):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("WEALTHY CLIENT REPORT", styles["Title"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Client Name: {name}", styles["Normal"]))
    content.append(Paragraph(f"Age: {age}", styles["Normal"]))

    content.append(Spacer(1, 10))
    content.append(Paragraph("This is a basic financial advisory report.", styles["Normal"]))

    doc.build(content)

    buffer.seek(0)
    return buffer


def pdf_report():
    st.title("📄 Generate Client PDF")

    clients = conn.execute("SELECT * FROM clients").fetchall()

    if clients:
        client_names = [f"{c[0]} - {c[1]}" for c in clients]
        selected = st.selectbox("Select Client", client_names)

        client_id = int(selected.split(" - ")[0])
        client = [c for c in clients if c[0] == client_id][0]

        if st.button("Generate PDF"):
            pdf = generate_pdf(client[1], client[2])

            st.download_button(
                label="📄 Download PDF",
                data=pdf,
                file_name="client_report.pdf",
                mime="application/pdf"
            )
    else:
        st.info("No clients found")
