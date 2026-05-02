from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["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"])

def generate_summary(name, age):
    prompt = f"""
    Create a professional financial advisory summary:
    Name: {name}
    Age: {age}
    """

    response = client.chat.completions.create(
        model="model="gpt-5.3",   # ✅ stable model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
