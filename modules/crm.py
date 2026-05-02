import streamlit as st
import sqlite3

# Connect DB
conn = sqlite3.connect("wealthy.db", check_same_thread=False)

# Create table
conn.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

def client_onboarding():
    st.title("🧾 Client Onboarding")

    name = st.text_input("Client Name")
    age = st.number_input("Age", 18, 100)

    if st.button("Save Client"):
        conn.execute("INSERT INTO clients (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        st.success("Client Saved!")

    st.subheader("📋 Saved Clients")

    data = conn.execute("SELECT * FROM clients").fetchall()
    for row in data:
        st.write(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]}")
