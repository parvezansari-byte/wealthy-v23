from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

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
