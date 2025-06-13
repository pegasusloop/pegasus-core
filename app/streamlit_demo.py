import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# ⬅️ This loads .env vars into your environment
load_dotenv()

# Now it will find the API key!
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Pegasus Streamlit Demo 🦄")
question = st.text_input("Ask Pegasus something:")

if question:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[{"role": "user", "content": question}]
        )
        st.success(response.choices[0].message.content)
