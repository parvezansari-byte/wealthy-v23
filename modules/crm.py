import streamlit as st
import sqlite3
import pandas as pd

# =========================
# DATABASE SETUP
# =========================
conn = sqlite3.connect("wealthy.db", check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")


# =========================
# FETCH DATA
# =========================
def get_clients():
    return pd.read_sql("SELECT * FROM clients", conn)


# =========================
# MAIN FUNCTION
# =========================
def client_onboarding():
    st.title("🧾 Client CRM Dashboard")

    st.subheader("➕ Add New Client")

    name = st.text_input("Client Name")
    age = st.number_input("Age", 18, 100)

    if st.button("Add Client"):
        conn.execute(
            "INSERT INTO clients (name, age) VALUES (?, ?)",
            (name, age)
        )
        conn.commit()
        st.success("Client Added!")

    st.divider()

    # =========================
    # SEARCH
    # =========================
    st.subheader("🔍 Search Client")

    search = st.text_input("Search by name")

    df = get_clients()

    if search:
        df = df[df["name"].str.contains(search, case=False)]

    st.dataframe(df, use_container_width=True)

    st.divider()

    # =========================
    # EDIT / DELETE
    # =========================
    st.subheader("✏️ Edit / Delete Client")

    if not df.empty:
        selected_id = st.selectbox("Select Client ID", df["id"])

        selected_client = df[df["id"] == selected_id].iloc[0]

        new_name = st.text_input("Edit Name", selected_client["name"])
        new_age = st.number_input("Edit Age", 18, 100, int(selected_client["age"]))

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Update Client"):
                conn.execute(
                    "UPDATE clients SET name=?, age=? WHERE id=?",
                    (new_name, new_age, selected_id)
                )
                conn.commit()
                st.success("Client Updated!")

        with col2:
            if st.button("Delete Client"):
                conn.execute(
                    "DELETE FROM clients WHERE id=?",
                    (selected_id,)
                )
                conn.commit()
                st.warning("Client Deleted!")

    else:
        st.info("No clients available")
