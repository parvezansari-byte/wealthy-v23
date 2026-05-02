from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(name, age):
    prompt = f"""
    Create a professional financial advisory summary for:
    Name: {name}
    Age: {age}
    """

    response = client.chat.completions.create(
        model="gpt-5.3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
