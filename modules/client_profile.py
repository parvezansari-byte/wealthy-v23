import streamlit as st
import sqlite3

conn = sqlite3.connect("wealthy.db", check_same_thread=False)

def client_profile():
    st.title("👤 Client Profile")

    clients = conn.execute("SELECT * FROM clients").fetchall()

    if clients:
        names = [f"{c[0]} - {c[1]}" for c in clients]
        selected = st.selectbox("Select Client", names)

        client_id = int(selected.split(" - ")[0])
        client = [c for c in clients if c[0] == client_id][0]

        st.subheader("Client Details")

        st.write(f"Name: {client[1]}")
        st.write(f"Age: {client[2]}")

    else:
        st.info("No clients available")
