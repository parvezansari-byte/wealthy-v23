from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_summary(name, age):
    prompt = f"""
    Create a professional financial advisory summary:
    Name: {name}
    Age: {age}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # ✅ stable model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
