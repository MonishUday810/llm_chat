import streamlit as st
import requests

st.title("Chat")

user_input = st.text_area("Ask about your child:")
if st.button("Submit"):
    with st.spinner("Thinking..."):
        try:
            res = requests.post("https://concise-faithful-sturgeon.ngrok-free.app/chat", json={"data": user_input})
            res.raise_for_status()
            st.write(res.json()["response"])
        except Exception as e:
            st.error(f"Something went wrong: {e}")
